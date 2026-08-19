---
name: paper-reading-workflow
description: Fill Obsidian paper-reading working notes from the Gemini Notebook workflow template using source-grounded paper evidence and active-reading placeholders.
when_to_use: "Use when the user asks to create, fill, scaffold, or update a paper reading workflow note from `Paper Reading Gemini Notebook Workflow.md`, especially for Gemini Notebook/NotebookLM-assisted reading in the Knowledge Hub vault. NOT for final paper-note synthesis only, concept-only updates, or claiming the user has completed reading without explicit evidence."
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
effort: medium
---

# Paper Reading Workflow — Gemini Notebook Working Notes

> Scaffold the reading process; do not replace the reader.

## Overview

This skill creates or updates Obsidian working notes based on `05 - Templates/Paper Reading Gemini Notebook Workflow.md`. It is designed for the user's Knowledge Hub paper-reading workflow: locate the paper/PDF/note, instantiate the template under `20 - Research/Paper Reading/`, fill source-grounded scaffolding where useful, and leave personal recall sections for the user unless they provided their own answers.

The output is a **reading-session note**, not the canonical paper note. It should help the user read with Gemini Notebook/NotebookLM while preserving the difference between paper facts, agent scaffolding, Gemini feedback, and the user's own understanding.

## When to Use

Good for:
- "Điền template Gemini Notebook cho paper X."
- "Tạo Paper Reading Gemini workflow cho paper này."
- "Làm mẫu workflow đọc paper theo template."
- "Update reading workflow note từ paper note/PDF/Gemini feedback."
- A paper-reading task that needs prompts, phase checklists, claim-evidence tables, equation queues, and handoff items.

Not for:
- Final canonical paper notes in `20 - Research/Papers/` without a working-note request.
- Concept-only enrichment in `04 - Concepts/`.
- Reading logs that only record "started/completed" progress.
- Marking `reading_status: completed` or writing first-person personal understanding without explicit user evidence.
- Long literature synthesis across multiple papers unless the user asks for a separate literature note.

## Vault Assumptions

- Vault root: `/Users/vinhlq2512/Obisidian/Knowledge Hub`.
- Template path: `05 - Templates/Paper Reading Gemini Notebook Workflow.md`.
- Output folder: `20 - Research/Paper Reading/`.
- Paper notes: `20 - Research/Papers/`.
- Paper PDFs: usually `00 - Sources/PDFs/Papers/`.
- Use Obsidian wikilinks for internal notes and PDF links.
- In Markdown tables, escape wikilink alias pipes: `[[Paper.pdf#page=4\|PDF tr. 4]]`.

## Protocol

### Step 1: Identify Inputs

Determine:
- target paper title, alias, acronym, or filename;
- whether the user wants a new note or an existing note updated;
- whether the user provided personal recall/Gemini output, or wants an agent-filled scaffold;
- desired phase depth: quick (`Phase 1-4`), standard (`Phase 1-9`), or deep (`Phase 1-13`).

If unspecified, default to `standard` for a paper the user is actively reading. Do not ask for paths if the title/acronym is enough to locate the paper locally.

### Step 2: Inventory Existing Vault Material

Use fast search first:

```bash
rg --files '00 - Sources' '20 - Research' '04 - Concepts' '05 - Templates' | rg -i '<paper title|acronym|key terms>'
```

Find:
- the source PDF;
- the canonical paper note;
- any existing `20 - Research/Paper Reading/` note for the same paper;
- related concept notes already linked by the paper note;
- the Gemini workflow template.

Avoid duplicate notes. If an appropriate workflow note already exists, update it rather than creating a new one, unless the user clearly wants a new dated session.

### Step 3: Read Sources Before Filling

Read the template and the existing paper note. Extract PDF text or inspect relevant PDF pages when filling factual paper sections.

Minimum evidence for a useful scaffold:
- problem/motivation/gap pages;
- method/architecture pages;
- key equations/losses;
- datasets/protocol/results;
- ablation and limitations.

If PDF extraction is unavailable, fill only from existing paper notes and label the result as `from existing note, PDF not rechecked`.

### Step 4: Choose Output Filename

For a new note, use:

