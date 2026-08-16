---
type: concept
status: understood
sources:
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
source_sections:
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - data-engineering
  - finance
---

# Financial Source of Truth

## Định nghĩa

Financial Source of Truth là pipeline hoặc data platform trung tâm cung cấp định nghĩa thống nhất cho doanh thu, chi phí, margin, reconciliation, ledger và báo cáo tài chính.

## Cách hiểu bằng lời của tôi

Với dữ liệu tài chính, nhiều pipeline riêng lẻ có vẻ nhanh lúc đầu nhưng dễ tạo ra nhiều "sự thật" khác nhau. [[Financial Source of Truth]] chậm hơn ở governance và change management, nhưng đổi lại tạo niềm tin vì mọi team dùng cùng logic, cùng data quality check và cùng metric definition.

## Cơ chế từ Agoda

- Gom raw data từ booking/payment vào pipeline trung tâm.
- Xử lý bằng distributed execution layer.
- Lưu kết quả trong data lake với validation.
- Downstream như finance, planning, ledger dùng cùng dataset đã kiểm tra.
- Dùng [[Data Freshness]], [[Data Contract]] và [[Shadow Testing]] để giảm rủi ro thay đổi.

## Trade-off

- Centralization tăng consistency và auditability.
- Đổi lại, delivery velocity giảm vì nhiều dependency, nhiều stakeholder và yêu cầu kiểm thử toàn pipeline.

## Liên kết

- [[Data Contract]]
- [[Shadow Testing]]
- [[Data Freshness]]
- [[Data Lifecycle Management]]
- [[Observability]]
