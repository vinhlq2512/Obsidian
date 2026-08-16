---
type: concept
status: seed
sources:
  - "[[2026-04-25_ep212-data-warehouse-vs-data-lake-vs-data-mesh]]"
source_sections:
  - "[[2026-04-25_ep212-data-warehouse-vs-data-lake-vs-data-mesh]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
---

# Data Lake

## Định nghĩa

[[Data Lake]] lưu nhiều loại dữ liệu ở dạng thô hoặc gần thô, như database dumps, logs, ảnh, video và event data, để xử lý khi có nhu cầu.

## Cách hiểu bằng lời của tôi

Data lake ưu tiên flexibility. Nó tốt cho machine learning và khám phá dữ liệu, nhưng nếu thiếu naming, format, ownership và documentation thì rất dễ biến thành kho dữ liệu trùng lặp, cũ và không ai tin.

## Trade-off

- Mạnh: giữ được nhiều loại dữ liệu chưa biết trước cách dùng.
- Mạnh: phù hợp workload ML hoặc backfill lớn.
- Yếu: cần governance mạnh để tránh data swamp.
- Yếu: người dùng downstream phải hiểu schema/chất lượng trước khi dùng.

## Liên kết

- [[Object Storage]]
- [[Data Warehouse]]
- [[Data Mesh]]
- [[Data Contract]]
- [[Data Lifecycle Management]]
