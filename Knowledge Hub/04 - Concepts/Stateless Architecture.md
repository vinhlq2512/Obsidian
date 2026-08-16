---
type: concept
status: seed
sources:
  - "[[2026-01-29_how-to-scale-an-api]]"
  - "[[2024-11-28_stateless-architecture-the-key-to-building-scalable-and-resi]]"
source_sections:
  - "[[2026-01-29_how-to-scale-an-api]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - architecture
  - scalability
---

# Stateless Architecture

## Định nghĩa

[[Stateless Architecture]] là thiết kế trong đó application instance không giữ session/state quan trọng trong memory local giữa các request.

## Cách hiểu bằng lời của tôi

Stateless API dễ scale ngang vì request nào cũng có thể chạy ở instance nào. Nếu một instance chết, không mất session cục bộ. State cần bền vững được đưa ra storage chung như database, Redis/session store hoặc token có chữ ký.

## Lợi ích

- Horizontal scaling đơn giản hơn.
- Instance có thể thêm/xóa/replace mà ít migration state.
- Load balancer không bắt buộc sticky session.
- Failure của một instance ít ảnh hưởng user hơn.

## Trade-off

- Cần external session/state store.
- Token/session design phải xử lý revoke, expiry và security.
- Không phải mọi workload stateful đều fit stateless API layer.

## Liên kết

- [[Horizontal Scaling]]
- [[Load Balancer]]
- [[Session-Based Authentication]]
- [[JSON Web Token]]
- [[Caching Strategy]]
