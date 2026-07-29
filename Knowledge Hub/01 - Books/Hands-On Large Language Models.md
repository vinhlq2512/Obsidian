---
type: book
author: Jay Alammar, Maarten Grootendorst
status: not-started
total_pages: 598
started:
target_date:
priority: high
source_file: "[[Hands-On Large Language Models.pdf]]"
tags:
  - book
  - llm
  - language-ai
  - generative-ai
---

# Hands-On Large Language Models

## Thông tin

- Tác giả: Jay Alammar, Maarten Grootendorst
- Nhà xuất bản: O'Reilly
- Năm: 2024
- Chủ đề chính: [[Large Language Model]], [[Tokenization]], [[Embedding]], [[Transformer]], [[Prompt Engineering]], [[Semantic Search]], [[Retrieval-Augmented Generation]], [[Multimodal LLM]], [[Fine-tuning]], [[Loss Function]], [[RLHF]], [[DPO]].

## Nguồn

- PDF gốc: [[Hands-On Large Language Models.pdf]]
- Vị trí: `00 - Sources/PDFs/Books`

## Mục tiêu đọc

- Xây nền tảng trực giác về cách language models biểu diễn, hiểu và sinh ngôn ngữ.
- Phân biệt rõ representation models và generative models.
- Biết dùng pretrained models cho classification, clustering, topic modeling, search, RAG và generation.
- Nắm các kỹ thuật training/fine-tuning quan trọng: contrastive learning, SBERT, SetFit, continued pretraining, SFT, PEFT, QLoRA, RLHF và DPO.
- Tách các định nghĩa cốt lõi thành concept notes để dùng lại khi học paper hoặc làm project.

## Cấu trúc sách

### Part I - Hiểu language models

- [[Hands-On LLM - Chapter 01 - An Introduction to Large Language Models]]
- [[Hands-On LLM - Chapter 02 - Tokens and Embeddings]]
- [[Hands-On LLM - Chapter 03 - Looking Inside Large Language Models]]

### Part II - Dùng pretrained language models

- [[Hands-On LLM - Chapter 04 - Text Classification]]
- [[Hands-On LLM - Chapter 05 - Text Clustering and Topic Modeling]]
- [[Hands-On LLM - Chapter 06 - Prompt Engineering]]
- [[Hands-On LLM - Chapter 07 - Advanced Text Generation Techniques and Tools]]
- [[Hands-On LLM - Chapter 08 - Semantic Search and Retrieval-Augmented Generation]]
- [[Hands-On LLM - Chapter 09 - Multimodal Large Language Models]]

### Part III - Training và fine-tuning

- [[Hands-On LLM - Chapter 10 - Creating Text Embedding Models]]
- [[Hands-On LLM - Chapter 11 - Fine-Tuning Representation Models for Classification]]
- [[Hands-On LLM - Chapter 12 - Fine-Tuning Generation Models]]

## Khái niệm phải nắm

- [[Language AI]]
- [[Large Language Model]]
- [[Representation Model]]
- [[Generative Model]]
- [[Tokenization]]
- [[Embedding]]
- [[Transformer]]
- [[Self-Attention]]
- [[Prompt Engineering]]
- [[Semantic Search]]
- [[Retrieval-Augmented Generation]]
- [[Multimodal LLM]]
- [[Contrastive Learning]]
- [[Loss Function]]
- [[Parameter-Efficient Fine-Tuning]]
- [[RLHF]]
- [[DPO]]

## Cách học đề xuất

- Với mỗi chapter: đọc mục tiêu, ghi lại định nghĩa, tự viết lại mental model, rồi tạo concept note nếu khái niệm có thể dùng lại.
- Với chapter có code: không cần chạy toàn bộ ngay; ưu tiên hiểu pipeline, input/output, trade-off và khi nào áp dụng.
- Với phần fine-tuning: ghi rõ dữ liệu, objective, loss, metric và chi phí tính toán.

## Câu hỏi lớn của sách

- Khi nào nên dùng representation model thay vì generative model?
- Khi nào embedding/search/RAG tốt hơn fine-tuning?
- Fine-tuning cần giải quyết vấn đề gì mà prompt engineering không đủ?
- Làm thế nào để đánh giá hệ thống LLM thay vì chỉ đánh giá một model đơn lẻ?

## Tiến độ tự động

```dataview
TABLE WITHOUT ID
  max(rows.current_page_after) AS "Trang hiện tại",
  this.total_pages AS "Tổng trang",
  round((max(rows.current_page_after) / this.total_pages) * 100) + "%" AS "Tiến độ"
FROM "03 - Daily Reading"
WHERE type = "daily-reading"
  AND status = "completed"
  AND book = this.file.link
  AND current_page_after
GROUP BY book
```
