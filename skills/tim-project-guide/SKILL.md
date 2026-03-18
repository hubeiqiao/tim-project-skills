---
name: tim-project-guide
description: "Use when structuring, formatting, evaluating, or reviewing a Technology Innovation Management (TIM) project report for Carleton University — provides report rules, chapter guidance, literature review expectations, research method templates, and a compliance-audit checklist."
---

# TIM Project Report Guide

## What This Skill Helps With

Use this skill when you are writing, revising, or reviewing a Carleton University Technology Innovation Management (TIM) project report and need help with structure, formatting, chapter expectations, or research-method guidance.

## Ask for this skill with prompts like

Use the exact skill name `$tim-project-guide` in your prompt. Include whether your work is a project or thesis, your program, the chapter or section you need help with, and any supervisor-specific constraints if you have them.

- `Use $tim-project-guide to check whether my TIM report structure is correct.`
- `Use $tim-project-guide to help me write the Introduction chapter for my TIM report.`
- `Use $tim-project-guide to review my abstract against the TIM requirements.`
- `Use $tim-project-guide to compare my literature review plan against the guideline.`
- `Use $tim-project-guide to evaluate my completed TIM report.`
- `Use $tim-project-guide to run a compliance audit on my TIM report before submission.`

## Source and Scope

This skill summarizes TIM project guideline materials for report formatting, report structure, research-method templates, and the project-versus-thesis distinctions that appear in the source materials. Use it as a working guide for TIM report assistance, then verify any final institutional requirements against the latest course or supervisor instructions.

**Source documents synthesized:**
1. Carleton University Formatting Guidelines
2. Guidelines to Write a TIM Project Report (newer version, preferred)
3. TIM Project Report Guideline (older version, for reference)
4. Research Method Templates

**Note on guideline versions:** Where the newer and older guideline documents differ, this skill documents both versions and recommends confirming with your supervisor. Key differences are flagged inline.

---

## 1. Formatting Rules

### Paper and Font
- Standard white printer paper, 8.5" x 11"
- 12-point standard font (no fanciful typestyles)
- One-sided printing only
- Double-spaced text throughout
- Footnotes and long quotations may be single-spaced
- Spacing may vary on table and figure material

### Margins
- **Left**: 1.5 inches (binding margin)
- **Top, Right, Bottom**: 1 inch each
- Margins may be wider but never narrower

### Pagination
- **Preliminary pages**: Small Roman numerals (ii, iii, iv...)
  - Title page = implied "i" but the number is NOT printed
  - Number all other preliminary pages
- **Body text**: Arabic numerals starting at 1
  - Continues consecutively through text, illustrations, bibliography, and appendices to the last page

### Title Page Requirements

**For TIM projects (NOT thesis)**, the required statement is:

> "A project submitted in partial fulfillment of the requirements for the degree of [degree] in Technology Innovation Management"

Where the degree is one of:
- Master of Applied Business Analytics in Technology Innovation Management
- Master of Digital Transformation and Entrepreneurship in Technology Innovation Management
- Master of Engineering in Technology Innovation Management
- Master of Entrepreneurship in Technology Innovation Management
- Master of Technology in Technology Innovation Management

**For thesis projects**, the statement is instead:

> "A thesis submitted to the Office of Graduate Studies in partial fulfillment of the requirements for the degree of [Master of Applied Science / Master of Science] in Technology Innovation Management"

**Title page layout (top to bottom):**
1. Title (clear wording, reflects the subject; avoid Greek letters, abbreviations, formulas, symbols)
2. "by"
3. Student name (first name last name order, must match Carleton registration)
4. Required statement (project or thesis version as above)
5. "in"
6. Program name (official name from graduate calendar, NOT department name)
7. "Carleton University"
8. "Ottawa, Ontario"
9. Copyright: (c) [Year] [Student Name]

### Abstract
- Single paragraph, maximum 150 words
- Must cover exactly 5 elements:
  1. Problem addressed or gap to fill
  2. Client served
  3. Deliverables/outcomes to produce
  4. Method used to produce deliverables
  5. Contribution (expected impact of results)
- No undefined abbreviations, no literature review findings, no in-text citations
- Write the abstract BEFORE writing the report; update frequently throughout

### Illustrative Material
- Use standard 8.5" x 11" pages unless strong reasons for larger
- No text or figures on backs of pages
- Coloured illustrations allowed; avoid black backgrounds (poor scanning)

### Table of Contents, List of Tables, List of Figures, List of Appendices

