---
type: concept
status: seed
sources:
  - "[[2025-05-01_inside-netflixs-radical-shift-to-a-single-foundation-model]]"
  - "[[2026-04-27_how-amazon-uses-llms-to-recommend-products]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - recommendation
  - foundation-model
  - ai
---

# Foundation Model for Recommendation

## Định nghĩa

Foundation model for recommendation là hướng xây một model nền chung cho nhiều bài toán recommendation, thay vì nhiều model nhỏ riêng cho từng surface hoặc mục tiêu.

## Cách hiểu bằng lời của tôi

Trong recommendation, "token" không nhất thiết là từ. Nó có thể là event người dùng xem phim, pause, search, click, bỏ qua, context thiết bị hoặc metadata item. Model học từ chuỗi event đó để dự đoán item/action tiếp theo giống cách LLM học từ chuỗi token, nhưng dữ liệu dị thể và mục tiêu serving khắt khe hơn.

## Cơ chế từ Netflix

ByteByteGo mô tả Netflix phải giải ba việc lớn:

- Representation: biến event dị thể thành token/embedding có thể học chung.
- Context compression: dùng hierarchical compression và sliding window sampling để giữ lịch sử dài nhưng vẫn phục vụ nhanh.
- Serving: kết hợp sparse attention, [[KV Cache]], batch pre-computation và vector store để latency ở mức vài chục mili-giây.

## Vấn đề production

- Cold start cần metadata-based initialization, vì item mới chưa có đủ hành vi.
- Entity drift làm embedding cũ và mới lệch nhau sau retrain.
- Feedback loop và presentation bias có thể khiến model học lại chính cách hệ thống từng hiển thị.
- [[Embedding Lifecycle Management]] trở thành phần của sản phẩm, không chỉ là chi tiết ML offline.

## Serving và specialization

Một model nền chung giảm duplication giữa nhiều surface, nhưng mỗi surface vẫn có nhu cầu khác nhau: search cần tốc độ/precision, homepage cần breadth, notification cần timeliness. Vì vậy production thường cần fine-tuned heads, adapters hoặc serving layer riêng để giữ specialization mà không tách rời hoàn toàn representation nền.

## Liên kết

- [[Product Recommendation System]]
- [[Semantic Search]]
- [[Vector Search Infrastructure]]
- [[KV Cache]]
- [[LLM Evaluation]]
- [[Embedding Lifecycle Management]]
- [[Cold Start Problem]]
