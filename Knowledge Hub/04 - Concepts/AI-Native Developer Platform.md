---
type: concept
status: understood
sources:
  - "[[2026-08-12_github-vs-vercel-vs-replit-what-dev-platforms-do-when-ai-cod]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - devops
  - platform
  - ai-agent
  - cloud
---

# AI-Native Developer Platform

## Định nghĩa

AI-Native Developer Platform (Nền tảng phát triển phần mềm nguyên bản cho AI) là thế hệ nền tảng điện toán đám mây và môi trường lập trình được thiết kế lại từ đầu để cho phép các AI Agent tự động viết code, tạo nhánh, kích hoạt build, triển khai hạ tầng ephemeral và chạy các bộ test độc lập mà không cần thao tác thủ công từ lập trình viên con người.

## Sự dịch chuyển mô hình

```text
Truyền thống: Human Dev -> IDE -> Git Push -> CI/CD Pipeline -> Cloud Deployment
AI-Native:   Human Prompt -> Agent Orchestrator -> Instant Sandbox/CDE -> Auto Preview -> One-Click Deploy
```

- **Cloud Development Environments (CDE)**: Môi trường dev dựa trên container/microVM tạm thời có tốc độ khởi tạo tính bằng giây (như Replit Agent hay Vercel Sandboxes).
- **Agent Permission & Isolation Boundary**: Định nghĩa chính sách phân quyền nghiêm ngặt để Agent có thể chạy command, cài đặt package và sửa code trong Sandbox an toàn mà không nguy hại tới tài nguyên sản xuất.
- **Autonomous CI/CD & Preview URLs**: Mỗi PR do Agent sinh ra được tự động gắn với một Preview Environment có sẵn database seed để Agent tự test lại giao diện và API.

## Trade-off

- **Chi phí điện toán**: Việc tạo hàng nghìn container sandbox ngắn hạn cho các agent chạy thử nghiệm tốn chi phí hạ tầng lớn.
- **Security & Supply Chain Risks**: Cần kiểm soát chặt chẽ các package do AI agent tự ý cài đặt từ internet.

## Liên kết

- [[Coding Agent]]
- [[Sandboxed Agent Execution]]
- [[Developer Velocity]]
- [[Deployment Pipeline]]
