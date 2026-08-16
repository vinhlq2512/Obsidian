---
type: concept
status: seed
sources:
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
source_sections:
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - data
---

# Rollup Pipeline

## Định nghĩa

[[Rollup Pipeline]] là pipeline gom nhiều event chi tiết thành các aggregate nhỏ hơn để query nhanh, giảm storage/read cost và giữ lại khả năng tính lại từ dữ liệu gốc khi cần.

## Cách hiểu bằng lời của tôi

Raw event là nguồn sự thật nhưng đọc trực tiếp rất đắt. Rollup tạo checkpoint: thay vì mỗi lần đọc phải scan toàn bộ event, hệ thống chỉ đọc aggregate đã tính đến một timestamp, rồi xử lý phần delta còn lại nếu cần.

## Cơ chế

```text
raw events
-> bucket theo time/counter key
-> rollup event báo counter cần aggregate
-> batch worker đọc event mới từ last_rollup_timestamp
-> ghi aggregate vào durable store
-> cache aggregate nóng để đọc nhanh
```

## Pattern từ nguồn Netflix

- Rollup event nhẹ chỉ báo "counter này cần xử lý", không mang toàn bộ raw data.
- Counter cùng key được route ổn định vào queue để giảm duplicate work.
- Nhiều event cho cùng counter được consolidate trong một window.
- Batch size thay đổi theo load và cardinality để tránh làm quá tải datastore.
- Low-cardinality counter có thể được rollup liên tục; high-cardinality counter cần chính sách re-queue tiết kiệm hơn.

## Trade-off

- Count/read nhanh hơn nhưng có độ trễ hội tụ.
- Nếu worker crash, một số signal rollup có thể mất; hệ thống cần operation sau đó kích hoạt rollup lại.
- Cần chọn window bất biến để tránh aggregate trên dữ liệu còn thay đổi.

## Liên kết

- [[Distributed Counter]]
- [[Event Log]]
- [[Backpressure]]
- [[Caching Strategy]]
- [[Eventual Consistency]]
