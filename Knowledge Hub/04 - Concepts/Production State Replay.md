---
type: concept
status: seed
sources:
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
source_sections:
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - evaluation
---

# Production State Replay

## Định nghĩa

[[Production State Replay]] là kỹ thuật lưu snapshot của trạng thái production và replay lại qua hệ thống/agent mới để kiểm tra regression trên tình huống thật đã biết.

## Cách hiểu bằng lời của tôi

Với diagnostic agent, test prompt nhân tạo không đủ. Cần đóng băng incident thật: schema, physical info, CPU, IOPS, log, diagnosis kỳ vọng; rồi chạy phiên bản agent mới qua snapshot đó để xem nó còn chẩn đoán đúng không.

## Liên kết

- [[Diagnostic Agent]]
- [[Agent Evaluation Stack]]
- [[LLM-as-Judge]]
- [[Shadow Testing]]
- [[Data Pipeline Validation]]
