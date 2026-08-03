---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: textbook-chapter
title: "SLP 2026 - Chapter 10 - Masked Language Models"
year: 2026
venue: ""
arxiv: ""
source_file: "[[SLP 2026 - Chapter 10 - Masked Language Models.pdf]]"
pages: 20
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Bidirectional Attention]]"
tags:
  - cs224n
  - textbook
---

# SLP 2026 - Chapter 10 - Masked Language Models

## Nguồn

- PDF gốc: [[SLP 2026 - Chapter 10 - Masked Language Models.pdf]]
- Vai trò trong CS224N: chapter nền về BERT và masked language modeling cho bidirectional encoders.

## Câu hỏi trung tâm

Masked language modeling khác causal language modeling như thế nào và vì sao nó hợp với encoder representations?

## Kiến thức cốt lõi

- Masked LM che một token ở giữa và yêu cầu model đoán bằng cả left/right context.
- Bidirectional encoders tập trung tạo contextualized representations cho input tokens.
- Causal models dễ sinh token tiếp theo; masked encoders mạnh cho understanding/sequence labeling.
- BERT là ví dụ tiêu biểu của pretrained bidirectional Transformer encoder.
- Fine-tuning thêm output head nhỏ cho downstream tasks như NER, QA, classification.

## Cơ chế / công thức / kiến trúc

```text
input sequence
-> mask một số tokens
-> Transformer encoder nhìn hai chiều
-> dự đoán masked tokens
-> hidden states dùng cho downstream tasks
```

## Khi áp dụng

- Dùng khi chọn encoder-only model cho NLU.
- Không dùng BERT thuần như decoder text generation left-to-right.
- Hữu ích cho sequence labeling vì mỗi token representation nhìn toàn câu.

## Kết quả / bằng chứng đáng giữ

- Chapter first page định nghĩa masked language modeling và BERT.
- Trang 2 nói bidirectional encoders tạo contextualized representations cùng độ dài input.
- Source phân biệt causal/generative models với bidirectional encoders.

## Cách hiểu bằng lời của tôi

Masked LM học bằng cách điền chỗ trống trong câu. Vì được nhìn cả hai phía, nó hiểu context rất mạnh nhưng không sinh văn bản tự nhiên như decoder-only LM.

## Câu hỏi review

1. MLM khác next-token prediction ở đâu?
2. Bidirectional encoder phù hợp task nào?
3. Vì sao BERT không phải generative LM theo nghĩa GPT?

## Liên kết

- [[Masked Language Modeling]]
- [[Bidirectional Attention]]
- [[Transformer]]
- [[Named Entity Recognition]]
- [[CS224N]]
