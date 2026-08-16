---
type: concept
status: understood
sources:
  - "[[2025-03-20_monolith-vs-microservices-vs-modular-monoliths-what-s-the-ri]]"
source_sections:
  - "[[2025-03-20_monolith-vs-microservices-vs-modular-monoliths-what-s-the-ri]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - architecture
  - system-design
---

# Modular Monolith

## Định nghĩa

Modular Monolith là kiến trúc một codebase/một deployable unit nhưng bên trong được chia thành module theo boundary rõ ràng.

## Cách hiểu bằng lời của tôi

Modular monolith cố giữ sự đơn giản vận hành của monolith, nhưng ép code có ranh giới như microservices. Đây thường là bước hợp lý trước khi tách service, vì nó giúp domain boundary rõ hơn mà chưa phải trả toàn bộ chi phí distributed system.

## Rủi ro

- Nếu không enforce boundary, module sẽ âm thầm gọi xuyên nhau và trở lại thành monolith rối.
- Không scale độc lập theo module được.
- Vẫn deploy toàn bộ app khi một module đổi.

## Liên kết

- [[Monolithic Architecture]]
- [[Microservices Architecture]]
- bounded context
- [[API Contract]]
