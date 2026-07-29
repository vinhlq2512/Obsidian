---
name: obsidian-book-reading
description: Maintain book learning notes in this Obsidian vault. Use when the user asks to create or update daily reading notes, answer daily reading sections, add chapter/section summaries, mark a reading day completed, update book progress, or create reusable concept notes from books such as NLP/LLM/AI texts.
---

# Obsidian Book Reading

## Overview

Use this skill to keep the Knowledge Hub book-learning system consistent while preserving existing notes. Prefer focused edits to the daily note, the related section note, and any reusable concept note.

## Core Workflow

1. Locate the relevant files with `rg` or `rg --files`.
2. Read the daily note, section note, book overview, and related concept notes before editing.
3. Decide whether the request needs:
   - a daily-reading update in `03 - Daily Reading/<Book Name>`;
   - a section update in `02 - Sections/<Book Name>`;
   - a concept note in `04 - Concepts`;
   - a book overview progress update in `01 - Books`.
4. Search existing concept notes before creating a new one.
5. Use `apply_patch` for manual edits.
6. Verify the changed snippets with `sed` or `rg`.

Before modifying more than five files, provide a short plan.

## Folder Rules

- Put daily book logs in `03 - Daily Reading/<Book Name>` using `dd-MM-yyyy.md`.
- Put chapter or section notes in `02 - Sections/<Book Name>`.
- Put reusable concepts in `04 - Concepts`.
- Put book overview notes in `01 - Books`.
- Do not modify `.obsidian` unless the user explicitly asks.
- Do not duplicate notes; update existing canonical notes when available.

## Metadata Rules

Use YAML frontmatter. Keep property names in English and lowercase snake_case. Use quoted wikilinks in YAML when Obsidian should treat a value as a link.

Daily reading notes should prefer:

```yaml
type: daily-reading
date: 2026-07-26
status: completed
target_minutes:
actual_minutes:
book: "[[Book Name]]"
section: "[[Section Note]]"
pages_planned: "78-98"
pages_read: "78-98"
current_page_after: 98
completed: true
need_review: true
review_date: 2026-07-28
tags:
  - daily-reading
```

Section notes should prefer:

```yaml
type: reading-section
book: "[[Book Name]]"
status:
chapter:
start_page:
end_page:
reading_date:
planned_sessions:
  - "2026-07-26 | 78-98 | Focus | 55 phút"
tags:
  - nlp
```

Concept notes should prefer:

```yaml
type: concept
status: seed
source:
  - "[[Source Section]]"
tags:
  - concept
```

## Writing Style

- Write headings and explanations in Vietnamese.
- Use Obsidian wikilinks for internal notes, for example `[[Self-Attention]]`.
- Summarize and explain; do not copy long book passages.
- Use compact formulas and short examples when they make the concept easier to recall.
- Keep book overview notes as maps; put detailed explanations in section or concept notes.

## Daily Completion

When the user says a day is finished:

- Set `status: completed`.
- Set `completed: true`.
- Fill `pages_read` from the user's range or the planned range.
- Add `current_page_after` when the end page is known.
- Keep `need_review` and `review_date` if review is still useful.
- Add concise "Viết lại bằng lời của tôi" notes and update checklist items.

## Concept Extraction

Create or update a concept note when an idea is reusable across books, papers, projects, or technical notes. A good concept note includes:

- `Định nghĩa`
- `Cách hiểu bằng lời của tôi`
- `Công thức trực giác` when relevant
- `Ví dụ trực quan`
- `Cần biết`
- `Liên kết`

Prefer one canonical note per concept, for example `Self-Attention`, `Multi-Head Attention`, `Feed-Forward Layer`, `Layer Normalization`.
