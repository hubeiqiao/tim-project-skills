#!/usr/bin/env python3
"""
TIM Report DOCX Verifier

Converts a .docx to markdown via pandoc, runs evaluation checks, and
optionally compares against markdown draft files for sync issues.

Usage:
    python verify_docx.py report.docx [--drafts path/to/TIM_Report_Draft/] [--pandoc path/to/pandoc]

Requires: pandoc (external tool)
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Import evaluation logic from evaluate_report.py (same directory)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from evaluate_report import (
    ALL_CHECKS,
    CHAPTER_FILES,
    load_texts,
    print_results,
    run_checks,
)


# ---------------------------------------------------------------------------
# Pandoc conversion
# ---------------------------------------------------------------------------

def find_pandoc(pandoc_path: str | None) -> str:
    """Locate pandoc binary."""
    if pandoc_path:
        if os.path.isfile(pandoc_path) and os.access(pandoc_path, os.X_OK):
            return pandoc_path
        print(f"Error: pandoc not found at '{pandoc_path}'.", file=sys.stderr)
        sys.exit(2)
    found = shutil.which("pandoc")
    if found:
        return found
    print(
        "Error: pandoc not found. Install it from https://pandoc.org/installing.html",
        file=sys.stderr,
    )
    sys.exit(2)


def convert_docx_to_md(docx_path: Path, pandoc: str) -> str:
    """Convert .docx to markdown string via pandoc."""
    result = subprocess.run(
        [pandoc, "-f", "docx", "-t", "markdown", "--wrap=none", str(docx_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error: pandoc conversion failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(2)
    return result.stdout


# ---------------------------------------------------------------------------
# Chapter splitting
# ---------------------------------------------------------------------------

CHAPTER_PATTERNS = [
    ("abstract", re.compile(r"^#\s+abstract", re.IGNORECASE)),
    ("ch1", re.compile(r"^#\s+(chapter\s+1|1\s*[\.:]\s*introduction)", re.IGNORECASE)),
    ("ch2", re.compile(r"^#\s+(chapter\s+2|2\s*[\.:]\s*literature)", re.IGNORECASE)),
    ("ch3", re.compile(r"^#\s+(chapter\s+3|3\s*[\.:]\s*method)", re.IGNORECASE)),
    ("ch4", re.compile(r"^#\s+(chapter\s+4|4\s*[\.:]\s*result)", re.IGNORECASE)),
    ("ch5", re.compile(r"^#\s+(chapter\s+5|5\s*[\.:]\s*discussion)", re.IGNORECASE)),
    ("ch6", re.compile(r"^#\s+(chapter\s+6|6\s*[\.:]\s*conclusion)", re.IGNORECASE)),
]


def split_into_chapters(md_text: str) -> dict[str, str]:
    """Split a single markdown document into chapter texts."""
    lines = md_text.split("\n")
    boundaries: list[tuple[int, str]] = []

    for i, line in enumerate(lines):
        for key, pat in CHAPTER_PATTERNS:
            if pat.match(line.strip()):
                boundaries.append((i, key))
                break

    chapters: dict[str, str] = {k: "" for k in CHAPTER_FILES}

    for idx, (start_line, key) in enumerate(boundaries):
        end_line = boundaries[idx + 1][0] if idx + 1 < len(boundaries) else len(lines)
        chapters[key] = "\n".join(lines[start_line:end_line])

    return chapters


def write_chapter_files(chapters: dict[str, str], outdir: Path) -> None:
    """Write chapter texts to individual files in outdir."""
    for key, text in chapters.items():
        if text:
            filename = CHAPTER_FILES[key]
            (outdir / filename).write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Sync comparison
# ---------------------------------------------------------------------------

def _extract_headings(text: str) -> list[str]:
    """Extract markdown headings from text."""
    return [
        line.strip()
        for line in text.split("\n")
        if re.match(r"^#{1,4}\s+", line.strip())
    ]


def _section_word_counts(text: str) -> dict[str, int]:
    """Return word counts per section heading."""
    sections: dict[str, int] = {}
    current_heading = "(preamble)"
    current_words: list[str] = []

    for line in text.split("\n"):
        if re.match(r"^#{1,4}\s+", line.strip()):
            if current_words:
                sections[current_heading] = len(current_words)
            current_heading = line.strip()
            current_words = []
        else:
            cleaned = re.sub(r"<!--.*?-->", "", line)
            current_words.extend(cleaned.split())

    if current_words:
        sections[current_heading] = len(current_words)

    return sections


def compare_chapters(docx_texts: dict[str, str], draft_texts: dict[str, str]) -> str:
    """Compare docx-converted chapters against draft markdown files."""
    output_lines = [
        "",
        "Sync Comparison: DOCX vs. Drafts",
        "=================================",
        "",
    ]

    for key in CHAPTER_FILES:
        docx_t = docx_texts.get(key, "")
        draft_t = draft_texts.get(key, "")

        if not docx_t and not draft_t:
            continue

        label = CHAPTER_FILES[key]
        output_lines.append(f"--- {label} ---")

        if not docx_t:
            output_lines.append("  [Not found in DOCX]")
            output_lines.append("")
            continue
        if not draft_t:
            output_lines.append("  [Not found in drafts]")
            output_lines.append("")
            continue

        # Heading comparison
        docx_headings = set(_extract_headings(docx_t))
        draft_headings = set(_extract_headings(draft_t))

        only_docx = docx_headings - draft_headings
        only_draft = draft_headings - docx_headings

        if only_docx:
            output_lines.append(f"  Headings only in DOCX:   {', '.join(sorted(only_docx)[:5])}")
        if only_draft:
            output_lines.append(f"  Headings only in draft:  {', '.join(sorted(only_draft)[:5])}")
        if not only_docx and not only_draft:
            output_lines.append("  Headings: match")

        # Word count comparison
        docx_wc = _section_word_counts(docx_t)
        draft_wc = _section_word_counts(draft_t)

        total_docx = sum(docx_wc.values())
        total_draft = sum(draft_wc.values())
        diff = total_docx - total_draft
        direction = "more" if diff > 0 else "fewer"
        output_lines.append(
            f"  Word count: DOCX={total_docx}, Draft={total_draft} "
            f"(DOCX has {abs(diff)} {direction} words)"
        )

        # Flag large section-level differences
        all_sections = set(docx_wc.keys()) | set(draft_wc.keys())
        big_diffs = []
        for sec in sorted(all_sections):
            dw = docx_wc.get(sec, 0)
            drw = draft_wc.get(sec, 0)
            if abs(dw - drw) > 50:
                big_diffs.append(f"    {sec}: DOCX={dw}w, Draft={drw}w (delta={dw - drw:+d})")
        if big_diffs:
            output_lines.append("  Sections with large differences (>50 words):")
            output_lines.extend(big_diffs)

        output_lines.append("")

    return "\n".join(output_lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify a TIM report .docx by converting to markdown and running checks."
    )
    parser.add_argument("docx", type=str, help="Path to the .docx file")
    parser.add_argument(
        "--drafts",
        type=str,
        default=None,
        help="Path to markdown drafts directory for sync comparison",
    )
    parser.add_argument(
        "--pandoc",
        type=str,
        default=None,
        help="Path to pandoc binary (auto-detected if omitted)",
    )
    args = parser.parse_args()

    docx_path = Path(args.docx).resolve()
    if not docx_path.is_file():
        print(f"Error: '{docx_path}' is not a file.", file=sys.stderr)
        return 2

    pandoc = find_pandoc(args.pandoc)

    # Convert
    print(f"Converting {docx_path.name} with pandoc...")
    md_text = convert_docx_to_md(docx_path, pandoc)

    # Split into chapters
    chapters = split_into_chapters(md_text)
    found = [k for k, v in chapters.items() if v]
    print(f"Found chapters: {', '.join(found)}")

    # Write to temp dir and run evaluation
    with tempfile.TemporaryDirectory(prefix="tim_verify_") as tmpdir:
        tmppath = Path(tmpdir)
        write_chapter_files(chapters, tmppath)

        texts = load_texts(tmppath)
        results = run_checks(texts)
        exit_code = print_results(f"{docx_path.name} (converted)", results)

    # Sync comparison
    if args.drafts:
        drafts_dir = Path(args.drafts).resolve()
        if not drafts_dir.is_dir():
            print(f"Warning: drafts directory '{drafts_dir}' not found.", file=sys.stderr)
        else:
            from evaluate_report import load_texts as load_draft_texts
            draft_texts = load_draft_texts(drafts_dir)
            comparison = compare_chapters(chapters, draft_texts)
            print(comparison)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
