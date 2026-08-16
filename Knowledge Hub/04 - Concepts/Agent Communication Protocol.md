---
type: concept
status: understood
sources:
  - "[[2026-07-18_mcp-vs-a2a-vs-acp-how-ai-agents-actually-talk-to-each-other]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - agent
  - protocol
  - interop
---

# Agent Communication Protocol

## Định nghĩa

Agent Communication Protocol (Giao thức giao tiếp giữa các AI Agent) là chuẩn giao tiếp có cấu trúc mở định nghĩa cách thức các agent tự động phát hiện (discovery), ủy quyền nhiệm vụ (task delegation), chia sẻ ngữ cảnh (context sharing) và đàm phán kết quả với nhau mà không phụ thuộc vào framework phát triển bên dưới.

## Phân loại các chuẩn giao thức

```text
+-------------------------------------------------------------+
|                Agent Communication Spectrum                 |
+------------------------------+------------------------------+
| Host-to-Tool / Local Context | Inter-Agent Task Delegation  |
|          ([[Model Context Protocol|MCP]])           |     ([[A2A Protocol|A2A]] / ACP)            |
+------------------------------+------------------------------+
```

1. **MCP (Model Context Protocol)**: Tập trung vào mối quan hệ **Host-to-Tool** (kết nối agent với các file system, database, API cụ thể trong một context cục bộ).
2. **A2A / ACP (Agent-to-Agent Protocol)**: Tập trung vào mối quan hệ **Agent-to-Agent** (kết nối các độc lập agent qua mạng IP, giao việc giữa Planner Agent và Sub-agent).

## Lợi ích cốt lõi

- **Interoperability**: Cho phép một agent phát triển bằng Python (LangGraph) gọi và giao việc cho một agent khác phát triển bằng TypeScript hay Go.
- **Dynamic Capabilities Discovery**: Agent tự động truy vấn danh sách capabilities và schema của agent khác ở runtime.
- **Trust & Boundary Enforcement**: Định nghĩa rõ ràng phạm vi phân quyền và token bảo mật khi giao tiếp xuyên tổ chức.

## Liên kết

- [[Model Context Protocol]]
- [[A2A Protocol]]
- [[Multi-Agent System]]
- [[Agent Orchestrator-Worker Pattern]]
- [[Agent Protocol Interoperability]]
