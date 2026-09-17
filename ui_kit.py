"""A few drawn widgets for the Tk app, in a clean, native style.

Everything else in the app is a standard ttk widget, which on macOS looks and
behaves like a native control and follows the system's light or dark mode.
The drawn pieces here use the system's own named colours on macOS for the same
reason.
"""

from __future__ import annotations

import re
import sys
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

AQUA = sys.platform == "darwin"

# Colours that read well in light and dark mode.
BLUE = "#2f7fd8"
RED = "#d64545"
GREEN = "#2e9e5b"
ORANGE = "#d9822b"
PURPLE = "#8e5bd8"
GREY = "#8a8f98"

SIDE_COLOURS = (BLUE, RED)

if AQUA:
    BACKGROUND = "systemWindowBackgroundColor"
    SURFACE = "systemTextBackgroundColor"
    TEXT = "systemTextColor"
    MUTED = "systemSecondaryLabelColor"
    TRACK = "systemSeparatorColor"
else:
    BACKGROUND, SURFACE, TEXT, MUTED, TRACK = "#f5f5f7", "#ffffff", "#1d1d1f", "#6e6e73", "#d2d2d7"


class Fonts:
    """System fonts in a small typographic scale."""

    def __init__(self, root):
        base = tkfont.nametofont("TkDefaultFont", root=root)
        family = base.actual("family")
        size = base.actual("size") or 13
        mono = "Menlo" if AQUA else "Courier"
        self.title = (family, size + 9, "bold")
        self.heading = (family, size + 1, "bold")
        self.body = (family, size)
        self.small = (family, size - 1)
        self.number = (family, size + 7, "bold")
        self.stat_value = (family, size + 3, "bold")
        self.log = (mono, size - 1)


def apply_style(root, fonts):
    style = ttk.Style(root)
    style.configure("Title.TLabel", font=fonts.title)
    style.configure("Heading.TLabel", font=fonts.heading)
    style.configure("Muted.TLabel", foreground=MUTED, font=fonts.small)
    style.configure("Error.TLabel", foreground=RED, font=fonts.small)
    style.configure("Accent.TLabel", foreground=BLUE, font=fonts.small)
    style.configure("Warning.TLabel", foreground=ORANGE, font=fonts.small)
    style.configure("Card.TLabelframe.Label", font=fonts.heading)
    root.configure(bg=BACKGROUND)


class StatTiles(tk.Canvas):
    """A statline as a row of rounded tiles: WS 7 | S 4 | ..."""

    NAMES = ("WS", "S", "T", "W", "I", "A", "Ld")

    def __init__(self, master, fonts, colour):
        super().__init__(master, height=52, bg=BACKGROUND, highlightthickness=0)
        self.fonts, self.colour = fonts, colour
        self.values, self.message = None, ""
        self.bind("<Configure>", lambda _e: self._draw())

    def show(self, values=None, message=""):
        self.values, self.message = values, message
        self._draw()

    def _draw(self):
        self.delete("all")
        width = max(self.winfo_width(), 280)
        if not self.values:
            self.create_text(2, 26, text=self.message, anchor="w", font=self.fonts.body, fill=RED)
            return
        gap = 6
        tile = (width - gap * 6) / 7
        for i, name in enumerate(self.NAMES):
            x0 = i * (tile + gap)
            _rounded(self, x0 + 1, 1, x0 + tile - 1, 50, 8, fill=SURFACE, outline=TRACK)
            self.create_text(x0 + tile / 2, 14, text=name, font=self.fonts.small, fill=MUTED)
            value = self.values.get(name)
            self.create_text(x0 + tile / 2, 33, text="–" if value is None else str(value),
                             font=self.fonts.stat_value, fill=self.colour)


