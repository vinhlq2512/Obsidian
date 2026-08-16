---
type: concept
status: seed
sources:
  - "[[2026-08-13_a-detailed-guide-to-api-composition-techniques]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - workflow
---

# API Orchestration

## Định nghĩa

API orchestration là dạng composition trong đó các call phụ thuộc lẫn nhau và phải chạy theo chuỗi hoặc theo workflow có thứ tự.

## Cách hiểu bằng lời của tôi

Orchestration xuất hiện khi call sau cần output của call trước, ví dụ order -> customer id -> address. Latency lúc này cộng dồn theo chain, và mỗi bước là một điểm có thể làm cả workflow dừng.

## Trade-off

- Dễ biểu diễn flow nghiệp vụ có dependency thật.
- Chậm hơn fan-out song song nếu dependency không cần thiết.
- Cần timeout, retry và error handling theo từng bước.
- Nếu orchestration nằm ở layer sai, nó dễ kéo business rule khỏi service sở hữu domain.

## Liên kết

- [[API Composition]]
- [[API Aggregation]]
- [[Timeout]]
- [[Retry Pattern]]
- [[API Contract]]
