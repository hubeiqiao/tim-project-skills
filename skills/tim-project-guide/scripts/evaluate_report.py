#!/usr/bin/env python3
"""
TIM Report Evaluation Script

Auto-checks ~17 checklist items on markdown chapter files for a TIM
(Technology Innovation Management) project report.

Usage:
    python evaluate_report.py path/to/TIM_Report_Draft/

Exit code: 0 if all pass, 1 if any fail.
"""

import argparse
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

CHAPTER_FILES = {
    "abstract": "abstract.md",
    "ch1": "ch1_introduction.md",
    "ch2": "ch2_literature_review.md",
    "ch3": "ch3_method.md",
    "ch4": "ch4_results.md",
    "ch5": "ch5_discussion.md",
    "ch6": "ch6_conclusions.md",
}

# Allow alternate filenames
ALTERNATE_FILES = {
    "ch5": ["ch5_discussion_outline.md"],
}


def _resolve(directory: Path, key: str) -> Path | None:
    """Return the first existing file for *key*."""
    primary = directory / CHAPTER_FILES[key]
    if primary.exists():
        return primary
    for alt in ALTERNATE_FILES.get(key, []):
        p = directory / alt
        if p.exists():
            return p
    return None


def _read(path: Path | None) -> str:
    if path is None:
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def _word_count(text: str) -> int:
    # Strip markdown headings, HTML comments, and blank lines
    cleaned = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    cleaned = re.sub(r"^#+\s.*$", "", cleaned, flags=re.MULTILINE)
    return len(cleaned.split())


def _has_heading(text: str, pattern: str) -> bool:
    """Check if text contains a markdown heading matching *pattern* (case-insensitive)."""
    return bool(re.search(r"^#{1,4}\s+.*" + pattern, text, re.IGNORECASE | re.MULTILINE))


def _has_summary(text: str) -> bool:
    return _has_heading(text, r"summary")


def _section_between(text: str, start_pat: str, end_pat: str | None) -> str:
    """Extract text between two heading patterns."""
    start = re.search(r"^(#{1,4}\s+.*" + start_pat + r".*)", text, re.IGNORECASE | re.MULTILINE)
    if not start:
        return ""
    rest = text[start.end():]
    if end_pat:
        end = re.search(r"^#{1,4}\s+.*" + end_pat, rest, re.IGNORECASE | re.MULTILINE)
        if end:
            rest = rest[: end.start()]
    return rest


# ---------------------------------------------------------------------------
# Individual checks — each returns (pass: bool, evidence: str)
# ---------------------------------------------------------------------------

def check_abstract_word_count(texts: dict) -> tuple[bool, str]:
    wc = _word_count(texts["abstract"])
    return (wc <= 150, f"{wc} words")


def check_abstract_elements(texts: dict) -> tuple[bool, str]:
    t = texts["abstract"].lower()
    elements = {
        "problem/gap": any(w in t for w in ["problem", "gap", "challenge", "lack", "limited", "despite"]),
        "client": any(w in t for w in ["client", "agi venture", "company", "organization", "firm"]),
        "deliverables": any(w in t for w in ["deliverable", "framework", "product", "brief", "artifact"]),
        "method": any(w in t for w in ["method", "design science", "dsr", "approach", "methodology"]),
        "contribution": any(w in t for w in ["contribut", "advance", "implicat", "value", "insight"]),
    }
    found = [k for k, v in elements.items() if v]
    missing = [k for k, v in elements.items() if not v]
    ok = len(missing) == 0
    if ok:
        return (True, f"Found: {', '.join(found)}")
    return (False, f"Missing: {', '.join(missing)}")


def check_ch1_sections(texts: dict) -> tuple[bool, str]:
    t = texts["ch1"]
    required = [
        ("1.1", r"1\.1\b.*objective"),
        ("1.2", r"1\.2\b.*deliverable"),
        ("1.3", r"1\.3\b.*relevance"),
        ("1.4", r"1\.4\b.*known"),
        ("1.5", r"1\.5\b.*contribution"),
        ("1.6", r"1\.6\b.*method"),
        ("1.7", r"1\.7\b.*organization"),
        ("1.8", r"1\.8\b.*summary"),
    ]
    found = []
    missing = []
    for label, pat in required:
        if re.search(pat, t, re.IGNORECASE):
            found.append(label)
        else:
            missing.append(label)
    ok = len(missing) == 0
    if ok:
        return (True, f"All 8 sections present")
    return (False, f"Missing: {', '.join(missing)}")


def check_ch1_7_one_paragraph(texts: dict) -> tuple[bool, str]:
    section = _section_between(texts["ch1"], r"1\.7\b", r"1\.8\b")
    if not section.strip():
        return (False, "Section 1.7 not found or empty")
    # Count non-empty paragraphs (blocks of text separated by blank lines)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", section.strip()) if p.strip()]
    # Filter out HTML comments
    paragraphs = [p for p in paragraphs if not re.match(r"^<!--.*-->$", p, re.DOTALL)]
    count = len(paragraphs)
    if count == 1:
        return (True, "1 paragraph")
    return (False, f"{count} paragraphs (expected 1)")


