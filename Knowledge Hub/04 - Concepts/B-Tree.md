---
type: concept
status: developing
sources:
  - "[[2026-04-23_b-trees-vs-lsm-trees-comparison-and-trade-offs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - storage
---

# B-Tree

## Định nghĩa

B-Tree là cấu trúc index/storage giữ key được sắp xếp trong các page trên disk, giúp lookup và range query nhanh, đổi lại write phải trả chi phí duy trì thứ tự.

## Cách hiểu bằng lời của tôi

B-Tree trả tiền tổ chức dữ liệu ngay khi write. Vì dữ liệu luôn được giữ gần đúng chỗ, read sau này nhanh và dự đoán được.

## B+ Tree

Trong database, "B-Tree" thường là B+ Tree:

- internal nodes giữ key/pointer;
- data thật nằm ở leaf;
- leaf nodes nối với nhau để range scan tuần tự.

## Trade-off

- Tốt cho read-heavy hoặc mixed OLTP workload.
- Range query mạnh vì key sorted và leaf linked.
- Write có random I/O, page split và update parent.
- Write amplification thường thấp hơn LSM nhưng mỗi write có latency cao hơn.

## Liên kết

- [[Database Indexing]]
- [[Storage Engine]]
- [[LSM Tree]]
- [[Write Amplification]]
- [[Read Amplification]]