class WinBar(tk.Canvas):
    """A stacked bar: side A wins | draws | side B wins, with percentages."""

    def __init__(self, master, fonts):
        super().__init__(master, height=96, bg=BACKGROUND, highlightthickness=0)
        self.fonts, self.data = fonts, None
        self.bind("<Configure>", lambda _e: self._draw())

    def show(self, name_a, win_a, draw, name_b, win_b):
        self.data = (name_a, win_a, draw, name_b, win_b)
        self._draw()

    def _draw(self):
        self.delete("all")
        if not self.data:
            return
        name_a, win_a, draw, name_b, win_b = self.data
        width = max(self.winfo_width(), 300)
        left, right, top, height = 2, width - 2, 36, 16
        span = right - left
        _rounded(self, left, top, right, top + height, 8, fill=TRACK, outline="")
        x = left
        for share, colour in ((win_a, SIDE_COLOURS[0]), (draw, GREY), (win_b, SIDE_COLOURS[1])):
            w = share * span
            if w >= 1:
                self.create_rectangle(x, top, x + w, top + height, fill=colour, width=0)
            x += w
        self.create_text(left, 16, anchor="w", text=f"{win_a * 100:.1f}%",
                         font=self.fonts.number, fill=SIDE_COLOURS[0])
        self.create_text(right, 16, anchor="e", text=f"{win_b * 100:.1f}%",
                         font=self.fonts.number, fill=SIDE_COLOURS[1])
        self.create_text(width / 2, 16, text=f"draw {draw * 100:.1f}%",
                         font=self.fonts.small, fill=MUTED)
        self.create_text(left, top + height + 16, anchor="w", text=name_a,
                         font=self.fonts.body, fill=TEXT)
        self.create_text(right, top + height + 16, anchor="e", text=name_b,
                         font=self.fonts.body, fill=TEXT)


class LogView(ttk.Frame):
    """A scrolling fight log with quiet colour coding."""

    STYLES = (
        ("round", r"^=== Round", BLUE, True),
        ("result", r"^(Result:|.*stands victorious|.*fall together|.*stalemate)", BLUE, True),
        ("note", r"^Note:", ORANGE, False),
        ("kill", r"(Killing Blow|Monster Slaying|Cleaving Blow|strikes .* down)", PURPLE, True),
        ("wound", r"(Wounded!|suffers \d+ wound)", RED, False),
        ("hit", r"- Hit!", GREEN, False),
        ("save", r"(Saved!|Regenerated!|wards off)", BLUE, False),
        ("miss", r"(Miss!|Failed!|no save)", GREY, False),
        ("head", r"(strikes at|makes \d+ (Impact Hits|Stomp Attacks)|Strike order)", None, True),
    )

    def __init__(self, master, fonts):
        super().__init__(master)
        self.text = tk.Text(self, font=fonts.log, wrap="word", relief="flat", padx=10, pady=8,
                            highlightthickness=0, height=10, bg=SURFACE, fg=TEXT)
        scroll = ttk.Scrollbar(self, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)
        self.text.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        bold = tkfont.Font(font=fonts.log)
        bold.configure(weight="bold")
        self._bold = bold
        for name, _pattern, colour, strong in self.STYLES:
            options = {"font": bold} if strong else {}
            if colour:
                options["foreground"] = colour
            self.text.tag_configure(name, **options)

    def show(self, content):
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        for line in content.splitlines():
            tag = next((n for n, pattern, _c, _s in self.STYLES if re.search(pattern, line)), None)
            self.text.insert("end", line + "\n", tag)
        self.text.configure(state="disabled")
        self.text.see("1.0")


def _rounded(canvas, x0, y0, x1, y1, r, **kw):
    """A rounded rectangle as a smoothed polygon."""
    r = min(r, (x1 - x0) / 2, (y1 - y0) / 2)
    points = [x0 + r, y0, x1 - r, y0, x1, y0, x1, y0 + r, x1, y1 - r, x1, y1,
              x1 - r, y1, x0 + r, y1, x0, y1, x0, y1 - r, x0, y0 + r, x0, y0]
    return canvas.create_polygon(points, smooth=True, **kw)
