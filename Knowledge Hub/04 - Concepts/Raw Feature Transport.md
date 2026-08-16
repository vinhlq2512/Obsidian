---
type: concept
status: seed
sources:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
source_sections:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - performance
---

# Raw Feature Transport

## Định nghĩa

[[Raw Feature Transport]] là cách truyền feature qua data plane dưới dạng bytes/raw representation và trì hoãn deserialize đến inference engine để giảm overhead.

## Cách hiểu bằng lời của tôi

Ở scale lớn, latency không chỉ nằm trong model. Snap phát hiện serialization/deserialization feature chiếm phần đáng kể, nên đổi API để feature đi dưới dạng raw bytes và chỉ deserialize bên trong inference engine. Đây là tối ưu "boring plumbing" nhưng có tác động rất lớn.

## Liên kết

- [[AI Model Serving]]
- [[Prediction Serving Fanout]]
- [[Latency]]
- [[Cost Optimization]]
- [[API Protocol]]
