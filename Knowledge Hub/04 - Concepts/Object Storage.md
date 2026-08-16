---
type: concept
status: seed
sources:
  - "[[2025-02-25_how-amazon-s3-stores-350-trillion-objects-with-11-nines-of-d]]"
  - "[[2025-02-19_how-canva-optimized-230-petabytes-of-data-and-saved-3-6-mill-byte-sized-design]]"
source_sections:
  - "[[2025-02-25_how-amazon-s3-stores-350-trillion-objects-with-11-nines-of-d]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - storage
  - system-design
---

# Object Storage

## Định nghĩa

[[Object Storage]] là mô hình lưu trữ dữ liệu dưới dạng object độc lập, mỗi object có key/id, metadata và nội dung bytes, thường được truy cập qua API thay vì mount như block/file system truyền thống.

## Cách hiểu bằng lời của tôi

Object storage hợp với dữ liệu lớn, nhiều file, ít cần update từng byte tại chỗ: ảnh, video, backup, log, dataset, static asset. Hệ thống scale bằng cách tách metadata/index khỏi data placement, rồi phân phối object qua nhiều node/zone để đạt durability và throughput cao.

## Cơ chế chính

```text
client
-> API request theo bucket/key
-> auth + routing
-> metadata index tìm vị trí object
-> storage layer đọc/ghi fragment
-> replication/erasure coding bảo vệ dữ liệu
```

## Trade-off

- Tối ưu cho put/get object hơn là transaction nhỏ kiểu database.
- Metadata/index trở thành lớp cực kỳ quan trọng cho latency và scale.
- Key naming có thể tạo hotspot nếu prefix phân phối kém.
- Chi phí phụ thuộc access pattern, storage class, request volume và retrieval cost.

## Liên kết

- [[Amazon S3]]
- [[Object Metadata Index]]
- [[Storage Class Tiering]]
- [[Multipart Upload]]
- [[Data Replication]]
- [[Data Lifecycle Management]]
