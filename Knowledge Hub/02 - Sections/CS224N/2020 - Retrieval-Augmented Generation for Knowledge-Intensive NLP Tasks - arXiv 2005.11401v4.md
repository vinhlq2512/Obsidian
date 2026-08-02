---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2020 - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
year: 2020
venue: "arXiv"
arxiv: "2005.11401v4"
source_file: "[[2020 - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks - arXiv 2005.11401v4.pdf]]"
pages: 19
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Retrieval-Augmented Generation]]"
  - "[[Retriever]]"
tags:
  - cs224n
  - paper
---

# 2020 - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks - arXiv 2005.11401v4

## Nguồn

- PDF gốc: [[2020 - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks - arXiv 2005.11401v4.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 10 - RAG and Language Agents]]
- Concept: [[Retrieval-Augmented Generation]], [[Retriever]], [[Reader]]

## Vấn đề paper giải quyết

Pretrained LM lưu tri thức trong tham số nhưng khó truy cập/chỉnh sửa chính xác, khó cập nhật world knowledge và khó cung cấp provenance. RAG thêm non-parametric memory để model truy xuất tài liệu khi sinh câu trả lời.

## Đóng góp chính

- Kết hợp pretrained seq2seq generator với retriever truy cập explicit memory.
- Đưa retrieval vào generation cho knowledge-intensive tasks.
- Làm rõ lợi ích của provenance và khả năng cập nhật tri thức ngoài tham số model.

## Cơ chế RAG

```text
query/input
-> retriever lấy passages liên quan
-> generator condition trên input + retrieved passages
-> sinh answer
```

Có hai điểm cần đánh giá riêng: retriever lấy đúng evidence không, và generator dùng evidence đó đúng không.

## Vì sao quan trọng với CS224N

Lecture 10 dùng RAG như nền cho hệ thống QA hiện đại và agent có memory/tool. Đây là cầu nối giữa [[Semantic Search]] và [[Text Generation]].

## Hạn chế / câu hỏi

- Retriever sai kéo generator vào ngữ cảnh sai.
- Passage đúng nhưng generator vẫn có thể hallucinate.
- Chunking/index/update policy trở thành một phần của model behavior.

## Câu hỏi review

1. RAG thêm loại memory nào vào LM?
2. Provenance quan trọng ở đâu?
3. Vì sao cần đánh giá retriever và generator riêng?
