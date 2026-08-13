---
name: obsidian-paper-notes
description: Create, update, and audit Vietnamese Obsidian research notes from academic papers and PDFs. Use when the user asks to ingest, summarize, analyze, review, compare, organize, or connect research papers in an Obsidian vault, including paper notes, page-grounded evidence maps, reusable concept notes, user-confirmed reading logs, and protocol-aware literature syntheses.
---

# Obsidian Paper Notes

## Overview

Turn research papers into Vietnamese Obsidian notes that support study and research. Create source-specific paper notes, reusable concept notes, user-confirmed reading logs, and protocol-aware literature syntheses without flattening incompatible experiments into one leaderboard.

Treat the vault as a source-independent knowledge graph:

- Paper notes store claims, methods, results, and evidence from one source.
- Concept notes explain reusable ideas independently of one paper.
- Literature notes compare multiple papers while preserving protocol differences.
- Reading logs record only progress or reflections explicitly provided by the user.

## Tool Use

- Use PDF tooling when extracting page counts, page-level text, outlines, figures, tables, equations, or visual evidence.
- Use Obsidian-specific Markdown or CLI tooling when available and useful.
- Fall back to filesystem-based Markdown, YAML, and link checks when Obsidian-specific tooling is unavailable.
- Use `rg` or `rg --files` before slower search methods.
- Prefer primary sources for metadata: publisher pages, ACL Anthology, AAAI, arXiv, DOI/Crossref, and official code repositories.
- Verify online only when venue, DOI, publication status, code availability, or another unstable fact matters or is missing from the provided source.

## Bundled Resources

- Read `references/note-templates.md` when creating or substantially restructuring paper, concept, or literature notes.
- Read `references/metadata-schema.md` when changing YAML fields, status semantics, or dashboard-sensitive metadata.
- Read `references/evidence-policy.md` when judging claims, results, protocol comparisons, personal reflections, or reproducibility language.
- Run `scripts/audit_notes.py` for deterministic filesystem QA of changed research notes when the edit touches multiple notes or PDF links.

## Operation And Depth

Determine the operation before editing:

- `ingest`: Store or update metadata, PDF links, and initial note status without deep analysis.
- `analyze`: Create or enrich a paper note from one source.
- `synthesize`: Compare multiple papers in a literature note.
- `reading-log`: Record user-confirmed reading progress, questions, or reflections.
- `audit`: Validate existing notes without substantively rewriting them.

Determine analysis depth from the request:

- `quick`: Record metadata, one-sentence summary, problem, method, main result, main limitation, and a compact evidence map.
- `standard`: Include all sections materially supported by the source, with important equations, protocol details, results, and limitations.
- `deep`: Include formalization, variables, tensor shapes, algorithm steps, figures, tables, ablations, failure modes, and reproducibility details.

Default to `standard` when the user does not specify depth. Do not generate empty sections merely to satisfy a template.

## Core Workflow

1. Identify the requested operation, depth, papers, theme, and intended vault changes.
2. Inventory the papers and existing notes with `rg --files` first.
   - Search `00 - Sources`, `00 - Sources/PDFs/Papers`, `20 - Research/Papers`, `20 - Research/Paper Reading`, `20 - Research/Literature Notes`, and `04 - Concepts` when they exist.
   - Match by normalized title, filename, DOI, arXiv id, citekey, aliases, and existing wikilinks.
   - Treat arXiv versions such as `v1` and `v2` as versions of the same paper unless evidence shows otherwise.
   - Do not create duplicate paper or concept notes.
3. Read the source before writing.
   - Extract text by page and record the physical PDF page count.
   - Inspect figures and tables visually when their layout carries meaning that text extraction may lose.
   - Use OCR cautiously for scanned PDFs and label uncertain extraction.
4. Plan before broad edits.
   - Before modifying more than five files, list the intended paper notes, concept notes, literature notes, reading logs, dashboards/templates, and PDF operations.
   - Ask the user only when a missing choice would materially change filenames, note identity, or existing personal content.
5. Make the smallest useful set of edits.
   - Create or update paper notes in `20 - Research/Papers`.
   - Create or enrich concept notes only when the concept threshold below is met.
   - Create or update a literature note only when the synthesis threshold below is met.
   - Create a reading log only when requested or when the user provides personal reading progress.
6. Ground important claims with page-level evidence and distinguish reported results from reproduced results.
7. Validate every changed note proportionally to the edit size before finishing.

If the user asks only for analysis, explanation, or review and does not request vault changes, do not modify files.

## Change Scope And Preservation

- Preserve user-authored explanations, highlights, questions, ratings, review answers, and reading progress.
- Never overwrite a user-authored passage merely to improve style. Edit it only when explicitly requested.
- Never write first-person personal reflections on behalf of the user.
- Place generated explanations under `Diễn giải học tập`, not under a section that implies the user personally wrote or understood them.
- Update `Ghi chú cá nhân` only when the user supplies the content or explicitly asks for a first-person draft.
- Do not infer that the user has read a paper from the existence of a generated analysis note.
- Do not delete or rename files unless the user explicitly asks.
- Do not modify `.obsidian`.
- Preserve `created_at`; update `updated_at` only when note content actually changes.

