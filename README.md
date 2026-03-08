# TIM Project Skills

Installable AI agent skills for Technology Innovation Management (TIM) project work, Gate 1 slide deck reviews, and targeted document troubleshooting.

This repository is designed for people who want to install a skill once and then ask their AI coding agent to use it directly.

## What These Skills Help With

- Structure and review a TIM project report.
- Review or build a TIM Gate 1 slide deck.
- Fix a specific `python-docx` style bug when low-level XML editing goes wrong.

## Before You Start

You need:

1. A terminal on your computer.
2. [Node.js](https://nodejs.org/) installed so `npx` works.
3. An AI coding agent that supports skill installation, such as Codex, Claude Code, Cursor, Cline, or another agent supported by the `skills` installer.

If you are not technical, that is enough. You do not need to understand Git or clone this repository manually.

## Install All Skills

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

## Install One Skill

If you only want one skill, copy and run:

```bash
npx skills add https://github.com/hubeiqiao/tim-project-skills --skill tim-project-guide
```

You can replace `tim-project-guide` with any skill name from the catalog below.

## Use a Skill After Installing It

After installation, ask your AI agent to use the skill by name.

Examples:

- `Use $tim-project-guide to help me structure my TIM report.`
- `Use $g1-slide-deck-guide to review my Gate 1 presentation outline.`
- `Use $python-docx-style-id-mismatch to fix why my Heading 2 paragraphs keep turning into Normal text.`

## Skill Catalog

| Skill | What it helps with | Example prompt |
| --- | --- | --- |
| `tim-project-guide` | TIM project report structure, formatting, and chapter expectations | `Use $tim-project-guide to review my chapter order and formatting.` |
| `g1-slide-deck-guide` | TIM Gate 1 slide deck structure, required content, and review guidance | `Use $g1-slide-deck-guide to check whether my slides match the G1 format.` |
| `python-docx-style-id-mismatch` | Fix the `python-docx` style-name vs style-ID bug | `Use $python-docx-style-id-mismatch to fix my custom heading insertion script.` |

## Troubleshooting

### `npx: command not found`

Install [Node.js](https://nodejs.org/) and open a new terminal window, then run the install command again.

### The skill does not appear in my agent

- Restart the agent app or terminal session.
- Re-run the install command.
- Make sure you selected the correct agent during installation.

### I installed the wrong skill or wrong agent target

Run the installer again and choose the correct skill or agent target.

### I want to see the available skills before installing

Run:

```bash
npx skills add https://github.com/hubeiqiao/tim-project-skills --list
```

## Provenance

The TIM-specific skills in this repository are adapted from TIM project guideline materials for the TIM report and Gate 1 slide deck.

## Important License Review Note

Some office-document skills in the local working collection include bundled `LICENSE.txt` files from upstream source materials that restrict redistribution. Those skills are not included in the current public test push until their licensing is resolved.

## License Notes

Unless a file or subdirectory says otherwise, original repository-authored material is available under the root [MIT License](LICENSE).

Some bundled skill directories also contain their own `LICENSE.txt` files. Those file-specific terms still apply to that directory.
