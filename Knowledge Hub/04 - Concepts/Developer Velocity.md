---
type: concept
status: seed
sources:
  - "[[2025-11-12_how-tinder-decomposed-its-ios-monolith-app-handling-70m-user]]"
  - "[[2026-05-26_how-vercel-cut-build-wait-times-from-90-seconds-to-5]]"
source_sections:
  - "[[2025-11-12_how-tinder-decomposed-its-ios-monolith-app-handling-70m-user]]"
  - "[[2026-05-26_how-vercel-cut-build-wait-times-from-90-seconds-to-5]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - engineering-productivity
  - platform
---

# Developer Velocity

## Định nghĩa

[[Developer Velocity]] là khả năng của team đi từ thay đổi code đến feedback/deploy an toàn với thời gian và ma sát thấp.

## Cách hiểu bằng lời của tôi

Velocity không chỉ là "code nhanh". Build graph, test time, provisioning delay, ownership boundary và confidence khi release đều ảnh hưởng đến tốc độ học. Tinder giảm build time bằng modularization; Vercel giảm build wait bằng runtime isolation và warm pool.

## Liên kết

- [[Critical Path Build Graph]]
- [[Mobile App Modularization]]
- [[Build Provisioning Warm Pool]]
- [[Deployment Pipeline]]
- [[Technical Debt]]
