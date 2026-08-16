---
type: concept
status: seed
sources:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
source_sections:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - java
  - performance
---

# Generational Garbage Collection

## Định nghĩa

[[Generational Garbage Collection]] là chiến lược GC tách object theo tuổi, dựa trên quan sát nhiều object trong ứng dụng chỉ sống rất ngắn.

## Cách hiểu bằng lời của tôi

Nếu đa số allocation chết nhanh, GC không nên xử lý mọi object như nhau. Generational GC tập trung dọn vùng object trẻ thường xuyên hơn, còn object sống lâu được đưa sang vùng khác. Trong backend latency-sensitive, mục tiêu không chỉ là throughput mà còn giảm pause spike.

## Từ nguồn Netflix

Netflix dùng G1 trong nhiều dịch vụ JVM, nhưng ở tải cao một số service gặp stop-the-world pause đủ dài để gây IPC timeout và retry. Generational ZGC trong JDK 21 thêm mô hình thế hệ cho ZGC, giúp giảm pause và làm hành vi cluster ổn định hơn dưới concurrency cao.

## Vì sao liên quan reliability

GC pause có thể biểu hiện như dependency chậm hoặc request timeout. Khi caller retry, một vấn đề runtime nội bộ có thể biến thành áp lực hệ thống: tăng traffic, tăng jitter, và làm khó xác định root cause.

## Liên kết

- [[Latency]]
- [[Timeout]]
- [[Retry Storm]]
- [[Runtime Platform Migration]]
- [[Observability]]
