# TIM Project Skills

Installable AI agent skills for Technology Innovation Management (TIM) project work, Gate 1 slide deck reviews, and targeted document troubleshooting.

![TIM Project Skills](og-image.png)

This repository is designed for people who want to install a skill once and then ask their AI coding agent to use it directly.

## What These Skills Help With

- Structure, evaluate, and submit a TIM project report — 9-section guide, 25-item compliance checklist, and 3 Python scripts.
- Review or build a TIM Gate 1 slide deck.
- Fix a specific `python-docx` style bug when low-level XML editing goes wrong.

## Before You Start

You need:

1. A terminal on your computer.
2. [Node.js](https://nodejs.org/) installed so `npx` works.
3. An AI coding agent that supports skill installation, such as Codex, Claude Code, Cursor, Cline, or another agent supported by the `skills` installer.

If you are not technical, that is enough. You do not need to understand Git or clone this repository manually.

## Install This Repo

Copy and run:

```bash
npx skills add https://github.com/hubeiqiao/tim-project-skills
```

The installer will guide you through the rest. It typically:

- reads the GitHub repo,
- finds the available skills,
- asks which agent(s) you want to install them into,
- asks whether to install globally or locally,
- shows an installation summary before proceeding.

## Install One Skill From This Repo

If you only want one skill, copy and run:

```bash
npx skills add https://github.com/hubeiqiao/tim-project-skills --skill tim-project-guide
```

You can replace `tim-project-guide` with any skill name from the catalog below.

## Install the Original Document Skills Separately

The original `docx`, `pdf`, and `pptx` skills come from Anthropic's public skills repository, not this repo.

Run this command:

```bash
npx skills add https://github.com/anthropics/skills
```

Then choose `docx`, `pdf`, and `pptx` during the installer flow.

If you want to preview what is available first, run:

```bash
npx skills add https://github.com/anthropics/skills --list
```

## Use a Skill After Installing It

After installation, ask your AI agent to use the skill by name.

Examples:

- `Use $tim-project-guide to help me structure my TIM report.`
- `Use $g1-slide-deck-guide to review my Gate 1 presentation outline.`
- `Use $python-docx-style-id-mismatch to fix why my Heading 2 paragraphs keep turning into Normal text.`

## Skill Catalog

| Skill | What it helps with | Example prompt |
| --- | --- | --- |
| `tim-project-guide` | TIM project report structure, formatting, chapter expectations, evaluation checklist, and reusable scripts | `Use $tim-project-guide to evaluate my completed TIM report.` |
| `g1-slide-deck-guide` | TIM Gate 1 slide deck structure, required content, and review guidance | `Use $g1-slide-deck-guide to check whether my slides match the G1 format.` |
| `python-docx-style-id-mismatch` | Fix the `python-docx` style-name vs style-ID bug | `Use $python-docx-style-id-mismatch to fix my custom heading insertion script.` |

### Scripts (`tim-project-guide`)

The `tim-project-guide` skill includes three Python scripts in `skills/tim-project-guide/scripts/`:

| Script | What it does | Requirements |
| --- | --- | --- |
| `evaluate_report.py` | Auto-checks ~15 checklist items on markdown chapter files. PASS/FAIL output with evidence. | Python 3.8+ (stdlib only) |
| `generate_shell.py` | Creates markdown skeleton files with all required section headings. Configurable approach, step count, and deliverable count. | Python 3.8+ (stdlib only) |
| `verify_docx.py` | Converts .docx to markdown via pandoc, runs evaluation checks, and compares against markdown drafts for sync issues. | Python 3.8+ and pandoc |

**Example usage:**

```bash
# Evaluate markdown drafts
python scripts/evaluate_report.py path/to/TIM_Report_Draft/

# Generate a report shell with 6 method steps and 4 deliverables
python scripts/generate_shell.py --steps 6 --deliverables 4 output/

# Verify a .docx against markdown drafts
python scripts/verify_docx.py report.docx --drafts path/to/TIM_Report_Draft/
```

## Troubleshooting

### `npx: command not found`

Install [Node.js](https://nodejs.org/) and open a new terminal window, then run the install command again.

### The skill does not appear in my agent

- Restart the agent app or terminal session.
- Re-run the install command.
- Make sure you selected the correct agent during installation.

### I installed the wrong skill or wrong agent target

Run the installer again and choose the correct skill or agent target.

### I need Word, PDF, or PowerPoint skills too

Those three are installed separately from Anthropic's public skills repo:

```bash
npx skills add https://github.com/anthropics/skills
```

Then select `docx`, `pdf`, and `pptx`.

### I want to see the available skills before installing

Run:

```bash
npx skills add https://github.com/hubeiqiao/tim-project-skills --list
```

## Provenance

The TIM-specific skills in this repository are adapted from TIM project guideline materials for the TIM report and Gate 1 slide deck.

## License Notes

Unless a file or subdirectory says otherwise, original repository-authored material is available under the root [MIT License](LICENSE).
