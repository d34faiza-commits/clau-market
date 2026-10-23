"""Regression tests for scripts/check_caption.py (stdlib unittest).

Run: python -m unittest discover -s scripts -p "test_*.py"
"""

import argparse
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_caption import EMOJI_RE, GUARANTEE_TERMS, check, cta_types, tag_range, term_hits  # noqa: E402


def default_args(**overrides):
    base = dict(max_hook=125, max_chars=2200, min_tags=3, max_tags=5, max_emoji=None,
                no_emoji_hook=False, max_cta=1, expect_cta=None)
    base.update(overrides)
    return argparse.Namespace(**base)


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

    def test_guarantee_terms_caught(self):
        # Travel & wedding: satwa, cuaca, keselamatan, dan hasil tidak bisa dijamin (rule 02).
        self.assertEqual(term_hits("Trip 3 hari, pasti lihat manta!", GUARANTEE_TERMS), ["pasti lihat"])
        self.assertEqual(term_hits("Snorkeling 100% aman untuk anak", GUARANTEE_TERMS), ["100% aman"])
        self.assertEqual(term_hits("Manta sering terlihat di musim ini, bila cuaca mendukung.", GUARANTEE_TERMS), [])


class HashtagLimit(unittest.TestCase):
    # Instagram accepts at most 5 hashtags per post/Reels since 2025-12-18 (knowledge/platforms/instagram.md).
    def test_five_tags_pass(self):
        caption = "Pagi di villa.\n#bali #ubud #villa #slowliving #staycation"
        self.assertEqual(check(caption, default_args(), []), [])

    def test_six_tags_fail(self):
        caption = "Pagi di villa.\n#bali #ubud #villa #slowliving #staycation #honeymoon"
        self.assertIn("6 hashtags, expected 3-5", check(caption, default_args(), []))


class PlatformPresets(unittest.TestCase):
    def test_presets(self):
        self.assertEqual(tag_range("instagram", None, None), (3, 5))
        self.assertEqual(tag_range("facebook", None, None), (1, 3))

    def test_explicit_flags_win(self):
        self.assertEqual(tag_range("facebook", None, 4), (1, 4))

    def test_facebook_without_hashtags_passes(self):
        caption = "Paket sarapan keluarga, Sabtu-Minggu 07.00-10.00. Pesan lewat tombol Kirim Pesan."
        self.assertEqual(check(caption, default_args(min_tags=1, max_tags=3), []), [])

    def test_facebook_five_tags_fail(self):
        caption = "Paket sarapan keluarga.\n#a #b #c #d #e"
        self.assertIn("5 hashtags, expected 1-3", check(caption, default_args(min_tags=1, max_tags=3), []))


class EmojiCount(unittest.TestCase):
    def test_modifiers_and_sequences_count_once(self):
        # Skin tone, variation selector and ZWJ family sequences are one visible emoji each.
        for text in ["👍🏽", "❤️", "👨‍👩‍👧"]:
            self.assertEqual(len(EMOJI_RE.findall(text)), 1, text)
        self.assertEqual(len(EMOJI_RE.findall("🌅 🌴")), 2)


if __name__ == "__main__":
    unittest.main()
