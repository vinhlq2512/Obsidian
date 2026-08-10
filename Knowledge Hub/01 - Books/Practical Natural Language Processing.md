---
type: book
author: Sowmya Vajjala, Bodhisattwa Majumder, Anuj Gupta, Harshit Surana
status: planned
total_pages: 798
started: 2026-08-04
target_date: 2026-08-27
priority: high
source_file: "[[Practical Natural Language Processing .pdf]]"
created_at: 2026-08-04
updated_at: 2026-08-04
tags:
  - book
  - nlp
  - practical-nlp
---

# Practical Natural Language Processing

## Thông tin

- Tác giả: Sowmya Vajjala, Bodhisattwa Majumder, Anuj Gupta, Harshit Surana.
- Trạng thái: Lên kế hoạch.
- Tổng số trang PDF: 798.
- Nội dung chính: xây dựng hệ thống NLP thực tế từ nền tảng, pipeline, representation, task cốt lõi, domain ứng dụng, đến quy trình end-to-end.

## Nguồn

- PDF gốc: [[Practical Natural Language Processing .pdf]]
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

## Cách đọc lần này

- Daily reading bắt đầu từ **Part II - Essentials**, tức [[Practical NLP - Chapter 04 - Text Classification]], vào ngày 2026-08-04.
- Part I - Foundations gồm Chapter 01-03 đã được tự note thành ghi chú nền để không chiếm daily reading.
- Khi đọc daily, ưu tiên case study, pipeline, trade-off, failure mode và gợi ý triển khai thực tế.

## Lý do đọc

- Bổ sung góc nhìn thực dụng cho NLP: không chỉ model, mà còn dữ liệu, pipeline, triển khai, monitoring và bài toán business.
- Làm cầu nối giữa kiến thức nền như [[Tokenization]], [[Embedding]], [[Text Classification]], [[Named Entity Recognition]] với use case thực tế.
- Chuẩn bị tư duy thiết kế hệ thống NLP end-to-end trước khi đi sâu hơn vào LLM/RAG/evaluation.

## Mục tiêu đọc

- Đọc từ ngày 2026-08-04 đến 2026-08-27, mỗi ngày một session khoảng 45-60 phút.
- Sau mỗi session, viết lại phần quan trọng bằng tiếng Việt trong daily note.
- Sau mỗi chapter, cập nhật section note bằng ý chính, câu hỏi review và concept cần tách.
- Ưu tiên cơ chế, pipeline, trade-off, case study và lời khuyên triển khai thực tế.

## Sections

- [x] [[Practical NLP - Chapter 01 - NLP A Primer]] - tự note nền trước daily
- [x] [[Practical NLP - Chapter 02 - NLP Pipeline]] - tự note nền trước daily
- [x] [[Practical NLP - Chapter 03 - Text Representation]] - tự note nền trước daily
- [ ] [[Practical NLP - Chapter 04 - Text Classification]]
- [ ] [[Practical NLP - Chapter 05 - Information Extraction]]
- [ ] [[Practical NLP - Chapter 06 - Chatbots]]
- [ ] [[Practical NLP - Chapter 07 - Topics in Brief]]
- [ ] [[Practical NLP - Chapter 08 - Social Media]]
- [ ] [[Practical NLP - Chapter 09 - E-Commerce and Retail]]
- [ ] [[Practical NLP - Chapter 10 - Healthcare Finance and Law]]
- [ ] [[Practical NLP - Chapter 11 - The End-to-End NLP Process]]

## Part I - Foundations đã tự note

- [[Practical NLP - Chapter 01 - NLP A Primer]]: bản đồ NLP thực tế, độ khó của ngôn ngữ tự nhiên, ba hướng tiếp cận heuristic/ML/DL, và walkthrough conversational agent.
- [[Practical NLP - Chapter 02 - NLP Pipeline]]: vòng đời NLP từ raw data đến cleanup, preprocessing, features, modeling, evaluation, deployment, monitoring và update loop.
- [[Practical NLP - Chapter 03 - Text Representation]]: cách biến text thành vector, từ sparse representation đến [[Embedding]] và representation dùng cho downstream task.

## Lịch đọc daily từ Part II - Essentials

