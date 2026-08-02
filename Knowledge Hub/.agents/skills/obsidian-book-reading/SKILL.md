---
name: obsidian-book-reading
description: Maintain book learning notes in this Obsidian vault. Use when the user asks to create or update daily reading notes, answer daily reading sections, add chapter/section summaries, mark a reading day completed, update book progress, or create reusable concept notes from books such as NLP/LLM/AI texts.
---

# Obsidian Book Reading

## Overview

Use this skill to keep the Knowledge Hub book-learning system consistent while preserving existing notes. Prefer focused edits to the daily note, the related section note, and any reusable concept note.

The vault is a source-independent knowledge graph. Books, papers, courses, documentation, articles, and experiments may all contribute to the same canonical concepts, synthesis notes, and maps of content.

## Core Workflow

1. Locate the relevant files with `rg` or `rg --files`.
2. Read the daily note, section note, book overview, and related concept notes before editing.
3. Decide whether the request needs:
   - a daily-reading update in `03 - Daily Reading/<Book Name>`;
   - a section update in `02 - Sections/<Book Name>`;
   - a concept note in `04 - Concepts`;
   - a reusable learning question in `07 - Questions`;
   - a synthesis note in `08 - Syntheses`;
   - a map of content in `09 - MOCs`;
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
- Put reusable learning questions in `07 - Questions`.
- Put multi-source synthesis notes in `08 - Syntheses`.
- Put maps of content in `09 - MOCs`.
- Put extracted learning figures, diagrams, charts, and crops in `06 - Attachments`.
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
sources:
  - "[[Source Section]]"
  - "[[Source Section 1]]"
  - "[[Source Section 2]]"
  - .....
source_sections:
  - "[[Source Section]]"
first_seen: 2026-07-26
last_updated: 2026-07-26
tags:
  - concept
