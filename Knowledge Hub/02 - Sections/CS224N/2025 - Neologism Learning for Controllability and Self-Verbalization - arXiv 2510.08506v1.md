---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2025 - Neologism Learning for Controllability and Self-Verbalization"
year: 2025
venue: "arXiv"
arxiv: "2510.08506v1"
source_file: "[[2025 - Neologism Learning for Controllability and Self-Verbalization - arXiv 2510.08506v1.pdf]]"
pages: 25
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - paper
---

# 2025 - Neologism Learning for Controllability and Self-Verbalization - arXiv 2510.08506v1

## Nguồn

- PDF gốc: [[2025 - Neologism Learning for Controllability and Self-Verbalization - arXiv 2510.08506v1.pdf]]
- Vai trò trong CS224N: paper về học từ mới/neologism để điều khiển và tự diễn đạt khái niệm trong model.

## Câu hỏi trung tâm

Model có thể học neologisms như ký hiệu điều khiển/khái niệm mới và tự verbalize ý nghĩa của chúng không?

## Kiến thức cốt lõi

- Neologism là từ/ký hiệu mới chưa có nghĩa ổn định trong dữ liệu cũ.
- Học neologism có thể tạo nút điều khiển hành vi hoặc khái niệm trong model.
- Self-verbalization kiểm tra model có diễn đạt được ý nghĩa ký hiệu mới không.
- Chủ đề này liên quan tới controllability, representation và interpretability.
- Paper nằm trong cụm advanced LLM behavior của CS224N.

## Cơ chế / công thức / kiến trúc

```text
introduce new token/word
-> associate with behavior/concept through training or prompting
-> test controllability
-> ask model verbalize meaning/use
```

## Khi áp dụng

- Dùng khi nghiên cứu control tokens hoặc learned concepts.
- Cần tách model thật sự học nghĩa với chỉ bắt chước pattern.
- Self-verbalization cần verification độc lập.

## Kết quả / bằng chứng đáng giữ

- Title nêu neologism learning for controllability and self-verbalization.
- Nguồn thuộc nhóm LLM/interpretability/reasoning mới trong CS224N.
- Chủ đề nối với tokenization và representation của khái niệm mới.

## Cách hiểu bằng lời của tôi

Một từ mới có thể trở thành tay cầm điều khiển model nếu training gắn nó với hành vi ổn định. Nhưng model nói được nghĩa của từ đó không có nghĩa nó luôn dùng đúng.

## Câu hỏi review

1. Neologism khác token thường ở điểm nào?
2. Controllability qua token/ký hiệu mới hoạt động ra sao?
3. Self-verbalization cần kiểm chứng gì?

## Liên kết

- [[Tokenization]]
- [[Representation Model]]
- [[Large Language Model]]
- [[CS224N]]
