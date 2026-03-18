#!/usr/bin/env python3
"""
TIM Report Shell Generator

Creates markdown skeleton files with all required section headings for a
TIM (Technology Innovation Management) project report.

Usage:
    python generate_shell.py [options] output_directory/

Options:
    --approach A|B       Ch2 literature review approach (default: A)
    --steps N            Number of method steps (default: 6)
    --deliverables N     Number of deliverables (default: 4)
    --numbering sequential|chapter  Table/figure numbering style (default: sequential)
"""

import argparse
import os
import sys
from pathlib import Path


def _d_placeholders(n: int) -> str:
    lines = []
    for i in range(1, n + 1):
        lines.append(f"- **D{i}:** [Deliverable {i} name]")
    return "\n".join(lines)


def _step_sections_ch3(steps: int) -> str:
    parts = []
    for i in range(1, steps + 1):
        parts.append(f"""## 3.{i} Step {i}: [Step Title]

<!-- Describe WHAT you did (activities) and HOW. Do NOT include outcomes here — those go in Ch4. -->
""")
    return "\n".join(parts)


def _step_sections_ch4(steps: int) -> str:
    parts = []
    for i in range(1, steps + 1):
        parts.append(f"""## 4.{i} Results of Step {i}: [Step Title]

<!-- Report the OUTCOMES of Step {i}. Past tense. Objective. No interpretation. -->
""")
    return "\n".join(parts)


def generate_abstract() -> str:
    return """# Abstract

<!-- Single paragraph, max 150 words. Must contain ALL 5 elements:
1. Problem / gap
2. Client
3. Deliverables
4. Method
5. Contribution
No undefined abbreviations. -->

[Write abstract here]
"""


def generate_ch1(num_deliverables: int) -> str:
    d_list = _d_placeholders(num_deliverables)
    return f"""# Chapter 1: Introduction

<!-- Introductory remarks (preamble): the client, the problem, reasons for choosing this topic, importance, previous attempts, insights from literature. This preamble sets the stage before the numbered sections. -->

## 1.1 Objective

<!-- State what the project accomplishes. Should be SMART: Specific, Measurable, Achievable, Relevant, Time-bound. -->

## 1.2 Deliverables

<!-- Bulleted list of deliverables (2-4 typical). Each must directly support the objective. These IDs (D1, D2, ...) must be used consistently in Ch3 and Ch4. -->

{d_list}

## 1.3 Relevance

<!-- Relevance to the client and client manager. Evidence of interest. Potential value to the client and beyond. -->

## 1.4 What Is Known and Not Known

<!-- State of current knowledge from both theory and practice. Emphasize peer-reviewed research. Identify the gap your project addresses. -->

## 1.5 Contribution

<!-- How the project advances knowledge. What will be known after the project that is not known now. -->

## 1.6 Overview of Method

<!-- Brief overall statement of the method used (e.g., Design Science Research). Keep it high-level; details go in Ch3. -->

## 1.7 Organization of the Report

<!-- ONE informative narrative paragraph describing the structure of the remaining chapters. Not a bulleted list. Not one paragraph per chapter. -->

## 1.8 Summary

<!-- Brief recap of the chapter's key points. Transition sentence to Chapter 2. -->
"""


def generate_ch2(approach: str) -> str:
    if approach.upper() == "A":
        body = """## 2.1 Review Method

<!-- Describe the scoping review protocol: databases searched, search terms, inclusion/exclusion criteria, number of studies. -->

## 2.2 Stream 1: [Stream Title]

<!-- Synthesize findings from the first thematic stream of literature. -->

## 2.3 Stream 2: [Stream Title]

<!-- Synthesize findings from the second thematic stream. -->

## 2.4 Stream 3: [Stream Title]

<!-- Synthesize findings from the third thematic stream. Add/remove streams as needed. -->

## 2.5 Summary

<!-- Recap the key themes and gaps identified. Transition to Ch3. -->
"""
    else:
        body = """## 2.1 Review Method

<!-- Describe the scoping review protocol: databases searched, search terms, inclusion/exclusion criteria, number of studies. -->

## 2.2 Review Question 1: [Question]

<!-- Synthesize literature addressing the first review question. -->

## 2.3 Review Question 2: [Question]

<!-- Synthesize literature addressing the second review question. -->

## 2.4 Review Question 3: [Question]

<!-- Synthesize literature addressing the third review question. Add/remove as needed. -->

## 2.5 Summary

<!-- Recap answers to the review questions and remaining gaps. Transition to Ch3. -->
"""
    return f"""# Chapter 2: Literature Review

<!-- NO personal opinions in this chapter. Save interpretation for Ch5.
All literature review content belongs here — not in Ch1, Ch3, or Ch4. -->

{body}"""


