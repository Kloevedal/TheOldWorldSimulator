#!/bin/zsh
# Double-click in Finder (or run from a terminal) to open the simulator.
# Prefers a uv-managed Python 3.13, whose Tk 8.6 renders properly on current
# macOS; the system python3 ships Apple's deprecated Tk 8.5.
cd "$(dirname "$0")"
UV="$(command -v uv || echo "$HOME/.local/bin/uv")"
if [ -x "$UV" ]; then
  exec "$UV" run --no-project --python 3.13 python simulator_app.py
fi
exec python3 simulator_app.py
