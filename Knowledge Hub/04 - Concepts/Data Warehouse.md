---
type: concept
status: seed
sources:
  - "[[2026-04-25_ep212-data-warehouse-vs-data-lake-vs-data-mesh]]"
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
source_sections:
  - "[[2026-04-25_ep212-data-warehouse-vs-data-lake-vs-data-mesh]]"
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
---

# Data Warehouse

## Định nghĩa

[[Data Warehouse]] là kho dữ liệu được tổ chức cho analytics, reporting và truy vấn phức tạp, thường tách khỏi production database để không ảnh hưởng user traffic.

## Cách hiểu bằng lời của tôi

Warehouse là nơi dữ liệu đã được làm sạch, định hình và tối ưu cho câu hỏi kinh doanh. Nó không thay production DB; nó nhận dữ liệu từ pipeline, trade freshness lấy khả năng query lớn và ổn định cho nhiều team.

## Khi phù hợp

- Dashboard/KPI cần schema ổn định.
- Reporting, phân tích ad, finance hoặc product analytics.
- Query lớn không nên chạy trực tiếp trên database phục vụ traffic live.

## Liên kết

- [[Change Data Capture]]
- [[Data Freshness]]
- [[Data Pipeline Validation]]
- [[Data Lake]]
- [[Data Mesh]]
