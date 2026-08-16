---
type: concept
status: seed
sources:
  - "[[2026-04-14_figma-design-to-code-code-to-design-clearly-explained]]"
source_sections:
  - "[[2026-04-14_figma-design-to-code-code-to-design-clearly-explained]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - frontend
  - design-system
---

# Design System Drift

## Định nghĩa

[[Design System Drift]] là hiện tượng design file, component library và code implementation dần lệch nhau qua nhiều vòng sửa đổi.

## Cách hiểu bằng lời của tôi

Design-to-code và code-to-design không phải vòng tròn không mất mát. Code có state, handler, API và route mà Figma không chứa; Figma có visual structure mà code có thể implement theo nhiều cách. Mỗi lần roundtrip, nếu thiếu component mapping, drift tăng.

## Liên kết

- [[Code Connect]]
- [[Component Mapping]]
- [[Design-to-Code Context]]
- [[Behavioral Compatibility]]
