"""Regression tests for scripts/check_caption.py (stdlib unittest).

Run: python -m unittest discover -s scripts -p "test_*.py"
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_caption import cta_types, term_hits  # noqa: E402


class CtaTypes(unittest.TestCase):
    def test_single_save(self):
        self.assertEqual(cta_types("Simpan post ini untuk trip berikutnya"), ["save"])

    def test_two_ctas_detected(self):
        self.assertEqual(cta_types("Simpan untuk nanti, atau kirim ke partner trip kamu."), ["save", "share"])

    def test_indonesian_words_are_not_ctas(self):
        # "tapi" (but) is not "tap"; "following" is not "follow"; "pesan sehari" is an order note.
        self.assertEqual(cta_types("Kolamnya kecil tapi tenang. Kami following tren."), [])
        self.assertEqual(cta_types("Private chef, pesan sehari sebelumnya."), [])

    def test_inflections(self):
        self.assertEqual(cta_types("Simpanlah untuk nanti"), ["save"])
        self.assertEqual(cta_types("Tell us your pick in the comments."), ["comment"])

    def test_hashtags_ignored(self):
        self.assertEqual(cta_types("Simpan ya #savethedate #follow"), ["save"])


class Terms(unittest.TestCase):
    def test_whole_word(self):
        self.assertEqual(term_hits("villa mewah di ubud", ["mewah"]), ["mewah"])
        self.assertEqual(term_hits("kemewahan", ["mewah"]), [])


if __name__ == "__main__":
    unittest.main()
