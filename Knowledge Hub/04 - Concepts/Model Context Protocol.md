---
type: concept
status: developing
sources:
  - "[[2026-05-04_connecting-llms-to-the-real-world-tool-use-function-calling]]"
  - "[[2025-09-30_why-anthropics-mcp-is-a-big-deal]]"
  - "[[2025-10-04_ep183-mcp-vs-api-whats-the-difference]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - agent
  - tool-use
---

# Model Context Protocol

## Định nghĩa

Model Context Protocol là chuẩn kết nối giữa ứng dụng dùng LLM và các nguồn/tool bên ngoài, để model có thể thấy tool metadata, gọi thao tác và nhận kết quả theo một giao thức chung.

## Cách hiểu bằng lời của tôi

MCP giống "cổng cắm tool" cho agent. Nếu không có chuẩn, mỗi app phải tự tích hợp từng tool theo cách riêng. Với MCP, host LLM nói chuyện với nhiều server tool qua cùng một kiểu hợp đồng, nên việc mở rộng bớt thành bài toán ghép adapter.

## Cần biết

- Host là ứng dụng điều phối LLM/agent.
- Client là phần trong host nói chuyện với MCP server.
- Server expose tool, resource hoặc prompt cho host.
- MCP không thay thế API nghiệp vụ; nó là lớp chuẩn hóa cách agent phát hiện và gọi API/tool.
- Tool schema, permission, auth và human approval vẫn phải do hệ thống thiết kế cẩn thận.

## Trade-off

- Giảm chi phí tích hợp khi có nhiều tool và nhiều ứng dụng agent.
- Tăng diện tích tấn công nếu expose tool quá rộng.
- Tool description chiếm context, nên cần chọn đúng tool thay vì nhồi toàn bộ server vào mỗi lượt.
- Debug phức tạp hơn API call trực tiếp vì có thêm lớp host/client/server.

## Liên kết

- [[Tool Use]]
- [[Function Calling]]
- [[LLM Agent]]
- [[Context Engineering]]
