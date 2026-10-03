#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PORT="${PORT:-8080}"
PY=python3
if ! "$PY" -c "import sys" >/dev/null 2>&1; then PY=python; fi
exec "$PY" -m app.main