def check_ch2_summary(texts: dict) -> tuple[bool, str]:
    ok = _has_summary(texts["ch2"])
    return (ok, "Summary heading found" if ok else "No Summary heading")


def check_ch3_summary(texts: dict) -> tuple[bool, str]:
    ok = _has_summary(texts["ch3"])
    return (ok, "Summary heading found" if ok else "No Summary heading")


def check_ch3_method_table(texts: dict) -> tuple[bool, str]:
    t = texts["ch3"]
    # Look for a markdown table (|---|) before any "3.1" heading
    m31 = re.search(r"^#{1,4}\s+3\.1\b", t, re.MULTILINE)
    before = t[: m31.start()] if m31 else t[:2000]
    has_table = bool(re.search(r"\|.*\|.*\|", before))
    return (has_table, "Table found before 3.1" if has_table else "No table found before 3.1")


def check_ch3_research_design(texts: dict) -> tuple[bool, str]:
    t = texts["ch3"]
    m31 = re.search(r"^#{1,4}\s+3\.1\b", t, re.MULTILINE)
    before = t[: m31.start()] if m31 else t[:3000]
    has_rd = bool(re.search(r"research\s+design", before, re.IGNORECASE))
    return (has_rd, "Research design content found" if has_rd else "No 'research design' mention before 3.1")


def check_ch4_past_tense(texts: dict) -> tuple[bool, str]:
    t = texts["ch4"].lower()
    present_markers = [
        r"\bwe\s+conduct\b", r"\bwe\s+analyze\b", r"\bwe\s+build\b",
        r"\bwe\s+develop\b", r"\bwe\s+create\b", r"\bwe\s+implement\b",
        r"\bwe\s+collect\b", r"\bwe\s+design\b", r"\bwe\s+evaluate\b",
        r"\bthis\s+shows\b", r"\bthis\s+demonstrates\b",
        r"\bwe\s+present\b", r"\bwe\s+describe\b",
    ]
    found = []
    for pat in present_markers:
        matches = re.findall(pat, t)
        if matches:
            found.extend(matches)
    if not found:
        return (True, "No present-tense markers detected")
    unique = list(set(found))[:5]
    return (False, f"Present-tense markers: {', '.join(repr(m) for m in unique)}")


def check_ch4_summary(texts: dict) -> tuple[bool, str]:
    ok = _has_summary(texts["ch4"])
    return (ok, "Summary heading found" if ok else "No Summary heading")


def check_ch5_summary(texts: dict) -> tuple[bool, str]:
    ok = _has_summary(texts["ch5"])
    return (ok, "Summary heading found" if ok else "No Summary heading")


def check_ch5_cross_refs(texts: dict) -> tuple[bool, str]:
    t = texts["ch5"]
    patterns = [r"Table\s+4\.", r"Section\s+4\.", r"Figure\s+4\.", r"Table\s+\d+", r"Section\s+\d+\.\d+", r"Figure\s+\d+"]
    found = []
    for pat in patterns:
        if re.search(pat, t):
            found.append(pat.replace(r"\s+", " ").replace(r"\.", ".").replace(r"\d+", "N"))
    if found:
        unique = sorted(set(found))[:4]
        return (True, f"Cross-refs found: {', '.join(unique)}")
    return (False, "No cross-references to tables/sections/figures found")


def check_ch5_lit_comparison(texts: dict) -> tuple[bool, str]:
    t = texts["ch5"].lower()
    markers = ["chapter 2", "ch2", "ch 2", "literature", "previous research", "prior research",
               "literature review", "scoping review"]
    found = [m for m in markers if m in t]
    if found:
        return (True, f"Literature references: {', '.join(found[:3])}")
    return (False, "No references to Ch2 / literature found")


def check_ch6_sections(texts: dict) -> tuple[bool, str]:
    t = texts["ch6"]
    checks = {
        "Conclusion(s)": _has_heading(t, r"conclusion"),
        "Limitation(s)": _has_heading(t, r"limitation"),
        "Future Research": _has_heading(t, r"future\s+research"),
    }
    found = [k for k, v in checks.items() if v]
    missing = [k for k, v in checks.items() if not v]
    if not missing:
        return (True, "All 3 sections present")
    return (False, f"Missing: {', '.join(missing)}")


def check_ch6_limitation_future_mapping(texts: dict) -> tuple[bool, str]:
    t = texts["ch6"]
    lim_section = _section_between(t, r"limitation", r"future\s+research")
    future_section = _section_between(t, r"future\s+research", None)
    lim_ok = len(lim_section.strip()) > 20
    fut_ok = len(future_section.strip()) > 20
    if lim_ok and fut_ok:
        return (True, "Both sections non-empty")
    issues = []
    if not lim_ok:
        issues.append("Limitations empty/missing")
    if not fut_ok:
        issues.append("Future Research empty/missing")
    return (False, "; ".join(issues))


