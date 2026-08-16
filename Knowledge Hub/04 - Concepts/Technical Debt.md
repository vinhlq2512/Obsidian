---
type: concept
status: seed
sources:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
  - "[[2025-02-18_tech-debt-can-accelerate-or-destroy-your-codebase-heres-how]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
source_sections:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
  - "[[2025-02-18_tech-debt-can-accelerate-or-destroy-your-codebase-heres-how]]"
  - "[[2025-12-18_how-salesforce-migrated-7-years-of-legacy-in-4-months-instea]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - software-architecture
  - platform-engineering
---

# Technical Debt

## Định nghĩa

[[Technical Debt]] là chi phí tích lũy từ các quyết định kỹ thuật làm hệ thống khó thay đổi, khó nâng cấp hoặc khó vận hành hơn theo thời gian.

## Cách hiểu bằng lời của tôi

Technical debt không chỉ là code xấu. Nó có thể là framework nội bộ cũ, dependency bị khóa version, build pipeline khó đổi, hoặc platform khiến các team không thể nâng runtime độc lập. Debt nguy hiểm nhất là loại âm thầm chặn mọi cải tiến sau này.

## Ví dụ từ nguồn Netflix

Netflix từng bị khóa ở JDK 8 vì framework nội bộ cũ và dependency coupling. Ngay cả khi Java mới có lợi ích rõ, service owner vẫn khó nâng cấp vì platform không sẵn sàng. Cách xử lý là migration có tooling, baseline Spring Boot mới, compatibility layer và lý do vận hành rõ ràng.

Trong case Salesforce, nợ không chỉ là code cũ mà là static method, global state, dependency graph không rõ và thiếu documentation. Khi đưa hệ thống vào môi trường multi-tenant, các giả định cũ trở thành rủi ro kiến trúc.

## Liên kết

- [[Runtime Platform Migration]]
- [[Dependency-Driven Migration]]
- [[Service Layer Refactoring]]
- [[Legacy System Modernization]]
- [[Observability]]
- [[Service Mesh]]
- [[GraphQL Federation]]
