// Runs the simulator (Python, via Pyodide) off the page's main thread.
// Messages in: {id, name, args}. Messages out: {id, result} | {id, error} | {id, progress}.
"use strict";

const PYODIDE = "https://cdn.jsdelivr.net/pyodide/v0.29.5/full/";
importScripts(PYODIDE + "pyodide.js");

const ready = (async () => {
  const pyodide = await loadPyodide({ indexURL: PYODIDE });
  const response = await fetch("sim.zip?v=__BUILD__");
  if (!response.ok) throw new Error("Could not download the simulator (" + response.status + ")");
  pyodide.unpackArchive(await response.arrayBuffer(), "zip", { extractDir: "/home/pyodide/sim" });
  pyodide.runPython("import sys; sys.path.insert(0, '/home/pyodide/sim')");
  return pyodide.pyimport("web_api");
})();

self.onmessage = async (event) => {
  const { id, name, args } = event.data;
  try {
    const api = await ready;
    const progress = name === "odds" ? (done) => self.postMessage({ id, progress: done }) : undefined;
    const reply = JSON.parse(api.call(name, JSON.stringify(args), progress));
    self.postMessage({ id, ...reply });
  } catch (err) {
    self.postMessage({ id, error: String(err && err.message ? err.message : err) });
  }
};
