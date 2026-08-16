---
type: concept
status: understood
sources:
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
source_sections:
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - observability
---

# Data Freshness

## Định nghĩa

Data Freshness đo việc dữ liệu trong bảng hoặc pipeline có được cập nhật đúng hạn so với SLA/SLO của downstream consumer hay không.

## Cách hiểu bằng lời của tôi

Dữ liệu đúng nhưng đến trễ vẫn có thể vô dụng. Trong financial pipeline, freshness là tín hiệu vận hành quan trọng ngang với correctness vì reconciliation, ledger và planning đều phụ thuộc vào lịch cập nhật.

Ở Figma, freshness là lý do kiến trúc chuyển từ full sync nhiều ngày sang CDC gần real-time. Dữ liệu warehouse không chỉ cần đúng ở cuối ngày; nó phải đủ mới để analytics, incident response và quyết định sản phẩm không nhìn vào ảnh chụp đã cũ.

## Cơ chế kiểm soát

- Theo dõi timestamp cập nhật của bảng hoặc partition.
- Alert khi dữ liệu trễ hơn ngưỡng đã cam kết.
- Kết hợp với data quality check để phân biệt "chưa có data", "data đến trễ" và "data đến nhưng sai".
- Đo lag giữa source write, event stream, merge job và bảng/query downstream.

## Liên kết

- [[Financial Source of Truth]]
- [[Service Level Objective]]
- [[Observability]]
- [[Alerting]]
- [[Data Contract]]
- [[Change Data Capture]]
- [[Data Pipeline Validation]]
