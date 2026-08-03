---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: course-note
title: "CS224N 2023 - Notes 01 - Introduction and Word2Vec - Draft"
year: 2023
venue: ""
arxiv: ""
source_file: "[[CS224N 2023 - Notes 01 - Introduction and Word2Vec - Draft.pdf]]"
pages: 13
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Embedding]]"
  - "[[Tokenization]]"
tags:
  - cs224n
  - course-note
---

# CS224N 2023 - Notes 01 - Introduction and Word2Vec - Draft

## Nguồn

- PDF gốc: [[CS224N 2023 - Notes 01 - Introduction and Word2Vec - Draft.pdf]]
- Vai trò trong CS224N: note nhập môn NLP và Word2Vec, đặt câu hỏi representation cho ngôn ngữ.

## Câu hỏi trung tâm

NLP nghiên cứu gì và vì sao biểu diễn từ bằng vector thấp chiều là ý tưởng nền tảng?

## Kiến thức cốt lõi

- NLP là lĩnh vực xây và nghiên cứu hệ thống hiểu/sinh ngôn ngữ tự nhiên.
- Ngôn ngữ người có cấu trúc, mơ hồ, giàu ngữ cảnh và khó biểu diễn bằng rule đơn giản.
- Representation là câu hỏi xuyên suốt khoá: máy nên biểu diễn word/sentence/document như thế nào?
- Word2Vec học low-dimensional real-valued vectors từ distributional signal.
- Note đặt nền cho applications như machine translation, QA, dialogue và information extraction.

## Cơ chế / công thức / kiến trúc

```text
raw language
-> tokenization / vocabulary
-> word representation
-> distributional learning objective
-> vector space dùng cho downstream NLP
```

## Khi áp dụng

- Đọc trước Lecture 02 nếu muốn bức tranh lớn về NLP.
- Luôn hỏi mỗi mô hình đang dùng representation gì.
- Dùng Word2Vec như ví dụ đầu tiên về representation learning.

## Kết quả / bằng chứng đáng giữ

- Source summary nói note giới thiệu NLP và Word2Vec.
- Trang đầu định nghĩa NLP là hệ thống hiểu và sinh natural languages.
- Note nhấn mạnh low-dimensional real-valued vectors learned from distributional signal.

## Cách hiểu bằng lời của tôi

NLP hiện đại bắt đầu từ câu hỏi rất căn bản: làm sao biến ngôn ngữ thành dạng mà model học được mà không làm mất nghĩa quá nhiều.

## Câu hỏi review

1. NLP gồm hai hướng lớn nào: hiểu và sinh?
2. Representation quan trọng vì sao?
3. Distributional signal trong Word2Vec là gì?

## Liên kết

- [[NLP]]
- [[Word2Vec]]
- [[Embedding]]
- [[Tokenization]]
- [[CS224N]]