## Folder And File Rules

- Store processed paper notes in `20 - Research/Papers`.
- Store paper reading logs in `20 - Research/Paper Reading` only for requested reading sessions or user-confirmed progress.
- Store literature syntheses in `20 - Research/Literature Notes`.
- Store reusable concepts in `04 - Concepts`.
- Store raw academic PDFs in `00 - Sources/PDFs/Papers` only when ingesting them into the vault is in scope.
- If a PDF already exists elsewhere under `00 - Sources`, preserve working links and move or rename it only when explicitly requested or clearly required by an ingestion task.
- Prefer an existing vault naming convention. If none exists, use a stable human-readable note name such as `First Author et al. - Year - Short Title.md` and avoid changing it later.
- Resolve same-basename collisions by exact path, metadata, aliases, and source identity before writing links.

## Paper Note Metadata

Use lowercase `snake_case` YAML properties. Read `references/metadata-schema.md` before changing paper metadata or migrating older values.

Default new paper notes to `status: draft` and `reading_status: not-started`. `status` describes note maturity; `reading_status` describes the user's personal reading progress. Change `reading_status` only from explicit user evidence.

If an existing dashboard relies on older values such as `status: unread`, preserve compatibility until the dashboard or query is deliberately migrated. Normalize DOI values without the `https://doi.org/` or `doi:` prefix, preserve arXiv versions in `source_version` when relevant, and quote wikilinks in YAML.

## Paper Note Standard

Read `references/note-templates.md` before creating or substantially restructuring notes. Include only sections supported by the requested depth and available evidence; do not generate empty sections merely to satisfy a template.

- `Tóm tắt một câu`
- `Nguồn`
- `Vấn đề paper giải quyết`
- `Gap và đóng góp`
- `Bài toán/formalization`
- `Phương pháp`
- `Mental model`
- `Thuật toán hoặc luồng xử lý`
- `Công thức quan trọng`
- `Experimental setup`
- `Protocol fingerprint`
- `Kết quả chính`
- `Ablation và phân tích`
- `Hạn chế, giả định, failure modes`
- `Đánh giá từ evidence`
- `Diễn giải học tập`
- `Ghi chú cá nhân`
- `Câu hỏi review`
- `Gợi ý trả lời câu hỏi review`
- `Cần đọc tiếp`
- `Evidence map`
- `Liên kết`

Write in Vietnamese using source-grounded, paraphrased prose. Do not copy long passages. Keep `Ghi chú cá nhân` unchanged unless the user provides or requests its content.

## Epistemic Labels

Read `references/evidence-policy.md` when writing claims, results, limitations, or comparisons. Distinguish the origin of important statements:

- `reported`: claimed or reported by the paper or its authors.
- `observed`: directly visible in a table, figure, equation, appendix, or experiment description.
- `inferred`: an analytical interpretation derived from the source.
- `reproduced`: obtained from an experiment actually run in the current research workflow.
- `unverified`: plausible but not yet confirmed from a primary source or experiment.

Use language such as `Paper báo cáo...` for reported claims and `Một cách diễn giải có thể là...` for inference. Never present reported results as locally reproduced results. Omit unsupported claims or mark them `Chưa xác minh`.

## Extraction Priorities

Do not summarize every paragraph equally. Prioritize:

1. Problem, assumptions, task setup, and evaluation protocol.
2. Definitions and terminology introduced by the paper.
3. Mathematical objectives, variables, tensor shapes, and algorithm steps.
4. Figures, tables, ablations, and page-specific evidence.
5. Novelty relative to prior work.
6. Results, exceptions, variance, and cases where the evidence is weaker than the headline claim.
7. Limitations, caveats, reproducibility issues, compute/data assumptions, and privacy claims.
8. Connections to existing concepts, competing methods, and open questions.

For loaded terms such as `rehearsal-free`, `zero-memory`, `privacy`, `continual`, `few-shot`, `task-aware`, or `state-of-the-art`, record the exact operational meaning used by the paper and its caveats.

## Experimental Protocol Fingerprint

For empirical machine-learning papers, capture when available:

- dataset and exact train/validation/test split;
- evaluation scenario and label space;
- backbone, tokenizer, parameter scale, and frozen/trainable components;
- number of runs, random seeds, mean, standard deviation, or confidence interval;
- metric definition and averaging method;
- baseline implementation source and whether hyperparameters were retuned;
- external data, retrieval corpus, teacher model, or generated data;
- compute, hardware, training time, and major preprocessing assumptions;
- whether a number is reported, observed, inferred, or reproduced.

For continual-learning, continual relation extraction, or few-shot papers, also capture:

- number of tasks, sessions, relations, and classes per task;
- task order and whether results are averaged over multiple orders;
- class-incremental, task-incremental, or domain-incremental setting;
- whether task identity is available during training or inference;
- replay/exemplar memory budget and what counts toward that budget;
- number of shots, support examples, or demonstrations;
- access to old labels, old data, prototypes, prompts, retrieval indexes, or teacher outputs;
- evaluation after each task, final average accuracy/F1, forgetting, backward transfer, and any custom metric;
- backbone changes, parameter growth, prompt growth, and inference-time overhead.

