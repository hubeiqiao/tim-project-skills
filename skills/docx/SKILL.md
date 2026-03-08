---
name: docx
description: "Use when creating, editing, reviewing, or extracting content from Microsoft Word documents (.docx) - provides public workflows for text extraction, python-docx editing, template-based generation, and targeted OOXML inspection."
---

# DOCX

## What This Skill Helps With

Use this skill when you need to create, edit, review, or inspect a `.docx` file and want a dependable workflow instead of guessing which library or format detail matters.

## Ask for this skill with prompts like

Use the exact skill name `$docx` in your prompt.

- `Use $docx to extract the text from this Word document.`
- `Use $docx to update this report and keep the headings and tables intact.`
- `Use $docx to create a new project brief from this outline.`
- `Use $docx to inspect the raw XML in this file because formatting keeps breaking.`

## Tools and Assumptions

This skill works best when the agent can use some of these tools:

- `python-docx` for most create and edit tasks
- `pandoc` for fast text extraction when available
- `zipfile`, `unzip`, or another archive tool for raw OOXML inspection
- `docxtpl` for template-driven generation when a `.docx` template is provided

If a tool is missing, install it first or fall back to a simpler workflow.

## Recommended Workflow

### 1. Read or extract content

- Prefer `pandoc` when you mainly need text and headings.
- Fall back to ZIP or XML inspection when you need comments, relationships, numbering, styles, or embedded assets.

Example:

```bash
pandoc input.docx -t markdown -o output.md
```

### 2. Create a new document

- Prefer `python-docx` for letters, reports, meeting notes, and basic tables.
- Prefer `docxtpl` when the user gives you a Word template with placeholders.
- Keep the first version simple before adding advanced styling or images.

### 3. Edit an existing document

- Use `python-docx` for text edits, headings, tables, lists, and basic formatting.
- Be conservative with complex layout changes.
- If the document has unusual numbering, section breaks, or field codes, inspect the XML before making broad edits.

### 4. Inspect OOXML directly

A `.docx` file is a ZIP archive. Inspect OOXML directly when:

- styles are broken,
- numbering resets unexpectedly,
- section breaks disappear,
- images or relationships are missing,
- comments or metadata need inspection.

Key files:

- `word/document.xml`
- `word/styles.xml`
- `word/numbering.xml`
- `word/comments.xml`
- `word/_rels/document.xml.rels`

## Important Limits

- Standard Python libraries do not reliably produce native Word tracked changes the way Microsoft Word does.
- If the user specifically needs true tracked changes or comment threads, say so clearly before editing.
- For simple final-text edits, `python-docx` is usually enough.
- For review-markup fidelity, a manual Word review step may still be necessary.

## Common Mistakes

- Treating `.docx` like plain text and losing structure.
- Making global XML edits before understanding the style or numbering model.
- Assuming tracked changes will be preserved automatically.
- Forgetting that low-level paragraph insertion may need XML style IDs instead of human-readable style names.

If paragraph styles silently fall back to `Normal`, use `$python-docx-style-id-mismatch`.
