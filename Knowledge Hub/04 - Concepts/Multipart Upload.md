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
  - performance
---

# Multipart Upload

## Định nghĩa

[[Multipart Upload]] là kỹ thuật chia một file/object lớn thành nhiều part để upload song song hoặc retry từng phần, sau đó server ghép lại thành object hoàn chỉnh.

## Cách hiểu bằng lời của tôi

Upload file lớn thất bại ở 99% mà phải làm lại từ đầu là rất tốn. Multipart upload biến một object lớn thành nhiều đơn vị nhỏ hơn: tăng parallelism, giảm ảnh hưởng timeout, và retry được part lỗi thay vì toàn bộ file.

## Khi hữu ích

- File/video/archive lớn.
- Mạng không ổn định hoặc latency cao.
- Cần tận dụng nhiều connection để tăng throughput.
- Client cần resume/retry hiệu quả.

## Cẩn thận

- Cần cleanup incomplete upload để tránh rác storage.
- Cần checksum/ETag để đảm bảo integrity.
- Part size quá nhỏ làm tăng overhead; quá lớn làm retry tốn.
- Nếu object cần encryption/versioning, metadata phải nhất quán khi complete.

## Liên kết

- [[Amazon S3]]
- [[Object Storage]]
- [[Write Path]]
- [[Retry Pattern]]
- [[Latency]]
