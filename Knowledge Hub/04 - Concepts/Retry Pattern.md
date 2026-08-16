---
type: concept
status: understood
sources:
  - "[[2025-12-18_a-guide-to-retry-pattern-in-distributed-systems]]"
  - "[[2026-07-30_a-detailed-guide-to-idempotency-delivery-semantics-and-dedup]]"
  - "[[2024-11-27_understanding-retry-storms-what-they-are-and-how-to-deal-wit]]"
source_sections:
  - "[[2025-12-18_a-guide-to-retry-pattern-in-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - distributed-systems
---

# Retry Pattern

## Cách hiểu bằng lời của tôi

[[Retry Pattern]] là tự động thử lại operation thất bại với giả định lỗi là transient. Retry đổi thêm latency để lấy perceived availability, nhưng nếu dùng sai có thể biến sự cố nhỏ thành retry storm.

## Cơ chế an toàn

```text
Attempt fails
-> phân loại lỗi transient hay permanent
-> kiểm tra retry budget / max attempts
-> chờ backoff
-> thêm jitter để tránh đồng bộ retry
-> retry nếu operation an toàn hoặc có idempotency
```

## Rule of thumb

- Không retry lỗi permanent như validation/auth/business rule.
- Retry synchronous user path ít lần vì user không chờ lâu.
- Retry async job có thể lâu hơn nhưng cần queue/dead-letter/visibility.
- Exponential backoff + jitter thường an toàn hơn retry ngay hoặc fixed interval.
- Retry nên tập trung ở một lớp, tránh mỗi service đều retry làm nhân tải theo chiều sâu call graph.

## Retry storm

[[Retry Storm]] xảy ra khi retry không còn giúp hồi phục mà trở thành bộ nhân tải. Các nguyên nhân hay gặp là fixed interval khiến retry đồng bộ, retry vô hạn, không có backoff, nhiều tầng service cùng retry, và thiếu tín hiệu backpressure từ downstream.

Khi thiết kế retry, câu hỏi không chỉ là "có nên thử lại không" mà là "thử lại có làm downstream đang đau càng đau hơn không".

## Liên kết

- [[Idempotency Key]]
- [[Backpressure]]
- [[Circuit Breaker]]
- [[Observability]]
- [[Retry Storm]]
