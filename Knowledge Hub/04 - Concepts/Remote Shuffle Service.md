---
type: concept
status: seed
sources:
  - "[[2025-10-07_how-pinterest-runs-spark-at-scale-with-moka]]"
source_sections:
  - "[[2025-10-07_how-pinterest-runs-spark-at-scale-with-moka]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - spark
---

# Remote Shuffle Service

## Định nghĩa

[[Remote Shuffle Service]] tách dữ liệu shuffle của Spark khỏi vòng đời compute node/executor để giảm contention, timeout và phụ thuộc vào local disk.

## Cách hiểu bằng lời của tôi

Shuffle là đoạn "đổi chỗ dữ liệu" giữa các stage Spark, thường rất nặng I/O. Nếu shuffle nằm chặt trên executor, autoscaling hoặc node cleanup dễ làm mất trạng thái hoặc nghẽn disk. Remote shuffle biến shuffle thành service riêng, giúp compute co giãn linh hoạt hơn.

## Tác dụng trong Moka

- Giảm disk contention so với external shuffle service cũ.
- Hỗ trợ dynamic executor scaling vì shuffle data không chết theo executor.
- Cải thiện độ ổn định và tốc độ trung bình của job.

## Liên kết

- [[Spark on Kubernetes Platform]]
- [[Kubernetes Autoscaling]]
- [[Data Pipeline Validation]]
- [[Cost Optimization]]
