---
type: concept
status: seed
sources:
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
  - "[[2025-10-07_how-pinterest-runs-spark-at-scale-with-moka]]"
source_sections:
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
  - "[[2025-10-07_how-pinterest-runs-spark-at-scale-with-moka]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - reliability
---

# Data Pipeline Validation

## Định nghĩa

[[Data Pipeline Validation]] là lớp kiểm tra để chứng minh pipeline dữ liệu tạo output đúng, đủ và tương thích với expectation của downstream.

## Cách hiểu bằng lời của tôi

Pipeline dữ liệu có thể "xanh" nhưng vẫn sai: thiếu một loại update, parse sai schema, mất một partition hoặc lệch checksum. Vì vậy validation phải kiểm tra dữ liệu, không chỉ kiểm tra job có chạy xong hay không.

## Pattern từ source

- Figma dựng một bootstrap độc lập vào schema tạm rồi so sánh cell-by-cell với bảng gốc đã căn cùng thời điểm bằng CDC.
- Pinterest chạy dry-run song song Hadoop và Moka, đổi output path sang bucket test, rồi so file size, record count và checksum trước khi migration.
- Điểm chung: validation càng độc lập với production path thì càng bắt được lỗi production path không tự phát hiện.

## Khi áp dụng

- Migration platform hoặc runtime cho nhiều job dữ liệu.
- CDC/warehouse pipeline phục vụ KPI hoặc quyết định kinh doanh.
- Re-bootstrap khi schema thay đổi hoặc cần rebuild dữ liệu lịch sử.

## Liên kết

- [[Shadow Testing]]
- [[Data Contract]]
- [[Data Freshness]]
- [[Snapshot Bootstrap]]
- [[Workflow Orchestration]]
- [[Zero-Downtime Infrastructure Migration]]
