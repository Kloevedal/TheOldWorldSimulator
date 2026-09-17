"""Desktop front end for the simulator (Tkinter, native look).

    ./run_app.command                 # or: python3 simulator_app.py

One screen: pick two fighters, press Fight.

* Duel / Units at the top switches between character duels and unit fights.
  Rank-and-file combat is not simulated yet, so units fight as single models;
  the Units screen says so.
* Each fighter card has the essentials: army, model, name, weapon, armour,
  mount and shield. "Extras…" opens upgrades, Marks of Chaos and Vows, and the
  magic item and ability shop, sorted into tabs, with a switch to show or hide
  the common (rulebook) items. Search matches item names and the rules they
  grant, so "killing blow" finds the Headsman's Axe.
* Each card shows the fighter's points: the model plus priced weapons,
  armour, shield, mount, upgrades and items.
* Odds fights 100 times to the death by default; Play-by-play fights once
  (six rounds by default) and shows every roll. Untick "To the death" to set
  a round limit; each mode remembers its own.
* Save… keeps a fighter under a name; saved fighters are listed under
  "★ Saved" in the army picker.
"""

from __future__ import annotations

import queue
import threading
import tkinter as tk
from tkinter import simpledialog, ttk

import ui_kit as ui
from app_model import (
    CHARACTER,
    DEFAULT_NARRATION_ROUNDS,
    DEFAULT_RUNS,
    TO_THE_DEATH,
    UNIT,
    UNIT_COMBAT_NOTE,
    CharacterStore,
    FighterSpec,
    armour_choices,
    choice_label,
    faction_names,
    gear_options,
    compare_stats,
    is_two_handed,
    item_matches,
    narrate_duel,
    option_price,
    points_breakdown,
    profile_names,
    purchasable_items,
    purchase_problem,
    rounds_text,
    run_statistics,
    spent,
    weapon_choices,
    weapon_summary,
)

SAVED = "★ Saved"
ON_FOOT = "On foot"
NOUN = {CHARACTER: "Character", UNIT: "Unit"}
DEFAULTS = {
    CHARACTER: [("High Elf Realms", "Prince"), ("Orc & Goblin Tribes", "Black Orc Warboss")],
    UNIT: [("Empire of Man", "State Troops"), ("Orc & Goblin Tribes", "Orc Mob")],
}
STATUS_MARKS = {"partial": "partly simulated", "not modelled": "not simulated",
                "no duel effect": "no effect in a duel"}


def _default_pick(kind, index):
    faction, profile = DEFAULTS[kind][index]
    if profile in profile_names(faction, kind):
        return faction, profile
    factions = faction_names(kind)
    if not factions:
        return None, None
    faction = factions[min(index, len(factions) - 1)]
    names = profile_names(faction, kind)
    return faction, (names[0] if names else None)


def _combo(master, variable, command, width=26):
    box = ttk.Combobox(master, textvariable=variable, state="readonly", width=width)
    box.bind("<<ComboboxSelected>>", lambda _e: command())
    return box


class LabelledChoice:
    """A read-only combobox whose entries carry extra text (price, profile)
    while get() and set() deal in the plain names."""

    def __init__(self, master, command, width=34):
        self.var = tk.StringVar()
        self.box = _combo(master, self.var, command, width=width)
        self._names, self._labels = {}, {}

    def set_choices(self, names, label=str):
        self._labels = {name: label(name) for name in names}
        self._names = {text: name for name, text in self._labels.items()}
        self.box["values"] = [self._labels[n] for n in names]

    def choices(self):
        return list(self._labels)

    def get(self):
        text = self.var.get()
        return self._names.get(text, text)

    def set(self, name):
        self.var.set(self._labels.get(name, name))


