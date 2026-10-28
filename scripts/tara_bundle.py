"""Build an allowlisted, exact-byte H2 artifact. No network or client data."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = Path('bundles/tara')
sys.path.insert(0, str(ROOT / 'core/scripts'))
from runtime_contracts import prompt_version, validate_contract  # noqa: E402


def read_json(path):
    def pairs(items):
        out = {}
        for k, v in items:
            if k in out:
                raise ValueError('duplicate_json_key')
            out[k] = v
        return out
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite_json')))


def component_bytes(root, relative):
    if not re.fullmatch(r'[a-zA-Z0-9_-]+(?:/[a-zA-Z0-9_-]+)*(?:\.[a-zA-Z0-9_-]+)?', relative):
        raise ValueError('unsafe_component_path')
    path = root
    for part in Path(relative).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('symlink_component')
    if not path.is_file() or path.stat().st_size > 1_048_576:
        raise ValueError('missing_or_oversized_component')
    return path.read_bytes()


def schema_for(core, name):
    """Copy only reachable definitions, preserving the authoritative H1 contract."""
    definitions = {}
    pending = [name]
    while pending:
        key = pending.pop()
        if key in definitions:
            continue
        definitions[key] = core['$defs'][key]
        pending.extend(re.findall(r'"\$ref":\s*"#/\$defs/([^"/]+)"', json.dumps(definitions[key])))
    return {'$schema': core['$schema'], '$ref': '#/$defs/' + name, '$defs': definitions}


def check(root=ROOT):
    manifest = read_json(root / BUNDLE / 'manifest.json')
    validate_contract('PromptBundle', manifest)
    sources = read_json(root / BUNDLE / 'sources.json')
    if [(c['kind'], c['path']) for c in manifest['components']] != [(c['kind'], c['path']) for c in sources]:
        raise ValueError('source_inventory_mismatch')
    for c in manifest['components']:
        if hashlib.sha256(component_bytes(root, c['path'])).hexdigest() != c['sha256']:
            raise ValueError('bundle_checksum_mismatch')
    version = prompt_version(manifest)
    if (root / BUNDLE / 'prompt-version.txt').read_text().strip() != version:
        raise ValueError('prompt_version_mismatch')
    schema = read_json(root / BUNDLE / 'output-schema.json')
    core = read_json(root / 'core/shared/runtime/v1/contracts.schema.json')
    if schema != schema_for(core, 'TaraGeneration'):
        raise ValueError('output_schema_drift')
    for fixture in read_json(root / BUNDLE / 'fixtures.json'):
        validate_contract('TaraGeneration', fixture)
    for tool in read_json(root / BUNDLE / 'tools.json'):
        validate_contract('ToolContract', tool)
        paths = {c['path'] for c in manifest['components']}
        if any(tool[k] not in paths for k in ('input_schema_component', 'output_schema_component')):
            raise ValueError('tool_schema_not_pinned')
    cases = read_json(root / BUNDLE / 'eval-cases.json')
    if len(cases) != 60 or len({c['id'] for c in cases}) != 60:
        raise ValueError('eval_case_count')
    for c in cases:
        if c['mode'] != 'SIMULASI' or not c['input'] or not c['assertions'] or c['result'] is not None:
            raise ValueError('eval_fixture_invalid')
    return manifest, version


def refresh(root=ROOT):
    # Explicit maintainer operation only; never called by check/build/CI.
    manifest = read_json(root / BUNDLE / 'manifest.json')
    manifest['components'] = [dict(c, sha256=hashlib.sha256(component_bytes(root, c['path'])).hexdigest())
                              for c in read_json(root / BUNDLE / 'sources.json')]
    validate_contract('PromptBundle', manifest)
    (root / BUNDLE / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    (root / BUNDLE / 'prompt-version.txt').write_text(prompt_version(manifest) + '\n')
    check(root)


def build(output, root=ROOT):
    manifest, version = check(root)
    if output.exists():
        raise ValueError('output_must_not_exist')
    output.mkdir(parents=True)
    for c in manifest['components']:
        target = output / c['path']
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(component_bytes(root, c['path']))
    (output / 'manifest.json').write_bytes((root / BUNDLE / 'manifest.json').read_bytes())
    (output / 'prompt-version.txt').write_text(version + '\n')
    return version


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'refresh', 'build'])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.command == 'refresh':
        refresh()
    elif args.command == 'build':
        if args.output is None:
            parser.error('--output is required')
        build(args.output)
    _, version = check()
    print(f'PASS H2 bundle {version}; synthetic fixtures only, real-model evaluation not run')
