# Metadata Schema

Use lowercase `snake_case` YAML properties. Quote wikilinks in YAML.

## Paper Fields

```yaml
type: paper
status: draft
title:
authors:
year:
venue:
url:
pdf: "[[Paper File.pdf]]"
zotero_key:
citekey:
doi:
arxiv:
code_url:
dataset_url:
source_version:
topic:
priority: medium
reading_status: not-started
rating:
related_concepts:
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
tags:
  - paper
```

## Status Semantics

- `status` is note maturity: `draft`, `reviewed`, `stable`, `archived`.
- `reading_status` is the user's reading progress: `not-started`, `in-progress`, `completed`.
- Default new generated paper notes to `status: draft` and `reading_status: not-started`.
- Change `reading_status` only from explicit user evidence.
- Preserve compatibility with existing dashboards before migrating old values such as `status: unread`.

## Normalization

- Normalize DOI without `https://doi.org/` or `doi:`.
- Preserve arXiv version in `source_version` when version differences matter.
- Do not change `created_at` during updates.
- Change `updated_at` only when note content changes.
- Leave unknown optional fields blank or omit them when the vault does not require a fixed schema.