def generate_ch3(steps: int) -> str:
    step_sections = _step_sections_ch3(steps)
    return f"""# Chapter 3: Method

<!-- Describe WHAT you did and HOW. Activities ONLY — no outcomes (those go in Ch4).
The structure of Ch3 and Ch4 should mirror each other. -->

<!-- Research Design: brief description of overall approach (e.g., Design Science Research) -->

<!-- Method overview table — include BEFORE section 3.1 -->

| Step | Activity | Output |
|------|----------|--------|
| 1    | [Activity 1] | [Output 1] |
| 2    | [Activity 2] | [Output 2] |
| 3    | [Activity 3] | [Output 3] |
| ...  | ...          | ...        |

{step_sections}
## 3.{steps + 1} Summary

<!-- Recap the method steps and how they connect. Transition to Ch4. -->
"""


def generate_ch4(steps: int) -> str:
    step_sections = _step_sections_ch4(steps)
    return f"""# Chapter 4: Results

<!-- Report OUTCOMES only. Past tense. Objective. No interpretation (save for Ch5).
The structure of Ch4 mirrors Ch3. -->

{step_sections}
## 4.{steps + 1} Summary

<!-- Recap the key results across all steps. Transition to Ch5. -->
"""


def generate_ch5() -> str:
    return """# Chapter 5: Discussion

<!-- Interpret results. Compare findings with Ch2 literature. Discuss implications.
Must include cross-references to Ch4 results (e.g., "Table 4.1", "Section 4.2"). -->

## 5.1 Interpretation of Results

<!-- What do the results mean? Connect back to the objective stated in Ch1. -->

## 5.2 Comparison with Literature

<!-- How do results align or diverge from the literature reviewed in Ch2? Reference specific studies. -->

## 5.3 Implications

<!-- Implications for theory and practice. What should practitioners or researchers take away? -->

## 5.4 Summary

<!-- Recap the discussion. Transition to Ch6. -->
"""


def generate_ch6() -> str:
    return """# Chapter 6: Conclusions

## 6.1 Conclusions

<!-- State the main conclusions drawn from the project. Tie back to the objective and deliverables. -->

## 6.2 Limitations

<!-- Up to 3 limitations. Be specific and honest. Each limitation should suggest a corresponding future research direction. -->

1. [Limitation 1]
2. [Limitation 2]
3. [Limitation 3]

## 6.3 Future Research

<!-- Future research directions that address the limitations above. Each should map to at least one limitation. -->

1. [Future direction addressing Limitation 1]
2. [Future direction addressing Limitation 2]
3. [Future direction addressing Limitation 3]

## 6.4 Summary

<!-- Brief final recap of the project's contribution. -->
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate TIM project report markdown skeleton files."
    )
    parser.add_argument(
        "output_directory",
        type=str,
        help="Directory to write skeleton chapter files into",
    )
    parser.add_argument(
        "--approach",
        choices=["A", "B"],
        default="A",
        help="Ch2 literature review approach: A=by stream (default), B=by review question",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=6,
        help="Number of method steps (default: 6)",
    )
    parser.add_argument(
        "--deliverables",
        type=int,
        default=4,
        help="Number of deliverables (default: 4)",
    )
    parser.add_argument(
        "--numbering",
        choices=["sequential", "chapter"],
        default="sequential",
        help="Table/figure numbering style (default: sequential)",
    )
    args = parser.parse_args()

    outdir = Path(args.output_directory).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    files = {
        "abstract.md": generate_abstract(),
        "ch1_introduction.md": generate_ch1(args.deliverables),
        "ch2_literature_review.md": generate_ch2(args.approach),
        "ch3_method.md": generate_ch3(args.steps),
        "ch4_results.md": generate_ch4(args.steps),
        "ch5_discussion.md": generate_ch5(),
        "ch6_conclusions.md": generate_ch6(),
    }

    for filename, content in files.items():
        path = outdir / filename
        path.write_text(content, encoding="utf-8")
        print(f"  Created: {path}")

    print()
    print(f"Generated {len(files)} skeleton files in {outdir}")
    print(f"  Approach: {args.approach} | Steps: {args.steps} | Deliverables: {args.deliverables} | Numbering: {args.numbering}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
