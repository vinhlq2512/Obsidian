---
type: synthesis
status: seed
concepts:
  - "[[Debugging as Code]]"
  - "[[Runbook Automation]]"
  - "[[Automated Root Cause Analysis]]"
  - "[[Analyzer Chaining]]"
  - "[[Diagnostic Agent]]"
  - "[[Production State Replay]]"
sources:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - reliability
  - debugging
---

# Debugging and Incident Intelligence Patterns

## Luận điểm chính

Debugging ở tổ chức lớn nên được xem như product/platform, không chỉ là kỹ năng cá nhân. Khi tri thức điều tra được codify thành analyzer, agent hoặc workflow có test, tổ chức giảm thời gian gom ngữ cảnh và giữ được expertise khi người đổi team.

## Pattern chính

- [[Debugging as Code]] biến investigation workflow thành code có review, backtest và CI/CD.
- [[Analyzer Chaining]] cho phép RCA đi qua dependency boundary thay vì dừng ở service báo triệu chứng.
- [[Runbook Automation]] tự động hóa các bước lấy dashboard/log/config lặp lại.
- [[Diagnostic Agent]] thêm interface ngôn ngữ tự nhiên nhưng vẫn cần tool, quyền hạn và validation rõ.
- [[Production State Replay]] dùng snapshot incident thật để regression-test agent/debugging workflow.

## Mental model

```text
alert hoặc câu hỏi
-> context gathering
-> analyzer/agent gọi tool
-> correlate metric, log, deploy, config, dependency
-> structured finding
-> engineer review mitigation
-> postmortem/action item
```

## Trade-off

- Giảm MTTR nhưng tạo code/workflow phải maintain.
- Automation tốt nhất nên đưa bằng chứng và khuyến nghị, không tự động làm action nguy hiểm khi chưa có approval.
- AI agent hữu ích khi tool/context đã được thống nhất; nếu dữ liệu phân mảnh và quyền hạn mơ hồ, agent chỉ làm confusion nhanh hơn.

## Liên kết

- [[Incident Response]]
- [[Root Cause Analysis]]
- [[Observability]]
- [[Distributed Tracing]]
- [[Agent Evaluation Stack]]