| Ngày | Nội dung | Trang PDF | Trọng tâm |
| --- | --- | --- | --- |
| 2026-08-04 | [[Practical NLP - Chapter 04 - Text Classification]] | 249-263 | Ứng dụng, pipeline, classifier cơ bản |
| 2026-08-05 | [[Practical NLP - Chapter 04 - Text Classification]] | 264-278 | SVM, neural embeddings, deep classification |
| 2026-08-06 | [[Practical NLP - Chapter 04 - Text Classification]] | 279-291 | Interpretability, low-data setting, case study |
| 2026-08-07 | [[Practical NLP - Chapter 05 - Information Extraction]] | 293-310 | IE applications, tasks, pipeline, keyphrase, NER mở đầu |
| 2026-08-08 | [[Practical NLP - Chapter 05 - Information Extraction]] | 311-330 | NER system, active learning, entity linking, RE mở đầu |
| 2026-08-09 | [[Practical NLP - Chapter 05 - Information Extraction]] | 331-351 | Relationship extraction, event extraction, template filling |
| 2026-08-10 | [[Practical NLP - Chapter 06 - Chatbots]] | 356-375 | Chatbot taxonomy, FAQ, goal-oriented dialog |
| 2026-08-11 | [[Practical NLP - Chapter 06 - Chatbots]] | 376-400 | Dialog state, slots, response generation |
| 2026-08-12 | [[Practical NLP - Chapter 06 - Chatbots]] | 401-425 | End-to-end dialog, RL, human-in-the-loop, Rasa |
| 2026-08-13 | [[Practical NLP - Chapter 07 - Topics in Brief]] | 429-447 | Search và information retrieval |
| 2026-08-14 | [[Practical NLP - Chapter 07 - Topics in Brief]] | 448-464 | Topic modeling và summarization |
| 2026-08-15 | [[Practical NLP - Chapter 07 - Topics in Brief]] | 465-483 | Recommender, machine translation, QA |
| 2026-08-16 | [[Practical NLP - Chapter 08 - Social Media]] | 488-514 | Social media challenges, tokenizer, trends, sentiment |
| 2026-08-17 | [[Practical NLP - Chapter 08 - Social Media]] | 515-540 | Social preprocessing, support, memes, fake news |
| 2026-08-18 | [[Practical NLP - Chapter 09 - E-Commerce and Retail]] | 545-563 | E-commerce catalog, search, attribute extraction |
| 2026-08-19 | [[Practical NLP - Chapter 09 - E-Commerce and Retail]] | 564-581 | Taxonomy, enrichment, deduplication, review sentiment |
| 2026-08-20 | [[Practical NLP - Chapter 09 - E-Commerce and Retail]] | 582-598 | Aspect sentiment và recommendations |
| 2026-08-21 | [[Practical NLP - Chapter 10 - Healthcare Finance and Law]] | 601-617 | Healthcare NLP, medical records, decision support |
| 2026-08-22 | [[Practical NLP - Chapter 10 - Healthcare Finance and Law]] | 618-637 | Mental health, medical IE, finance/law mở đầu |
| 2026-08-23 | [[Practical NLP - Chapter 10 - Healthcare Finance and Law]] | 638-652 | Finance NLP, legal NLP, risk |
| 2026-08-24 | [[Practical NLP - Chapter 11 - The End-to-End NLP Process]] | 657-670 | Deploying NLP software, reproducibility |
| 2026-08-25 | [[Practical NLP - Chapter 11 - The End-to-End NLP Process]] | 671-684 | Troubleshooting, interpretability, monitoring, technical debt |
| 2026-08-26 | [[Practical NLP - Chapter 11 - The End-to-End NLP Process]] | 685-700 | Data science process, team, problem framing, data readiness |
| 2026-08-27 | [[Practical NLP - Chapter 11 - The End-to-End NLP Process]] | 701-712 | Organization readiness, horizon, tổng kết sách |

## Khái niệm liên quan

- [[Language AI]]
- [[NLP Pipeline]]
- [[Text Representation]]
- [[Tokenization]]
- [[Embedding]]
- [[Text Classification]]
- [[Named Entity Recognition]]
- [[Topic Modeling]]
- [[Summarization]]
- [[Question Answering]]

## Gợi ý concept cần rà trong lúc đọc

- Information extraction
- Dialog system
- Information retrieval
- Aspect-level sentiment analysis
- Model monitoring
- Technical debt trong ML/NLP

## Ghi chú sau khi hoàn thành

-
