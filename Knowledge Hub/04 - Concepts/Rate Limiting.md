---
type: concept
status: understood
sources:
  - "[[2025-09-04_a-guide-to-rate-limiting-strategies-bytebytego-newsletter]]"
  - "[[2024-10-03_api-gateway-newsletter]]"
  - "[[2026-01-29_how-to-scale-an-api]]"
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
source_sections:
  - "[[2025-09-04_a-guide-to-rate-limiting-strategies-bytebytego-newsletter]]"
  - "[[2024-10-03_api-gateway-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
---

# Rate Limiting

## Cách hiểu bằng lời của tôi

[[Rate Limiting]] là cơ chế đặt "ngân sách request" cho một client, tenant, IP, API key, endpoint hoặc tài nguyên backend. Mục tiêu không chỉ là chặn tấn công, mà còn giữ hệ thống trong vùng vận hành ổn định: tránh spike làm đầy connection pool, tránh retry khuếch đại lỗi, tránh một tenant dùng hết capacity chung, và kiểm soát chi phí.

Điểm quan trọng: rate limit khác với quota. Quota thường kiểm soát tổng mức dùng trong cửa sổ dài như ngày/tháng. Rate limit kiểm soát nhịp ngắn và burst để bảo vệ capacity tức thời.

## Cơ chế

```text
Request
-> xác định key chịu trách nhiệm: user, tenant, API key, IP, endpoint
-> đọc trạng thái limit của key
-> thuật toán quyết định allow / reject / delay
-> trả response kèm tín hiệu retry khi bị giới hạn
```

Các thuật toán thường gặp:

- Fixed window counter: rẻ và dễ hiểu, nhưng có lỗi biên cửa sổ.
- Sliding window log: chính xác hơn vì lưu timestamp từng request, đổi lại tốn bộ nhớ hơn.
- Sliding window counter: xấp xỉ sliding window với chi phí thấp hơn.
- Token bucket: cho phép burst ngắn nhưng vẫn giữ tốc độ dài hạn bằng refill rate.
- Leaky bucket: làm mượt đầu ra bằng queue và drain rate cố định.

## Trade-off cần nhớ

- Accuracy: limit có bám sát ngân sách thật không.
- Predictability: client có thấy hành vi ổn định hay bị allow burst rồi block dài.
- Fairness: một key nóng có làm ảnh hưởng key khác không.
- Overhead: kiểm tra limit nằm trên request path nên không được quá chậm.

## Khi áp dụng

Dùng rate limiting ở edge/API gateway khi cần bảo vệ backend chung, chống abuse, phân tầng plan, hoặc giữ chi phí external API trong kiểm soát. Với API nội bộ, rate limit vẫn hữu ích khi service downstream có capacity nhỏ hơn upstream.

Response nên cung cấp tín hiệu như limit, remaining và reset time để client tự điều chỉnh. Khi hệ thống cần delay hoặc làm chậm thay vì chỉ reject, xem thêm [[Throttling]].

## Liên kết

- [[API Gateway]]
- [[Throttling]]
- [[Load Balancer]]
- [[Backpressure]]
- [[Scalable Distributed Systems Patterns]]
