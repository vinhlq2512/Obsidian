# Note Templates

Use these as conditional templates. Do not create empty sections merely because they appear here.

## Paper Note

```markdown
---
type: paper
status: draft
title:
authors:
year:
venue:
url:
pdf: "[[Paper File.pdf]]"
zotero_key:
citekey:
doi:
arxiv:
code_url:
dataset_url:
source_version:
topic:
priority: medium
reading_status: not-started
rating:
related_concepts:
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
tags:
  - paper
---

# Title

## Tóm tắt một câu

## Nguồn

## Vấn đề paper giải quyết

## Gap và đóng góp

## Bài toán/formalization

## Phương pháp

## Protocol fingerprint

## Kết quả chính

## Hạn chế, giả định, failure modes

## Đánh giá từ evidence

## Diễn giải học tập

## Ghi chú cá nhân

## Câu hỏi review

## Evidence map

## Liên kết
```

## Concept Note

```markdown
---
type: concept
status: seed
sources:
source_sections:
first_seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags:
  - concept
---

# Concept

## Định nghĩa ngắn

## Diễn giải học tập

## Vì sao quan trọng

## Cơ chế

## Công thức hoặc ví dụ

## Khi áp dụng

## Trade-off và failure modes

## Liên quan

## Nguồn đã dùng

## Câu hỏi review
```

Use `Cách hiểu bằng lời của tôi` only when the user supplies personal wording or explicitly asks for a first-person draft.

## Literature Note

```markdown
---
type: literature-note
status: seed
topic:
scope:
papers:
related_concepts:
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
tags:
  - literature-note
---

# Title

## Câu hỏi trung tâm

## Bức tranh tổng quan

## Các paper trong scope

## Protocol và fairness khi so sánh

## Các hướng tiếp cận

## Điểm đồng thuận

## Điểm còn tranh luận

## Khoảng trống nghiên cứu

## Roadmap đọc tiếp

## Câu hỏi review
```
