
# Obsidian Vault Instructions

This repository is an Obsidian knowledge vault named Knowledge Hub. It is used for book learning, daily reading, developer knowledge, academic research, paper management, reusable concepts, experiments, and projects.

## Core Rules

- All notes must use Markdown.
- Preserve existing note content.
- Do not delete or rename files unless explicitly requested.
- Use Obsidian wiki links: [[Note Name]].
- Do not create duplicate notes.
- Use YAML frontmatter for metadata.
- Use Vietnamese for headings and explanations.
- Keep property names in English and lowercase snake_case.
- Before modifying more than five files, provide a plan.
- Never modify the `.obsidian` directory unless explicitly requested.

## Folder Responsibilities

- Store quick capture notes in `00 - Inbox`.
- Store raw source files in `00 - Sources`.
- Store book overview notes in `01 - Books`.
- Store book chapter/section notes in `02 - Sections/<Book Name>`.
- Store reading logs in `03 - Daily Reading/<Book Name>` when there are multiple daily notes for a book.
- Store reusable concepts in `04 - Concepts`.
- Store reusable templates in `05 - Templates`.
- Store attachments in `06 - Attachments`.
- Store reusable learning questions in `07 - Questions`.
- Store multi-source synthesis notes in `08 - Syntheses`.
- Store maps of content in `09 - MOCs`.
- Store developer knowledge in `10 - Technical`.
- Store academic research notes in `20 - Research`.
- Store coding and research project notes in `30 - Projects`.

## Sources Rules

- `00 - Sources` is for raw files only: PDFs, images, datasets, web clips, and external documents.
- Store ebook PDFs in `00 - Sources/PDFs/Books`.
- Store academic paper PDFs in `00 - Sources/PDFs/Papers`.
- Store technical docs, manuals, and whitepapers in `00 - Sources/PDFs/Docs`.
- Store images, screenshots, and diagrams in `00 - Sources/Images`.
- Store small datasets in `00 - Sources/Datasets`.
- Do not write long analysis notes inside `00 - Sources`; create processed notes in the proper knowledge folder instead.
- Link raw files from processed notes using wikilinks, for example `source_file: "[[Hands-On Large Language Models.pdf]]"`.

## Book Notes

- A book overview note belongs in `01 - Books`.
- Use `type: book`.
- Link the source PDF with `source_file`.
- Book chapters or sections belong in `02 - Sections/<Book Name>`.
- Daily reading notes for a book belong in `03 - Daily Reading/<Book Name>`.
- Keep book notes as maps of the book: goals, source, section links, key concepts, progress, and major questions.
- Do not put detailed chapter notes directly in the book overview if a section note exists.

Recommended book properties:

```yaml
type: book
author:
status:
total_pages:
started:
target_date:
priority:
source_file:
tags:
  - book
```

## Reading Section Notes

- Use `type: reading-section`.
- Store under `02 - Sections/<Book Name>`.
- Each section note should link back to its book using `book: "[[Book Name]]"`.
- Good section note headings include:
  - `Mục tiêu cần hiểu`
  - `Định nghĩa quan trọng`
  - `Mental model`
  - `Phần cần biết`
  - `Khi áp dụng`
  - `Câu hỏi review`
  - `Gợi ý trả lời câu hỏi review`
  - `Liên kết`

## Daily Reading Notes

- Use `type: daily-reading`.
- Use file names in `dd-MM-yyyy.md` format because `/` cannot be used in filenames.
- Keep the internal `date` property in ISO format, for example `date: 2026-07-23`, so Dataview can sort correctly.
- Store book-specific daily reading notes in `03 - Daily Reading/<Book Name>`.
- Use `current_page_after` in daily reading notes to power automatic book progress.
- Do not rely on a manual `current_page` property in book notes.

Recommended daily reading properties:

```yaml
type: daily-reading
date:
status:
target_minutes:
actual_minutes:
book:
section:
pages_planned:
pages_read:
current_page_after:
completed:
focus_score:
energy_level:
need_review:
review_date:
next_section:
tags:
  - daily-reading
```

## Concept Notes

- Store reusable concepts in `04 - Concepts`.
- Use `type: concept`.
- Create a concept note when an idea is reused across multiple books, papers, projects, or technical notes.
- Avoid duplicate concept notes; search existing concepts before creating a new one.
- Concept notes should define the idea, explain it in Vietnamese, list what must be known, and link to sources.
- Concept notes are source-independent canonical knowledge. A concept may be enriched by books, papers, courses, documentation, articles, projects, or experiments.
- When new source material discusses an existing concept, reconcile it into the canonical concept note instead of creating a duplicate note.
- Preserve source attribution with `sources` and `source_sections` when possible.
- Do not silently overwrite the user's own explanation; distinguish source claims from synthesized understanding.

