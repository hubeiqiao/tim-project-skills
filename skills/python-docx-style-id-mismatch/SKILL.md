---
name: python-docx-style-id-mismatch
description: "Use when python-docx paragraphs created via OxmlElement ignore the intended style or fall back to Normal - explains the style-name vs style-ID mismatch, shows the fix, and notes the related section-break removal pitfall."
---

# python-docx Style ID Mismatch (OxmlElement)

## What This Skill Helps With

Use this skill when your low-level `python-docx` XML edits look correct in code but Word still renders the paragraph as `Normal` instead of the heading or list style you expected.

## Ask for this skill with prompts like

- `Use $python-docx-style-id-mismatch to fix why my Heading 2 paragraphs render as Normal.`
- `Use $python-docx-style-id-mismatch to explain the difference between style names and style IDs in python-docx.`
- `Use $python-docx-style-id-mismatch to review this OxmlElement paragraph insertion code.`

## Problem

When creating Word document paragraphs using python-docx's low-level
`OxmlElement` API, setting `w:pStyle` with the style's **display name**
(e.g., "Heading 2") causes the paragraph to silently fall back to "Normal"
style. No error is raised. The XML requires the **style ID** (e.g.,
"Heading2") which differs from the display name.

## Context / Trigger Conditions

- Creating paragraphs via `OxmlElement('w:p')` instead of `doc.add_paragraph()`
- Setting style with `pStyle.set(qn('w:val'), 'Heading 2')` (WITH space)
- Paragraphs render as Normal/body text instead of the intended style
- `paragraph.style.name` shows "Normal" even though you set a heading style
- No error or warning is raised -- complete silent failure
- Affects all styles with spaces in their display names

## Root Cause

python-docx has two name systems:
- **Display name** (`style.name`): Human-readable, e.g., "Heading 2", "List Bullet", "Body Text"
- **XML style ID** (`style.style_id`): Used in the XML, e.g., "Heading2", "ListBullet", "BodyText"

When you use `doc.add_paragraph(style='Heading 2')`, python-docx handles
the mapping internally. But when using `OxmlElement` directly to set
`w:pStyle`, you must provide the **XML style ID**.

## Solution

Create a mapping dictionary and helper function:

```python
STYLE_ID_MAP = {
    'Normal': 'Normal',
    'Heading 1': 'Heading1',
    'Heading 2': 'Heading2',
    'Heading 3': 'Heading3',
    'Heading 4': 'Heading4',
    'List Bullet': 'ListBullet',
    'List Number': 'ListNumber',
    'Caption': 'Caption',
    'table of figures': 'TableofFigures',
    'Body Text': 'BodyText',
    'First Paragraph': 'FirstParagraph',
    'Compact': 'Compact',
}

def get_style_id(style_name):
    """Convert a style display name to its XML style ID."""
    return STYLE_ID_MAP.get(style_name, style_name.replace(' ', ''))
```

Then use it when setting styles via OxmlElement:

```python
# WRONG - silent failure, falls back to Normal
pStyle.set(qn('w:val'), 'Heading 2')

# CORRECT - uses XML style ID
pStyle.set(qn('w:val'), get_style_id('Heading 2'))  # -> 'Heading2'
```

The fallback `style_name.replace(' ', '')` handles most cases since Word
typically just removes spaces, but some styles have non-obvious IDs (e.g.,
"table of figures" -> "TableofFigures" with different casing).

## Verification

After applying the fix, verify styles are correctly assigned:

```python
for i, p in enumerate(doc.paragraphs):
    if p.style.name.startswith('Heading'):
        print(f"[{i}] style.name='{p.style.name}' text='{p.text[:60]}'")
```

If headings appear as "Normal" in this output, the style ID is wrong.

To inspect what XML style ID a document actually uses:

```python
for style in doc.styles:
    if style.name.startswith('Heading'):
        print(f"Display: '{style.name}' -> ID: '{style.style_id}'")
```

## Related Issue: Section Breaks Lost During Paragraph Removal

When removing paragraphs between chapter boundaries using lxml's
`body.remove(element)`, any `w:sectPr` elements embedded in paragraph
properties (`w:pPr`) are removed along with the paragraphs. This silently
destroys section breaks (used for Roman/Arabic page numbering).

**Fix:** After content replacement operations, verify section count and
re-add section breaks if needed:

```python
# Check sections
print(f"Sections: {len(doc.sections)}")

# Re-add section break before a target paragraph
prev_para = doc.paragraphs[target_idx - 1]
prev_pPr = prev_para._element.get_or_add_pPr()
sectPr = OxmlElement('w:sectPr')
# ... configure sectPr properties ...
prev_pPr.append(sectPr)
```

## Example

Full pattern for creating a heading paragraph via OxmlElement:

```python
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def create_heading(doc, ref_element, text, level=2):
    p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    pStyle = OxmlElement('w:pStyle')
    # Key line: use get_style_id, not raw display name
    pStyle.set(qn('w:val'), get_style_id(f'Heading {level}'))
    pPr.append(pStyle)
    p.append(pPr)

    r = OxmlElement('w:r')
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    r.append(t)
    p.append(r)

    ref_element.addprevious(p)
    return p
```

## Notes

- This only affects the low-level OxmlElement API. Using
  `doc.add_paragraph(style='Heading 2')` works correctly because
  python-docx resolves the name internally.
- The OxmlElement approach is necessary when inserting paragraphs at
  specific positions (before a reference element) rather than appending
  to the end.
- Custom styles defined in a document may have arbitrary IDs. Always
  check `style.style_id` for the actual XML ID if unsure.
- The `style_name.replace(' ', '')` heuristic works for ~95% of built-in
  Word styles but won't catch casing differences.
