---
name: obsidian-review-hygiene
description: Check and fix Obsidian note metadata, review dates, reading dashboard reminders, malformed YAML properties, Dataview compatibility, and review-related workflows in the Knowledge Hub vault. Use when the user mentions broken metadata, Obsidian properties showing wrong types, review_date reminders, need_review, Dataview dashboards, or reading review queues.
---

# Obsidian Review Hygiene

## Overview

Use this skill to keep Obsidian properties readable by Obsidian and sortable by Dataview. Focus on metadata correctness, review queues, and dashboard queries.

## Core Workflow

1. Locate affected notes with `rg` or `rg --files`.
2. Read frontmatter before editing.
3. Identify whether the issue is YAML syntax, Obsidian property type display, Dataview sorting, or missing review fields.
4. Use `apply_patch` for manual edits.
5. Verify with `rg` and spot-read changed frontmatter.

Before modifying more than five files, provide a short plan.

## YAML Hygiene

- Keep property names in English and lowercase snake_case.
- Quote wikilinks in YAML, for example `book: "[[Natural Language Processing with Transformers]]"`.
- Use ISO dates for sortable date fields, for example `date: 2026-07-26`.
- Store page ranges as quoted strings, for example `pages_read: "78-98"`.
- Avoid inline JSON-like objects in properties when Obsidian UI displays them poorly.
- Prefer list strings for planned sessions:

```yaml
planned_sessions:
  - "2026-07-28 | 119-149 | NER và token-level labels | 60 phút"
```

## Review Fields

Use these fields consistently:

```yaml
need_review: true
review_date: 2026-07-28
status: completed
completed: true
```

Use `need_review: false` only when the user explicitly does not need review or the note is not part of recall workflow.

## Dashboard Queries

For due reviews, prefer a Dataview query like:

```dataview
TABLE
  type AS "Loại",
  book AS "Sách",
  section AS "Section",
  review_date AS "Ngày review",
  status AS "Trạng thái"
FROM ""
WHERE need_review = true
  AND review_date
  AND review_date <= date(today)
  AND !contains(file.path, "05 - Templates")
SORT review_date ASC, file.name ASC
```

For upcoming reviews, use a future window:

```dataview
TABLE
  type AS "Loại",
  book AS "Sách",
  section AS "Section",
  review_date AS "Ngày review",
  status AS "Trạng thái"
FROM ""
WHERE need_review = true
  AND review_date
  AND review_date > date(today)
  AND review_date <= date(today) + dur(7 days)
  AND !contains(file.path, "05 - Templates")
SORT review_date ASC, file.name ASC
```

## Common Fixes

- If Obsidian shows a wikilink as malformed array text, change `book: [[Name]]` to `book: "[[Name]]"`.
- If a property displays orange or as unknown/invalid, check for unquoted colons, inline objects, or invalid YAML list syntax.
- If Dataview does not sort a date, ensure the value is ISO `yyyy-MM-dd`.
- If a reading day is done but absent from progress, add `current_page_after`.
- If a template pollutes dashboards, exclude `05 - Templates`.

## Verification

After edits:

- Run `rg -n "^book:\\s*\\[\\["` to find unquoted wikilinks.
- Run `rg -n "review_date:|need_review:|current_page_after:"` on changed folders.
- Spot-read frontmatter with `sed -n '1,40p'`.
- Report exactly which notes were changed.
