// The Old World Duel Simulator page. The simulator itself runs in worker.js.
//
// Safety rule for this file: never use innerHTML (or insertAdjacentHTML,
// outerHTML, document.write). Fighter names come from share links and saved
// data, so every piece of text goes in with textContent via el().
"use strict";

// -- helpers -------------------------------------------------------------------

function el(tag, props = {}, ...children) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(props)) {
    if (key === "class") node.className = value;
    else if (key === "dataset") Object.assign(node.dataset, value);
    else if (key.startsWith("on")) node.addEventListener(key.slice(2), value);
    else if (key in node) node[key] = value;
    else node.setAttribute(key, value);
  }
  for (const child of children.flat()) {
    if (child === null || child === undefined || child === false) continue;
    node.append(child instanceof Node ? child : document.createTextNode(String(child)));
  }
  return node;
}

const $ = (id) => document.getElementById(id);
const store = {
  get(key, fallback) {
    try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; } catch { return fallback; }
  },
  set(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch { return false; }
  },
};

function encodeSpec(spec) {
  const bytes = new TextEncoder().encode(JSON.stringify(spec));
  let binary = "";
  bytes.forEach((b) => { binary += String.fromCharCode(b); });
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function decodeSpec(text) {
  if (typeof text !== "string" || text.length > 4000 || !/^[A-Za-z0-9_-]+$/.test(text)) return null;
  try {
    const binary = atob(text.replace(/-/g, "+").replace(/_/g, "/"));
    const data = JSON.parse(new TextDecoder().decode(Uint8Array.from(binary, (c) => c.charCodeAt(0))));
    return data && typeof data === "object" && !Array.isArray(data) ? data : null;
  } catch { return null; }
}

// -- the simulator worker --------------------------------------------------------

const worker = new Worker("worker.js?v=__BUILD__");
const pending = new Map();
let nextId = 1;
worker.onmessage = ({ data }) => {
  const job = pending.get(data.id);
  if (!job) return;
  if ("progress" in data) { job.onProgress?.(data.progress); return; }
  pending.delete(data.id);
  if ("error" in data) job.reject(new Error(data.error)); else job.resolve(data.result);
};
worker.onerror = (e) => fail("The simulator could not start: " + (e.message || "unknown error"));

function api(name, args = [], onProgress) {
  return new Promise((resolve, reject) => {
    const id = nextId++;
    pending.set(id, { resolve, reject, onProgress });
    worker.postMessage({ id, name, args });
  });
}

// -- state -----------------------------------------------------------------------

const SAVED = "★ Saved";
const ON_FOOT = "On foot";
const NOUN = { character: "Character", unit: "Unit" };
const STAT_NAMES = ["WS", "S", "T", "W", "I", "A", "Ld"];
const LOG_STYLES = [
  ["round", /^=== Round/], ["result", /^(Result:|.*stands victorious|.*fall together|.*stalemate)/],
  ["note", /^Note:/], ["kill", /(Killing Blow|Monster Slaying|Cleaving Blow|strikes .* down)/],
  ["wound", /(Wounded!|suffers \d+ wound)/], ["hit", /- Hit!/], ["save", /(Saved!|Regenerated!|wards off)/],
  ["miss", /(Miss!|Failed!|no save)/], ["head", /(strikes at|makes \d+ (Impact Hits|Stomp Attacks)|Strike order)/],
];

let catalog = null;
let mode = "character";
let runMode = "odds";
const runSettings = { odds: { rounds: 6, death: true }, narrate: { rounds: 6, death: false } };
const decks = {};  // mode -> [Card, Card]

function savedFighters(kind) {
  const all = store.get("tow-saved", {});
  return all && typeof all[kind] === "object" ? all[kind] : {};
}

function setStatus(text, isError = false) {
  $("status").textContent = text;
  $("status").classList.toggle("error", isError);
}

function fail(text) {
  $("loading").hidden = false;
  $("loading").replaceChildren(el("p", { class: "error" }, text),
    el("p", { class: "muted" }, "Reload the page to try again."));
}

// -- a fighter card ----------------------------------------------------------------

class Card {
  constructor(kind, side) {
    this.kind = kind;
    this.side = side;
    this.faction = null;
    this.profile = null;
    this.opts = null;
    this.optionalRules = [];
    this.exclusive = {};
    this.items = [];
    this.shopItems = null;
    this.version = 0;
    this.lastSpec = null;
    this.build();
  }

  build() {
    const select = (label, onchange) => {
      const s = el("select", { onchange });
      return [s, el("label", { class: "row" }, el("span", {}, label), s)];
    };
    [this.army, this.armyRow] = select("Army", () => this.armyChanged());
    [this.model, this.modelRow] = select(NOUN[this.kind], () => this.modelChanged());
    this.nameInput = el("input", { type: "text", maxLength: 40, oninput: () => this.refresh() });
    [this.weapon, this.weaponRow] = select("Weapon", () => this.weaponChanged());
    [this.armour, this.armourRow] = select("Armour", () => this.refresh());
    [this.mount, this.mountRow] = select("Mount", () => this.refresh());
    this.shield = el("input", { type: "checkbox", onchange: () => this.refresh() });
    this.shieldText = el("span", {}, "Shield");
    this.models = el("input", { type: "number", min: 1, max: 200, value: 20, oninput: () => this.refresh() });
    this.frontage = el("input", { type: "number", min: 1, max: 40, value: 5, oninput: () => this.refresh() });
    // A unit's command group: only the models its page offers can be ticked.
    this.command = {};
    this.championItems = [];
    for (const role of ["champion", "standard", "musician"]) {
      const box = el("input", { type: "checkbox", checked: true, onchange: () => this.commandChanged() });
      const label = el("span", {}, { champion: "Champion", standard: "Standard bearer", musician: "Musician" }[role]);
      this.command[role] = { box, label, wrap: el("label", { class: "check" }, box, label) };
    }
    this.standardSelect = el("select", { onchange: () => this.standardChanged() });
    this.standardRow = el("label", { class: "row" }, el("span", {}, "Magic standard"), this.standardSelect);
    this.championList = el("div", { class: "item-list" });
    this.championSummary = el("summary", {}, "Champion's items");
    this.championBox = el("details", { class: "champion-items" }, this.championSummary, this.championList);
    this.itemError = el("p", { class: "error small" });

    this.tiles = el("div", { class: "tiles" });
    this.weaponLine = el("p", { class: "muted small" });
    this.points = el("p", { class: "points" });
    this.breakdown = el("p", { class: "muted small" });
    this.rules = el("p", { class: "muted small" });
    this.extrasLine = el("p", { class: "accent small" });
    this.error = el("p", { class: "error small" });
    this.extrasButton = el("button", { type: "button", class: "secondary", onclick: () => openExtras(this) }, "Extras…");
    this.saveButton = el("button", { type: "button", class: "secondary", onclick: () => this.save() }, "Save…");
    this.deleteButton = el("button", { type: "button", class: "secondary", onclick: () => this.remove() }, "Delete");

    const form = el("div", { class: "form" },
      this.armyRow, this.modelRow,
      el("label", { class: "row" }, el("span", {}, "Name"), this.nameInput),
      this.weaponRow, this.armourRow, this.kind === "character" ? this.mountRow : null,
      el("label", { class: "check indent" }, this.shield, this.shieldText),
      this.kind === "unit" ? el("div", { class: "row size" },
        el("span", {}, "Models"), this.models, el("span", {}, "Width"), this.frontage) : null,
      this.kind === "unit" ? el("div", { class: "command-row" },
        ...["champion", "standard", "musician"].map((r) => this.command[r].wrap)) : null,
      this.kind === "unit" ? this.standardRow : null,
      this.kind === "unit" ? this.championBox : null,
      this.kind === "unit" ? this.itemError : null);
    this.node = el("article", { class: `card card-${"ab"[this.side]}` },
      el("h2", {}, `Fighter ${"AB"[this.side]}`), form, this.tiles,
      el("p", { class: "muted tiny right" }, "With gear (bare profile) · first-round values"),
      this.weaponLine, this.points, this.breakdown, this.rules, this.extrasLine, this.error,
      el("div", { class: "buttons" }, this.extrasButton, this.saveButton, this.deleteButton));
  }

  fillArmies() {
    const armies = Object.keys(catalog.kinds[this.kind]);
    const saved = Object.keys(savedFighters(this.kind));
    const current = this.army.value;
    this.army.replaceChildren(...armies.map((a) => el("option", { value: a }, a)),
      saved.length ? el("option", { value: SAVED }, SAVED) : null);
    if ([...this.army.options].some((o) => o.value === current)) this.army.value = current;
  }

  async pick(faction, profile, spec = null) {
    this.fillArmies();
    this.army.value = faction;
    this.fillModels();
    this.model.value = profile;
    await this.load(faction, profile, spec);
  }

  fillModels() {
    const names = this.army.value === SAVED
      ? Object.keys(savedFighters(this.kind)) : catalog.kinds[this.kind][this.army.value] || [];
    this.model.replaceChildren(...names.map((n) => el("option", { value: n }, n)));
  }

  async armyChanged() {
    this.fillModels();
    await this.modelChanged();
  }

  async modelChanged() {
    if (this.army.value === SAVED) {
      const spec = savedFighters(this.kind)[this.model.value];
      if (spec) await this.load(spec.faction, spec.profile, spec);
    } else {
      await this.load(this.army.value, this.model.value, null);
    }
  }

  async load(faction, profile, spec) {
    const version = ++this.version;
    this.faction = faction;
    this.profile = profile;
    this.items = spec ? [...(spec.magic_items || [])] : [];
    const opts = await api("options", [faction, profile, this.items]);
    if (version !== this.version) return;
    this.opts = opts;
    this.shopItems = null;
    const chosen = spec ? spec.optional_rules || [] : [];
    this.exclusive = {};
    for (const group of opts.exclusive) {
      const hit = group.choices.find((c) => chosen.includes(c.name));
      this.exclusive[group.group] = hit ? hit.name : group.default;
    }
    this.optionalRules = chosen.filter((r) => opts.optional_rules.some((o) => o.name === r));
    this.fillEquipment();
    const d = opts.defaults;
    this.weapon.value = spec?.weapon || d.weapon;
    this.armour.value = spec?.armour || d.armour;
    this.shield.checked = spec ? !!spec.shield : d.shield;
    this.nameInput.value = spec?.name || profile;
    this.fillMounts(spec?.mount);
    if (this.kind === "unit") {
      const minimum = opts.unit?.minimum_size || 1;
      this.models.value = spec?.models || Math.max(minimum, 10);
      this.frontage.value = spec?.frontage || Math.min(Number(this.models.value), 5);
      this.fillCommand(opts.command, spec?.extras || {});
    }
    this.deleteButton.disabled = this.army.value !== SAVED;
    this.extrasButton.disabled = !(opts.optional_rules.length || opts.exclusive.length ||
                                   Object.keys(opts.allowance).length);
    await this.weaponChanged();
  }

  fillCommand(cmd, extras) {
    this.cmd = cmd;
    const costs = cmd.costs || {};
    for (const [role, parts] of Object.entries(this.command)) {
      const allowed = cmd.roles.includes(role);
      parts.box.disabled = !allowed;
      parts.box.checked = allowed && extras[role] !== false;
      const name = role === "champion" ? (cmd.champion || "Champion") : parts.label.textContent.split(" · ")[0];
      parts.label.textContent = costs[role] ? `${name} · +${costs[role]} pts` : name;
    }
    const budget = (b) => Object.entries(b || {}).map(([k, v]) => `${k} up to ${v} pts`).join(", ");
    this.standardSelect.replaceChildren(el("option", { value: "" }, "None"),
      ...cmd.standards.map((s) => el("option", { value: s.name },
        `${s.name} · ${s.cost} pts${s.summary ? " · " + s.summary : ""}${s.note ? " (" + s.note + ")" : ""}`)));
    this.standardSelect.value = (extras.standard_items || [])[0] || "";
    this.standardRow.hidden = !cmd.standards.length;
    this.championItems = [...(extras.champion_items || [])];
    this.championSummary.textContent = `${cmd.champion || "Champion"}'s items (${budget(cmd.champion_budget)})`;
    this.championList.replaceChildren(...cmd.champion_items.map((item) => {
      const box = el("input", { type: "checkbox", checked: this.championItems.includes(item.name),
                                onchange: (e) => this.championItemChanged(item.name, e.target) });
      return el("label", { class: "check item" }, box,
        el("span", {}, `${item.name} · ${item.cost} pts`),
        item.summary ? el("span", { class: "muted" }, ` ${item.summary}`) : null,
        item.note ? el("span", { class: "tag warn" }, item.note) : null);
    }));
    this.championBox.hidden = !cmd.champion_items.length;
    this.itemError.textContent = "";
    this.commandChanged(false);
  }

  commandChanged(refresh = true) {
    this.standardSelect.disabled = !this.command.standard.box.checked;
    for (const box of this.championList.querySelectorAll("input")) box.disabled = !this.command.champion.box.checked;
    if (refresh) this.refresh();
  }

  async check(role, items) {
    const problem = await api("check_unit_items", [this.faction, this.profile, role, items]);
    this.itemError.textContent = problem;
    return !problem;
  }

  async standardChanged() {
    const name = this.standardSelect.value;
    if (name && !(await this.check("standard", [name]))) { this.standardSelect.value = ""; }
    this.refresh();
  }

  async championItemChanged(name, box) {
    const wanted = box.checked ? [...this.championItems, name] : this.championItems.filter((n) => n !== name);
    if (box.checked && !(await this.check("champion", wanted))) { box.checked = false; return; }
    this.itemError.textContent = "";
    this.championItems = wanted;
    this.refresh();
  }

  fillEquipment() {
    const fill = (select, entries) => {
      const current = select.value;
      select.replaceChildren(...entries.map((e) => el("option", { value: e.name }, e.label)));
      if (entries.some((e) => e.name === current)) select.value = current;
    };
    fill(this.weapon, this.opts.weapons);
    fill(this.armour, this.opts.armour);
    const cost = this.opts.shield_cost;
    this.shieldText.textContent = cost ? `Shield · +${cost} pts` : "Shield";
  }

  fillMounts(chosen) {
    const fixed = this.opts.fixed_mount;
    if (fixed) {
      this.mount.replaceChildren(el("option", { value: fixed }, fixed));
      this.mount.disabled = true;
      return;
    }
    const mounts = this.opts.mounts;
    this.mount.replaceChildren(el("option", { value: "" }, ON_FOOT),
      ...mounts.map((m) => el("option", { value: m.name }, m.label)));
    this.mount.value = mounts.some((m) => m.name === chosen) ? chosen : "";
    this.mount.disabled = !mounts.length;
  }

  async weaponChanged() {
    const usable = this.opts.shield && !this.opts.two_handed.includes(this.weapon.value);
    this.shield.disabled = !usable;
    if (!usable) this.shield.checked = false;
    await this.refresh();
  }

  chosenRules() {
    const rules = [...this.optionalRules];
    for (const group of this.opts?.exclusive || []) {
      const picked = this.exclusive[group.group] || group.default;
      if (picked !== group.default) rules.push(picked);
    }
    return rules;
  }

  spec() {
    const mount = this.mount.value;
    return {
      kind: this.kind, faction: this.faction, profile: this.profile,
      name: this.nameInput.value.trim() || this.profile,
      weapon: this.weapon.value, armour: this.armour.value, shield: this.shield.checked,
      optional_rules: this.chosenRules(), magic_items: [...this.items],
      mount: !mount || mount === this.opts?.fixed_mount ? null : mount,
      models: Number(this.models.value) || 1, frontage: Number(this.frontage.value) || 1,
      extras: this.kind === "unit" ? {
        champion: this.command.champion.box.checked, standard: this.command.standard.box.checked,
        musician: this.command.musician.box.checked,
        standard_items: this.command.standard.box.checked && this.standardSelect.value ? [this.standardSelect.value] : [],
        champion_items: this.command.champion.box.checked ? [...this.championItems] : [],
      } : {},
    };
  }

  async refresh() {
    if (!this.profile) return;
    const version = ++this.version;
    const info = await api("describe", [this.spec()]).catch((e) => ({ ok: false, error: e.message }));
    if (version !== this.version) return;
    this.lastSpec = info.spec || null;
    this.error.textContent = info.ok ? "" : info.error;
    if (!info.ok) {
      this.tiles.replaceChildren(el("p", { class: "error" }, "Not a legal loadout"));
      for (const n of [this.weaponLine, this.points, this.breakdown, this.rules, this.extrasLine]) n.textContent = "";
      return;
    }
    this.tiles.replaceChildren(...info.stats.map((s) => {
      const changed = String(s.value) !== String(s.bare);
      const up = parseInt(s.value, 10) > parseInt(s.bare, 10);
      const down = parseInt(s.value, 10) < parseInt(s.bare, 10);
      return el("div", { class: "tile" }, el("span", { class: "tile-name" }, s.name),
        el("span", { class: `tile-value${changed ? (up ? " up" : down ? " down" : "") : ""}` }, s.value ?? "–"),
        el("span", { class: "tile-bare" }, `(${s.bare ?? "–"})`));
    }));
    this.weaponLine.textContent = info.weapon ? `${info.spec.weapon}: ${info.weapon}` : "";
    this.points.textContent = `${info.points} points`;
    this.breakdown.textContent = info.breakdown.length > 1
      ? info.breakdown.map((b) => `${b.label} ${b.cost}`).join(" + ") : "";
    this.rules.textContent = info.rules.join(", ") || "No special rules";
    const lines = [];
    const extras = [...this.chosenRules(), ...this.items];
    if (extras.length) lines.push("Extras: " + extras.join(", "));
    for (const p of info.mount_parts) lines.push(`${p.name}: WS${p.WS} S${p.S} I${p.I} A${p.A}`);
    if (info.formation) lines.push(info.formation);
    this.extrasLine.textContent = lines.join("\n");
  }

  save() {
    const spec = this.lastSpec;
    if (!spec) { setStatus("Fix the loadout before saving.", true); return; }
    const name = (prompt("Save fighter as:", spec.name) || "").trim().slice(0, 40);
    if (!name) return;
    const all = store.get("tow-saved", {});
    all[this.kind] = { ...(all[this.kind] || {}), [name]: { ...spec, name } };
    if (!store.set("tow-saved", all)) { setStatus("This browser won't let the page save.", true); return; }
    for (const card of Object.values(decks).flat()) card.fillArmies();
    this.army.value = SAVED;
    this.fillModels();
    this.model.value = name;
    this.deleteButton.disabled = false;
    setStatus(`Saved "${name}" on this device.`);
  }

  async remove() {
    const name = this.model.value;
    const all = store.get("tow-saved", {});
    if (!all[this.kind] || !(name in all[this.kind])) return;
    if (!confirm(`Delete the saved fighter "${name}"?`)) return;
    delete all[this.kind][name];
    store.set("tow-saved", all);
    for (const card of Object.values(decks).flat()) card.fillArmies();
    const [faction, profile] = catalog.defaults[this.kind][this.side];
    await this.pick(faction, profile);
  }
}

// -- the extras dialog ---------------------------------------------------------------

const extras = { card: null, rules: [], exclusive: {}, items: [], pane: null };

async function openExtras(card) {
  extras.card = card;
  extras.rules = [...card.optionalRules];
  extras.exclusive = { ...card.exclusive };
  extras.items = [...card.items];
  $("extras-title").textContent = `Extras — ${card.profile}`;
  $("extras-error").textContent = "";
  $("search").value = "";

  const upgrades = [];
  for (const rule of card.opts.optional_rules) {
    upgrades.push(el("label", { class: "check" },
      el("input", { type: "checkbox", checked: extras.rules.includes(rule.name), onchange: (e) => {
        extras.rules = e.target.checked ? [...extras.rules, rule.name] : extras.rules.filter((r) => r !== rule.name);
      } }), `${rule.name}${rule.cost ? ` · +${rule.cost} pts` : ""}`));
  }
  for (const group of card.opts.exclusive) {
    const s = el("select", { onchange: (e) => { extras.exclusive[group.group] = e.target.value; } },
      ...group.choices.map((c) => el("option", { value: c.name }, `${c.name}${c.cost ? ` · +${c.cost} pts` : ""}`)));
    s.value = extras.exclusive[group.group] || group.default;
    upgrades.push(el("label", { class: "row" }, el("span", {}, group.group), s));
  }
  $("upgrades").replaceChildren(...(upgrades.length ? [el("h3", {}, "Upgrades"), ...upgrades] : []));

  const hasShop = Object.keys(card.opts.allowance).length > 0;
  $("shop").hidden = !hasShop;
  if (hasShop && !card.shopItems) card.shopItems = await api("shop", [card.faction, card.profile]);
  if (hasShop) {
    const common = card.shopItems.filter((i) => i.common).length;
    $("common-label").textContent = `Common items (${common})`;
    extras.pane = null;
    await renderShop();
  }
  $("extras").showModal();
}

function shopMatches(item, query) {
  if (!$("common").checked && item.common) return false;
  const words = query.toLowerCase().split(/\s+/).filter(Boolean);
  return words.every((w) => item.search.includes(w));
}

async function renderShop() {
  const card = extras.card;
  const query = $("search").value;
  const shown = card.shopItems.filter((i) => shopMatches(i, query));
  const panes = [...new Set(card.shopItems.map((i) => i.pane))].sort();
  const counts = Object.fromEntries(panes.map((p) => [p, shown.filter((i) => i.pane === p).length]));
  if (!extras.pane || (query && !counts[extras.pane])) extras.pane = panes.find((p) => counts[p]) || panes[0];
  $("tabs").replaceChildren(...panes.map((p) => el("button", {
    type: "button", role: "tab", class: p === extras.pane ? "tab active" : "tab",
    "aria-selected": String(p === extras.pane), onclick: () => { extras.pane = p; renderShop(); },
  }, `${p} (${counts[p]})`)));

  const rows = shown.filter((i) => i.pane === extras.pane).map((item) => el("tr", {},
    el("td", {}, el("button", { type: "button", class: "link", title: "Add", onclick: () => addItem(item.name) }, item.name),
      item.common ? el("span", { class: "tag" }, "common") : null,
      item.note ? el("span", { class: "tag warn" }, item.note) : null),
    el("td", { class: "num" }, item.cost),
    el("td", { class: "muted" }, item.summary || "–"),
    el("td", {}, item.link ? el("a", { href: item.link, target: "_blank", rel: "noopener noreferrer" }, "rules ↗") : "")));
  $("items").tBodies[0].replaceChildren(...(rows.length ? rows
    : [el("tr", {}, el("td", { colSpan: 4, class: "muted" }, "Nothing matches."))]));
  await renderChosen();
}

async function renderChosen() {
  const card = extras.card;
  const byName = Object.fromEntries((card.shopItems || []).map((i) => [i.name, i]));
  $("chosen").replaceChildren(...extras.items.map((name, index) => el("li", {},
    el("span", {}, name), el("span", { class: "muted" }, ` ${byName[name]?.cost ?? ""} pts `),
    el("button", { type: "button", class: "link", title: "Remove", onclick: () => {
      extras.items.splice(index, 1); renderChosen();
    } }, "✕"))));
  const { spent } = await api("check_items", [card.faction, card.profile, extras.items]);
  $("budgets").textContent = Object.entries(card.opts.allowance).map(([budget, limit]) => limit === null
    ? `${budget}: ${extras.items.filter((n) => byName[n]?.budget === budget).length} chosen`
    : `${budget}: ${spent[budget] || 0}/${limit} pts`).join("   ");
}

async function addItem(name) {
  const card = extras.card;
  const { problem } = await api("check_items", [card.faction, card.profile, [...extras.items, name]]);
  $("extras-error").textContent = problem;
  if (!problem) { extras.items.push(name); await renderChosen(); }
}

async function extrasDone() {
  const card = extras.card;
  const { problem } = await api("check_items", [card.faction, card.profile, extras.items]);
  if (problem) { $("extras-error").textContent = problem; return; }
  card.optionalRules = extras.rules;
  card.exclusive = extras.exclusive;
  card.items = [...extras.items];
  $("extras").close();
  // Bought abilities can unlock weapons and armour (Warden of Saphery's sword of Hoeth).
  const opts = await api("options", [card.faction, card.profile, card.items]);
  card.opts = { ...card.opts, weapons: opts.weapons, armour: opts.armour };
  card.fillEquipment();
  await card.weaponChanged();
}

// -- running fights -------------------------------------------------------------------

function cards() { return decks[mode]; }

function readRunSettings() {
  runSettings[runMode] = { rounds: Number($("rounds").value) || 6, death: $("death").checked };
}

function showRunSettings() {
  const s = runSettings[runMode];
  $("rounds").value = s.rounds;
  $("death").checked = s.death;
  $("rounds").disabled = s.death;
  $("runs").disabled = runMode === "narrate";
  for (const b of $("run-mode").children) b.setAttribute("aria-pressed", String(b.dataset.value === runMode));
}

function number(input, label, low, high) {
  const value = Number(input.value);
  if (!Number.isInteger(value) || value < low || value > high) throw new Error(`${label} must be a whole number from ${low} to ${high}`);
  return value;
}

let fighting = false;
async function fight() {
  if (fighting) return;
  const [a, b] = cards();
  if (!a.lastSpec || !b.lastSpec) { setStatus("Both fighters need a legal loadout.", true); return; }
  let runs, rounds, seed;
  try {
    rounds = $("death").checked ? null : number($("rounds"), "Rounds", 1, 50);
    runs = runMode === "odds" ? number($("runs"), "Fights", 1, 20000) : 1;
    const seedText = $("seed").value.trim();
    seed = seedText === "" ? null : number($("seed"), "Seed", 0, 2147483647);
  } catch (e) { setStatus(e.message, true); return; }

  fighting = true;
  $("fight").disabled = true;
  setStatus(runMode === "odds" ? `Fighting ${runs} times…` : "Fighting…");
  try {
    if (runMode === "narrate") {
      showLog(await api("narrate", [a.lastSpec, b.lastSpec, rounds ?? "death", seed]));
    } else {
      $("progress").hidden = false;
      $("progress").value = 0;
      const stats = await api("odds", [a.lastSpec, b.lastSpec, runs, rounds ?? "death", seed],
        (done) => { $("progress").value = done / runs; });
      showOdds(stats);
    }
    setStatus("");
  } catch (e) {
    setStatus(e.message, true);
  } finally {
    fighting = false;
    $("fight").disabled = false;
    $("progress").hidden = true;
  }
}

function showOdds(s) {
  const pct = (n) => (100 * n / (s.runs || 1)).toFixed(1) + "%";
  $("pct-a").textContent = pct(s.wins_a);
  $("pct-b").textContent = pct(s.wins_b);
  $("pct-draw").textContent = "draw " + pct(s.draws);
  $("bar-a").style.width = pct(s.wins_a);
  $("bar-draw").style.width = pct(s.draws);
  $("bar-b").style.width = pct(s.wins_b);
  $("name-a").textContent = s.name_a;
  $("name-b").textContent = s.name_b;
  const line = (name, wins, kills, left) =>
    `${name}: ${wins} wins (${kills} by slaying, ${wins - kills} on wounds), ` +
    `${(wins ? left / wins : 0).toFixed(2)} wounds left on average when winning`;
  const lines = s.lines ? [`${s.runs} fights, ${s.rounds}`, ...s.lines] : [
    `${s.runs} fights, ${s.rounds}`,
    line(s.name_a, s.wins_a, s.kills_a, s.wounds_left_a),
    line(s.name_b, s.wins_b, s.kills_b, s.wounds_left_b),
    `Draws: ${s.draws}`,
  ];
  $("details").replaceChildren(...lines.map((t) => el("div", {}, t)));
  $("result").hidden = false;
  $("winbar").hidden = false;
  $("log").hidden = true;
}

function showLog(text) {
  $("log").replaceChildren(...text.split("\n").map((line) => {
    const style = LOG_STYLES.find(([, re]) => re.test(line));
    return el("span", { class: style ? `log-${style[0]}` : "" }, line + "\n");
  }));
  $("result").hidden = false;
  $("winbar").hidden = true;
  $("log").hidden = false;
  $("log").scrollTop = 0;
}

// -- share links --------------------------------------------------------------------------
// The fight lives in the URL fragment (#...), which browsers never send to the server.

async function share() {
  const [a, b] = cards();
  if (!a.lastSpec || !b.lastSpec) { setStatus("Both fighters need a legal loadout to share.", true); return; }
  const params = new URLSearchParams({ mode, a: encodeSpec(a.lastSpec), b: encodeSpec(b.lastSpec) });
  const url = `${location.origin}${location.pathname}#${params}`;
  history.replaceState(null, "", url);
  try {
    await navigator.clipboard.writeText(url);
    setStatus("Link copied. Anyone who opens it gets these two fighters.");
  } catch {
    setStatus("Copy the link from the address bar to share these two fighters.");
  }
}

async function loadShared() {
  const params = new URLSearchParams(location.hash.slice(1));
  if (!params.has("a") && !params.has("b")) return false;
  const kind = params.get("mode") === "unit" ? "unit" : "character";
  await setMode(kind);
  let problems = 0;
  for (const [index, key] of [[0, "a"], [1, "b"]]) {
    const spec = decodeSpec(params.get(key));
    const known = spec && catalog.kinds[kind][spec.faction]?.includes(spec.profile);
    if (!known) { problems++; continue; }
    await decks[kind][index].pick(spec.faction, spec.profile, spec);
  }
  setStatus(problems ? "Part of this link could not be read; the default fighter is shown instead." : "Loaded a shared fight.", problems > 0);
  return true;
}

// -- modes and start-up -----------------------------------------------------------------------

async function setMode(kind) {
  mode = kind;
  for (const b of $("mode").children) b.setAttribute("aria-pressed", String(b.dataset.value === kind));
  if (!decks[kind]) {
    decks[kind] = [new Card(kind, 0), new Card(kind, 1)];
    await Promise.all(decks[kind].map((card, i) => {
      const [faction, profile] = catalog.defaults[kind][i];
      return card.pick(faction, profile);
    }));
  }
  const [a, b] = decks[kind];
  $("cards").replaceChildren(a.node, el("div", { class: "vs" }, "vs"), b.node);
  $("unit-note").hidden = kind !== "unit";
  $("unit-note").textContent = catalog.unit_note;
  $("result").hidden = true;
}

async function start() {
  try {
    catalog = await api("catalog");
  } catch (e) {
    fail("The simulator could not start: " + e.message);
    return;
  }
  $("runs").value = catalog.default_runs;
  runSettings.odds.rounds = runSettings.narrate.rounds = catalog.default_rounds;
  showRunSettings();
  if (!(await loadShared())) await setMode("character");
  $("loading").hidden = true;
  $("cards").hidden = false;
  $("controls").hidden = false;

  $("mode").addEventListener("click", (e) => {
    const value = e.target.closest("button")?.dataset.value;
    if (value && value !== mode) setMode(value);
  });
  $("run-mode").addEventListener("click", (e) => {
    const value = e.target.closest("button")?.dataset.value;
    if (!value || value === runMode) return;
    readRunSettings();
    runMode = value;
    showRunSettings();
  });
  $("death").addEventListener("change", () => { $("rounds").disabled = $("death").checked; });
  $("fight").addEventListener("click", fight);
  $("share").addEventListener("click", share);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.metaKey || e.ctrlKey) && !$("extras").open) fight();
  });
  $("search").addEventListener("input", () => renderShop());
  $("common").addEventListener("change", () => renderShop());
  $("extras-cancel").addEventListener("click", () => $("extras").close());
  // Enter in the search box must not submit (and so close) the dialog.
  $("extras").querySelector("form").addEventListener("submit", (e) => e.preventDefault());
  $("extras-done").addEventListener("click", extrasDone);
}

start();
