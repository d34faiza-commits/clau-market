#!/usr/bin/env python3
"""Mechanical caption checks for CLAU-AI-CONTENT (stdlib only).

Checks each caption for:
  - hook (first line) length <= --max-hook characters (default 125)
  - total length <= --max-chars (default 2200; ASSUMPTION until TASK-011 verifies)
  - hashtag count within --min-tags..--max-tags (default 3..8) when hashtags are used
  - emoji count <= --max-emoji, and no emoji in the hook when --no-emoji-hook
  - forbidden terms: rule 02 positioning words + brief restrictions.forbidden_terms
  - CTA count (heuristic): distinct call-to-action types (save, share, comment,
    click, dm, book, follow, tag) <= --max-cta (default 1; rule 05: one content, one CTA)
  - with --expect-cta TYPE: the CTA found must be that type (brief channels[].cta.type)

It does NOT judge claims, tone, truthfulness, or whether the CTA suits the brief
beyond --expect-cta. Output therefore says "PASS (mekanis)": a mechanical pass is
not a QA pass. Claims, voice, and brief fit stay with the QA gates (qa/).

Usage:
  python scripts/check_caption.py caption.txt
  python scripts/check_caption.py --markdown drafts.md --brief brief.json
      (only ```text blocks with hashtags = captions; add --all-blocks for every block)
  python scripts/check_caption.py caption.txt --expect-cta save   # CTA from brief channels[].cta.type
  echo "caption" | python scripts/check_caption.py -
Exit code 0 = all captions pass, 1 = at least one failure.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Rule 02 — positioning words that are claims (see rules/02, "Kata positioning & nama brand").
POSITIONING_TERMS = [
    "mewah", "luxury", "luxurious", "premium", "eksklusif", "exclusive",
    "5-star", "7-star", "bintang 5", "bintang lima", "world-class", "kelas dunia",
    "terbaik", "best", "nomor 1", "number one", "termurah",
]
# Voice guide — clichés.
CLICHES = [
    "hidden gem", "surga tersembunyi", "pengalaman tak terlupakan", "unforgettable experience",
    "nestled", "dream getaway", "kemewahan tiada tara", "unparalleled",
]
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
HASHTAG_RE = re.compile(r"#\w+")
FENCE_RE = re.compile(r"```text\n(.*?)```", re.DOTALL)
# CTA heuristic: imperative phrases per CTA type (ID + EN). Deliberately narrow:
# "pesan"/"book" alone also mean "message"/"reserve ahead" in facts, so only
# explicit call phrases count. Brief cta.type values map onto these keys.
CTA_PATTERNS = {
    "save": [r"simpan", r"save"],
    "share": [r"kirim ke", r"bagikan", r"share", r"send (?:this|it) to"],
    "comment": [r"komentar", r"comment", r"tell us", r"tulis di kolom"],
    "click": [r"klik", r"click", r"tap", r"link (?:di|in) bio", r"swipe up"],
    "dm": [r"\bdm\b", r"kirim pesan", r"send us a message", r"chat (?:kami|us)"],
    "book": [r"book now", r"pesan sekarang", r"reservasi sekarang", r"booking sekarang"],
    "follow": [r"follow", r"ikuti akun"],
    "tag": [r"tag (?:teman|partner|your|a friend|someone)", r"mention"],
}
CTA_ALIASES = {"link-sticker": "click", "link": "click", "whatsapp": "dm", "booking": "book"}


def load_captions(args: argparse.Namespace) -> list[tuple[str, str]]:
    if args.markdown:
        text = Path(args.markdown).read_text(encoding="utf-8")
        blocks = FENCE_RE.findall(text)
        return [
            (f"{args.markdown} block {i + 1}", b.strip("\n"))
            for i, b in enumerate(blocks)
            if args.all_blocks or HASHTAG_RE.search(b)
        ]
    source = args.file
    text = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
    return [(source, text.strip("\n"))]


def forbidden_terms(brief_path: str | None) -> list[str]:
    terms = POSITIONING_TERMS + CLICHES
    if brief_path:
        brief = json.loads(Path(brief_path).read_text(encoding="utf-8"))
        terms += brief.get("restrictions", {}).get("forbidden_terms", [])
    return sorted({t.lower() for t in terms})


def term_hits(text: str, terms: list[str]) -> list[str]:
    lower = text.lower()
    return [t for t in terms if re.search(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", lower)]


def cta_types(text: str) -> list[str]:
    """Distinct CTA types found outside hashtags (heuristic; see CTA_PATTERNS)."""
    lower = HASHTAG_RE.sub(" ", text.lower())
    return [
        cta for cta, patterns in CTA_PATTERNS.items()
        if any(re.search(r"(?<![\w-])" + p, lower) for p in patterns)
    ]


def check(caption: str, args: argparse.Namespace, terms: list[str]) -> list[str]:
    problems: list[str] = []
    lines = [line for line in caption.splitlines() if line.strip()]
    hook = lines[0] if lines else ""
    if len(hook) > args.max_hook:
        problems.append(f"hook {len(hook)} chars > {args.max_hook}")
    if len(caption) > args.max_chars:
        problems.append(f"length {len(caption)} chars > {args.max_chars} (limit is ASSUMPTION)")
    tags = HASHTAG_RE.findall(caption)
    if tags and not args.min_tags <= len(tags) <= args.max_tags:
        problems.append(f"{len(tags)} hashtags, expected {args.min_tags}-{args.max_tags}")
    if len(set(t.lower() for t in tags)) != len(tags):
        problems.append("duplicate hashtags")
    emojis = EMOJI_RE.findall(caption)
    if args.max_emoji is not None and len(emojis) > args.max_emoji:
        problems.append(f"{len(emojis)} emoji > {args.max_emoji}")
    if args.no_emoji_hook and EMOJI_RE.search(hook):
        problems.append("emoji in hook")
    hits = term_hits(caption, terms)
    if hits:
        problems.append("forbidden/positioning terms: " + ", ".join(hits))
    ctas = cta_types(caption)
    if len(ctas) > args.max_cta:
        problems.append(f"{len(ctas)} CTA types > {args.max_cta}: " + ", ".join(ctas))
    if args.expect_cta:
        expected = CTA_ALIASES.get(args.expect_cta, args.expect_cta)
        if expected not in ctas:
            found = ", ".join(ctas) or "none"
            problems.append(f"expected CTA '{args.expect_cta}' (brief), found: {found}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file", nargs="?", default="-", help="caption file, or - for stdin")
    parser.add_argument("--markdown", help="check ```text blocks that contain hashtags (captions) in a Markdown file")
    parser.add_argument("--all-blocks", action="store_true", help="with --markdown, check every ```text block")
    parser.add_argument("--brief", help="brief.json; adds restrictions.forbidden_terms")
    parser.add_argument("--max-hook", type=int, default=125)
    parser.add_argument("--max-chars", type=int, default=2200)
    parser.add_argument("--min-tags", type=int, default=3)
    parser.add_argument("--max-tags", type=int, default=8)
    parser.add_argument("--max-emoji", type=int, default=None)
    parser.add_argument("--no-emoji-hook", action="store_true")
    parser.add_argument("--max-cta", type=int, default=1, help="max distinct CTA types (heuristic)")
    parser.add_argument("--expect-cta", choices=sorted(set(CTA_PATTERNS) | set(CTA_ALIASES)),
                        help="CTA type the brief sets for this channel (channels[].cta.type)")
    args = parser.parse_args()
    if args.expect_cta and args.markdown:
        parser.error("--expect-cta applies to one caption; check Markdown blocks per channel instead")

    terms = forbidden_terms(args.brief)
    failed = 0
    for name, caption in load_captions(args):
        problems = check(caption, args, terms)
        if problems:
            failed += 1
            print(f"FAIL  {name}")
            for p in problems:
                print(f"      - {p}")
        else:
            print(f"PASS (mekanis)  {name}")
    print("note: mekanis saja. Klaim, voice, dan kecocokan dengan brief tetap dicek di QA gate (qa/).")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
