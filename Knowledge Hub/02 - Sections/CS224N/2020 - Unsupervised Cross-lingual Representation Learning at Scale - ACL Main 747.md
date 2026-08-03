---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2020 - Unsupervised Cross-lingual Representation Learning at Scale"
year: 2020
venue: "ACL"
arxiv: ""
source_file: "[[2020 - Unsupervised Cross-lingual Representation Learning at Scale - ACL Main 747.pdf]]"
pages: 12
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - paper
---

# 2020 - Unsupervised Cross-lingual Representation Learning at Scale - ACL Main 747

## Nguồn

- PDF gốc: [[2020 - Unsupervised Cross-lingual Representation Learning at Scale - ACL Main 747.pdf]]
- Vai trò trong CS224N: paper nền về cross-lingual/multilingual representation learning ở scale lớn.

## Câu hỏi trung tâm

Làm thế nào học representation đa ngôn ngữ mạnh mà không cần supervision song ngữ lớn cho mọi ngôn ngữ?

## Kiến thức cốt lõi

- Unsupervised cross-lingual learning tận dụng dữ liệu đơn ngữ lớn ở nhiều ngôn ngữ.
- Shared subword vocabulary và pretraining objective giúp representation giữa ngôn ngữ có vùng chung.
- Scale dữ liệu/model cải thiện transfer nhưng cũng tạo vấn đề imbalance.
- Cross-lingual transfer cho phép fine-tune ở ngôn ngữ nhiều nhãn và áp dụng sang ngôn ngữ ít nhãn.
- Đây là nền cho multilingual Transformer trong NLP hiện đại.

## Cơ chế / công thức / kiến trúc

```text
monolingual corpora nhiều ngôn ngữ
-> shared tokenizer / shared Transformer
-> pretraining objective
-> contextual representations đa ngôn ngữ
-> transfer sang downstream tasks
```

## Khi áp dụng

- Dùng khi làm zero-shot cross-lingual transfer.
- Cần kiểm tra tokenizer fairness và data imbalance.
- Không giả định multilingual model tốt đều cho mọi ngôn ngữ.

## Kết quả / bằng chứng đáng giữ

- Tên paper nhấn mạnh unsupervised cross-lingual representation learning at scale.
- Lecture 14 dùng multilinguality như chủ đề chính.
- Cụm nguồn này nối với tokenization cost và fairness giữa ngôn ngữ.

## Cách hiểu bằng lời của tôi

Multilingual representation là nỗ lực tạo một không gian chung cho nhiều ngôn ngữ, nhưng không có nghĩa mọi ngôn ngữ được đối xử công bằng nếu dữ liệu/tokenization lệch.

## Câu hỏi review

1. Cross-lingual transfer là gì?
2. Shared tokenizer giúp và hại gì?
3. Vì sao data imbalance quan trọng trong multilingual models?

## Liên kết

- [[Multilingual Transformer]]
- [[Cross-Lingual Transfer]]
- [[Zero-shot Learning]]
- [[Tokenization]]
- [[CS224N]]
