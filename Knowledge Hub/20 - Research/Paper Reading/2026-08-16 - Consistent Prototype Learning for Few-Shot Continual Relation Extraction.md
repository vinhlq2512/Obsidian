---
type: paper-reading
date: 2026-08-16
status: scaffolded
paper: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
pdf: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]"
created_at: 2026-08-16
updated_at: 2026-08-23
tags:
  - paper-reading
  - relation-extraction
  - continual-learning
---

# 2026-08-16 - Consistent Prototype Learning for Few-Shot Continual Relation Extraction

## Tiến độ

- Bắt đầu đọc paper này.
- Working note chi tiết đã được scaffold ở [[2026-08-19 - ConPL - Gemini Notebook Workflow]].
- Trạng thái đọc cá nhân vẫn không được tự động đổi thành completed.

## Bản đồ đọc nhanh

- **Problem:** few-shot continual relation extraction cần học relation mới từ rất ít ví dụ mà không làm méo representation của relation cũ.
- **Main idea:** dùng prompt + prototype memory, rồi thêm các loss nhất quán để giữ sample gần prototype và giữ cấu trúc tương đối giữa sample với toàn bộ prototype space.
- **Kết quả chính:** ConPL đạt T8 85.77 trên FewRel 10-way 5-shot và 76.38 trên TACRED 5-way 5-shot trong Table 1 của paper note chính.
- **Ablation đáng nhớ:** bỏ $L_{fc}$ làm FewRel T8 giảm mạnh nhất, từ 85.77 xuống 75.11; bỏ prototype memory giảm còn 82.21.

## Việc đọc tiếp

- [ ] Tự giải thích khác nhau giữa prototype memory và sample memory.
- [ ] Đọc Eq. 4-10, nhất là $L_{cc}$, $L_{fc}$ và $L_{dc}$.
- [ ] Kiểm caveat: Eq. 7 được gọi là focal loss nhưng không giống focal loss chuẩn nếu chỉ nhìn công thức trong PDF.

## Liên kết

- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]
- [[2026-08-19 - ConPL - Gemini Notebook Workflow]]
