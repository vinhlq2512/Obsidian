---
type: concept
status: seed
sources:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
source_sections:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - debugging
---

# Automated Root Cause Analysis

## Định nghĩa

[[Automated Root Cause Analysis]] là hệ thống tự động gom tín hiệu, correlate triệu chứng với thay đổi/dependency, và xuất ra giả thuyết root cause có bằng chứng cho engineer kiểm tra.

## Cách hiểu bằng lời của tôi

Tự động RCA không thay thế judgement. Nó rút ngắn đoạn tốn sức nhất: mở nhiều dashboard, tìm baseline, nhớ dependency, hỏi đúng team và nối các dấu hiệu rời rạc thành một hướng điều tra.

## Pattern từ source

- Meta DrP chạy analyzer khi alert bắn và chain qua analyzer của dependency.
- Databricks agent đọc metrics/logs/config và cho phép hỏi tiếp bằng ngôn ngữ tự nhiên.
- Cả hai đều cần output có cấu trúc để người trực có thể review nhanh.

## Liên kết

- [[Root Cause Analysis]]
- [[Debugging as Code]]
- [[Analyzer Chaining]]
- [[Diagnostic Agent]]
- [[Incident Response]]
- [[Distributed Tracing]]
