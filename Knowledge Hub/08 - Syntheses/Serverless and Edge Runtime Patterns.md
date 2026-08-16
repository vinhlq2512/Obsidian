---
type: synthesis
status: seed
concepts:
  - "[[Serverless Architecture]]"
  - "[[Function as a Service]]"
  - "[[Backend as a Service]]"
  - "[[Serverless Cold Start]]"
  - "[[Lambda Execution Environment]]"
  - "[[Firecracker MicroVM]]"
  - "[[Lambda SnapStart]]"
  - "[[Provisioned Concurrency]]"
  - "[[Serverless Worker Sharding]]"
sources:
  - "[[2023-11-16_serverless-has-servers]]"
  - "[[2025-01-28_aws-lambda-turns-10]]"
  - "[[2026-02-17_how-cloudflare-eliminates-cold-starts-for-serverless-workers]]"
  - "[[2024-11-01_baselime-s-big-move-from-aws-to-cloudflare-faster-simpler-ch]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - serverless
  - system-design
---

# Serverless and Edge Runtime Patterns

## Luận điểm chính

Serverless là một hợp đồng vận hành: developer nhận autoscaling, pay-per-use và ít phải quản lý server; provider phải giải bài toán placement, isolation, cold start, routing, billing và observability.

## Các lớp chính

- [[Function as a Service]] chạy business logic stateless theo event.
- [[Backend as a Service]] cung cấp stateful capability qua managed API.
- [[Lambda Execution Environment]] và [[Firecracker MicroVM]] cho thấy runtime vẫn cần isolation và placement cụ thể.
- [[Serverless Cold Start]] là trade-off của scale-to-zero; [[Lambda SnapStart]], [[Provisioned Concurrency]] và [[Serverless Worker Sharding]] là các cách giảm hoặc né chi phí khởi động.
- [[Serverless Cost Model]] tốt cho workload bursty, nhưng workload liên tục hoặc nhiều managed dependency có thể cần so lại với container/service truyền thống.

## Mental model

```text
event/request
-> platform routing và placement
-> execution environment warm hoặc cold
-> function logic
-> BaaS/storage/queue/analytics
-> logs, metrics, billing
```

## Trade-off cần nhớ

- Serverless giảm ops cho team app nhưng tăng phụ thuộc vào behavior của platform.
- Low-latency path phải xử lý cold start như một reliability/tail-latency problem.
- FaaS tốt cho logic ngắn và event-driven; không phải mặc định tốt nhất cho workflow dài, stateful hoặc cần runtime kiểm soát sâu.

## Liên kết

- [[Edge Function]]
- [[API Gateway]]
- [[Event Stream]]
- [[Cost Optimization]]
- [[Observability]]
