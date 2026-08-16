---
type: concept
status: understood
sources:
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
source_sections:
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - security
---

# Zero-Secret Agent Architecture

## Định nghĩa

Zero-Secret Agent Architecture là thiết kế trong đó agent không bao giờ có quyền đọc trực tiếp secret, token hoặc credential; quyền đó nằm ở proxy/gateway/container tin cậy khác.

## Cách hiểu bằng lời của tôi

Không nên bảo agent "đừng đọc secret"; phải thiết kế để secret không nằm trong tầm với. GitHub đưa token vào MCP gateway/API proxy thay vì container agent. Agent chỉ gọi interface được kiểm soát, còn secret ở trust boundary khác.

## Liên kết

- [[Sandboxed Agent Execution]]
- [[Least Privilege]]
- [[Prompt Injection]]
- [[Model Context Protocol]]
- [[Agent Trust Boundary Logging]]