def check_all_summaries(texts: dict) -> tuple[bool, str]:
    chapters = ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6"]
    missing = []
    for ch in chapters:
        if texts[ch] and not _has_summary(texts[ch]):
            missing.append(ch)
    if not missing:
        return (True, "All chapters have Summary")
    return (False, f"Missing Summary: {', '.join(missing)}")


def check_deliverable_consistency(texts: dict) -> tuple[bool, str]:
    deliverables = ["D1", "D2", "D3", "D4"]
    ch_keys = ["ch1", "ch3", "ch4"]
    presence = {}
    for d in deliverables:
        presence[d] = []
        for ch in ch_keys:
            if re.search(r"\b" + d + r"\b", texts[ch]):
                presence[d].append(ch)
    issues = []
    for d in deliverables:
        chs = presence[d]
        if 0 < len(chs) < 3:
            missing = [c for c in ch_keys if c not in chs]
            issues.append(f"{d} in {','.join(chs)} but not {','.join(missing)}")
    if not issues:
        return (True, "D1-D4 consistent across Ch1, Ch3, Ch4")
    return (False, "; ".join(issues))


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

ALL_CHECKS: list[tuple[str, callable]] = [
    ("Abstract <= 150 words", check_abstract_word_count),
    ("Abstract has 5 elements", check_abstract_elements),
    ("Ch1 sections present", check_ch1_sections),
    ("Ch1.7 is one paragraph", check_ch1_7_one_paragraph),
    ("Ch2 has Summary", check_ch2_summary),
    ("Ch3 has Summary", check_ch3_summary),
    ("Ch3 method table before 3.1", check_ch3_method_table),
    ("Ch3 research design before 3.1", check_ch3_research_design),
    ("Ch4 uses past tense", check_ch4_past_tense),
    ("Ch4 has Summary", check_ch4_summary),
    ("Ch5 has Summary", check_ch5_summary),
    ("Ch5 has cross-references", check_ch5_cross_refs),
    ("Ch5 literature comparison", check_ch5_lit_comparison),
    ("Ch6 has 3 sections", check_ch6_sections),
    ("Ch6 limitation-future mapping", check_ch6_limitation_future_mapping),
    ("Every chapter has Summary", check_all_summaries),
    ("Deliverable consistency (D1-D4)", check_deliverable_consistency),
]

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def load_texts(directory: Path) -> dict[str, str]:
    texts = {}
    for key in CHAPTER_FILES:
        path = _resolve(directory, key)
        texts[key] = _read(path)
    return texts


def run_checks(texts: dict) -> list[tuple[str, bool, str]]:
    results = []
    for label, fn in ALL_CHECKS:
        try:
            passed, evidence = fn(texts)
        except Exception as exc:
            passed, evidence = False, f"Error: {exc}"
        results.append((label, passed, evidence))
    return results


def print_results(directory: str, results: list[tuple[str, bool, str]]) -> int:
    print()
    print("TIM Report Evaluation")
    print("=====================")
    print(f"Directory: {directory}")
    print()

    # Compute column widths
    num_w = len(str(len(results)))
    label_w = max(len(r[0]) for r in results)
    res_w = 4  # PASS/FAIL

    header = f"| {'#':>{num_w}} | {'Check':<{label_w}} | {'Result':<{res_w}} | Evidence"
    sep = f"|{'-' * (num_w + 2)}|{'-' * (label_w + 2)}|{'-' * (res_w + 2)}|{'-' * 40}"
    print(header)
    print(sep)

    pass_count = 0
    fail_count = 0
    for i, (label, passed, evidence) in enumerate(results, 1):
        status = "PASS" if passed else "FAIL"
        if passed:
            pass_count += 1
        else:
            fail_count += 1
        print(f"| {i:>{num_w}} | {label:<{label_w}} | {status:<{res_w}} | {evidence}")

    total = pass_count + fail_count
    print()
    print(f"Summary: {pass_count}/{total} PASS, {fail_count} FAIL")
    print()

    return 0 if fail_count == 0 else 1


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate a TIM project report (markdown chapter files)."
    )
    parser.add_argument(
        "directory",
        type=str,
        help="Path to directory containing chapter markdown files",
    )
    args = parser.parse_args()

    directory = Path(args.directory).resolve()
    if not directory.is_dir():
        print(f"Error: '{directory}' is not a directory.", file=sys.stderr)
        return 2

    texts = load_texts(directory)

    # Check that at least some files exist
    found_files = [k for k in texts if texts[k]]
    if not found_files:
        print(f"Error: No chapter files found in '{directory}'.", file=sys.stderr)
        return 2

    results = run_checks(texts)
    return print_results(str(directory), results)


if __name__ == "__main__":
    sys.exit(main())
