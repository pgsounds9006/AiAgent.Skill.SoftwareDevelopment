"""Check that the plugin exposes the canonical skill and its release version."""
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
plugin_root = root / 'src'
manifest = json.loads((plugin_root / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
if manifest['name'] != 'software-development' or manifest['skills'] != './skills/':
    raise SystemExit('Plugin must expose the canonical software-development skill')
skill = plugin_root / manifest['skills'] / manifest['name'] / 'SKILL.md'
parts = skill.read_text(encoding='utf-8').split('---', 2)
if len(parts) != 3 or parts[0].strip():
    raise SystemExit('Missing skill frontmatter')
version = re.search(r'^version: (\d+\.\d+\.\d+)\s*$', parts[1], re.M)
if not version or manifest['version'] != version[1]:
    raise SystemExit('Plugin version must match the version in SKILL.md')
print(f'Plugin source and version verified: {version[1]}')
