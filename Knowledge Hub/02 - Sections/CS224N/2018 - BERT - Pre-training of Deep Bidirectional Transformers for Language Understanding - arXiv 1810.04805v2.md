---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2018 - BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2018
venue: "arXiv"
arxiv: "1810.04805v2"
source_file: "[[2018 - BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding - arXiv 1810.04805v2.pdf]]"
pages: 16
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Bidirectional Attention]]"
tags:
  - cs224n
  - paper
---
# 2018 - BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding - arXiv 1810.04805v2

## Nguồn

- PDF gốc: [[2018 - BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding - arXiv 1810.04805v2.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 07 - Pretraining]], [[SLP 2026 - Chapter 10 - Masked Language Models]]
- Concept: [[Bidirectional Attention]], [[Transformer]], [[Transfer Learning]]

## Vấn đề paper giải quyết

Các language representation model trước BERT thường không pretrain sâu hai chiều trong mọi layer. BERT đặt mục tiêu học deep bidirectional representations từ unlabeled text và fine-tune đơn giản cho nhiều task.

## Đóng góp chính

- Giới thiệu Bidirectional Encoder Representations from Transformers.
- Pretrain bằng masked language modeling để dùng cả left và right context.
- Fine-tune với rất ít thay đổi kiến trúc cho QA, entailment và nhiều NLU tasks.
- Đặt chuẩn cho encoder-only pretrained models.

## Cơ chế cần nhớ

```text
input text
-> mask một số token
-> encoder Transformer nhìn hai chiều
-> dự đoán token bị mask
-> fine-tune cho downstream task bằng head nhỏ
```

## Vì sao quan trọng với CS224N

BERT minh hoạ nhánh encoder của pretraining revolution: khi mục tiêu là hiểu input, bidirectional context cực mạnh.

## Hạn chế / câu hỏi

- Không phải mô hình sinh autoregressive tự nhiên như GPT.
- MLM tạo mismatch giữa pretraining và fine-tuning vì token `[MASK]` không xuất hiện ở downstream text thật.
- Cần so sánh với decoder-only và encoder-decoder để chọn kiến trúc đúng task.

## Câu hỏi review

1. Vì sao BERT được gọi là bidirectional?
2. MLM cho phép nhìn hai chiều như thế nào?
3. Vì sao BERT hợp với NLU hơn generation mở?
