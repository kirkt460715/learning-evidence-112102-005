import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FixtureTests(unittest.TestCase):
    def test_synthetic_records_match_documented_envelope(self):
        path = ROOT / 'fixtures' / 'records.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(data['dataset'], 'rubric')
        self.assertIsInstance(data['records'], list)
        self.assertGreaterEqual(len(data['records']), 3)
        identifiers = [row['id'] for row in data['records']]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertTrue(all(isinstance(row, dict) for row in data['records']))

    def test_team_artifact_and_personal_evidence_have_separate_records(self):
        data = json.loads((ROOT / 'fixtures' / 'records.json').read_text(encoding='utf-8'))
        kinds = {row['kind'] for row in data['records']}
        self.assertTrue({'artifact-review', 'decision-log', 'membership-change', 'individual-review'} <= kinds)
        self.assertTrue(any(row.get('event') == 'left-team' for row in data['records']))
        self.assertEqual({row['rubric'] for row in data['catalogs']['projects']}, {'r1', 'r2'})

if __name__ == '__main__':
    unittest.main()
