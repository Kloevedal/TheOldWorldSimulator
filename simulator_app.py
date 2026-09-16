"""Desktop front end for the duel simulator (Tkinter, no extra dependencies).

    ./run_app.command                 # or: python3 simulator_app.py

Pick a faction, unit and gear for each fighter, then either run N duels for
statistics or fight one duel with round-by-round narration. Loadouts can be
saved as named custom characters; they appear under "Saved characters".
"""

from __future__ import annotations

import queue
import sys
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from app_model import (
    CharacterStore,
    FighterSpec,
    faction_names,
    gear_options,
    narrate_duel,
    profile_names,
    run_statistics,
)

SAVED = "★ Saved characters"
MONO = ("Menlo", 12) if sys.platform == "darwin" else ("Courier", 11)


class FighterPanel(ttk.LabelFrame):
    """Faction → unit → gear selectors for one fighter."""

    def __init__(self, master, title, store, on_saved, default_faction, default_profile):
        super().__init__(master, text=title, padding=10)
        self.store = store
        self.on_saved = on_saved
        self.faction = None  # the real faction/profile behind the selection,
        self.profile = None  # also when a saved character is selected

        self.faction_var = tk.StringVar()
        self.unit_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.weapon_var = tk.StringVar()
        self.armour_var = tk.StringVar()
        self.shield_var = tk.BooleanVar()
        self.rule_vars = {}
        self.honour_vars = {}

        self.columnconfigure(1, weight=1)
        self.faction_box = self._combo(self.faction_var, self._faction_changed)
        self.unit_box = self._combo(self.unit_var, self._unit_changed)
        self.weapon_box = self._combo(self.weapon_var, self._refresh_info)
        self.armour_box = self._combo(self.armour_var, self._refresh_info)
        row = 0
        for label, widget in (
            ("Faction", self.faction_box),
            ("Unit", self.unit_box),
            ("Name", ttk.Entry(self, textvariable=self.name_var)),
            ("Weapon", self.weapon_box),
            ("Armour", self.armour_box),
        ):
            ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=2)
            widget.grid(row=row, column=1, sticky="ew", pady=2)
            row += 1

        self.shield_check = ttk.Checkbutton(
            self, text="Shield", variable=self.shield_var, command=self._refresh_info
        )
        self.shield_check.grid(row=row, column=1, sticky="w", pady=2)
        row += 1

        self.rules_frame = ttk.Frame(self)
        self.rules_frame.grid(row=row, column=0, columnspan=2, sticky="ew")
        row += 1

        self.stat_label = ttk.Label(self, font=MONO)
        self.stat_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(8, 2))
        row += 1
        self.rules_label = ttk.Label(self, wraplength=360, foreground="gray")
        self.rules_label.grid(row=row, column=0, columnspan=2, sticky="w")
        row += 1

        buttons = ttk.Frame(self)
        buttons.grid(row=row, column=0, columnspan=2, sticky="e", pady=(8, 0))
        self.delete_button = ttk.Button(buttons, text="Delete", command=self._delete)
        self.delete_button.pack(side="right")
        ttk.Button(buttons, text="Save character…", command=self._save).pack(
            side="right", padx=(0, 6)
        )

        self.faction_box["values"] = faction_names() + [SAVED]
        self.faction_var.set(default_faction)
        self._faction_changed()
        self.unit_var.set(default_profile)
        self._unit_changed()

    def _combo(self, var, callback):
        box = ttk.Combobox(self, textvariable=var, state="readonly", width=30)
        box.bind("<<ComboboxSelected>>", lambda _e: callback())
        return box

    # -- selection ------------------------------------------------------------

    def is_saved_selection(self):
        return self.faction_var.get() == SAVED

    def refresh_saved(self):
        """Called after any save/delete so both panels list the same characters."""
        if not self.is_saved_selection():
            return
        names = self.store.names()
        self.unit_box["values"] = names
        if self.unit_var.get() not in names:
            self.unit_var.set(names[0] if names else "")
            self._unit_changed()

    def _faction_changed(self):
        if self.is_saved_selection():
            units = self.store.names()
        else:
            units = profile_names(self.faction_var.get())
        self.unit_box["values"] = units
        self.unit_var.set(units[0] if units else "")
        self._unit_changed()

    def _unit_changed(self):
        unit = self.unit_var.get()
        if not unit:
            self.faction = self.profile = None
            self._set_gear(None)
            return
        if self.is_saved_selection():
            spec = self.store.get(unit)
            self.faction, self.profile = spec.faction, spec.profile
            self._set_gear(spec)
        else:
            self.faction, self.profile = self.faction_var.get(), unit
            self._set_gear(None)
            self.name_var.set(unit)

    def _set_gear(self, spec):
        """Populate gear widgets from the profile, then apply a saved spec."""
        for child in self.rules_frame.winfo_children():
            child.destroy()
        self.rule_vars, self.honour_vars = {}, {}
        self.delete_button.state(["!disabled" if spec else "disabled"])

        if self.profile is None:
            for box in (self.weapon_box, self.armour_box):
                box["values"] = []
            self.weapon_var.set("")
            self.armour_var.set("")
            self.name_var.set("")
            self._refresh_info()
            return

        opts = gear_options(self.faction, self.profile)
        defaults = opts["defaults"]
        self.weapon_box["values"] = opts["weapons"]
        self.armour_box["values"] = opts["armour"]
        self.weapon_var.set(spec.weapon if spec else defaults["weapon"])
        self.armour_var.set(spec.armour if spec else defaults["armour"])
        self.shield_var.set(spec.shield if spec else defaults["shield"])
        self.shield_check.state(["!disabled" if opts["shield"] else "disabled"])
        if not opts["shield"]:
            self.shield_var.set(False)

        chosen = set(spec.optional_rules + spec.honours) if spec else set()
        for heading, names, store in (
            ("Upgrades", opts["optional_rules"], self.rule_vars),
            ("Elven Honours", opts["honours"], self.honour_vars),
        ):
            if not names:
                continue
            group = ttk.LabelFrame(self.rules_frame, text=heading, padding=4)
            group.pack(fill="x", pady=(4, 0))
            for i, name in enumerate(names):
                var = tk.BooleanVar(value=name in chosen)
                store[name] = var
                ttk.Checkbutton(
                    group, text=name, variable=var, command=self._refresh_info
                ).grid(row=i // 2, column=i % 2, sticky="w", padx=(0, 12))

        if spec:
            self.name_var.set(spec.name)
        self._refresh_info()

    def _refresh_info(self):
        if self.profile is None:
            self.stat_label["text"] = "No saved characters yet."
            self.rules_label["text"] = ""
            return
        try:
            spec = self.spec()
            self.stat_label["text"] = spec.statline()
            self.rules_label["text"] = ", ".join(spec.rules()) or "No special rules"
        except ValueError as exc:
            self.stat_label["text"] = "Illegal loadout"
            self.rules_label["text"] = str(exc)

    def spec(self):
        if self.profile is None:
            raise ValueError(f"{self['text']}: choose a unit first")
        return FighterSpec(
            name=self.name_var.get().strip() or self.profile,
            faction=self.faction,
            profile=self.profile,
            weapon=self.weapon_var.get(),
            armour=self.armour_var.get(),
            shield=self.shield_var.get(),
            optional_rules=[n for n, v in self.rule_vars.items() if v.get()],
            honours=[n for n, v in self.honour_vars.items() if v.get()],
        )

    # -- saving ---------------------------------------------------------------

    def _save(self):
        try:
            spec = self.spec()
            spec.build()
        except ValueError as exc:
            messagebox.showerror("Cannot save", str(exc), parent=self)
            return
        name = simpledialog.askstring(
            "Save character", "Name:", initialvalue=spec.name, parent=self
        )
        if name is None or not name.strip():
            return
        spec.name = name.strip()
        if spec.name in self.store and not messagebox.askyesno(
            "Replace character", f"Replace the saved “{spec.name}”?", parent=self
        ):
            return
        try:
            self.store.save(spec)
        except (OSError, ValueError) as exc:
            messagebox.showerror("Cannot save", str(exc), parent=self)
            return
        self.faction_var.set(SAVED)
        self.unit_box["values"] = self.store.names()
        self.unit_var.set(spec.name)
        self._unit_changed()
        self.on_saved()

    def _delete(self):
        name = self.unit_var.get()
        if not self.is_saved_selection() or name not in self.store:
            return
        if not messagebox.askyesno("Delete character", f"Delete “{name}”?", parent=self):
            return
        try:
            self.store.delete(name)
        except OSError as exc:
            messagebox.showerror("Cannot delete", str(exc), parent=self)
            return
        self.unit_var.set("")
        self.on_saved()


class SimulatorApp(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding=12)
        self.root = root
        self.store = CharacterStore()
        self.events = queue.Queue()
        self.worker = None

        root.title("The Old World Simulator")
        root.minsize(820, 640)
        self.grid(sticky="nsew")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1), weight=1, uniform="fighters")
        self.rowconfigure(2, weight=1)

        self.panels = [
            FighterPanel(self, "Fighter A", self.store, self._saved_changed,
                         "High Elves", "Prince"),
            FighterPanel(self, "Fighter B", self.store, self._saved_changed,
                         "Orcs", "Black Orc Warboss"),
        ]
        for col, panel in enumerate(self.panels):
            panel.grid(row=0, column=col, sticky="nsew", padx=(0, 6) if col == 0 else (6, 0))

        self._build_controls().grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)
        self._build_output().grid(row=2, column=0, columnspan=2, sticky="nsew")

        root.bind("<Command-Return>", lambda _e: self.run())
        root.bind("<Control-Return>", lambda _e: self.run())

    def _build_controls(self):
        bar = ttk.Frame(self)
        self.mode_var = tk.StringVar(value="stats")
        self.runs_var = tk.IntVar(value=1000)
        self.rounds_var = tk.IntVar(value=4)
        self.seed_var = tk.StringVar()

        ttk.Radiobutton(bar, text="Statistics", value="stats",
                        variable=self.mode_var, command=self._mode_changed).pack(side="left")
        ttk.Radiobutton(bar, text="Narrated duel", value="narrate",
                        variable=self.mode_var, command=self._mode_changed).pack(side="left", padx=(8, 16))
        ttk.Label(bar, text="Runs").pack(side="left")
        self.runs_box = ttk.Spinbox(bar, from_=1, to=1_000_000, increment=100,
                                    textvariable=self.runs_var, width=8)
        self.runs_box.pack(side="left", padx=(4, 12))
        ttk.Label(bar, text="Rounds").pack(side="left")
        ttk.Spinbox(bar, from_=1, to=50, textvariable=self.rounds_var, width=4).pack(
            side="left", padx=(4, 12))
        ttk.Label(bar, text="Seed").pack(side="left")
        ttk.Entry(bar, textvariable=self.seed_var, width=8).pack(side="left", padx=(4, 12))

        self.run_button = ttk.Button(bar, text="Fight!  ⌘↩", command=self.run)
        self.run_button.pack(side="right")
        self.progress = ttk.Progressbar(bar, length=140, maximum=100)
        self.progress.pack(side="right", padx=8)
        return bar

    def _build_output(self):
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        self.output = tk.Text(frame, font=MONO, wrap="word", height=16,
                              borderwidth=0, highlightthickness=0, padx=8, pady=8)
        if self.root.tk.call("tk", "windowingsystem") == "aqua":
            self.output.configure(background="systemTextBackgroundColor",
                                  foreground="systemTextColor")
        scroll = ttk.Scrollbar(frame, command=self.output.yview)
        self.output["yscrollcommand"] = scroll.set
        self.output.grid(row=0, column=0, sticky="nsew")
        scroll.grid(row=0, column=1, sticky="ns")
        self._show("Choose two fighters and press Fight!")
        return frame

    def _mode_changed(self):
        self.runs_box.state(["!disabled" if self.mode_var.get() == "stats" else "disabled"])

    def _saved_changed(self):
        for panel in self.panels:
            panel.refresh_saved()

    def _show(self, text):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.configure(state="disabled")

    # -- running --------------------------------------------------------------

    def _read_int(self, var, label, low, high):
        try:
            value = int(var.get())
        except (tk.TclError, ValueError):
            raise ValueError(f"{label} must be a whole number")
        if not low <= value <= high:
            raise ValueError(f"{label} must be between {low} and {high}")
        return value

    def run(self):
        if self.worker and self.worker.is_alive():
            return
        try:
            spec_a, spec_b = (p.spec() for p in self.panels)
            rounds = self._read_int(self.rounds_var, "Rounds", 1, 50)
            seed_text = self.seed_var.get().strip()
            seed = int(seed_text) if seed_text else None
            if self.mode_var.get() == "narrate":
                self._show(narrate_duel(spec_a, spec_b, rounds, seed))
                self.output.see("end")
                return
            runs = self._read_int(self.runs_var, "Runs", 1, 1_000_000)
            spec_a.build()
            spec_b.build()
        except ValueError as exc:
            messagebox.showerror("Cannot fight", str(exc), parent=self.root)
            return

        self.run_button.state(["disabled"])
        self.progress["value"] = 0
        self._show(f"Fighting {runs} duels…")

        def work():
            try:
                stats = run_statistics(
                    spec_a, spec_b, runs, rounds, seed,
                    progress=lambda done: self.events.put(("progress", 100 * done / runs)),
                )
                self.events.put(("done", stats.summary()))
            except Exception as exc:  # surfaced in the UI, not lost in a thread
                self.events.put(("error", f"{type(exc).__name__}: {exc}"))

        self.worker = threading.Thread(target=work, daemon=True)
        self.worker.start()
        self.after(50, self._poll)

    def _poll(self):
        finished = False
        while True:
            try:
                kind, payload = self.events.get_nowait()
            except queue.Empty:
                break
            if kind == "progress":
                self.progress["value"] = payload
            else:
                finished = True
                self.progress["value"] = 100 if kind == "done" else 0
                self._show(payload if kind == "done" else f"Simulation failed:\n{payload}")
        if finished:
            self.run_button.state(["!disabled"])
        else:
            self.after(50, self._poll)


def main():
    root = tk.Tk()
    SimulatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