Do not compare headline numbers across papers until these protocol fields are checked.

## Concept Notes

Before creating a concept note, search `04 - Concepts` by exact name, acronym, expanded name, aliases, and related terms. Update the canonical note when it exists.

Create or enrich a concept note only when at least one condition holds:

- the user explicitly requests it;
- the concept is central and reusable beyond one paper;
- the canonical concept note already exists and the source materially enriches it;
- the concept appears across multiple independent sources;
- the concept is important to the user's active research question and cannot be explained adequately with a short paper-note section.

Concept notes should remain source-independent. Use evidence from papers to enrich:

- `Định nghĩa ngắn`
- `Cách hiểu bằng lời của tôi` only when the user supplies or explicitly requests a personal draft; otherwise use `Diễn giải học tập`
- `Vì sao quan trọng`
- `Cơ chế`
- `Công thức hoặc ví dụ`
- `Khi áp dụng`
- `Trade-off và failure modes`
- `Liên quan`
- `Nguồn đã dùng`
- `Câu hỏi review`

Use concept maturity conservatively:

- `seed`: newly encountered or lightly defined.
- `developing`: partially explained and linked to evidence.
- `understood`: contains a coherent explanation plus review answers, confirmed by the user or demonstrated through application.
- `verified`: supported by at least two genuinely independent sources.
- `mastered`: the user can apply, implement, or teach it confidently.

Never mark a concept `verified` merely because several papers are variants from the same method lineage. Never infer `understood` or `mastered` solely from an AI-generated note.

## Literature Notes

Create or update a literature note only when at least one condition holds:

- the user asks for comparison, synthesis, novelty analysis, or a research thread;
- an existing literature note matches the research question;
- at least three papers form a meaningful theme where protocol differences or competing assumptions matter.

Do not create a literature note merely because several papers were ingested together.

Good sections include:

- `Câu hỏi trung tâm`
- `Bức tranh tổng quan`
- `Các paper trong scope`
- `Protocol và fairness khi so sánh`
- `Các hướng tiếp cận`
- `Representation của knowledge cũ`
- `Replay, prompting, prototype, hoặc retrieval`
- `Kết quả nên giữ`
- `Điểm đồng thuận`
- `Điểm còn tranh luận`
- `Khoảng trống nghiên cứu`
- `Roadmap đọc tiếp`
- `Câu hỏi review`

Make dataset, split, task order, memory budget, backbone, metric, seed count, and task-identity differences explicit before comparing results. Do not flatten incompatible protocols into one ranking.

## Evidence And Linking

Ground important claims with physical PDF page links. Treat `#page=N` as a 1-indexed physical PDF page, not the printed page label inside the document.

```markdown
[[Paper File.pdf#page=4|PDF, tr. 4]]
```

For Markdown tables, do not put an unescaped alias pipe inside a table cell. Use a safe escaped pipe:

```markdown
| Trang PDF | Evidence |
|---|---|
| [[Paper File.pdf#page=4\|PDF tr. 4]] | Method figure |
```

Alternatively, separate the link and page label:

```markdown
| Link | Trang | Evidence |
|---|---:|---|
| [[Paper File.pdf#page=4]] | PDF tr. 4 | Method figure |
```

Use wikilinks for vault files and Markdown links for external URLs. Quote wikilinks in YAML:

```yaml
pdf: "[[Paper File.pdf]]"
sources:
  - "[[Paper Note]]"
```

An evidence map should connect a claim or note section to its strongest source location, not list every page mechanically. Prefer tables, figures, equations, experiment definitions, and limitation statements over incidental mentions.

## Results And Comparison Rules

- Record the metric name, direction, aggregation, value, dataset, protocol, and source page together.
- Record whether higher or lower is better when the metric is non-obvious.
- Keep mean and variance together; do not report only the best run when the paper reports multiple runs.
- Distinguish the paper's own implementation of a baseline from numbers copied from prior work.
- Do not call a method state of the art unless the comparison scope and protocol support that statement.
- Record exceptions where the proposed method loses to a baseline or where gains fall within reported variance.
- Never insert locally estimated values into a table of reported results without an explicit label.

## QA Checklist

Run checks proportional to the edit size:

1. Reread changed snippets with `sed` or `nl`.
2. Run `scripts/audit_notes.py` on changed notes or relevant research folders when PDF links, metadata, or tables changed.
3. For full YAML parsing with dates, use Ruby safe YAML when available.
4. Confirm `reading_status`, personal reflections, ratings, and concept mastery were not upgraded without user evidence.
5. Confirm reported, inferred, and reproduced results remain distinguishable.
6. If Obsidian CLI is available, optionally inspect rendered output or metadata. Otherwise, state that validation was filesystem-based.

## Completion Report

When vault files were changed, report concisely:

- files created or updated;
- PDFs ingested, if any;
- concepts or literature notes created and why they met the threshold;
- validation performed;
- unresolved metadata, extraction uncertainty, protocol mismatch, or evidence gaps.

Do not claim that the user has read, understood, verified, or mastered material unless the user explicitly provided that evidence.
