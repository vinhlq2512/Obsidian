---
type: concept
status: seed
sources:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
  - "[[2025-09-29_how-grabs-migration-from-go-to-rust-cut-costs-by-70]]"
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
source_sections:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
  - "[[2025-09-29_how-grabs-migration-from-go-to-rust-cut-costs-by-70]]"
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - platform-engineering
  - software-architecture
---

# Runtime Platform Migration

## Định nghĩa

[[Runtime Platform Migration]] là quá trình nâng cấp runtime/framework nền của nhiều service mà vẫn giữ khả năng deploy, compatibility và vận hành ổn định.

## Cách hiểu bằng lời của tôi

Nợ platform thường không nằm trong một service mà nằm ở coupling giữa framework nội bộ, dependency cũ, build tooling và thói quen vận hành. Muốn nâng runtime ở scale lớn, chỉ "bảo team upgrade" là không đủ; cần baseline mới, tooling tự động, compatibility layer và lý do hiệu năng/vận hành đủ rõ.

## Pattern từ nguồn Netflix

- Di chuyển khỏi framework nội bộ cũ vì nó khóa hệ service ở JDK 8.
- Chuẩn hóa phần lớn service Java lên Spring Boot và JDK mới hơn.
- Dùng automated tooling để transform code/config/deployment thay vì migrate thủ công từng service.
- Khi Spring Boot 3 đổi từ `javax.*` sang `jakarta.*`, dùng Gradle plugin để bytecode transform library cũ ở artifact resolution time.
- Đổi runtime mở đường cho [[Java Virtual Threads]] và [[Generational Garbage Collection]].

## Trade-off

- Migration platform tốn effort tập trung, nhưng mở khóa nhiều cải tiến runtime sau đó.
- Compatibility layer giúp đi nhanh hơn nhưng phải được quản lý để không thành nợ mới.
- Thành công phụ thuộc vào tooling và golden path, không chỉ quyết định kiến trúc.
- Với migration ngôn ngữ/runtime, cần kiểm tra [[Behavioral Compatibility]] và dependency ecosystem; latency có thể không cải thiện dù resource efficiency tốt hơn.

## Liên kết

- [[Java Virtual Threads]]
- [[Generational Garbage Collection]]
- [[Observability]]
- [[Service Mesh]]
- [[Technical Debt]]
- [[Codemod Migration]]
- [[Idiomatic Rewrite]]
- [[Behavioral Compatibility]]