Recommended concept properties:

```yaml
type: concept
status:
sources:
source_sections:
first_seen:
last_updated:
tags:
  - concept
```

Recommended concept maturity values:

```text
seed
developing
understood
verified
mastered
```

Only mark a concept `verified` when it is supported by at least two independent sources. Only mark it `mastered` when it can be applied, implemented, or taught confidently.

## Learning Questions

- Store reusable personal learning questions in `07 - Questions`.
- Use `type: question`.
- Use research questions under `20 - Research/Research Questions` only for academic or experiment-driven research.
- Link each question to relevant concepts and sources.
- Mark questions resolved when a later source provides a satisfactory answer.

Recommended question properties:

```yaml
type: question
status:
concepts:
sources:
created_at:
updated_at:
tags:
  - question
```

## Synthesis Notes And MOCs

- Store multi-source synthesis notes in `08 - Syntheses`.
- Store maps of content in `09 - MOCs`.
- Use synthesis notes for larger mechanisms or comparisons that require several concepts.
- Use MOCs as navigational maps for a domain, not as long explanations.
- Book overview notes should remain source maps; do not turn them into MOCs.

Recommended synthesis properties:

```yaml
type: synthesis
status:
concepts:
sources:
questions:
created_at:
updated_at:
tags:
  - synthesis
```

Recommended MOC properties:

```yaml
type: moc
status:
area:
concepts:
syntheses:
questions:
created_at:
updated_at:
tags:
  - moc
```

## Technical Knowledge

- Store developer knowledge in `10 - Technical`.
- Use `10 - Technical/Programming` for language/runtime/framework knowledge.
- Use `10 - Technical/System Design` for architecture, scalability, reliability, databases, and distributed systems.
- Use `10 - Technical/AI Engineering` for LLM systems, RAG, evaluation, inference, deployment, and ML engineering.
- Use `10 - Technical/Tools` for CLI, IDE, debugging, and workflow tools.
- Use `10 - Technical/Snippets` for reusable code snippets.
- Use `type: technical-note`.

## Research And Papers

- Store paper notes in `20 - Research/Papers`.
- Store paper reading logs in `20 - Research/Paper Reading`.
- Store literature synthesis notes in `20 - Research/Literature Notes`.
- Store research questions in `20 - Research/Research Questions`.
- Store experiments in `20 - Research/Experiments`.
- Store paper PDFs in `00 - Sources/PDFs/Papers` and link them with the `pdf` property.

Recommended paper properties:

```yaml
type: paper
status:
title:
authors:
year:
venue:
url:
pdf:
doi:
arxiv:
topic:
priority:
reading_status:
rating:
related_concepts:
tags:
  - paper
```

## Projects

- Store coding project notes in `30 - Projects/Coding Projects`.
- Store research project notes in `30 - Projects/Research Projects`.
- Use `type: project`.
- Link projects to related papers, concepts, experiments, and technical notes.

## Linking Rules

- Use wikilinks for internal vault references.
- Use Markdown links only for external URLs.
- Link source files from book/paper notes.
- Link section notes back to book notes.
- Link concept notes back to source sections, books, papers, or technical notes.
- Link experiments to research questions and projects.
- Prefer one canonical note per concept.

## Graph Hygiene

- Daily reading notes and source files are useful for tracking but can make Graph view noisy.
- Recommended Graph filter for knowledge graph work:

```text
-path:"03 - Daily Reading" -path:"00 - Sources"
```

- Recommended Graph filter for core knowledge:

```text
path:"01 - Books" OR path:"02 - Sections" OR path:"04 - Concepts" OR path:"07 - Questions" OR path:"08 - Syntheses" OR path:"09 - MOCs" OR path:"20 - Research" OR path:"30 - Projects"
```

## Dashboards

- Reading dashboard: `03 - Daily Reading/Reading Dashboard.md`.
- Research dashboard: `20 - Research/Research Dashboard.md`.
- Technical dashboard: `10 - Technical/Technical Dashboard.md`.
- Keep dashboard queries based on stable properties such as `type`, `status`, `book`, `date`, `reading_status`, and `priority`.

## Template Rules

- Store all templates in `05 - Templates`.
- Update templates when adding a recurring note type.
- Keep template property names in English and lowercase snake_case.
- Keep template headings and explanations in Vietnamese.

## PDF Processing Rules

- When given a PDF, first place or reference the raw file in `00 - Sources`.
- Create a processed book note or paper note instead of writing notes directly beside the PDF.
- For books, create chapter/section notes under `02 - Sections/<Book Name>` when doing detailed study.
- For papers, create paper notes under `20 - Research/Papers`.
- Summarize and explain; do not copy long passages from copyrighted sources.