**Heading styles are the foundation — use them from day one.** Apply Heading 1 for chapter titles, Heading 2 for sections (1.1, 2.3, etc.), and Heading 3 for subsections. Never format a heading by manually changing font size and bolding — always use the built-in heading styles. This single habit makes everything below work automatically.

**Create the ToC once, early:**
- **MS Word:** References > Table of Contents > insert an automatic style
- **LibreOffice Writer:** Insert > Table of Contents and Index

The ToC is a permanent element of your document. You do not recreate it; you update it.

**Use Insert Caption for all tables and figures.** This auto-generates the List of Tables and List of Figures via the same References > Insert Table of Figures dialog. Never type "Table 1:" or "Figure 3:" by hand.

**Never type ToC entries manually.** If a heading does not appear in the ToC, the fix is to apply the correct heading style — not to type the entry into the ToC.

**Final step before submission — update all fields:**
1. Select all (Ctrl+A / Cmd+A)
2. Update fields (F9 on Windows; Cmd+Option+Shift+U on Mac; or right-click any field > Update Field)
3. For the ToC specifically: right-click > Update Field > "Update Entire Table"

This single action refreshes the ToC, List of Tables, List of Figures, List of Appendices, all cross-references, and all caption numbers. Do this as one of your very last steps before generating the PDF for submission.

---

## 2. Report Structure

### Getting Started

The guidelines recommend this preparation sequence:
1. **Write the abstract first** — update frequently as you make progress (from both guidelines)
2. **Draft the four starting points for Ch1** before writing the chapter: purpose, deliverables, contributions, audience profiles (from both guidelines)
3. **Draft the four starting points for Ch3** before writing it: research design, method table, data acquisition plan, data analysis plan (from both guidelines)
4. **Build the Table of Contents structure early** using heading styles (from both guidelines)
5. **Use the report shell** as a structural starting point — each chapter starts on a new page with the required section headings (from both guidelines; see `scripts/generate_shell.py`)

**Example reports** for reference (if available in your Guidelines directory):
- Guilherme Barbassa (MEng, 2024) — Product-Market Fit Analysis
- Naznoosh Mohammad Zadeh (MEng, 2025) — CRA project

### Preliminary Pages (in order)

1. **Title page** (implied "i", not printed)
2. **Abstract** (required)
3. **Acknowledgements** (optional)
4. **Table of Contents** (required; auto-generated recommended)
5. **List of Tables** (required)
6. **List of Figures** (required)
7. **List of Appendices** (required)
8. **Glossary of Terms** (optional; placed last, immediately before Ch1)

**Glossary format** (if included): Alphabetical list with three columns:
- Term
- Definition (concise, contextualized)
- Source (citation with page number)

**Note on Glossary of Terms:** The newer guideline ("Guidelines to Write") includes the Glossary of Terms as an optional preliminary page placed immediately before Chapter 1. The older guideline ("TIM Project Report Guideline") does not mention a Glossary of Terms in the preliminary pages. If you plan to include a glossary, confirm with your supervisor that it is appropriate for your project.

### Chapter 1: Introduction

Introduces topic, provides context, states objectives, deliverables, contribution, and importance.

**Sections:**
1. **Introductory remarks (preamble)** - follows chapter heading with no section number:
   - The client
   - The problem being solved or gap being filled
   - Reasons for choosing this topic
   - Importance of the topic
   - Previous attempts to solve the problem
   - Insights from scholarly literature
2. **1.1 Objective** - what the project accomplishes
3. **1.2 Deliverables** - bulleted list; 2-4 typical; provided in Ch4; must support the objective. *(From newer guideline: deliverables should be consistent with those of the G0 slide deck and the SAR.)*
4. **1.3 Relevance** - relevance to client and client manager; evidence of interest; potential value
5. **1.4 What is known and not known** - state of current knowledge (theory and practice); emphasize peer-reviewed research
6. **1.5 Contribution** - how the project advances knowledge
7. **1.6 Overview of method** - brief overall statement of the method
8. **1.7 Organization of the report** - one informative narrative paragraph (not a bulleted list)
   > **Common mistake:** "One informative narrative paragraph" means exactly ONE paragraph — not one paragraph per chapter and not a bulleted list. A single flowing paragraph that walks the reader through the report structure.
9. **1.8 Summary** - brief recap of the chapter's key points; transitions to Chapter 2 *(recommended from practice; not explicitly listed in either guideline for Ch1, but listed for Ch3–5)*

### Chapter 2: Literature Review

Summary of published research by scholars and experts. NOT a forum for personal opinions.

**Purpose:**
- Present review question(s) that shaped the review
- Summarize and critically evaluate the literature
- Apply lessons and insights to the project
- Describe the review process and methodology
- Identify limitations and how the project addresses gaps