```

Concept maturity values:

- `seed`: newly encountered.
- `developing`: partially understood, with known gaps.
- `understood`: can be explained clearly in the user's own words.
- `verified`: confirmed across at least two independent sources.
- `mastered`: can be applied, implemented, or taught confidently.

Do not upgrade maturity without evidence in the note. Only upgrade to `understood` when the note contains a coherent "Cách hiểu bằng lời của tôi" section. Only upgrade to `verified` when at least two independent sources support it.

## Writing Style

- Write headings and explanations in Vietnamese.
- Use Obsidian wikilinks for internal notes, for example `[[Self-Attention]]`. Actively try to link to existing concepts in the vault.
- Summarize and explain; do not copy long book passages.
- Focus strictly on the source material. Do not hallucinate or add external information not present in the source.
- Use compact formulas and short examples when they make the concept easier to recall.
- Keep book overview notes as maps; put detailed explanations in section or concept notes.
- Treat source notes as evidence, not the final home of reusable knowledge.
- Distinguish source claims from synthesized understanding.
- Do not turn uncertain interpretations into facts.

## Priority Extraction

Do not summarize all source material equally.

The goal is to extract high-value knowledge rather than produce exhaustive chapter summaries. Optimize for what helps the learner understand, remember, link, and apply knowledge later.

When reading source material, prioritize information in this order:

1. Learner signals: highlights, annotations, notes, questions, marked passages, or passages the learner asks about.
2. Equations, formulas, mathematical relationships, and tensor shapes.
3. High-value figures, diagrams, charts, tables, visual explanations, and tensor-flow visuals.
4. Explicit definitions and key claims.
5. Mechanisms and processes: how something works.
6. Why and intuition: why a design, technique, formula, or architecture exists.
7. Algorithms and architectures: input, output, processing steps, parameters, and invariants.
8. Examples that clarify an abstract concept or reveal behavior.
9. Evidence and results, especially for papers.
10. Assumptions, limitations, failure modes, and trade-offs.
11. Learner confusion or unanswered questions.

Compress or omit background prose, transitions, repeated explanations, historical context, and narrative text unless they materially improve understanding.

### P0 — Learner Signals

Treat explicit learner signals as the strongest evidence of importance:

- highlights;
- annotations;
- handwritten or typed notes;
- questions from the learner;
- text marked as important;
- passages the learner asks about.

Never omit a learner-highlighted passage simply because it appears redundant with surrounding text.

For each meaningful highlight, determine whether it represents:

- a definition;
- a key claim;
- a mechanism;
- a formula;
- an intuition;
- an example;
- a limitation;
- a question;
- a reusable concept.

Do not copy highlights verbatim into permanent notes unless exact wording is important. Convert them into concise knowledge while preserving their meaning.

### P1 — Definitions

Prioritize explicit definitions of important concepts. Capture:

- what the concept is;
- what problem it solves;
- how it differs from related concepts;
- important terminology and aliases.

Prefer linking to or updating a canonical concept note.

### P1 — Equations and Mathematical Relationships

Equations are high-priority knowledge.

When an important equation appears:

1. Preserve the equation accurately.
2. Define every important variable.
3. Explain what the equation means intuitively.
4. Explain relationships between variables.
5. Record important assumptions or conditions.
6. Add a small example when it improves understanding.
7. Link the equation to the concept it belongs to.

Do not store equations without explanations.

### P1 — Mechanisms

Capture mechanisms that explain how a system works.

Look especially for language such as:

- "works by";
- "consists of";
- "first ... then ...";
- "because";
- "allows";
- "causes";
- "is computed by";
- "the purpose of".

Represent mechanisms as compact sequences when useful:

```text
Input
-> Projection into Q/K/V
-> Attention scores
-> Scaling
-> Softmax
-> Weighted values
-> Output
```

### P1 — Why and Intuition

Prioritize explanations of why a technique, equation, architecture, or design decision exists.

A good permanent note should answer both:

- How does it work?
- Why is it designed this way?

If the source only states how something works but the reason is not given, do not invent the reason. Record it as an unanswered question if important.

### P2 — Algorithms and Architectures

For algorithms and architectures, extract:

- input;
- output;
- important intermediate representations;
- processing steps;
- important parameters;
- invariants;
- computational relationships;
- interaction with other components.

Prefer data-flow explanations over prose-heavy summaries.

### P2 — Assumptions, Limitations, and Trade-offs

Actively capture:

- assumptions;
- edge cases;
- limitations;
- failure modes;
- computational cost;
- memory cost;
- accuracy/speed trade-offs;
- situations where the technique should or should not be used.

These are often more valuable than general descriptive text.

### P2 — Evidence and Results

For research papers, prioritize evidence supporting the main idea. Capture:

- important experiment;
- metric;
- baseline;
- result;
- ablation;
- finding.

Do not copy large result tables unless individual values are important. Keep exact numbers only when they support an important conclusion.

### P3 — Examples

Keep examples only when they:

- clarify an abstract concept;
- reveal an edge case;
- show how an algorithm behaves;
- help construct a useful mental model.

Do not preserve examples merely because they appear in the source.

## Highlight Processing

Highlights are not the final notes. A highlight is a signal that a piece of source material deserves processing.

For every meaningful highlight:

```text
Highlight
-> Identify why it matters
-> Determine related concept
-> Rewrite in the learner's knowledge structure
-> Merge with existing knowledge
-> Preserve source reference
```

Do not create permanent notes like:

```text
Highlight:
Dot products can produce arbitrarily large numbers...
```

Instead, find the related concept note, such as `[[Scaled Dot-Product Attention]]`, and add the processed knowledge under a meaningful heading such as `Tại sao phải scale attention score?`.

## Formula Extraction

A formula deserves permanent storage when at least one of the following is true:

- it defines a concept;
- it describes an algorithm;
- it expresses an important relationship;
- it is required to implement the technique;
- it explains an important model behavior;
- the learner highlighted or questioned it.

For each important formula, extract:

### Công thức

The exact mathematical expression.

### Thành phần

Define symbols and tensor shapes when relevant.

### Trực giác

Explain the relationship without relying only on mathematics.

### Tại sao cần nó?

Explain the design motivation only when supported by the source.

### Khi nào dùng?

Describe the role or context of the equation.

### Ví dụ

Include only if it improves recall.

### Liên hệ

Link related concepts.

For machine-learning formulas, include tensor shapes when they materially improve understanding.

## Figure Extraction

When a source contains figures, diagrams, charts, tables, or visual explanations, treat them as potential high-value learning signals.

Do not extract every image. Prefer figures that:

- explain an architecture;
- illustrate a mechanism;
- show data flow;
- clarify a mathematical relationship;
- visualize tensor shapes;
- compare approaches;
- present an important experiment or result;
- provide a mental model that is difficult to reproduce with text alone.

Ignore decorative images, logos, covers, repeated screenshots, and visuals that do not materially improve understanding.

### Figure workflow

For every useful figure:

1. Identify what concept or claim the figure explains.
2. Preserve or extract the figure when technically possible.
3. Store it in `06 - Attachments`.
4. Use a stable and descriptive filename.
5. Embed it in the relevant source, concept, or synthesis note.
6. Add a short explanation below the figure.
7. Preserve provenance back to the source.
8. Summarize the important takeaway in text; do not rely on the image alone.

Prefer:

```markdown
![[transformer-multi-head-attention-architecture.png]]

**Ý chính:** Hình cho thấy input được chiếu thành nhiều Q/K/V riêng cho từng attention head, sau đó các head được concatenate trước khi qua projection cuối.

