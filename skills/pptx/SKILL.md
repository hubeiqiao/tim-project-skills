---
name: pptx
description: "Use when creating, editing, reviewing, or extracting content from PowerPoint presentation files (.pptx) - provides public workflows for python-pptx editing, speaker-note inspection, theme analysis, and OOXML-level troubleshooting."
---

# PPTX

## What This Skill Helps With

Use this skill when you need to create, edit, review, or inspect a PowerPoint deck and want a dependable workflow for slides, notes, themes, and structure.

## Ask for this skill with prompts like

Use the exact skill name `$pptx` in your prompt.

- `Use $pptx to summarize this presentation and the speaker notes.`
- `Use $pptx to create a slide deck from this outline.`
- `Use $pptx to inspect the theme colors and fonts in this example deck.`
- `Use $pptx to review whether this presentation structure is clear and professional.`

## Tools and Assumptions

This skill works best when the agent can use some of these tools:

- `python-pptx` for standard slide creation and edits
- ZIP or XML inspection tools for notes, relationships, and deeper OOXML debugging
- optional export tooling when previews or PDFs are needed

If a requested feature is not supported well by `python-pptx`, inspect the PPTX as OOXML instead of forcing a fragile high-level edit.

## Recommended Workflow

### 1. Read and summarize an existing deck

- Extract slide titles, body text, and any visible structure first.
- If the task mentions speaker notes, inspect the notes content explicitly.
- Summarize slide by slide before proposing edits.

### 2. Create a new deck

- Use `python-pptx` for standard business, academic, or technical decks.
- Start from a clear outline: title, purpose, audience, and one message per slide.
- Keep layouts simple before adding design polish.

### 3. Edit an existing deck

- Use `python-pptx` for text, shapes, tables, and images when the layout is straightforward.
- Be cautious with masters, complex animations, and unusual theme behavior.
- Preserve the original file until the revised deck is verified.

### 4. Inspect theme and OOXML structure

A `.pptx` file is a ZIP archive. Inspect OOXML directly when:

- fonts or colors are inconsistent,
- speaker notes are missing from high-level extraction,
- slide relationships are broken,
- layout inheritance behaves unexpectedly,
- comments or embedded assets need inspection.

Key areas:

- `ppt/presentation.xml`
- `ppt/slides/slideN.xml`
- `ppt/notesSlides/notesSlideN.xml`
- `ppt/theme/theme1.xml`
- `ppt/slideLayouts/`
- `ppt/slideMasters/`

## Important Limits

- `python-pptx` does not cover every PowerPoint feature.
- Speaker notes, comments, and advanced theme behavior may require XML inspection.
- Exported previews do not guarantee the deck will render identically in every PowerPoint environment.

## Common Mistakes

- Editing slide text without checking the intended audience and message hierarchy.
- Rebuilding a complex master or theme when a smaller content edit would do.
- Ignoring speaker notes when the user asked for a presentation review.
- Overwriting the original before testing slide order, text overflow, and theme consistency.