```text
20 - Research/Paper Reading/YYYY-MM-DD - <Short Paper Name> - Gemini Notebook Workflow.md
```

Examples:
- `2026-08-19 - ConPL - Gemini Notebook Workflow.md`
- `2026-08-19 - Attention Is All You Need - Gemini Notebook Workflow.md`

Prefer a short stable acronym if the paper is known by one; otherwise use a short title.

### Step 5: Instantiate Template Metadata

Replace template placeholders with concrete frontmatter:

```yaml
type: paper-reading
date: YYYY-MM-DD
status: draft
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[Paper Note Name]]"
pdf: "[[Paper File.pdf]]"
paper_note: "[[Paper Note Name]]"
notebook_url:
target_minutes:
actual_minutes:
reading_goal:
current_phase: map
completed: false
need_review: true
review_date:
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
tags:
  - paper-reading
  - gemini-notebook
```

Add domain tags when clear, e.g. `relation-extraction`, `continual-learning`, but avoid noisy tags.

### Step 6: Fill the Note Safely

Preserve active-reading boundaries:
- Fill factual scaffold sections with source-grounded, paraphrased Vietnamese.
- Leave sections titled like `Closed-book recall của tôi`, `Mình tự trả lời`, or `My thoughts` blank unless the user provided text.
- If adding an agent-filled example, label it clearly as `mẫu đã điền từ nguồn` or `scaffold từ paper note/PDF`.
- Never write first-person personal understanding on behalf of the user.
- Do not mark `completed: true` or paper `reading_status: completed` without explicit user confirmation.

Recommended sections to fill:
- `Setup`
- `Phase 1 — Paper Map`
- `Phase 3 — Problem / Motivation / Gap`
- `Phase 4 — Method / Architecture`
- `Phase 6 — Equations` queue
- `Phase 8 — Experiments` protocol fields
- `Phase 9 — Claim → Evidence`
- `Phase 10 — Ablation Study`
- `Phase 11 — Critical Reading` prompts/checklist
- `Final Paper Note Handoff`

Keep prompts from the template intact unless the user asks for a shorter custom prompt bank.

### Step 7: Evidence Rules

Use page-grounded links for important claims:

```markdown
[[Paper File.pdf#page=4|PDF tr. 4]]
```

Inside Markdown tables:

```markdown
[[Paper File.pdf#page=4\|PDF tr. 4]]
```

Distinguish:
- `reported`: paper reports or claims it;
- `observed`: directly visible in table/figure/equation;
- `inferred`: agent interpretation;
- `reproduced`: only if actually run locally;
- `unverified`: plausible but not checked.

Do not present Gemini output as source evidence. Gemini can help find citations; the evidence should still point back to the paper/PDF.

### Step 8: Optional Update to Existing Reading Log

Only update an existing simpler reading log if it improves navigation and does not imply progress. Safe additions:
- link to the new workflow note;
- note that a workflow scaffold was created;
- keep `status`, `completed`, and personal progress unchanged unless the user explicitly says otherwise.

### Step 9: Validate

Run checks proportional to the edit:

```bash
ruby -ryaml -rdate -e 'ARGV.each { |f| s=File.read(f); y=s[/\A---\n(.*?)\n---/m,1]; YAML.safe_load(y, permitted_classes:[Date], aliases:true); puts "ok #{f}" }' '<changed note>'
```

When in the Knowledge Hub vault and the audit script exists:

```bash
.agents/skills/obsidian-paper-notes/scripts/audit_notes.py '<changed note>' --vault-root .
```

Also reread the beginning and any filled tables with `sed`/`nl`.

## Best Practices

- Keep the workflow note operational: prompts and blanks should be easy to use during reading.
- Prefer a partially filled high-signal scaffold over a fake-complete note.
- Use Vietnamese headings/explanations and English lowercase snake_case properties.
- Link to the paper note, PDF, related concepts, and related paper-reading notes.
- Avoid duplicate concept creation; link existing concepts where possible.
- Keep final paper-note handoff as a checklist, not as automatic migration.

## Completion Report

When finished, tell the user:
- the created/updated workflow note path;
- which phases were filled;
- what was deliberately left blank for user recall;
- validation performed;
- any evidence gaps or PDF extraction uncertainty.
