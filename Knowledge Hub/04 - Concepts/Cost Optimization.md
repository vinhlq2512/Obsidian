---
type: concept
status: seed
sources:
  - "[[2025-02-19_how-canva-optimized-230-petabytes-of-data-and-saved-3-6-mill-byte-sized-design]]"
  - "[[2025-08-05_how-confluent-cut-kafka-costs-by-60percent]]"
source_sections:
  - "[[2025-02-19_how-canva-optimized-230-petabytes-of-data-and-saved-3-6-mill-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - cost
  - system-design
---

# Cost Optimization

## Định nghĩa

[[Cost Optimization]] là quá trình giảm chi phí vận hành hệ thống mà vẫn giữ được yêu cầu về latency, availability, durability, security và trải nghiệm người dùng.

## Cách hiểu bằng lời của tôi

Tối ưu chi phí không phải là chọn option rẻ nhất. Nó là đo workload thật, hiểu cost driver, rồi chuyển phần ít quan trọng hơn sang tài nguyên/lớp storage/lịch xử lý phù hợp hơn. Nếu không đo retrieval, request volume hoặc access pattern, "tiết kiệm" rất dễ chuyển thành latency xấu hoặc hóa đơn khác tăng lên.

## Pattern thường gặp

- Đo usage và access pattern trước khi migrate.
- Tách hot path/cold path.
- Dùng lifecycle policy hoặc tiering cho dữ liệu cũ.
- Giảm duplicate work bằng caching, batching hoặc compaction.
- Theo dõi cả storage cost, request cost, compute cost và operational risk.

## Liên kết

- [[Storage Class Tiering]]
- [[Data Lifecycle Management]]
- [[Caching Strategy]]
- [[Observability]]
- [[Latency]]