class FighterCard(ttk.LabelFrame):
    """One side of the fight."""

    def __init__(self, master, app, kind, side, default):
        super().__init__(master, text=f"Fighter {'AB'[side]}", padding=12, style="Card.TLabelframe")
        self.app, self.kind, self.side = app, kind, side
        self.faction = self.profile = None
        self.opts = {}
        self.optional_rules, self.exclusive, self.magic_items = [], {}, []

        self.army_var, self.model_var, self.name_var = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.shield_var = tk.BooleanVar()
        self.models_var, self.frontage_var = tk.IntVar(value=20), tk.IntVar(value=5)

        form = ttk.Frame(self)
        form.pack(fill="x")
        form.columnconfigure(1, weight=1)
        self.army_box = _combo(form, self.army_var, self._army_changed)
        self.model_box = _combo(form, self.model_var, self._model_changed)
        self.weapon_var = LabelledChoice(form, self._weapon_changed)
        self.armour_var = LabelledChoice(form, self.refresh)
        self.mount_var = LabelledChoice(form, self.refresh)
        self.weapon_box, self.armour_box, self.mount_box = (
            self.weapon_var.box, self.armour_var.box, self.mount_var.box)
        rows = [("Army", self.army_box), (NOUN[kind], self.model_box),
                ("Name", ttk.Entry(form, textvariable=self.name_var)),
                ("Weapon", self.weapon_box), ("Armour", self.armour_box)]
        if kind == CHARACTER:
            rows.append(("Mount", self.mount_box))
        for row, (text, widget) in enumerate(rows):
            ttk.Label(form, text=text).grid(row=row, column=0, sticky="w", pady=3, padx=(0, 10))
            widget.grid(row=row, column=1, sticky="ew", pady=3)
        row = len(rows)
        self.shield_check = ttk.Checkbutton(form, text="Shield", variable=self.shield_var,
                                            command=self.refresh)
        self.shield_check.grid(row=row, column=1, sticky="w", pady=(4, 0))
        if kind == UNIT:
            size = ttk.Frame(form)
            size.grid(row=row + 1, column=0, columnspan=2, sticky="w", pady=(6, 0))
            ttk.Label(size, text="Models").pack(side="left")
            ttk.Spinbox(size, from_=1, to=200, width=5, textvariable=self.models_var,
                        command=self.refresh).pack(side="left", padx=(6, 14))
            ttk.Label(size, text="Width").pack(side="left")
            ttk.Spinbox(size, from_=1, to=40, width=4, textvariable=self.frontage_var,
                        command=self.refresh).pack(side="left", padx=6)
            self.ranks_label = ttk.Label(size, style="Muted.TLabel")
            self.ranks_label.pack(side="left", padx=6)

        self.stats = ui.StatTiles(self, app.fonts, ui.SIDE_COLOURS[side])
        self.stats.pack(fill="x", pady=(12, 0))
        ttk.Label(self, text="With gear (bare profile) · first-round values",
                  style="Muted.TLabel").pack(anchor="e")
        self.weapon_label = ttk.Label(self, style="Muted.TLabel", justify="left", wraplength=430)
        self.weapon_label.pack(fill="x", pady=(2, 4))
        self.points_label = ttk.Label(self, style="Heading.TLabel")
        self.points_label.pack(fill="x")
        self.points_detail = ttk.Label(self, style="Muted.TLabel", justify="left", wraplength=430)
        self.points_detail.pack(fill="x", pady=(0, 4))
        self.rules_label = ttk.Label(self, style="Muted.TLabel", justify="left", wraplength=430)
        self.rules_label.pack(fill="x")
        self.extras_label = ttk.Label(self, style="Accent.TLabel", justify="left", wraplength=430)
        self.extras_label.pack(fill="x", pady=(4, 0))

        buttons = ttk.Frame(self)
        buttons.pack(fill="x", pady=(10, 0))
        self.extras_button = ttk.Button(buttons, text="Extras…", command=self._open_extras)
        self.extras_button.pack(side="left")
        ttk.Button(buttons, text="Save…", command=self._save).pack(side="left", padx=6)
        self.delete_button = ttk.Button(buttons, text="Delete", command=self._delete)
        self.delete_button.pack(side="left")

        self.army_box["values"] = faction_names(kind) + [SAVED]
        faction, profile = default
        self.army_var.set(faction or SAVED)
        self._army_changed()
        if profile:
            self.model_var.set(profile)
            self._model_changed()

    # -- choices ----------------------------------------------------------------

    def is_saved(self):
        return self.army_var.get() == SAVED

    def refresh_saved(self):
        if not self.is_saved():
            return
        names = self.app.store.names(self.kind)
        self.model_box["values"] = names
        if self.model_var.get() not in names:
            self.model_var.set(names[0] if names else "")
            self._model_changed()

    def _army_changed(self):
        names = (self.app.store.names(self.kind) if self.is_saved()
                 else profile_names(self.army_var.get(), self.kind))
        self.model_box["values"] = names
        self.model_var.set(names[0] if names else "")
        self._model_changed()

    def _model_changed(self):
        chosen = self.model_var.get()
        spec = None
        if not chosen:
            self.faction = self.profile = None
        elif self.is_saved():
            spec = self.app.store.get(chosen, self.kind)
            self.faction, self.profile = spec.faction, spec.profile
        else:
            self.faction, self.profile = self.army_var.get(), chosen
        self._load(spec)

    def _load(self, spec):
        """Reset the card to a profile, then apply a saved spec if given."""
        self.delete_button.state(["!disabled" if spec else "disabled"])
        if self.profile is None:
            for var in (self.weapon_var, self.armour_var, self.mount_var):
                var.set_choices([])
                var.set("")
            self.name_var.set("")
            self.opts, self.optional_rules, self.exclusive, self.magic_items = {}, [], {}, []
            self.refresh()
            return
        opts = self.opts = gear_options(self.faction, self.profile)
        defaults = opts["defaults"]
        self.magic_items = list(spec.magic_items) if spec else []
        chosen_rules = list(spec.optional_rules) if spec else []
        self.exclusive = {group: next((r for r in chosen_rules if r in choices), default)
                          for group, choices, default in opts["exclusive"]}
        self.optional_rules = [r for r in chosen_rules if r in opts["optional_rules"]]
        self._update_equipment_lists()
        self.weapon_var.set(spec.weapon if spec else defaults["weapon"])
        self.armour_var.set(spec.armour if spec else defaults["armour"])
        self.shield_var.set(spec.shield if spec else defaults["shield"])
        self.name_var.set(spec.name if spec else self.profile)
        self._set_mounts(spec.mount if spec else None)
        if self.kind == UNIT:
            minimum = (opts["unit"] or {}).get("minimum_size", 1)
            self.models_var.set(spec.models if spec else max(minimum, 10))
            self.frontage_var.set(spec.frontage if spec else min(self.models_var.get(), 5))
        has_extras = bool(opts["optional_rules"] or opts["exclusive"] or opts["allowance"])
        self.extras_button.state(["!disabled" if has_extras else "disabled"])
        self._weapon_changed()

    def _set_mounts(self, chosen):
        fixed = self.opts.get("fixed_mount")
        if fixed:
            self.mount_var.set_choices([fixed])
            self.mount_var.set(fixed)
            self.mount_box.state(["disabled"])
            return
        mounts = self.opts.get("mounts", [])
        self.mount_var.set_choices([ON_FOOT] + mounts, lambda m: m if m == ON_FOOT else
                                   choice_label(self.faction, self.profile, "mounts", m))
        self.mount_var.set(chosen if chosen in mounts else ON_FOOT)
        self.mount_box.state(["!disabled" if mounts else "disabled"])

    def _update_equipment_lists(self):
        """Weapons and armour, including any the bought abilities unlock."""
        weapons = weapon_choices(self.faction, self.profile, self.magic_items)
        armour = armour_choices(self.faction, self.profile, self.magic_items)
        self.weapon_var.set_choices(
            weapons, lambda w: choice_label(self.faction, self.profile, "weapons", w))
        self.armour_var.set_choices(
            armour, lambda a: choice_label(self.faction, self.profile, "armour", a))
        shield_cost = option_price(self.faction, self.profile, "shield", "Shield")
        self.shield_check.configure(text=f"Shield · +{shield_cost} pts" if shield_cost else "Shield")
        defaults = self.opts["defaults"]
        if self.weapon_var.get() not in weapons:
            self.weapon_var.set(defaults["weapon"])
        if self.armour_var.get() not in armour:
            self.armour_var.set(defaults["armour"])

    def _weapon_changed(self):
        usable = self.opts.get("shield") and not is_two_handed(self.weapon_var.get())
        self.shield_check.state(["!disabled" if usable else "disabled"])
        if not usable:
            self.shield_var.set(False)
        self.refresh()

    def chosen_rules(self):
        """Upgrades plus any Mark or Vow that differs from the profile default."""
        rules = list(self.optional_rules)
        for group, _choices, default in self.opts.get("exclusive", []):
            picked = self.exclusive.get(group, default)
            if picked != default:
                rules.append(picked)
        return rules

    def spec(self):
        if self.profile is None:
            raise ValueError(f"Fighter {'AB'[self.side]}: choose a {NOUN[self.kind].lower()} first")
        models = frontage = 1
        if self.kind == UNIT:
            try:
                models, frontage = int(self.models_var.get()), int(self.frontage_var.get())
            except (tk.TclError, ValueError):
                raise ValueError("Models and width must be whole numbers")
        mount = self.mount_var.get()
        if mount in (ON_FOOT, "") or mount == self.opts.get("fixed_mount"):
            mount = None
        return FighterSpec(
            name=self.name_var.get().strip() or self.profile,
            faction=self.faction, profile=self.profile,
            weapon=self.weapon_var.get(), armour=self.armour_var.get(),
            shield=self.shield_var.get(), optional_rules=self.chosen_rules(),
            magic_items=list(self.magic_items), mount=mount,
            kind=self.kind, models=models, frontage=frontage,
        )

    def refresh(self):
        if self.profile is None:
            self.stats.show(message=f"No saved {NOUN[self.kind].lower()}s yet")
            self._show_points(None)
            self.weapon_label.configure(text="")
            self.rules_label.configure(text="")
            self.extras_label.configure(text="")
            return
        try:
            spec = self.spec()
            built = spec.build()
        except ValueError as exc:
            self.stats.show(message="Not a legal loadout")
            self._show_points(None)
            self.weapon_label.configure(text="")
            self.rules_label.configure(text=str(exc))
            self.extras_label.configure(text="")
            return
        self.stats.show(compare_stats(spec))
        profile = weapon_summary(spec.weapon)
        self.weapon_label.configure(text=f"{spec.weapon}: {profile}" if profile else "")
        self._show_points(spec)
        self.rules_label.configure(text=", ".join(built.SpecialRules) or "No special rules")
        lines = []
        extras = [*self.chosen_rules(), *self.magic_items]
        if extras:
            lines.append("Extras: " + ", ".join(extras))
        for part in built.mount_parts:
            label = part.name.split("'s ", 1)[-1]
            lines.append(f"{label}: WS{part.WeaponSkill} S{part.Strength} "
                         f"I{part.Initiative} A{part.Attacks}")
        self.extras_label.configure(text="\n".join(lines))
        if self.kind == UNIT:
            self.ranks_label.configure(text=f"{spec.ranks} ranks")

    def _show_points(self, spec):
        if spec is None:
            self.points_label.configure(text="")
            self.points_detail.configure(text="")
            return
        lines = points_breakdown(spec)
        self.points_label.configure(text=f"{sum(c for _l, c in lines)} points")
        self.points_detail.configure(
            text=" + ".join(f"{label} {cost}" for label, cost in lines) if len(lines) > 1 else "")

    # -- extras, saving -------------------------------------------------------

    def _open_extras(self):
        if self.profile is not None:
            ExtrasDialog(self)

    def extras_changed(self):
        self._update_equipment_lists()
        self._weapon_changed()

    def _save(self):
        try:
            spec = self.spec()
            spec.build()
        except ValueError as exc:
            self.app.status(str(exc), error=True)
            return
        name = simpledialog.askstring("Save fighter", "Name:", initialvalue=spec.name, parent=self)
        if not name or not name.strip():
            return
        spec.name = name.strip()
        try:
            self.app.store.save(spec)
        except (OSError, ValueError) as exc:
            self.app.status(str(exc), error=True)
            return
        self.army_var.set(SAVED)
        self.model_box["values"] = self.app.store.names(self.kind)
        self.model_var.set(spec.name)
        self._model_changed()
        self.app.saved_changed()
        self.app.status(f"Saved {spec.name}")

    def _delete(self):
        name = self.model_var.get()
        if not self.is_saved() or not self.app.store.contains(name, self.kind):
            return
        self.app.store.delete(name, self.kind)
        self.model_var.set("")
        self.app.saved_changed()
        self.app.status(f"Deleted {name}")


