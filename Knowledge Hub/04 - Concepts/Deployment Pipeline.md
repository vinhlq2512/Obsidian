---
type: concept
status: understood
sources:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
source_sections:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - devops
  - system-design
---

# Deployment Pipeline

## Định nghĩa

Deployment Pipeline là chuỗi bước tự động đưa code từ source control qua build, test, staging, một phần production và full production.

## Cách hiểu bằng lời của tôi

Pipeline là hệ thống kiểm soát rủi ro của release. Mỗi stage phải trả lời một câu hỏi: code build được không, test logic đúng không, dependency ổn không, production metrics có xấu không, và rollback có cần kích hoạt không.

## Stage thường gặp

- Source: pull request, review, merge policy.
- Build: compile, unit test, artifact.
- Test environment: integration tests, dependency tests.
- 1-box/canary: một phần traffic production.
- Production: full rollout với [[Rollback Alarm]] và [[Bake Period]].

## Liên kết

- [[Continuous Integration]]
- [[Continuous Delivery]]
- [[Canary Deployment]]
- [[Phased Rollout]]
- [[Rollback Strategy]]
