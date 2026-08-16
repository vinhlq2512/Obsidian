---
type: concept
status: seed
sources:
  - "[[2023-11-07_shipping-to-production]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
source_sections:
  - "[[2023-11-07_shipping-to-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - deployment
  - reliability
---

# Phased Rollout

## Định nghĩa

[[Phased Rollout]] là chiến lược triển khai thay đổi theo từng giai đoạn nhỏ, có criteria quan sát giữa các bước trước khi mở rộng phạm vi.

## Cách hiểu bằng lời của tôi

Thay vì đưa thay đổi tới 100% traffic ngay, phased rollout tăng blast radius từ nhỏ tới lớn: internal, region nhỏ, vài phần trăm user, rồi toàn cầu. Điểm cốt lõi không phải là chia phần trăm cho đẹp, mà là có tín hiệu dừng/rollback rõ ở mỗi giai đoạn.

## Cần có

- Health metrics và business metrics đi kèm rollout.
- Control group hoặc canary để so sánh.
- Automated rollback nếu metric xấu.
- Owner theo dõi trong thời gian rollout.
- Quy tắc pause nếu [[Error Budget]] đã cạn.

## Bài học từ outage

Nguồn OpenAI cho thấy thay đổi hạ tầng có thể pass staging nhưng fail ở production-scale cluster. Vì vậy phased rollout cho infra/config cần quan sát cả workload service lẫn control plane, không chỉ app-level metrics.

## Liên kết

- [[Error Budget]]
- [[Load Testing]]
- [[Postmortem]]
- [[Blast Radius]]
- [[Observability]]
- [[Rollback Strategy]]