Nguồn: [[Attention Is All You Need]] — Figure 2
```

### Figure naming

Use descriptive filenames instead of generic names.

Prefer:

- `transformer-multi-head-attention.png`
- `bert-pretraining-objectives.png`
- `lora-low-rank-decomposition.png`
- `flashattention-memory-access.png`

Avoid:

- `image1.png`
- `figure2.png`
- `screenshot-2026-08-02.png`

### Prefer figure cropping over raw extraction

If raw extraction loses labels, captions, arrows, or layout context, prefer cropping the complete figure region from the rendered source page.

The learning value of the complete visual is more important than extracting the original image object.

### Figure interpretation

For important figures, record:

- what the figure represents;
- input and output;
- important components;
- direction of data flow;
- relationships between components;
- what the learner should notice;
- related concepts.

Do not let figures become dead attachments. Connect them to canonical concepts, source sections, synthesis notes, or MOCs.

### Visual deduplication

Before storing a figure:

- search existing attachments;
- check whether the same figure or an equivalent diagram already exists;
- reuse the canonical visual when appropriate;
- avoid duplicate copies from different sources unless the differences themselves are meaningful.

## Tensor and Shape Priority

For ML, NLP, and deep-learning material, preserve important tensor shapes.

Especially capture shapes when:

- tensors are multiplied;
- dimensions are projected;
- attention heads are split or concatenated;
- model input/output dimensions change;
- broadcasting occurs;
- shapes explain how an operation works.

Prefer compact shape traces:

```text
X: [batch, sequence, d_model]

Q = XW_Q
W_Q: [d_model, d_k]
Q: [batch, sequence, d_k]

Attention scores:
QK^T -> [batch, sequence, sequence]
```

## Should This Become a Note?

Before storing information permanently, ask:

1. Will I likely need to recall this later?
2. Does it explain why or how something works?
3. Is it reusable outside this exact source?
4. Does it change or deepen an existing concept?
5. Is it required to implement or apply the technique?
6. Is it a formula, definition, limitation, or important result?
7. Did the learner explicitly highlight or question it?
8. Is it a figure or visual that explains a mechanism, architecture, result, formula, or tensor flow better than text alone?

If none are true, prefer leaving the information only in the source note.

Do not create permanent notes simply because information exists in the source.

## Concept Reconciliation

When new source material discusses an existing concept:

1. Open the canonical concept note.
2. Compare the new source with existing knowledge.
3. Identify:
   - new information;
   - clearer explanations;
   - contradictions;
   - alternative terminology;
   - new examples;
   - unanswered questions.
4. Merge only genuinely new knowledge.
5. Preserve source attribution.
6. Do not duplicate explanations unless they provide a meaningfully different mental model.
7. Never silently overwrite the learner's own explanation.
8. Record disagreements between sources explicitly.
9. Keep citations back to every contributing source.

## Knowledge Integration

When processing new material:

1. Update the daily reading note.
2. Update the source section note.
3. Extract newly introduced concepts.
4. Search canonical concept notes.
5. Merge new knowledge into existing concepts when appropriate.
6. Create concept notes only when no canonical note exists.
7. Record unanswered questions.
8. Update relevant synthesis notes when several concepts together explain a larger mechanism.
9. Add important links from the relevant MOC.
10. Update source or book progress only when the user clearly indicates completion.

The desired flow is:

```text
Source -> Source Section -> Concept -> Synthesis -> MOC
```

Treat highlights, formulas, figures, definitions, results, and questions as knowledge signals that may feed this flow.

Daily notes are learning logs and should not become the permanent location of reusable knowledge.

## Questions

When the learner raises a meaningful unresolved question:

- record it in the source or daily note;
- link it to relevant concepts;
- create a dedicated question note in `07 - Questions` when it is reusable or important;
- use `20 - Research/Research Questions` only for academic or experiment-driven questions;
- mark the question resolved when a later source provides a satisfactory answer.

## Multi-Source Synthesis

When multiple sources cover the same topic:

1. Locate all related canonical concept notes.
2. Collect relevant source notes.
3. Compare definitions, terminology, assumptions, and examples.
4. Identify consensus.
5. Identify complementary explanations.
6. Identify contradictions or unresolved differences.
7. Update canonical concepts.
8. Update or create a synthesis note in `08 - Syntheses`.
9. Keep citations back to every contributing source.

## MOCs

Use MOCs in `09 - MOCs` as navigational maps for major areas such as NLP, Transformers, LLMs, ML engineering, or RAG. Do not make book overview notes do this job. MOCs should link to concepts, synthesis notes, important source notes, projects, and reusable questions.

## Atomicity

A concept note should answer one primary question. Prefer notes such as `Self-Attention`, `Scaled Dot-Product Attention`, `Query Key Value`, and `Causal Masking` over one large note such as `Everything About Attention`.

Do not make concepts so small that they will not be reused independently.

## Knowledge Safety

- Never overwrite the user's own explanation silently.
- Preserve existing personal notes unless demonstrably incorrect.
- Distinguish source claims from synthesized understanding.
- Do not turn uncertain interpretations into facts.
- Mark unclear or conflicting information explicitly.
- Do not add external knowledge unless the user asks for enrichment beyond the source.

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

Prefer one canonical note per concept, for example `Self-Attention`, `Multi-Head Attention`, `Feed-Forward Layer`, `Layer Normalization`. If an existing concept note lacks information compared to the new source material, proactively update the concept note with the missing details.
