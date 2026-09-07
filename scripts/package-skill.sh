#!/usr/bin/env bash
# Keep the existing CI/release entry point; use the same packager on all hosts.
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
python "$SCRIPT_DIR/package-skill.py" "$@"