**Review Questions should:**
- Conform to a framework (e.g., PCC - Population, Concept, Context)
- Be clear and concise
- Be answerable by the literature
- Impact deliverable content or development process
- Help deliverables address client pain or create value
- Help understand or implement the results of your project

**Structure (two approaches):**

*Approach A - By stream (traditional; described by the newer guideline as used by "many strong projects"):*
1. Summary table of literature review (row per stream, columns for highlights and citations)
2. Method used to identify articles
3. One section per stream
4. Chapter summary

*Approach B - By review question (use when the project organizes the literature review around specific review questions and the answers from the literature):*

The guideline describes this structure:

1. **Introduction** — Provide background, explain the review's objective, and clearly define the client's problem. Present the review question(s) using a framework like PCC.
2. **Methods** — Define your criteria for studies, including study types, participant groups, and expected outcomes. Explain the search methods (databases, keywords) and data collection strategies.
3. **Results** — Present findings, cite the studies, and assess the risk of bias. Summarize and synthesize the results, breaking them down into their core components.
4. **Conclusion** — Summarize the main findings and how they relate to your project's objectives.
5. **Summary** — Provide a clear, brief overview that allows the reader to understand the core content without reading the entire chapter. Reflects the structure of the chapter. Avoids personal opinions or interpretations.

**Practical extensions for formal scoping/systematic reviews:** When the project involves PRISMA/PRISMA-ScR reporting, consider expanding Approach B with these additional elements (derived from practice, not from the guideline text):

- Under **Methods**: add search strategy detail (databases, search strings, PRISMA-ScR flow with numbers at each stage), inclusion/exclusion criteria table
- Under **Results**: add overview of included studies table, cross-study insights, demographic characteristics
- Add **Thematic sections** between Results and Conclusion (as many as needed, organized by findings — e.g., Theoretical Foundations, Mechanisms, Relationships). Synthesize across studies, not study-by-study.
- Add **Key Findings** (numbered, synthesized from the evidence)
- Add **Design Applications / Practical Implications** (literature-derived, NOT personal opinion)
- Add **Discussion within Ch2** (distinct from Ch5): integration with existing literature, limitations of the review itself, future research directions in the literature

**When to use Approach B:** Use when the project organizes the literature review around review questions rather than by stream. The formal scoping/systematic review extensions are appropriate when the literature review is itself a significant methodological contribution.

**Key principles:**
- Tables are intermediate products for organizing thinking; most won't appear in Ch2
- Ch2 is primarily narrative text, not a collection of tables
- Distinguish "lessons learned" (practical, process) from "insights gained" (conceptual, theoretical)
- No personal opinions; save interpretations for Ch5
- All literature review belongs in Ch2 only (not in Ch3 or Ch4)

### Chapter 3: Method

Describes activities undertaken to produce deliverables. NO OUTCOMES in Ch3.

> **Guideline tension:** The method table lists an "Outcomes" column for each step (from the guideline). The narrative text of each section should describe only activities. Outcomes listed in the method table are reported in detail in Ch4. This means the method table previews what each step produces, but the Ch3 narrative focuses on *how* the work was done, not *what* was found.

**Four foundational parts to draft first:**
1. Research design - overall design rationale
2. Method table - steps, activities, outcomes
3. Data acquisition - variables, measures, sources
4. Data analysis - how data will be analyzed

**Common patterns in Ch3** (practical tips from completed projects, not from the guideline text):

- **Data acquisition plan table:** Include a table specifying Variables, Operational Measures, and Sources. This makes the evaluation design explicit and traceable. Place this in the Research Design section.
- **Data analysis plan:** Describe how each data type will be analyzed (descriptive statistics, thematic coding, funnel analysis, etc.) and what software tools will be used.
- **Ethical considerations:** Include a brief section explaining whether Research Ethics Board (REB) approval was required and why or why not. If the project uses standard commercial analytics rather than controlled experiments with human subjects, state this explicitly.
- **Multi-layer framework pattern:** When the project produces a design framework (common in DSR), describe the layer structure in the relevant method step. For example, a theory-to-mechanism-to-feature-to-metric mapping creates a traceable chain from academic literature to measurable product outcomes. Each layer should be described as an activity in Ch3; the completed framework itself is reported in Ch4.

**Sections (from the guideline):**
1. **Research design** (before section 3.1) - rationale for chosen method; cite published articles using similar methods. This section may include:
   - Data acquisition plan (table: variables, measures, sources)
   - Data analysis plan (methods, tools, significance levels)
   - Ethical considerations (REB applicability statement, if applicable)
