---
type: synthesis
status: seed
concepts:
  - "[[Object Storage]]"
  - "[[Amazon S3]]"
  - "[[Object Metadata Index]]"
  - "[[Storage Class Tiering]]"
  - "[[Multipart Upload]]"
  - "[[Distributed Key-Value Store]]"
  - "[[Derived Data Store]]"
  - "[[Data Lifecycle Management]]"
sources:
  - "[[2025-02-25_how-amazon-s3-stores-350-trillion-objects-with-11-nines-of-d]]"
  - "[[2025-02-19_how-canva-optimized-230-petabytes-of-data-and-saved-3-6-mill-byte-sized-design]]"
  - "[[2025-01-07_how-airbnb-built-a-key-value-store-for-petabytes-of-data]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage-byte-sized-design]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - storage
  - system-design
  - bytebytego
---

# Object and Key-Value Storage Patterns

## Ý chính

Storage ở quy mô lớn thường tách thành hai câu hỏi: dữ liệu vật lý nằm ở đâu và metadata/key được tìm như thế nào. [[Object Storage]] tối ưu cho file/object lớn qua API; [[Distributed Key-Value Store]] tối ưu cho lookup theo key với latency thấp. Cả hai đều sống chết bởi partitioning, replication, lifecycle và fallback.

## Hai kiểu storage cần phân biệt

| Pattern | Mental model | Điểm mạnh | Cẩn thận |
|---|---|---|---|
| [[Object Storage]] | Bucket/key -> object bytes | Ảnh, video, backup, dataset, archive | Metadata index, hot prefix, lifecycle cost |
| [[Distributed Key-Value Store]] | Key -> value/read model | Low-latency lookup, derived data, config | Source-of-truth, replication lag, blast radius |

## Bài học từ các case

- [[Amazon S3]] cho thấy object storage không scale bằng một storage engine duy nhất, mà bằng front-end routing, metadata index, data placement, replication, erasure coding và background repair.
- Canva cho thấy chi phí storage phải được tối ưu bằng access-pattern measurement trước khi chuyển class.
- Airbnb Mussel cho thấy derived data store cần kết hợp batch bulk load, realtime log và partition management để phục vụ read-heavy workloads.
- Cloudflare KV cho thấy cache/hot data không thay thế được fallback cho cold reads nếu storage phụ thuộc nằm trên critical path.

## Câu hỏi thiết kế

- Workload là object lớn, key-value lookup, hay database transaction?
- Key/prefix có tạo hot partition không?
- Metadata/index có replicate và repair độc lập không?
- Cold read/write phụ thuộc vào source-of-truth nào?
- Data cũ có thể chuyển storage class hoặc expire không?
- Khi storage backend chết, service fail open, fail closed hay degrade một phần?

## Liên kết

- [[Object Storage]]
- [[Distributed Key-Value Store]]
- [[Data Replication]]
- [[Database Sharding]]
- [[High Availability]]
- [[Graceful Degradation]]
