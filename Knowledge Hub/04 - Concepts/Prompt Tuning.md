---
type: concept
status: developing
sources:
  - "[[Adaptive Prompting for Continual Relation Extraction]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[Adaptive Prompting for Continual Relation Extraction#2. Task-specific prompt pool]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction#2. Task-specific prompt pool]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Module 1 — Prototype-based classification]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#1. Hybrid prompt representation]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - prompting
  - peft
  - few-shot
---

# Prompt Tuning

## Định nghĩa

Prompt tuning là họ kỹ thuật thích nghi pretrained model bằng cách học hoặc thiết kế prompt tokens/representations để đưa task vào đúng “giao diện” mà model đã học trong pretraining, thay vì nhất thiết fine-tune toàn bộ model.

Trong nghĩa hẹp, prompt tuning thường chỉ learned continuous prompt embeddings ở input. Trong literature rộng hơn, “prompt-based learning” còn bao gồm hard prompts, hybrid prompts và [[Prefix Tuning]]. Vì tên gọi dễ lẫn, note/paper nên ghi rõ prompt được chèn ở đâu và parameters nào được train.

## Phân biệt với Prompt Engineering

| | [[Prompt Engineering]] | Prompt tuning |
|---|---|---|
| Prompt | Text/instruction do người viết | Learned vectors hoặc template có trainable tokens |
| Optimization | Không nhất thiết có gradient | Train bằng gradient trên task data |
| Model | Thường generative API/LLM | Thường pretrained model có truy cập parameters |
| Reproducibility | Phụ thuộc prompt/model version | Phụ thuộc checkpoint, init và training config |

## Ba dạng trong bốn paper

### Discrete cloze prompt — ConPL

```text
[CLS] head_entity [MASK] tail_entity [SEP] sentence [SEP]
```

Hidden state tại `[MASK]` làm relation representation. Prompt không dùng verbalizer để dự đoán token label; prototype classifier quyết định relation.

### Hybrid hard + soft prompt — CPL

```text
sentence [v] head [v] [MASK] [v] tail [v]
```

- Entity order/`[MASK]` là hard structure.
- `[v]` là continuous trainable vectors.
- `[MASK]` state làm embedding cho contrastive/prototype classification.

Hybrid prompt cho inductive bias rõ hơn soft-only prompt, đặc biệt khi data ít. Trong ablation CPL, bỏ prompt representation làm $T_8$ accuracy giảm 13,41 điểm trên FewRel và 14,78 điểm trên TACRED. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7|CPL PDF, tr. 7]]

### Prefix prompts — WAVE/WAVE++

Continuous key/value prefixes được chèn vào attention layers. Nhiều prefixes được tổ chức thành [[Prompt Pool]] và route theo input. Xem [[Prefix Tuning]].

## Tại sao prompt giúp few-shot learning?

- Đưa task gần objective/pretraining interface như masked-token representation.
- Chèn entity structure làm inductive bias, giảm số pattern model phải tự khám phá.
- Train ít parameters hơn nên có thể giảm overfit.
- Khai thác pretrained semantics thay vì học classifier hoàn toàn từ đầu.

Nhưng random-initialized soft prompts vẫn có thể khó hội tụ khi chỉ có vài examples; hard/hybrid structure giúp ổn định hơn.

## Verbalizer hay metric classifier?

### Verbalizer

Map class sang token/phrase rồi dùng probability ở `[MASK]`.

- Tận dụng LM head.
- Khó chọn label words tốt; relation names có thể không khớp vocabulary.

### Metric/prototype classifier

Dùng `[MASK]` hidden state như embedding, so với class prototypes.

- Dễ thêm class mới mà không mở rộng fixed softmax head.
- Phụ thuộc embedding geometry và prototype quality.

ConPL/CPL dùng hướng thứ hai.

## Prompt design dimensions

- Hard, soft hay hybrid.
- Prompt đặt trước/sau câu hay quanh entity.
- Có dùng entity markers và direction không.
- Có verbalizer hay metric classifier.
- Số prompt tokens và initialization.
- Chèn chỉ input hay nhiều layers.
- Backbone freeze toàn bộ hay fine-tune cùng prompt.
- Một prompt/task hay input-dependent pool.

## Failure modes

- Soft prompt khó học dưới cực ít data.
- Template leak label hoặc phụ thuộc relation description.
- Entity order/head-tail direction bị đảo.
- Prompt tokens chiếm context length.
- Learned prompt overfit task order/domain.
- Chọn sai prompt khi inference.
- Gọi mọi learned prompt là “prompt engineering” làm mất khác biệt kỹ thuật.

## Câu hỏi review

1. Prompt tuning khác prompt engineering ở đâu?
2. Hard, soft và hybrid prompt khác nhau thế nào?
3. Vì sao `[MASK]` state có thể dùng mà không cần verbalizer?
4. Tại sao hybrid prompt hữu ích trong few-shot RE?
5. Prefix tuning là một dạng prompt tuning ở điểm nào và khác input prompt ở đâu?

## Gợi ý trả lời

1. Prompt tuning học vector bằng gradient; prompt engineering thiết kế text/instruction.
2. Hard là tokens cố định, soft là vectors học được, hybrid kết hợp cả hai.
3. Nó làm relation embedding để metric/prototype classifier dự đoán class.
4. Hard structure mã hóa entity roles, soft tokens vẫn thích nghi task, giảm gánh nặng học từ ít data.
5. Cùng học prompt parameters, nhưng prefix chèn key/value vào nhiều attention layers thay vì chỉ input embeddings.

## Liên kết

- [[Prompt Engineering]]
- [[Prefix Tuning]]
- [[Prompt Pool]]
- [[Parameter-Efficient Fine-Tuning]]
- [[Masked Language Modeling]]
- [[Few-shot Learning]]
- [[Prototype Learning]]
- [[Continual Learning]]
