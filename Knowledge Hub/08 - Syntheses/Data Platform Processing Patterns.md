---
type: synthesis
status: seed
concepts:
  - "[[Batch Processing]]"
  - "[[Micro-Batch Processing]]"
  - "[[Stream Processing]]"
  - "[[Change Data Capture]]"
  - "[[Snapshot Bootstrap]]"
  - "[[Data Pipeline Validation]]"
  - "[[Spark on Kubernetes Platform]]"
  - "[[Data Platform as Code]]"
sources:
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
  - "[[2026-07-09_streaming-vs-batch-two-philosophies-of-data-processing]]"
  - "[[2025-10-07_how-pinterest-runs-spark-at-scale-with-moka]]"
  - "[[2025-11-11_how-spotify-built-its-data-platform-to-understand-1-4-trilli]]"
  - "[[2026-04-25_ep212-data-warehouse-vs-data-lake-vs-data-mesh]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - data-engineering
  - system-design
---

# Data Platform Processing Patterns

## Luận điểm chính

Data platform tốt không chỉ là chỗ chạy job. Nó là hệ thống biến dữ liệu thô thành dữ liệu đáng tin bằng bốn quyết định lặp lại: đợi bao lâu để coi dữ liệu là đủ, bootstrap trạng thái ban đầu thế nào, kiểm chứng output ra sao, và ai sở hữu dataset sau khi pipeline chạy.

## Các pattern nối với nhau

- [[Batch Processing]] phù hợp khi dữ liệu có boundary rõ và correctness quan trọng hơn freshness.
- [[Micro-Batch Processing]] là mặc định thực dụng khi cần gần real-time nhưng không cần phản ứng từng event.
- [[Stream Processing]] cần thêm [[Data Processing Window]], [[Watermark]] và chính sách [[Late Data]] vì stream không tự kết thúc.
- [[Change Data Capture]] biến write log thành nguồn incremental, nhưng cần [[Snapshot Bootstrap]] để không mất khoảng dữ liệu ban đầu.
- [[Data Pipeline Validation]] là lớp niềm tin: so record count/checksum/cell-level hoặc chạy dry-run độc lập trước migration.
- [[Spark on Kubernetes Platform]] cho thấy batch platform hiện đại cần operator, scheduler, remote shuffle và observability chứ không chỉ container.
- [[Data Platform as Code]] và [[Data Mesh]] giúp ownership scale khi số pipeline/dataset vượt khả năng của một team trung tâm.

## Mental model

```text
raw events / production DB
-> collection hoặc CDC
-> batch, micro-batch hoặc stream processing
-> validation và freshness check
-> warehouse/lake/domain data product
-> analytics, ML, reporting, incident response
```

## Trade-off cần nhớ

- Full sync dễ hiểu nhưng chi phí tăng theo kích thước bảng.
- CDC giảm chi phí và latency nhưng thêm complexity về offset, merge, replay và validation.
- Streaming nhanh hơn nhưng correctness phụ thuộc window, watermark, late-data policy và idempotent side effects.
- Data mesh tăng ownership nhưng chỉ hiệu quả khi có platform self-service và chuẩn chung.

## Liên kết

- [[Data Warehouse]]
- [[Data Lake]]
- [[Data Mesh]]
- [[Data Freshness]]
- [[Workflow Orchestration]]
- [[Cost Optimization]]