2. **Method visualization** (before section 3.1) - table/diagram/flowchart of steps, activities, outcomes
   - Must produce the deliverables from Ch1
   - Should match the SAR (Supervisor Assignment Report)
   - **Structure note (from newer guideline):** "The steps will provide the structure for the sections of chapter 3 and also the sections of chapter 4." Each method step becomes a section in both Ch3 and Ch4.
3. **3.1, 3.2, 3.3...** - one section per step of the method, detailing:
   - Activities at each step
   - Variables used
   - Statistical tests and significance levels
   - Software packages used
4. **Summary**

**Note:** The research design and method visualization come before section 3.1. Then sections 3.1, 3.2, 3.3, etc. each describe one step of the method. If you need subsections within a step, use 3.1.1, 3.1.2, etc.

**Critical rules:**
- Data acquisition != literature review (finding/reading articles is NOT data acquisition)
- Data analysis != literature review
- Do not confuse data acquisition with data analysis
- NO outcomes in Ch3; outcomes go in Ch4

**Data acquisition nuance (from newer guideline):** Some projects acquire and analyze data in a single step; others spread data acquisition and analysis across multiple steps. Structure your method table to reflect your project's actual workflow — there is no single correct pattern.

### Chapter 4: Results

Reports outcomes of the research. Deliverables identified in Ch1, produced via Ch3 method.

**Two organizational approaches:**

*Approach 1 - By method steps (preferred by most TIM projects; recommended by newer guideline):*
- 4.1 = outcomes of step 1
- 4.2 = outcomes of step 2, etc.
- Easiest for reader to connect outcomes to method activities

*Approach 2 - By deliverables (the only approach in the older guideline):*
- 4.1 = results for deliverable 1
- 4.2 = results for deliverable 2, etc.
- Fewer but longer sections

**Note:** The newer guideline ("Guidelines to Write") presents both approaches and notes that Approach 1 is used by most TIM projects. The older guideline ("TIM Project Report Guideline") presents only Approach 2 (by deliverables). Discuss with your supervisor which approach is best for your project.

**Gate 1 vs. Final Report:** The newer guideline notes: "For the gate 1 report, include completed and in-progress steps. For the final report, include all steps." Plan your Ch4 draft accordingly — a gate 1 submission may have partial results.

**Common result types and table patterns** (practical examples from completed projects, not from the guideline text):

- **Competitive feature matrix** (ecosystem profiling outcome): Table comparing products across capability dimensions derived from the literature review. Follow with a market gap analysis narrative.
- **Design framework / mapping table** (framework construction outcome): Table tracing theory to mechanism to feature to metric. Present the summary version in the chapter body; place the full mapping in an appendix.
- **Decision matrix** (technology selection outcome): Table comparing technology candidates or design alternatives against evaluation criteria (cost, accuracy, scalability, alignment with framework).
- **Product/prototype presentation** (build outcome): Include architecture overview, key feature descriptions, mechanism-to-feature implementation mapping, product specifications (tech stack, deployment details), and screenshots/figures.
- **Usage metrics tables** (evaluation outcome): Tables presenting acquisition funnel, feature usage counts, repeat behavior, revenue, and operational observations from the evaluation period.
- **Investment/recommendation brief** (synthesis outcome): Structured assessment synthesizing findings from prior steps into actionable client guidance.

**Guidance on presenting product/prototype results** (practical tips, not from the guideline text):
- Start with a product overview paragraph stating what was built, where it is deployed, and what it does
- Include an architecture overview (technology stack diagram or description)
- Present mechanism-to-feature implementation as a table showing how each theoretical mechanism maps to a specific product feature
- Include product screenshots or figures with descriptive captions
- Report product specifications (languages, frameworks, databases, APIs, hosting)
- Keep all descriptions factual and past tense; do not interpret whether the product "succeeded"

**Writing rules:**
- Always written in past tense (completed work)
- Report results factually, clearly, concisely
- Results do NOT prove or disprove anything
- State objectively without interpretation
- Include figures, charts, tables etc. with proper labels
- Place raw data and intermediate calculations in appendices
- End with summary
- NO activities in Ch4; activities are in Ch3

### Chapter 5: Discussion of Results

The most important chapter for many readers.

**Sections:**
1. **Client problem and project objective** - restate
2. **Interpretation of results** - what findings mean relative to research questions/hypotheses
   - Succinct answer to each research question, anchored in Ch4 results
   - Summary of solution to client problem, anchored in Ch4 results
   - Include cross-references to Ch4 sections, tables, figures
