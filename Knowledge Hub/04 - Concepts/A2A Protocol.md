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
---

# A2A Protocol

## Định nghĩa

A2A (Agent-to-Agent Protocol) là giao thức mở cho phép các AI Agent độc lập giao tiếp và tương tác trực tiếp với nhau thông qua mạng IP để phân rã nhiệm vụ, trao đổi dữ liệu và hoàn thành công việc phức tạp theo mô hình phân tán.

## Cơ chế hoạt động

```text
Orchestrator Agent
-> Discover Peer Agent Capabilities via A2A Manifest (`/.well-known/agent.json`)
-> Authenticate & Establish Session Token
-> Send Task Payload (Async Webhook / Streaming Connection)
-> Peer Agent Executes Subtask & Returns Status Update / Checkpoint
```

- **Agent Manifest**: Mọi agent hỗ trợ A2A đều expose file cấu hình định nghĩa tên, mục tiêu, các action hỗ trợ và định dạng input/output.
- **Async Execution**: Giao tiếp giữa các agent là phi đồng bộ vì thời gian thực thi của từng agent có thể kéo dài vài giây đến vài phút.

## So sánh A2A và MCP

- [[Model Context Protocol|MCP]]: Client-Server pattern để nạp tool/resource vào context của một LLM đơn lẻ.
- **A2A Protocol**: Peer-to-Peer hoặc Orchestrator-Worker pattern để điều phối nhiều agent hoàn chỉnh làm việc độc lập.

## Liên kết

- [[Agent Communication Protocol]]
- [[Model Context Protocol]]
- [[Multi-Agent System]]
- [[Agent Protocol Interoperability]]
