---
type: concept
status: understood
sources:
  - "[[2026-05-09_ep214-claude-code-vs-openclaw-5-design-dimensions]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai
  - coding-agent
  - cli
  - developer-tools
---

# CLI AI Coding Assistants

## Định nghĩa

CLI AI Coding Assistants (Trợ lý lập trình AI trên dòng lệnh Terminal) là các công cụ AI Agent tự chủ tích hợp trực tiếp vào giao diện dòng lệnh (Command Line Interface) của nhà phát triển, có khả năng đọc/viết mã nguồn, thực thi các lệnh shell (build, test, git), tự động debug lỗi và tương tác với các công cụ hệ thống.

## Kiến trúc & 5 Chiều Thiết kế Cốt lõi

```text
User CLI Terminal
-> Agent Loop (Read Files, Execute Shell Commands, Analyze Output)
-> Subagent Delegation & Orchestration
-> Permission Gatekeeper (Human-in-the-Loop Confirmation)
-> Workspace File Updates & Git Commits
```

1. **Context & File Access**: Khả năng tự động quét workspace, phân tích file AST và đọc log lỗi mà không cần người dùng copy-paste thủ công.
2. **Execution & Tool Harness**: Khả năng tự chạy các lệnh terminal (`npm test`, `pytest`, `cargo build`), đọc kết quả stdio và tự động khắc phục lỗi nếu test thất bại.
3. **Subagent Orchestration**: Khả năng ủy quyền nhiệm vụ nghiên cứu hoặc kiểm thử cho các sub-agent chạy nền song song.
4. **Human-in-the-Loop Safety**: Cung cấp cơ chế xác nhận quyền hạn đối với các lệnh có thể gây nguy hiểm (xóa file, push git, gọi API tốn phí).
5. **Memory & State Persistence**: Lưu giữ lịch sử lệnh, thông tin cấu hình và hướng dẫn tùy chỉnh (Skills/Rules).

## So sánh tiêu biểu

- **Claude Code**: Thiết kế tối giản, tập trung vào agentic loop nhanh, tích hợp chặt chẽ với hệ sinh thái Anthropic và các công cụ bash.
- **OpenClaw / Open-Source Assistants**: Khả năng tùy biến mô hình LLM backend cao, mở rộng quy trình tự động hóa linh hoạt.

## Liên kết

- [[Coding Agent]]
- [[Agent Harness]]
- [[Sandboxed Agent Execution]]
- [[AI-Native Developer Platform]]
