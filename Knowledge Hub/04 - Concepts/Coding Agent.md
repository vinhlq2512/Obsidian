---
type: concept
status: developing
sources:
  - "[[2026-03-18_how-openai-codex-works]]"
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
  - "[[2025-07-29_how-cursor-serves-billions-of-ai-code-completions-every-day]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - agent
  - coding
  - llm
---

# Coding Agent

## Định nghĩa

Coding agent là LLM agent chuyên làm việc trên codebase: đọc file, tìm kiếm, sửa code, chạy command/test/linter và lặp lại cho tới khi có kết quả kiểm chứng được.

## Cách hiểu bằng lời của tôi

Coding agent không phải autocomplete dài hơn. Nó là một hệ thống có model, [[Agent Harness]], tool, sandbox, context retrieval và verification loop. Giá trị nằm ở khả năng inspect -> edit -> test -> sửa tiếp.

## Thành phần quan trọng

- Agentic coding model học từ trajectory tool use, không chỉ text completion.
- Codebase indexing hoặc retrieval kéo đúng file/snippet vào context.
- Tool harness cung cấp search/read/write/apply patch/terminal.
- Sandbox giới hạn filesystem, network và command nguy hiểm.
- Verification chạy test, lint, typecheck hoặc build.

## Failure modes

- Diff problem: model tạo patch sai format, sai line hoặc apply nhầm.
- Latency compounds: mỗi vòng search/edit/test thêm vài giây, tổng task dễ chậm.
- Context bloat: log, stack trace và file content cũ làm prompt nhiễu.
- Trust break: một edit nguy hiểm có thể làm user ngừng dùng agent.

## Liên kết

- [[LLM Agent]]
- [[Agent Harness]]
- [[Agentic Loop]]
- [[Tool Use]]
- [[Context Engineering]]
- [[LLM Evaluation]]
- [[LLM Security]]
