---
type: concept
status: seed
sources:
  - "[[2025-05-01_inside-netflixs-radical-shift-to-a-single-foundation-model]]"
source_sections:
  - "[[2025-05-01_inside-netflixs-radical-shift-to-a-single-foundation-model]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - recommendation
  - ai
---

# Embedding Lifecycle Management

## Định nghĩa

[[Embedding Lifecycle Management]] là việc version, align, migrate và kiểm soát compatibility của embedding khi model, catalog hoặc downstream consumers thay đổi theo thời gian.

## Cách hiểu bằng lời của tôi

Embedding không phải artifact tĩnh. Khi model retrain, vector space có thể xoay/lệch; khi catalog đổi, item mới chưa có history; khi downstream service phụ thuộc embedding cũ, thay đổi thiếu kiểm soát có thể làm retrieval/ranking hỏng dù API vẫn chạy.

## Vấn đề trong recommendation

- Entity drift: item catalog thêm/xóa liên tục, embedding cần cập nhật mà không retrain toàn bộ model mỗi lần.
- Cold start: item mới cần proxy embedding từ metadata trước khi có đủ interaction.
- Serving compatibility: downstream team dùng embedding cho nhiều surface khác nhau.
- Presentation bias: embedding học từ hành vi chịu ảnh hưởng bởi những gì hệ thống từng hiển thị.

## Pattern từ nguồn Netflix

- Metadata-based initialization tạo proxy embedding cho title mới.
- Mixing layer cân bằng metadata embedding và ID embedding theo tuổi item.
- Low-rank orthogonal transformation giúp giữ embedding ổn định hơn giữa các lần retrain.
- Versioning và hygiene là phần của hạ tầng recommendation, không chỉ của training pipeline.

## Liên kết

- [[Foundation Model for Recommendation]]
- [[Product Recommendation System]]
- [[Cold Start Problem]]
- [[Vector Search Infrastructure]]
- [[Model Benchmarking]]
