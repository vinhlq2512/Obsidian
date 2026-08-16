---
type: concept
status: seed
sources:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
source_sections:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - ranking
---

# Prediction Serving Fanout

## Định nghĩa

[[Prediction Serving Fanout]] là hiện tượng một user request mở rộng thành hàng trăm hoặc hàng nghìn model evaluations cho nhiều candidate trước khi trả về danh sách ngắn.

## Cách hiểu bằng lời của tôi

Ranking workload bất đối xứng: một request vào, rất nhiều cặp user-candidate cần score, rồi chỉ vài item ra. Vì vậy latency budget bị chi phối bởi retrieval, feature lookup, batching, serialization và inference parallelism chứ không chỉ model latency đơn lẻ.

## Liên kết

- [[Recommendation Funnel]]
- [[Feature Collocation]]
- [[AI Model Serving]]
- [[Reranking]]
- [[Latency]]
