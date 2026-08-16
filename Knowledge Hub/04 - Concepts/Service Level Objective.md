---
type: concept
status: seed
sources:
  - "[[2025-01-20_the-engineers-guide-to-observability-making-metrics-logs-and]]"
  - "[[2023-11-07_shipping-to-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - observability
---

# Service Level Objective

## Định nghĩa

Service Level Objective là mục tiêu định lượng cho một [[Service Level Indicator]], ví dụ 99.9% request thành công trong 30 ngày hoặc p99 latency dưới 500ms.

## Cách hiểu bằng lời của tôi

SLI là thứ đo; SLO là ngưỡng cam kết nội bộ. Nếu không có SLO, alert dễ biến thành cảm tính: cái gì cũng có vẻ đáng lo nhưng không rõ cái gì cần đánh thức người trực.

## Cần biết

- SLO nên phản ánh user impact và business flow quan trọng.
- Alert nên bám vào SLO burn hoặc symptom quan trọng hơn CPU/memory đơn lẻ.
- SLO quá chặt gây alert fatigue; quá lỏng thì không bảo vệ trải nghiệm.
- SLO tạo nền cho [[Error Budget]], giúp quyết định khi nào nên chấp nhận rollout rủi ro và khi nào phải ưu tiên reliability.

## Liên kết

- [[Service Level Indicator]]
- [[Error Budget]]
- [[Metrics]]
- [[Alerting]]
- [[High Availability]]
