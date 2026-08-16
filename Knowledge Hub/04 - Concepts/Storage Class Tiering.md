---
type: concept
status: seed
sources:
  - "[[2025-02-19_how-canva-optimized-230-petabytes-of-data-and-saved-3-6-mill-byte-sized-design]]"
  - "[[2025-02-25_how-amazon-s3-stores-350-trillion-objects-with-11-nines-of-d]]"
source_sections:
  - "[[2025-02-19_how-canva-optimized-230-petabytes-of-data-and-saved-3-6-mill-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - storage
  - cost
---

# Storage Class Tiering

## Định nghĩa

[[Storage Class Tiering]] là chiến lược đặt dữ liệu vào nhiều lớp lưu trữ khác nhau theo access pattern, latency cần thiết, retrieval cost và thời gian giữ dữ liệu.

## Cách hiểu bằng lời của tôi

Không phải object nào cũng đáng nằm ở lớp đắt nhất. Dữ liệu mới hoặc hot cần truy cập nhanh; dữ liệu cũ, ít đọc có thể chuyển sang lớp rẻ hơn. Điểm khó là phải dựa trên đo đạc, vì chuyển sai lớp có thể tiết kiệm tiền storage nhưng làm tăng retrieval cost hoặc ảnh hưởng trải nghiệm.

## Pattern từ Canva/S3

- Phân tích access pattern trước khi chuyển lớp.
- Dùng lifecycle policy để tự động chuyển object theo tuổi hoặc tag.
- Giữ dữ liệu hay truy cập ở lớp latency thấp.
- Chuyển dữ liệu infrequently accessed hoặc archival sang lớp rẻ hơn nếu retrieval vẫn đáp ứng UX.

## Câu hỏi thiết kế

- Object nào được đọc trong vài ngày đầu, rồi nguội dần?
- Retrieval latency có nằm trên critical path của user không?
- Chi phí request/retrieval có làm mất phần tiết kiệm storage không?
- Có cần object tagging để áp policy khác nhau cho từng dataset không?

## Liên kết

- [[Object Storage]]
- [[Amazon S3]]
- [[Data Lifecycle Management]]
- [[Caching Strategy]]
- [[Cost Optimization]]
