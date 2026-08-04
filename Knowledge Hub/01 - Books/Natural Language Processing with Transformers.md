---
type: book
author: Lewis Tunstall, Leandro von Werra, Thomas Wolf
status: completed
total_pages: 479
started: 2026-07-23
target_date: 2026-08-09
priority: high
source_file: "[[Natural Language Processing with Transformers.pdf]]"
tags:
  - book
  - nlp
  - transformers
  - hugging-face
---

# Natural Language Processing with Transformers

## Thông tin

- Tác giả: Lewis Tunstall, Leandro von Werra, Thomas Wolf
- Trạng thái: Hoàn thành
- Tổng số trang PDF: 479
- Chủ đề chính: NLP hiện đại, Transformer, Hugging Face, fine-tuning, production, few-shot learning.

## Nguồn

- PDF gốc: [[Natural Language Processing with Transformers.pdf]]
- Vị trí: `00 - Sources/PDFs/Books`

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

## Lý do đọc

- Hiểu cách xây dựng ứng dụng NLP thực tế bằng Transformer.
- Nắm workflow Hugging Face từ dataset, tokenizer, model, trainer đến deployment.
- Tạo được demo nhỏ theo từng chapter để biến kiến thức thành kỹ năng.

## Mục tiêu đọc

- Hoàn thành 1 chapter mỗi session hoặc chia nhỏ nếu chapter dài.
- Sau mỗi chapter, viết lại ý chính bằng tiếng Việt.
- Chạy hoặc phác thảo ít nhất 1 demo thực hành.
- Tách các khái niệm quan trọng sang `04 - Concepts` khi cần dùng lại.

## Sections

- [x] [[NLP Transformers - Chapter 01 - Hello Transformers]]
- [x] [[NLP Transformers - Chapter 02 - Text Classification]]
- [x] [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
- [x] [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
- [x] [[NLP Transformers - Chapter 05 - Text Generation]]
- [x] [[NLP Transformers - Chapter 06 - Summarization]]
- [x] [[NLP Transformers - Chapter 07 - Question Answering]]
- [x] [[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]
- [x] [[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]
- [x] [[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]
- [x] [[NLP Transformers - Chapter 11 - Future Directions]]

## Lịch đọc đề xuất

| Ngày | Nội dung | Trang | Mục tiêu |
| --- | --- | --- | --- |
| 2026-07-23 | [[NLP Transformers - Chapter 01 - Hello Transformers]] | 21-38 | Tổng quan Transformer, Hugging Face và pipeline |
| 2026-07-24 | [[NLP Transformers - Chapter 02 - Text Classification]] | 39-57 | Dataset, nhãn, độ dài văn bản và tokenization |
| 2026-07-25 | [[NLP Transformers - Chapter 02 - Text Classification]] | 58-77 | Feature extraction, fine-tuning và workflow |
| 2026-07-26 | [[NLP Transformers - Chapter 03 - Transformer Anatomy]] | 78-98 | Self-attention và positional embeddings |
| 2026-07-27 | [[NLP Transformers - Chapter 03 - Transformer Anatomy]] | 99-118 | Encoder, decoder và encoder-decoder |
| 2026-07-28 | [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]] | 119-149 | NER và cross-lingual transfer |
| 2026-07-29 | [[NLP Transformers - Chapter 05 - Text Generation]] | 150-163 | Decoding strategies |
| 2026-07-30 | [[NLP Transformers - Chapter 06 - Summarization]] | 164-179 | Summarization và metrics |
| 2026-07-31 | [[NLP Transformers - Chapter 06 - Summarization]] | 180-194 | Fine-tuning summarization |
| 2026-08-01 | [[NLP Transformers - Chapter 07 - Question Answering]] | 195-214 | Extractive QA |
| 2026-08-02 | [[NLP Transformers - Chapter 07 - Question Answering]] | 215-233 | Retriever-reader pipeline |
| 2026-08-03 | [[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]] | 234-259 | Benchmark production |
| 2026-08-04 | [[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]] | 260-285 | Distillation, quantization, ONNX, pruning |
| 2026-08-05 | [[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]] | 286-305 | Baseline và ít nhãn |
| 2026-08-06 | [[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]] | 306-325 | Prompting, augmentation và unlabeled data |
| 2026-08-07 | [[NLP Transformers - Chapter 10 - Training Transformers from Scratch]] | 326-358 | Corpus và tokenizer |
| 2026-08-08 | [[NLP Transformers - Chapter 10 - Training Transformers from Scratch]] | 359-392 | Pretraining loop và chi phí |
| 2026-08-09 | [[NLP Transformers - Chapter 11 - Future Directions]] | 393-416 | Future directions và tổng kết sách |

## Ý tưởng quan trọng

- Transformer là nền tảng kiến trúc cho nhiều bài toán NLP hiện đại.
- Hugging Face giúp chuẩn hóa vòng đời NLP: dữ liệu, tokenization, model, training, evaluation, deployment.
- Fine-tuning, evaluation và tối ưu production quan trọng không kém việc chọn model.

## Concepts nên tách

- [[Transformer]]
- [[Self-Attention]]
- [[Transfer Learning]]
- [[Hugging Face]]
- [[Tokenization]]
- [[Fine-tuning]]
- [[Named Entity Recognition]]
- [[Text Generation]]
- [[Decoding Strategies for Text Generation]]
- [[Summarization]]
- [[Text Summarization Pipelines]]
- [[Training a Summarization Model]]
- [[Summarization Baseline]]
- [[Measuring the Quality of Generated Text]]
- [[Comparing Different Summaries]]
- [[Evaluating PEGASUS on the CNN-DailyMail Dataset]]
- [[ROUGE]]
- [[BLEU]]
- [[PEGASUS]]
- [[Question Answering]]
- [[Building a Review-Based QA System]]
- [[SubjQA]]
- [[SQuAD]]
- [[Extractive QA]]
- [[Extracting Answers from Text]]
- [[Tokenizing Text for QA]]
- [[Sliding Window for QA]]
- [[Span Classification]]
- [[Using Haystack to Build a QA Pipeline]]
- [[Sparse Retriever]]
- [[Dense Passage Retrieval]]
- [[BM25]]
- [[Evaluating the Retriever]]
- [[Recall@k]]
- [[Mean Average Precision]]
- [[Evaluating the Reader]]
- [[Exact Match]]
- [[F1 Score]]
- [[Model Benchmarking]]
- [[Transformer Inference Optimization]]
- [[Knowledge Distillation]]
- [[KL Divergence]]
- [[Pretraining]]
- [[Hyperparameter Optimization]]
- [[Quantization]]
- [[ONNX]]
- [[ONNX Runtime]]
- [[Graph Optimization]]
- [[Pruning]]
- [[Few-shot Learning]]
- [[Tokenizer Training]]
- [[Language Modeling]]
- [[Training Loop]]
- [[Scaling Laws]]
- [[Vision Transformer]]
- [[Multimodal Transformer]]

## Demo tổng thể

- Tạo một notebook hoặc script nhỏ chạy các pipeline cơ bản của Hugging Face.
- Sau mỗi chapter, thêm một demo riêng để kiểm chứng ý tưởng chính.

## Ghi chú sau khi hoàn thành

- Đã hoàn thành toàn bộ lộ trình đọc từ Chapter 01 đến Chapter 11. Phần giá trị nhất của cuốn sách không chỉ là biết các task NLP riêng lẻ, mà là có được một khung quyết định thực tế cho dữ liệu, model, evaluation, fine-tuning, production optimization và hướng phát triển tiếp theo.
