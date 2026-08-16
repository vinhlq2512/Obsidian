---
type: concept
status: developing
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - event-driven
---

# Change Data Capture

## Định nghĩa

Change Data Capture (CDC) là cơ chế đọc log thay đổi của database rồi phát các thay đổi đó sang hệ downstream.

## Cách hiểu bằng lời của tôi

CDC biến database write thành event stream gần real-time. Thay vì application phải dual-write sang nhiều nơi, một process đọc binlog/WAL và cập nhật search index, warehouse, cache hoặc service khác.

Trong case Figma, CDC được dùng để thay full sync đắt đỏ bằng incremental sync: snapshot ban đầu tạo điểm xuất phát, sau đó stream thay đổi từ Kafka được merge vào warehouse. Điểm quan trọng là offset của CDC phải bao phủ thời điểm snapshot, vì duplicate có thể xử lý ở bước merge nhưng khoảng trống dữ liệu thì rất khó phát hiện.

## Trade-off

- Đáng tin hơn dual-write vì dựa vào log đã commit.
- Coupled với format/log semantics của storage engine.
- Downstream vẫn có lag và cần observability cho stuck consumer, out-of-order event và replay.
- Cần [[Snapshot Bootstrap]] và [[Data Pipeline Validation]] nếu downstream là warehouse/reporting system đòi hỏi correctness cao.

## Liên kết

- [[Write-Ahead Log]]
- [[Eventual Consistency]]
- [[Specialized Read Store]]
- [[Transactional Outbox]]
- [[Message Broker]]
- [[Event Stream]]
- [[Snapshot Bootstrap]]
- [[Data Pipeline Validation]]