3. **Comparison with previous research** - compare with Ch2 literature
   - Similarities, differences, new insights
   - Position results within broader scholarship
   - Reference key sources from each Ch2 stream
4. **Explanation of unexpected findings** - if any
   - Methodology limitations or external factors
   - Distinguish certainties from speculations
   - This is where speculation is permitted
5. **Implications** - broader impact on field/industry; changes for future research, policy, practice
6. **Summary**

**Organizational tips from practice** (not from the guideline text, but based on completed projects):

- **Organize around 2-3 strongest takeaways** rather than exhaustive coverage. State these takeaways in the opening paragraph and use them as the organizing logic for subsections. For example: "The discussion is organized around three main takeaways: (1) ..., (2) ..., (3) ..."
- **Cross-reference Ch4 evidence explicitly.** Each interpretation claim should cite specific Ch4 sections, tables, or figures (e.g., "as shown in Table 4.1" or "the alpha data in Section 4.6.1").
- **Comparison with previous research (Section 5.3):** Organize by theme rather than by individual source. Reference specific studies from Ch2 streams. Compare what the Ch2 literature predicted with what Ch4 actually showed.
- **Speculation rules:** In the "Explanation of unexpected findings" section, speculation IS permitted but must be clearly labeled. In the "Interpretation of results" section, claims must be anchored in Ch4 evidence. In "Implications," broader claims are acceptable but should reference the evidence base.

> **Common mistake:** Step-number references (e.g., "Step 1 showed…") are NOT sufficient cross-references. Use specific section numbers, table numbers, and figure numbers (e.g., "as shown in Table 4.1" or "the retention data in Section 4.6.1"). The reader should be able to locate the exact evidence without searching.

### Chapter 6: Conclusions, Limitations, and Future Research

Three sections:

1. **Conclusion**
   - Extent to which results solve the problem or fill the gap
   - Interpretation of results
   - Short and long-term implications of the proposed solution

2. **Limitations** (up to 3)
   - Typical: limited data access, time constraints, cultural biases, sample selection, insufficient sample size, lack of prior research

3. **Future Research**
   - Ways future TIM students can overcome the identified limitations
   - **Each limitation should map to at least one future research item** (from guideline: "ways future TIM students can overcome the identified limitations"). The logical-sequence emphasis and numbering convention are from practice.
   - Future research items may also include next steps beyond the limitations (e.g., extending to new markets, adding new data collection methods)
   - Number the items for clarity and traceability to the limitations *(from practice)*

> **Common mistake:** Even the concluding chapter benefits from a Summary section. A brief closing paragraph that restates the project's contribution and ends the report cleanly is recommended from practice, though not explicitly required by the guideline.

### References
- Provide both in-text citations and a reference list
- **Recommended style: Academy of Management (AoM)** - resource: https://library.carleton.ca/guides/help/aom
  - **Note:** The newer guideline recommends AoM style. The older guideline recommends Harvard style. Confirm with your supervisor which citation style to use.
- Alphabetical order by first author's last name
- Every reference must be cited at least once; every citation must have a reference
- Consistent citation style throughout

### Appendices
- Optional; some projects have none, others have many
- Each appendix on a separate page, about one piece of information
- Typical content: background info, letters/emails, supporting importance data, interview transcripts, mathematical computations, questionnaires, raw data, surveys, source code or GitHub links

---

## 3. Critical Alignment Rules

These alignment requirements are non-negotiable:

| Rule | Details |
|------|---------|
| **Deliverables alignment** | Deliverables must be IDENTICAL across Ch1, Ch3 method table, and Ch4 |
| **Activities vs. Outcomes** | Activities in Ch3 ONLY; outcomes in Ch4 ONLY; never mixed |
| **Literature stays in Ch2** | All literature review in Ch2; none in Ch3 or Ch4 |
| **Data acquisition != lit review** | Finding/reading articles is NOT data acquisition |
| **Data analysis != lit review** | Analyzing literature is NOT data analysis |
| **Ch4 tense** | Always past tense |
| **Ch4 objectivity** | No interpretation in Ch4; save for Ch5 |
| **Ch2 objectivity** | No personal opinions in Ch2; save for Ch5 |
| **Method-results mirror** | Ch3 and Ch4 structure should mirror each other |
| **Limitation-future research mapping** | Each limitation in Ch6 should map to at least one future research item |
| **Ch5 anchored in Ch2** | Ch5 comparison must reference specific sources from Ch2 streams |
| **Every chapter has a summary** | Every chapter must end with a Summary section that recaps key points and transitions to the next chapter. *(Ch3/4/5 summaries are from the guideline; Ch1/2/6 summaries are recommended from practice.)* |

