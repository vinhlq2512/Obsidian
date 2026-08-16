---
type: concept
status: understood
sources:
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
source_sections:
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - security
---

# Sandboxed Agent Execution

## Định nghĩa

Sandboxed Agent Execution là việc chạy command, build, test, script hoặc tool call của agent trong môi trường isolated, giới hạn network, filesystem và tài nguyên.

## Cách hiểu bằng lời của tôi

Coding agent phải chạy code để verify, nhưng không thể được tin như developer local. Sandbox là ranh giới an toàn: agent vẫn có thể thử build/test, nhưng destructive command, secret access hoặc network exfiltration bị chặn hoặc cần approval.

## Bài học từ source

- Cursor xem sandbox như serving infrastructure: cần scheduler, fast provisioning và recycling.
- GitHub dùng nhiều container, firewall, MCP gateway và proxy để agent không trực tiếp chạm secret hoặc network tùy ý.

## Liên kết

- [[Coding Agent]]
- [[Control Groups]]
- [[Linux Namespace]]
- [[Zero-Secret Agent Architecture]]
- [[Least Privilege]]
