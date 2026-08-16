---
type: synthesis
status: seed
concepts:
  - "[[Video Streaming Architecture]]"
  - "[[Content Delivery Network]]"
  - "[[Proactive Caching]]"
  - "[[Live Streaming Origin]]"
  - "[[CQRS]]"
  - "[[In-Memory Read Model]]"
  - "[[Workflow Orchestration]]"
sources:
  - "[[2024-01-04_netflix-what-happens-when-you-press-play]]"
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
  - "[[2025-09-09_how-netflix-tudum-supports-20-million-users-with-cqrs]]"
  - "[[2025-04-15_how-netflix-orchestrates-millions-of-workflow-jobs-with-maes]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - system-design
  - bytebytego
---

# Netflix Streaming and Workflow Architecture

## Ý chính

Cụm nguồn Netflix của ByteByteGo cho thấy một pattern lớn: scale không đến từ một hệ thống chung chung, mà từ việc tách rõ đường điều khiển, đường dữ liệu, đường đọc, đường ghi và workflow state.

## Bản đồ kiến trúc

```text
User/client
-> AWS backend/control plane: auth, license, catalog, playback decision
-> Open Connect/CDN data plane: stream video từ edge gần user
-> client SDK: probe endpoint, đổi OCA, đổi chất lượng

Media source
-> transcoding pipeline
-> proactive caching tới OCA
-> playback ở edge

Live source
-> live encode/package
-> Live Origin
-> Open Connect
-> client

Editorial/content workflow
-> write path/CMS
-> read model
-> in-memory read path cho page construction/search/personalization

Data/ML workflows
-> workflow definition/DAG
-> scheduler/signal
-> engine/queue/state store
-> event publishing và observability
```

## Pattern học được

- Tách control plane và data plane giúp backend ra quyết định còn data-heavy serving chạy ở lớp tối ưu riêng.
- Với video, đưa dữ liệu gần user quan trọng hơn cố scale origin trung tâm.
- Với live, write path phải được bảo vệ vì mỗi segment có deadline rất ngắn.
- CQRS hữu ích, nhưng read path nhiều hop/cache refresh có thể làm preview bị stale; in-memory read model là một cách đổi latency lấy RAM và sync complexity.
- Workflow orchestration cần state đáng tin cậy, queue để hấp thụ spike, và lineage/rollup để debug những pipeline rất lớn.

## Trade-off chung

Netflix thường chọn tăng kiểm soát ở những phần là năng lực lõi: client SDK, video CDN, live origin, content read path và workflow platform. Đổi lại, hệ thống phức tạp hơn và cần nhiều lớp observability, consistency control, cache policy và operational tooling.

## Liên kết

- [[Video Streaming Architecture]]
- [[Adaptive Bitrate Streaming]]
- [[Video Transcoding Pipeline]]
- [[Proactive Caching]]
- [[Live Streaming Origin]]
- [[Content Delivery Network]]
- [[CQRS]]
- [[In-Memory Read Model]]
- [[Workflow Orchestration]]
