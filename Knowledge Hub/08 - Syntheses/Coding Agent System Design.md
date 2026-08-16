---
type: synthesis
status: developing
concepts:
  - "[[Coding Agent]]"
  - "[[Agent Harness]]"
  - "[[Agentic Loop]]"
  - "[[Context Engineering]]"
  - "[[LLM Security]]"
  - "[[LLM Evaluation]]"
sources:
  - "[[2026-03-18_how-openai-codex-works]]"
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
  - "[[2026-07-29_how-chatgpt-optimizes-its-agent-loop-harness-api-and-inferen]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - coding-agent
  - llm
  - system-design
---

# Coding Agent System Design

## Luồng hệ thống

```text
user task
-> harness builds context
-> model proposes action or answer
-> harness executes tool in sandbox
-> output returns as observation
-> model decides next step
-> verification produces evidence
```

## Ý chính

Coding agent đáng tin không đến từ model đơn lẻ. Nó cần một hệ thống quanh model: context retrieval để đọc đúng code, tool harness để thao tác an toàn, sandbox để chạy command, compaction để tránh context phình, và eval/verification để biết edit có thật sự chạy.

## Ba áp lực production

- Correct edits: diff phải apply đúng, giữ phần không liên quan, không phá format.
- Compounded latency: nhiều vòng search/edit/test làm vài giây nhỏ cộng thành phút.
- Safe execution: test/build cần chạy thật nhưng không được mở quyền terminal vô hạn.

## Bài học thiết kế

- Train/evaluate trên trajectory, không chỉ final answer.
- Tối ưu cost per successful task, không chỉ token latency từng call.
- Giữ prompt prefix ổn định và tool discovery gọn để cache không bị phá.
- Verification là một phần của product loop, không phải bước trang trí cuối.

## Liên kết

- [[Production LLM System Design]]
- [[AI Engineering Systems from RAG to Agents]]
- [[Model Router]]
