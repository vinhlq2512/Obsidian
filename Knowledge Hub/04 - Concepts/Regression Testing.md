---
type: concept
status: seed
sources:
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
source_sections:
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - testing
---

# Regression Testing

## Định nghĩa

[[Regression Testing]] là kiểm thử để đảm bảo thay đổi mới không làm hỏng hành vi đã từng đúng.

## Cách hiểu bằng lời của tôi

Regression test đặc biệt quan trọng cho platform vì thay đổi hạ tầng có thể làm hỏng nhiều model/service mà team platform không hiểu hết business logic. Với ML serving, model self-test là một dạng regression test gắn với model artifact; với diagnostic agent, production state replay cũng là regression test bằng incident cũ.

## Liên kết

- [[Model Self-Test]]
- [[Production State Replay]]
- [[Behavioral Compatibility]]
- [[Deployment Pipeline]]
