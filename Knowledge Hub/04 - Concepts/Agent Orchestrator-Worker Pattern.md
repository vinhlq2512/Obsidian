---
type: concept
status: understood
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
source_sections:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - system-design
---

# Agent Orchestrator-Worker Pattern

## Định nghĩa

Agent Orchestrator-Worker Pattern là kiến trúc trong đó một agent điều phối phân rã nhiệm vụ, tạo subagent, gom kết quả và quyết định vòng lặp tiếp theo.

## Cách hiểu bằng lời của tôi

Trong multi-agent research, lead agent không làm mọi việc. Nó giống coordinator: lập kế hoạch, chia nhánh tìm kiếm, cấp objective cho worker, rồi tổng hợp kết quả. Mỗi worker có context riêng nên hệ thống mở rộng theo chiều rộng tốt hơn single-agent một context window.

## Khi phù hợp

- Nhiệm vụ mở, cần breadth-first exploration.
- Các nhánh có thể chạy song song tương đối độc lập.
- Outcome đủ giá trị để trả chi phí token/tool call cao.

## Không phù hợp

- Tác vụ phụ thuộc chặt từng bước như sửa code trong một vùng thay đổi nhỏ.
- Bài toán đơn giản mà orchestration overhead lớn hơn lợi ích.

## Liên kết

- [[Multi-Agent System]]
- [[Agentic Loop]]
- [[Agent Evaluation]]
- [[Context Engineering]]
