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
  - reliability
---

# Diagnostic Agent

## Định nghĩa

[[Diagnostic Agent]] là AI agent dùng tool để truy vấn metrics, logs, config, schema hoặc trạng thái production nhằm hỗ trợ điều tra sự cố.

## Cách hiểu bằng lời của tôi

Diagnostic agent không chỉ trả lời từ kiến thức chung. Nó phải biết lấy bằng chứng live qua tool, diễn giải tín hiệu trong ngữ cảnh hệ thống, hỏi thêm nếu thiếu dữ liệu và đưa ra hướng xử lý an toàn.

## Kiến trúc từ Databricks

- Router nhận câu hỏi và chuyển đến đúng context/tool.
- LLM quyết định cần gọi tool nào để lấy metric/log/config.
- Tool output quay lại context để agent diễn giải.
- Specialized agents có thể tách theo database, system issue hoặc traffic pattern.
- Validation replay snapshot production để phát hiện regression.

## Liên kết

- [[LLM Agent]]
- [[Agentic Loop]]
- [[Tool Use]]
- [[Production State Replay]]
- [[Agent Evaluation Stack]]
- [[Fine-Grained Authorization]]