class ExtrasDialog(tk.Toplevel):
    """Upgrades, Marks/Vows and the item shop for one fighter."""

    def __init__(self, card):
        super().__init__(card)
        self.card = card
        self.title(f"Extras — {card.profile}")
        self.configure(bg=ui.BACKGROUND)
        self.transient(card.winfo_toplevel())
        body = ttk.Frame(self, padding=14)
        body.pack(fill="both", expand=True)

        self.optional = {r: tk.BooleanVar(value=r in card.optional_rules)
                         for r in card.opts["optional_rules"]}
        self.exclusive = {g: tk.StringVar(value=card.exclusive.get(g, d))
                          for g, _c, d in card.opts["exclusive"]}
        self.items = list(card.magic_items)
        self.catalogue = {i["name"]: i for i in purchasable_items(card.faction, card.profile)}

        options = ttk.Frame(body)
        options.pack(fill="x")
        if self.optional:
            box = ttk.LabelFrame(options, text="Upgrades", padding=8)
            box.pack(side="left", fill="y", padx=(0, 10))
            for rule, var in self.optional.items():
                ttk.Checkbutton(box, text=rule, variable=var).pack(anchor="w")
        for group, choices, _default in card.opts["exclusive"]:
            box = ttk.LabelFrame(options, text=group, padding=8)
            box.pack(side="left", fill="y", padx=(0, 10))
            for choice in choices:
                ttk.Radiobutton(box, text=choice, value=choice,
                                variable=self.exclusive[group]).pack(anchor="w")

        if self.catalogue:
            self._build_shop(body)
        self.message = ttk.Label(body, style="Error.TLabel")
        self.message.pack(fill="x", pady=(8, 0))
        buttons = ttk.Frame(body)
        buttons.pack(fill="x", pady=(6, 0))
        ttk.Button(buttons, text="Done", command=self._done, default="active").pack(side="right")
        ttk.Button(buttons, text="Cancel", command=self.destroy).pack(side="right", padx=8)
        self.bind("<Return>", lambda _e: self._done())
        self.bind("<Escape>", lambda _e: self.destroy())
        self._refresh_shop()
        self.grab_set()

    # -- the shop -------------------------------------------------------------

    def _build_shop(self, body):
        shop = ttk.LabelFrame(body, text="Magic items & abilities", padding=10)
        shop.pack(fill="both", expand=True, pady=(10, 0))
        top = ttk.Frame(shop)
        top.pack(fill="x")
        ttk.Label(top, text="Search names & rules").pack(side="left")
        self.search = tk.StringVar()
        entry = ttk.Entry(top, textvariable=self.search, width=28)
        entry.pack(side="left", padx=6)
        entry.bind("<KeyRelease>", lambda _e: self._refresh_shop())
        self.show_common = tk.BooleanVar(value=True)
        common_count = sum(1 for i in self.catalogue.values() if i["common"])
        ttk.Checkbutton(top, text=f"Common items ({common_count})", variable=self.show_common,
                        command=self._refresh_shop).pack(side="left", padx=12)
        self.budget_label = ttk.Label(top, style="Muted.TLabel")
        self.budget_label.pack(side="right")

        panes = ttk.Frame(shop)
        panes.pack(fill="both", expand=True, pady=(8, 0))
        self.notebook = ttk.Notebook(panes)
        self.notebook.pack(side="left", fill="both", expand=True)
        self.trees = {}
        for pane in sorted({i["pane"] for i in self.catalogue.values()}):
            frame = ttk.Frame(self.notebook)
            tree = self._tree(frame, ("cost", "profile", "notes"), ("Points", "Profile", "Notes"),
                              (60, 300, 130), width=220)
            tree.bind("<Double-1>", lambda _e, t=tree: self._add(t))
            tree.bind("<<TreeviewSelect>>", lambda _e, t=tree: self._describe(t))
            self.notebook.add(frame, text=pane)
            self.trees[pane] = (frame, tree)

        side = ttk.Frame(panes)
        side.pack(side="left", fill="y", padx=(10, 0))
        ttk.Button(side, text="Add →", command=self._add_selected).pack(fill="x")
        ttk.Button(side, text="← Remove", command=self._remove).pack(fill="x", pady=6)
        ttk.Label(side, text="Chosen", style="Heading.TLabel").pack(anchor="w", pady=(8, 2))
        chosen_frame = ttk.Frame(side)
        chosen_frame.pack(fill="both", expand=True)
        self.chosen = self._tree(chosen_frame, ("cost",), ("Points",), (60,), width=200)
        self.chosen.bind("<Double-1>", lambda _e: self._remove())
        self.chosen.bind("<<TreeviewSelect>>", lambda _e: self._describe(self.chosen))

        self.description = ttk.Label(shop, style="Muted.TLabel", justify="left", wraplength=820)
        self.description.pack(fill="x", pady=(8, 0))

    def _tree(self, master, columns, headings, widths, width=300):
        tree = ttk.Treeview(master, columns=columns, height=12, selectmode="browse")
        tree.heading("#0", text="Name")
        tree.column("#0", width=width, stretch=True)
        for column, heading, w in zip(columns, headings, widths):
            tree.heading(column, text=heading)
            tree.column(column, width=w, stretch=False, anchor="w")
        scroll = ttk.Scrollbar(master, command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        return tree

    def _refresh_shop(self):
        if not self.catalogue:
            return
        needle = self.search.get().strip().lower()
        show_common = self.show_common.get()
        first_hit = None
        for pane, (frame, tree) in self.trees.items():
            tree.delete(*tree.get_children())
            shown = 0
            for item in self.catalogue.values():
                if item["pane"] != pane or (item["common"] and not show_common):
                    continue
                if needle and not item_matches(item, needle):
                    continue
                notes = STATUS_MARKS.get(item["status"], "")
                if item["common"]:
                    notes = ("common · " + notes) if notes else "common"
                tree.insert("", "end", iid=item["name"], text=item["name"],
                            values=(item["cost"], item["summary"] or "–", notes))
                shown += 1
            self.notebook.tab(frame, text=f"{pane} ({shown})")
            if shown and first_hit is None:
                first_hit = frame
        # Searching jumps to a tab with results if the current one has none.
        current = self.notebook.select()
        if needle and first_hit is not None and not any(
                str(f) == current and t.get_children() for f, t in self.trees.values()):
            self.notebook.select(first_hit)
        self.chosen.delete(*self.chosen.get_children())
        for index, name in enumerate(self.items):
            self.chosen.insert("", "end", iid=str(index), text=name,
                               values=(self.catalogue.get(name, {}).get("cost", ""),))
        used = spent(self.items)
        parts = []
        for budget, limit in self.card.opts["allowance"].items():
            if limit is None:
                count = sum(1 for n in self.items if self.catalogue.get(n, {}).get("budget") == budget)
                parts.append(f"{budget}: {count} chosen")
            else:
                parts.append(f"{budget}: {used.get(budget, 0)}/{limit} pts")
        self.budget_label.configure(text="   ".join(parts))

    def _describe(self, tree):
        selection = tree.selection()
        if not selection:
            return
        name = tree.item(selection[0], "text")
        item = self.catalogue.get(name, {"text": ""})
        status = STATUS_MARKS.get(item.get("status"), "simulated")
        summary = item.get("summary")
        profile = f"\n{summary}" if summary else ""
        self.description.configure(text=f"{name} ({status}){profile}\n{item.get('text', '')}")

    def _add_selected(self):
        current = self.notebook.select()
        for frame, tree in self.trees.values():
            if str(frame) == current:
                self._add(tree)

    def _add(self, tree):
        selection = tree.selection()
        if not selection:
            return
        name = tree.item(selection[0], "text")
        problem = purchase_problem(self.card.faction, self.card.profile, self.items + [name])
        if problem:
            self.message.configure(text=problem)
            return
        self.items.append(name)
        self.message.configure(text="")
        self._refresh_shop()

    def _remove(self):
        selection = self.chosen.selection()
        if selection:
            del self.items[int(selection[0])]
            self._refresh_shop()

    def _done(self):
        card = self.card
        previous = (list(card.optional_rules), dict(card.exclusive), list(card.magic_items))
        card.optional_rules = [r for r, v in self.optional.items() if v.get()]
        card.exclusive = {g: v.get() for g, v in self.exclusive.items()}
        card.magic_items = list(self.items)
        card.extras_changed()
        try:
            card.spec().build()
        except ValueError as exc:
            card.optional_rules, card.exclusive, card.magic_items = previous
            card.extras_changed()
            self.message.configure(text=str(exc))
            return
        self.destroy()


class BattleScreen(ttk.Frame):
    """Both fighters for one mode, side by side."""

    def __init__(self, master, app, kind):
        super().__init__(master)
        self.kind = kind
        if kind == UNIT:
            ttk.Label(self, text=UNIT_COMBAT_NOTE, style="Warning.TLabel", wraplength=1000,
                      justify="left").pack(fill="x", pady=(0, 8))
        row = ttk.Frame(self)
        row.pack(fill="both", expand=True)
        row.columnconfigure((0, 2), weight=1, uniform="cards")
        self.cards = [FighterCard(row, app, kind, i, _default_pick(kind, i)) for i in (0, 1)]
        self.cards[0].grid(row=0, column=0, sticky="nsew")
        ttk.Label(row, text="vs", style="Heading.TLabel").grid(row=0, column=1, padx=14)
        self.cards[1].grid(row=0, column=2, sticky="nsew")


class SimulatorApp(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding=16)
        self.root = root
        self.fonts = ui.Fonts(root)
        ui.apply_style(root, self.fonts)
        self.store = CharacterStore()
        self.events = queue.Queue()
        self.worker = None
        root.title("Old World Simulator")
        root.minsize(980, 700)
        self.pack(fill="both", expand=True)

        header = ttk.Frame(self)
        header.pack(fill="x", pady=(0, 12))
        ttk.Label(header, text="Old World Simulator", style="Title.TLabel").pack(side="left")
        self.mode_var = tk.StringVar(value=CHARACTER)
        modes = ttk.Frame(header)
        modes.pack(side="right")
        for value, text in ((CHARACTER, "Duel"), (UNIT, "Units")):
            ttk.Radiobutton(modes, text=text, value=value, variable=self.mode_var,
                            style="Toolbutton", command=self._mode_changed).pack(side="left")

        self.screens = {kind: BattleScreen(self, self, kind) for kind in (CHARACTER, UNIT)}
        self.screen = self.screens[CHARACTER]
        self.screen.pack(fill="x")
        self._build_controls()
        self._build_results()
        self.status_label = ttk.Label(self, style="Muted.TLabel")
        self.status_label.pack(fill="x", pady=(6, 0))
        for key in ("<Command-Return>", "<Control-Return>"):
            root.bind(key, lambda _e: self.run())

    @property
    def cards(self):
        return self.screens[self.mode_var.get()].cards

    def _build_controls(self):
        bar = ttk.Frame(self)
        bar.pack(fill="x", pady=12)
        self.controls = bar
        self.run_mode = tk.StringVar(value="odds")
        for value, text in (("odds", "Odds"), ("narrate", "Play-by-play")):
            ttk.Radiobutton(bar, text=text, value=value, variable=self.run_mode, style="Toolbutton",
                            command=self._run_mode_changed).pack(side="left")
        self.runs_var = tk.IntVar(value=DEFAULT_RUNS)
        self.rounds_var = tk.IntVar(value=DEFAULT_NARRATION_ROUNDS)
        self.death_var = tk.BooleanVar(value=True)
        # Each run mode keeps its own round settings.
        self.mode_rounds = {"odds": (DEFAULT_NARRATION_ROUNDS, True),
                            "narrate": (DEFAULT_NARRATION_ROUNDS, False)}
        self.seed_var = tk.StringVar()
        ttk.Label(bar, text="Fights").pack(side="left", padx=(16, 4))
        self.runs_box = ttk.Spinbox(bar, from_=1, to=100000, increment=100, width=7,
                                    textvariable=self.runs_var)
        self.runs_box.pack(side="left")
        ttk.Label(bar, text="Rounds").pack(side="left", padx=(16, 4))
        self.rounds_box = ttk.Spinbox(bar, from_=1, to=50, width=4, textvariable=self.rounds_var)
        self.rounds_box.pack(side="left")
        ttk.Checkbutton(bar, text="To the death", variable=self.death_var,
                        command=self._death_changed).pack(side="left", padx=(8, 0))
        self._death_changed()
        ttk.Label(bar, text="Seed").pack(side="left", padx=(16, 4))
        ttk.Entry(bar, textvariable=self.seed_var, width=8).pack(side="left")
        self.fight_button = ttk.Button(bar, text="Fight", command=self.run, default="active")
        self.fight_button.pack(side="right")
        self.progress = ttk.Progressbar(bar, length=160, maximum=1.0)
        self.progress.pack(side="right", padx=12)

    def _build_results(self):
        self.results = ttk.LabelFrame(self, text="Result", padding=12, style="Card.TLabelframe")
        self.results.pack(fill="both", expand=True)
        self.winbar = ui.WinBar(self.results, self.fonts)
        self.details = ttk.Label(self.results, style="Muted.TLabel", justify="left")
        self.log = ui.LogView(self.results, self.fonts)
        self.placeholder = ttk.Label(self.results, text="Pick two fighters and press Fight.",
                                     style="Muted.TLabel")
        self._show_only(self.placeholder)

    def _show_only(self, *widgets):
        for child in (self.winbar, self.details, self.log, self.placeholder):
            child.pack_forget()
        for widget in widgets:
            widget.pack(fill="both" if widget is self.log else "x", expand=widget is self.log)

    def _mode_changed(self):
        self.screen.pack_forget()
        self.screen = self.screens[self.mode_var.get()]
        self.screen.pack(fill="x", before=self.controls)
        self._show_only(self.placeholder)

    def _death_changed(self):
        self.rounds_box.state(["disabled" if self.death_var.get() else "!disabled"])

    def _run_mode_changed(self):
        """Odds defaults to fighting to the death, Play-by-play to six rounds;
        each mode gets its own settings back when switched to."""
        mode = self.run_mode.get()
        narrate = mode == "narrate"
        left = "odds" if narrate else "narrate"
        try:
            current = int(self.rounds_var.get())
        except (tk.TclError, ValueError):
            current = self.mode_rounds[left][0]
        self.mode_rounds[left] = (current, self.death_var.get())
        rounds, death = self.mode_rounds[mode]
        self.rounds_var.set(rounds)
        self.death_var.set(death)
        self.runs_box.state(["disabled" if narrate else "!disabled"])
        self._death_changed()

    def saved_changed(self):
        for screen in self.screens.values():
            for card in screen.cards:
                card.refresh_saved()

    def status(self, text, error=False):
        self.status_label.configure(text=text, style="Error.TLabel" if error else "Muted.TLabel")

    # -- running ------------------------------------------------------------------

    def busy(self):
        return bool(self.worker and self.worker.is_alive())

    def _number(self, var, label, low, high):
        try:
            value = int(var.get())
        except (tk.TclError, ValueError):
            raise ValueError(f"{label} must be a whole number")
        if not low <= value <= high:
            raise ValueError(f"{label} must be between {low} and {high}")
        return value

    def run(self):
        if self.busy():
            return
        try:
            spec_a, spec_b = (card.spec() for card in self.cards)
            rounds = (TO_THE_DEATH if self.death_var.get()
                      else self._number(self.rounds_var, "Rounds", 1, 50))
            seed_text = self.seed_var.get().strip()
            seed = int(seed_text) if seed_text else None
            if self.run_mode.get() == "narrate":
                self.log.show(narrate_duel(spec_a, spec_b, rounds, seed))
                self._show_only(self.log)
                self.status("")
                return
            runs = self._number(self.runs_var, "Fights", 1, 100000)
            spec_a.build()
            spec_b.build()
        except ValueError as exc:
            self.status(str(exc), error=True)
            return

        self.fight_button.state(["disabled"])
        self.progress["value"] = 0
        self.status(f"Fighting {runs} times…")

        def work():
            try:
                stats = run_statistics(
                    spec_a, spec_b, runs, rounds, seed,
                    progress=lambda done: self.events.put(("progress", done / runs)))
                self.events.put(("done", stats))
            except Exception as exc:  # shown in the window, not lost in a thread
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
            elif kind == "done":
                finished = True
                self._show_stats(payload)
            else:
                finished = True
                self.status(payload, error=True)
        if finished:
            self.fight_button.state(["!disabled"])
        else:
            self.after(50, self._poll)

    def _show_stats(self, stats):
        runs = stats.runs or 1
        self.winbar.show(stats.name_a, stats.wins_a / runs, stats.draws / runs,
                         stats.name_b, stats.wins_b / runs)

        def line(name, wins, kills, left):
            average = left / wins if wins else 0
            return (f"{name}: {wins} wins ({kills} by slaying, {wins - kills} on wounds), "
                    f"{average:.2f} wounds left on average when winning")

        text = "\n".join([
            f"{stats.runs} fights, {rounds_text(stats.rounds)}",
            line(stats.name_a, stats.wins_a, stats.kills_a, stats.wounds_left_a),
            line(stats.name_b, stats.wins_b, stats.kills_b, stats.wounds_left_b),
            f"Draws: {stats.draws}",
        ])
        if stats.kind == UNIT:
            text = "Units fight as single models for now.\n" + text
        self.details.configure(text=text)
        self._show_only(self.winbar, self.details)
        self.progress["value"] = 1
        self.status("")


def main():
    root = tk.Tk()
    SimulatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
