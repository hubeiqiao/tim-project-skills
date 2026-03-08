---
name: pdf
description: "Use when extracting text or tables from PDFs, filling forms, splitting or merging files, or inspecting PDF structure - provides public workflows for pypdf, pdfplumber, OCR-aware extraction, and form handling."
---

# PDF

## What This Skill Helps With

Use this skill when you need to extract text, capture tables, fill forms, split or merge files, or diagnose why a PDF is difficult to parse.

## Ask for this skill with prompts like

Use the exact skill name `$pdf` in your prompt.

- `Use $pdf to extract every table from this PDF into CSV.`
- `Use $pdf to split this file into one PDF per page.`
- `Use $pdf to merge these three PDFs into a single packet.`
- `Use $pdf to fill this form and save a completed copy.`

## Tools and Assumptions

This skill works best when the agent can use some of these tools:

- `pypdf` for splitting, merging, rotating, and basic metadata work
- `pdfplumber` for text and table extraction
- OCR tooling for scanned PDFs when there is no machine-readable text

If extraction returns almost nothing, assume the PDF may be image-based and switch to OCR.

## Recommended Workflow

### 1. Check whether the PDF is text-based or scanned

- Try normal text extraction first.
- If the result is empty or unreadable, the document is probably scanned.
- For scanned PDFs, use OCR or a vision-capable workflow instead of repeating text extraction blindly.

### 2. Extract text or tables

- Use `pdfplumber` when layout and tables matter.
- Use `pypdf` for simpler metadata or page-level operations.
- Export tables into CSV, JSON, or markdown so the result is usable.

Example:

```python
import pdfplumber

with pdfplumber.open("input.pdf") as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    tables = first_page.extract_tables()
```

### 3. Split, merge, or rotate pages

- Use `pypdf` for page operations.
- Preserve the original file until the new output is verified.

### 4. Fill forms

- First detect whether the PDF has actual form fields.
- If it does, fill them programmatically.
- If it does not, explain that the file is visually form-like but not machine-fillable.

## Important Limits

- Table extraction quality depends on how the PDF was authored.
- Scanned PDFs often need OCR before they become searchable.
- Some PDFs look like forms but do not contain real form fields.
- Complex or encrypted PDFs may require a more manual workflow.

## Common Mistakes

- Assuming every PDF contains selectable text.
- Treating image scans like text PDFs.
- Extracting tables without checking for merged cells or header rows.
- Overwriting the original before confirming page order and orientation.
