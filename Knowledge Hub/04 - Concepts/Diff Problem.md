---
type: concept
status: understood
sources:
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
source_sections:
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - coding-agent
  - ai-engineering
---

# Diff Problem

## Định nghĩa

Diff Problem là khó khăn của coding agent khi phải sửa file hiện có bằng patch/diff chính xác: đúng vị trí, đúng indentation, đúng format và không làm hỏng phần không liên quan.

## Cách hiểu bằng lời của tôi

Viết code mới dễ hơn chỉnh code thật. Một patch sai line number hoặc format có thể không apply; tệ hơn là apply nhầm và làm hỏng repo. Vì vậy coding agent cần học edit trajectory và dùng tool edit an toàn, không chỉ generate text.

## Cách giảm rủi ro

- Train trên cặp original code, edit command, final code.
- Dùng structured edit tool thay vì raw prose.
- Verify bằng build/test/lint sau mỗi thay đổi đáng kể.
- Giữ context code liên quan đủ chính xác trước khi edit.

## Liên kết

- [[Coding Agent]]
- [[Agent Harness]]
- testing
- [[Deployment Pipeline]]
