---
type: concept
status: seed
sources:
  - "[[2025-04-15_how-netflix-orchestrates-millions-of-workflow-jobs-with-maes]]"
source_sections:
  - "[[2025-04-15_how-netflix-orchestrates-millions-of-workflow-jobs-with-maes]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - workflow
---

# Workflow Orchestration

## Định nghĩa

[[Workflow Orchestration]] là cách định nghĩa, schedule, chạy và theo dõi nhiều bước xử lý có dependency, thường được biểu diễn bằng DAG hoặc state machine.

## Cách hiểu bằng lời của tôi

Orchestrator là nơi giữ "ai chạy trước, ai chờ ai, retry thế nào, state hiện tại là gì". Nó đặc biệt hữu ích khi pipeline có nhiều job dữ liệu/ML, backfill lớn, conditional branch, subworkflow, hoặc trigger theo lịch và theo event.

## Thành phần thường gặp

- Workflow definition: DAG, step, dependency, parameter, condition.
- Scheduler: trigger theo cron/interval, thường cần at-least-once và dedup.
- Signal/event service: trigger hoặc mở gate cho step khi upstream data sẵn sàng.
- State store: lưu workflow instance, step instance, version và trạng thái.
- Queue: decouple engine, worker và service để scale ngang.
- UI/observability: timeline, lineage, rollup, aggregated view.

## Pattern scale từ nguồn Maestro

- Stateless service giúp scale bằng cách thêm instance.
- Distributed queue hấp thụ traffic spike và tách tốc độ giữa các component.
- Strongly consistent database giữ workflow state đáng tin cậy.
- Foreach/nested foreach tránh phải materialize thủ công hàng trăm nghìn step trong definition.
- Event publishing cho downstream system, monitoring và notification biết state transition.

## Liên kết

- [[API Orchestration]]
- [[Message Broker]]
- [[Distributed Systems]]
- [[Strong Consistency]]
- [[Horizontal Scaling]]
- [[Observability]]
