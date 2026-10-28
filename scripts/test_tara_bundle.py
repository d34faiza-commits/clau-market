"""Artifact regressions, not real-model or human evaluation."""
import copy
import hashlib
import tempfile
import unittest
from pathlib import Path
import tara_bundle as bundle


class TaraBundleTests(unittest.TestCase):
    def test_pinned_components_and_contracts(self):
        manifest, version = bundle.check()
        self.assertEqual(len(version), 64)
        self.assertEqual(manifest['model_settings']['provider'], 'fake')

    def test_build_allowlist_and_bytes(self):
        manifest, version = bundle.check()
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'artifact'
            self.assertEqual(bundle.build(output), version)
            actual = {p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file()}
            self.assertEqual(actual, {c['path'] for c in manifest['components']} | {'manifest.json','prompt-version.txt'})
            for c in manifest['components']:
                self.assertEqual(hashlib.sha256((output / c['path']).read_bytes()).hexdigest(), c['sha256'])
            with self.assertRaises(ValueError):
                bundle.build(output)

    def test_missing_unsafe_and_symlink_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'good.md').write_text('data')
            (root / 'link.md').symlink_to(root / 'good.md')
            for path in ('../escape.md','/etc/passwd','missing.md','link.md'):
                with self.subTest(path=path), self.assertRaises(ValueError):
                    bundle.component_bytes(root, path)

    def test_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'bad.json'
            p.write_text('{"status":"approved","status":"draft"}')
            with self.assertRaises(ValueError):
                bundle.read_json(p)

    def test_settings_and_components_affect_version(self):
        manifest, version = bundle.check()
        modified = copy.deepcopy(manifest)
        modified['model_settings']['max_output_tokens'] += 1
        self.assertNotEqual(bundle.prompt_version(modified), version)
        modified = copy.deepcopy(manifest)
        modified['components'][0]['sha256'] = '0' * 64
        self.assertNotEqual(bundle.prompt_version(modified), version)

    def test_matrix_coverage_and_no_fabricated_results(self):
        cases = bundle.read_json(bundle.ROOT / bundle.BUNDLE / 'eval-cases.json')
        expected = {'primary':16,'extended':8,'platform':8,'claim':8,'consent':6,'context':6,'adversarial':4,'voice':4}
        self.assertEqual({g:sum(c['group'] == g for c in cases) for g in expected}, expected)
        self.assertEqual({c['input']['language'] for c in cases}, {'id','en'})
        self.assertEqual({c['input']['platform'] for c in cases}, {'instagram','facebook','tiktok','google-business-profile'})
        for c in cases:
            self.assertIsNone(c['result'])
            self.assertIsNone(c['human_score'])
            self.assertIn('Contoh', c['input']['brand'])
            self.assertIn(c['expected_status'], {'draft','clarification_required','escalation_required'})


if __name__ == '__main__':
    unittest.main()