### Table/Figure/Appendix Numbering

**IMPORTANT: Two versions exist in official guidelines. Confirm with supervisor.**

- **Version A (newer "Guidelines to Write" document)**: Sequential numbering regardless of chapter
  - Table 1, Table 2, Table 3... (the 4th table is Table 4 no matter which chapter)
  - Figure 1, Figure 2, Figure 3...
- **Version B (older "TIM Project Report Guideline")**: Chapter-based X.Y format
  - Table 3.4 = 4th table in Chapter 3
  - Figure 2.1 = 1st figure in Chapter 2

Use word processor captioning and cross-reference features for auto-updating.

---

## 4. Research Method Templates

Ten method templates are available for TIM projects. Each provides a structured table of steps, activities, and outcomes.

| # | Template Name | Typical Application |
|---|--------------|-------------------|
| 1 | **Identify opportunities using topic modeling and chance discovery** | Identify opportunities to improve products, enter markets, discover trends, or develop landscape views using LDA topic modeling and chance discovery |
| 2 | **Combine two models, frameworks, or processes to build an artifact** | Combine two existing frameworks into a coherent whole, apply the combination, learn from experience, and iterate (e.g., digital marketing plan) |
| 3 | **Develop prototype to reduce a gap** | Find gap between theory and practice, develop plan to reduce it, suggest a prototype (e.g., responsible AI evaluation framework) |
| 4 | **Synthesize literature and observations to construct an artifact** | Review literature and cases, synthesize findings, develop a model/strategy, make recommendations (e.g., internationalization strategy, social media strategy) |
| 5 | **Synthesize theory and practice to build a prototype and learn from use** | Profile ecosystem, construct decision framework, assemble best practices, select approach, develop MVP prototype, observe user behavior and collect lessons |
| 6 | **Combine filled template and case report to produce an artifact** | Select template for XYZ, operationalize it, interview stakeholders, produce case report via NVivo, combine into strategy, prepare implementation plan (e.g., digital strategy) |
| 7 | **Use literature to build artifacts, assess artifacts and workshop data** | Review literature for challenges, develop workshop artifacts, organize workshop, assess results, develop recommendations (e.g., speculative design for responsible AI) |
| 8 | **Combine literature and user feedback to modify a tool for a new market** | Review tool usage in two markets, collect stakeholder feedback, test use cases, identify highest-value application for new market (e.g., HR analytics to education) |
| 9 | **Define complex problem using frame creation** | Review literature on problem space, research focal location, capture stakeholder views, identify paradoxes and opposing forces, develop themes and frames, plan phase 2 |
| 10 | **Design a business model using a design process** | Frame design effort with incumbent templates and PEST analysis, synthesize findings, generate and evaluate alternatives, prototype business model, iterate with feedback |

Each template includes a detailed step-by-step table with columns: Steps, Activities, Outcomes. Refer to the full "Research Method Templates" document in `Guidelines/TIM Project Report/Research Method Templates.txt` for complete details.

---

## 5. Common Supervisor Feedback Patterns

Based on revision cycles from completed TIM projects (practical guidance, not from the guideline documents), anticipate these common feedback areas:

| Feedback Pattern | What It Means | How to Address |
|-----------------|---------------|----------------|
| **Tighten terminology** | Technical terms used without definition, or terms used inconsistently | Define every technical term at first use; maintain a glossary; use consistent terminology throughout |
| **Make DSR iteration explicit** | The report presents the method as purely linear | Acknowledge where iteration occurred (e.g., "Steps 5 and 6 included iterative refinement, with deployment observations informing adjustments") |
| **Identify 2-3 strongest takeaways** | Ch4/Ch5 lack a clear organizing logic | State the takeaways explicitly in Ch4 summary and Ch5 opening; use them to organize Ch5 subsections |
| **Activities leaked into Ch4** | Ch4 contains descriptions of what was done (activities) rather than what was found (outcomes) | Review every Ch4 paragraph: if it describes a process or procedure, move it to Ch3 |
| **Outcomes leaked into Ch3** | Ch3 reveals results before they should appear | Review every Ch3 paragraph: if it states a finding or conclusion, move it to Ch4 |
| **Table formatting inconsistency** | Tables use different styles, column naming, or alignment | Audit all tables for consistent formatting, column headers, and numbering style |
| **Ch2 contains personal opinions** | Interpretive language ("this shows that..." or "clearly...") in the literature review | Replace with objective synthesis language; save interpretation for Ch5 |
| **Ch5 not anchored in Ch4** | Discussion makes claims without cross-referencing specific results | Add explicit cross-references (section numbers, table numbers, figure numbers) for every interpretive claim |
| **Limitations-future research mismatch** | Limitations and future research items are disconnected | Ensure each limitation maps to at least one future research item |
| **Summary sections missing or weak** | Chapter summaries are absent or merely restate the section headings | Every chapter must end with a summary that recaps key points and transitions to the next chapter |

