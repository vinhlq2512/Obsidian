---
type: concept
status: seed
sources:
  - "[[2025-02-06_the-tech-lead-s-guide-to-load-testing-like-a-pro-byte-sized-design]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
source_sections:
  - "[[2025-02-06_the-tech-lead-s-guide-to-load-testing-like-a-pro-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - performance
---

# Load Testing

## Định nghĩa

[[Load Testing]] là việc mô phỏng traffic và workflow gần thực tế để đo latency, throughput, bottleneck, failure point và khả năng chịu tải của toàn hệ thống.

## Cách hiểu bằng lời của tôi

Load test tốt không phải là bắn thật nhiều request vào một endpoint. Nó phải mô phỏng user behavior, data distribution, network condition, database/cache/message queue/background job và traffic pattern. Nếu staging không giống production scale, nhiều failure mode sẽ chỉ xuất hiện khi đã rollout thật.

## Các kiểu test

- Smoke test: tải rất nhỏ để lấy baseline và kiểm tra health.
- Average-load test: tải ngày thường.
- Stress test: tăng tải vượt peak để tìm điểm yếu.
- Spike test: tăng tải đột ngột như flash sale/viral event.
- Breakpoint test: tìm ngưỡng hệ bắt đầu degrade hoặc fail.
- Soak test: chạy lâu để lộ memory leak, resource exhaustion, database slowdown.

## Pitfall

- Reuse data quá nhiều làm cache skew kết quả.
- Chỉ test API mà bỏ database, cache, queue và job nền.
- Không test cold start, packet loss, jitter hoặc mobile network chậm.
- Không có success criteria rõ như p95 latency, error rate, max throughput.

## Liên kết

- [[Capacity Planning]]
- [[Peak QPS]]
- [[Chaos Engineering]]
- [[Synthetic Monitoring]]
- [[Observability]]
- [[Latency]]
