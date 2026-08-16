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
  - aws
---

# Amazon S3

## Định nghĩa

[[Amazon S3]] là managed [[Object Storage]] service của AWS, dùng bucket/key để lưu object, hỗ trợ scale tự động, nhiều storage class, metadata indexing, replication, versioning và access control.

## Cách hiểu bằng lời của tôi

S3 không chỉ là "folder chứa file trên cloud". Nó là một distributed storage system lớn: front-end nhận request, metadata service map key tới vị trí vật lý, storage layer đặt object qua nhiều node/AZ, còn background service audit, repair, rebalance và quản lý lifecycle.

## Write path rút gọn

```text
client/SDK/CLI
-> DNS/routing
-> front-end auth + validation
-> metadata index ghi key/location/permission
-> data placement + encryption
-> replication/erasure coding qua nhiều AZ
-> trả ETag/version
```

## Điểm thiết kế đáng nhớ

- Durability đến từ replication, erasure coding, checksum, background auditor và repair.
- Latency lookup phụ thuộc mạnh vào [[Object Metadata Index]].
- Throughput cao cần tránh hot prefix và dùng partitioning/rebalancing tốt.
- Chi phí dài hạn cần [[Storage Class Tiering]] và lifecycle policy, không chỉ mua thêm dung lượng.

## Liên kết

- [[Object Storage]]
- [[Object Metadata Index]]
- [[Storage Class Tiering]]
- [[Multipart Upload]]
- [[Data Replication]]
- [[High Availability]]
- [[Load Balancer]]