---

## 6. Quick Reference Checklist

Use this when reviewing any section of the report:

### Structure and Formatting
- [ ] Deliverables identical in Ch1, Ch3 method table, and Ch4
- [ ] Abstract <= 150 words with all 5 required elements
- [ ] Title page uses correct statement (project vs. thesis)
- [ ] Preliminary pages in correct order with Roman numeral pagination
- [ ] Body pages numbered with Arabic numerals starting at 1
- [ ] Margins: 1.5" left, 1" other three sides
- [ ] Double-spaced text, 12pt font
- [ ] ToC, List of Tables, List of Figures, List of Appendices generated automatically as final step before submission
- [ ] Tables/figures properly numbered and labeled (confirm numbering version with supervisor)

### Chapter Content
- [ ] Ch1 includes a 1.8 Summary section
- [ ] Ch2 contains only literature review (no opinions)
- [ ] Ch2 Approach B includes PRISMA-ScR flow with numbers at each stage (if applicable)
- [ ] Ch3 contains only activities (no outcomes)
- [ ] Ch3 includes data acquisition plan table, data analysis plan, and ethical considerations
- [ ] Ch4 contains only outcomes (no activities), past tense, no interpretation
- [ ] Ch4 presents product/prototype results with architecture overview and mechanism-to-feature mapping (if applicable)
- [ ] Ch5 interprets results and compares with Ch2 literature
- [ ] Ch5 organized around 2-3 strongest takeaways with explicit Ch4 cross-references
- [ ] Ch6 has exactly 3 sections: Conclusions, Limitations, Future Research
- [ ] Ch6 limitations each map to at least one future research item
- [ ] Each chapter ends with a summary section

### Citations and References
- [ ] All citations have corresponding references and vice versa
- [ ] Consistent citation style throughout (AoM recommended by newer guideline; confirm with supervisor)
- [ ] All technical terms defined at first use
- [ ] DSR iteration acknowledged where applicable

### Appendices
- [ ] Appendices each on separate page, one topic per appendix

---

## 7. Report Evaluation Workflow

Use this section to run a formal PASS/FAIL compliance audit on a completed TIM report. This is the same checklist used in Section 6, applied as a structured evaluation process.

### How to Run an Evaluation

1. **Read every chapter** of the report (markdown drafts or the .docx file).
2. **Evaluate each item** in the checklist below against the actual report content.
3. **Assign PASS or FAIL** to each item. A FAIL requires a specific reason.
4. **Produce a summary table** with the format below.

### Evaluation Output Format

| # | Check | Result | Evidence / Reason |
|---|-------|--------|-------------------|
| 1 | Abstract ≤ 150 words, 5 elements | PASS | 142 words; all 5 elements present |
| 2 | Deliverables identical Ch1/Ch3/Ch4 | FAIL | Ch3 table says "Design Framework"; Ch1 says "Evidence-Based Design Framework" |
| ... | ... | ... | ... |

### Items Most Likely to Fail

Based on evaluation experience with a completed TIM report, these items are the most common failure points:

| Item | Why It Fails | What to Check |
|------|-------------|---------------|
| Ch1.7 "one paragraph" | Authors write one paragraph *per chapter* or use a bulleted list | Count paragraphs in Section 1.7; must be exactly 1 |
| Ch5 cross-references | Authors use step numbers instead of section/table/figure numbers | Search Ch5 for "Step 1", "Step 2" etc. — these should be replaced with "Section 4.x", "Table 4.x" |
| Ch6 Summary section | Authors end after Future Research without a closing summary | Check that Ch6 has a final Summary subsection |
| Deliverable name consistency | Minor wording differences across Ch1, Ch3 method table, and Ch4 headings | Compare exact strings |
| Ch3/Ch4 activity/outcome bleed | Activities leak into Ch4 or outcomes leak into Ch3 | Look for process verbs in Ch4 ("we conducted", "we searched") or result statements in Ch3 |

### Automation

For markdown-based reports, the `scripts/evaluate_report.py` script can auto-check approximately 15 of the 25 checklist items. Run it against your chapter files:

```bash
python scripts/evaluate_report.py path/to/TIM_Report_Draft/
```

The remaining items require human or AI judgment (e.g., "Ch5 organized around 2-3 strongest takeaways").

---

## 8. Final Submission Checklist

Use this checklist as the last step before submitting your report. These are formatting and mechanical checks — content should already be finalized.

### Document Formatting
- [ ] 12pt standard font throughout (no fanciful typestyles)
- [ ] Double-spaced text (footnotes and long quotations may be single-spaced)
- [ ] One-sided printing
- [ ] Margins: 1.5" left, 1" top/right/bottom
- [ ] **Landscape pages:** When a page is rotated to landscape, the 1.5" binding margin moves to the TOP of the landscape page (not the left). This is from the Carleton formatting guidelines.

### Pagination
- [ ] Title page = implied "i", number NOT printed
- [ ] Preliminary pages: Roman numerals (ii, iii, iv…)
- [ ] Body pages: Arabic numerals starting at 1
- [ ] Page numbers consecutive through text, illustrations, bibliography, and appendices to the last page

### Auto-Generated Lists
- [ ] Table of Contents generated from heading styles (not manually typed)
- [ ] List of Tables generated from Insert Caption
- [ ] List of Figures generated from Insert Caption
- [ ] List of Appendices present (if appendices exist)
- [ ] All cross-references use field codes (not manually typed numbers)
- [ ] **Final update performed:** Ctrl+A → F9 (or equivalent), then right-click ToC → Update Entire Table

### Title Page
- [ ] Title reflects subject clearly; no abbreviations, formulas, or Greek letters
- [ ] Student name matches Carleton registration (first name last name order)
- [ ] Correct required statement (project vs. thesis version)
- [ ] Program name matches official graduate calendar name
- [ ] Copyright line: © [Year] [Student Name]

### References
- [ ] Every in-text citation has a corresponding reference list entry
- [ ] Every reference list entry is cited at least once in the text
- [ ] **"Each reference is complete and correct"** (from guideline) — verify author names, year, title, journal/publisher, volume, pages, DOI
- [ ] Consistent citation style throughout (AoM recommended; confirm with supervisor)
- [ ] Reference list in alphabetical order by first author's last name

### Final Quality
- [ ] No orphan headings (heading at bottom of page with text on next page)
- [ ] All tables and figures have captions and are referenced in the text
- [ ] Appendices each start on a new page
- [ ] Abstract ≤ 150 words with no undefined abbreviations

---

## 9. Document Management Workflow

This section describes how to maintain markdown drafts alongside the .docx submission file. This workflow is optional — if you write directly in Word, skip to the "Handling Supervisor Feedback" subsection, which applies regardless of your writing tool.

### Recommended Setup

| Component | Purpose |
|-----------|---------|
| `TIM_Report_Draft/*.md` | Content source — where you write and revise |
| `TIM_Project_Report_[Name]_[Date].docx` | Submission artifact — formatted for printing and grading |

The markdown files are your single source of truth for content. The .docx file is the delivery format.

### When to Edit Markdown vs. .docx

| Scenario | Edit Where | Then |
|----------|-----------|------|
| Writing new content | Markdown | Sync to .docx |
| Restructuring sections | Markdown | Sync to .docx |
| Fixing formatting (margins, fonts, spacing) | .docx only | No sync needed |
| Applying supervisor feedback on content | Markdown first, then sync | Keep markdown as source of truth |
| Applying supervisor feedback on formatting | .docx only | No sync needed |
| Final pre-submission polish | .docx only | No sync needed |

### Sync Approaches

**1. Programmatic full replacement** (most reliable for major updates):
Use a script that reads the markdown files and writes complete chapter content into the .docx, preserving styles and formatting. Best when the entire chapter has changed.

**2. Targeted edits** (for small changes):
Use the AI agent's document editing skill to find and replace specific passages in the .docx. Best for sentence-level revisions after the document structure is stable.

**3. Manual copy-paste** (simplest):
Copy the relevant text from the markdown file and paste it into the .docx, then reapply formatting. Best for one-off fixes when tooling is unavailable.

### Handling Supervisor Feedback

Supervisor feedback typically arrives as comments or tracked changes in the .docx file.

**Recommended workflow:**
1. **Read the feedback** in Word or export to a readable format
2. **Triage each comment:** accept, reject, or discuss
3. **Apply accepted changes** to your markdown source files first
4. **Sync** the updated markdown back to the .docx
5. **Resolve the comments** in the .docx to keep the document clean

**Note for non-technical users:** If you write directly in Word, apply feedback directly in the .docx using Track Changes. The supervisor feedback handling tips above (triage, accept/reject, resolve comments) still apply.
