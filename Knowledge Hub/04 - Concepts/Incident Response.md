---
type: concept
status: seed
sources:
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage-byte-sized-design]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
source_sections:
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - incident
---

# Incident Response

## Định nghĩa

[[Incident Response]] là quy trình phát hiện, phân loại, điều phối, mitigate, communicate và phục hồi khi hệ thống có sự cố ảnh hưởng tới user hoặc business.

## Cách hiểu bằng lời của tôi

Incident response là phần "vận hành trong lúc cháy": biết ai ra quyết định, service nào đang ảnh hưởng, mitigation nào an toàn, khi nào fail closed/fail open, và thông tin nào cần gửi cho người dùng hoặc stakeholder. Sau đó nó nối sang [[Postmortem]] để biến sự cố thành thay đổi bền vững.

## Cần có

- Severity và escalation path rõ.
- War room/comms channel cho team liên quan.
- Impact scope: user path, region, tenant, product, dependency.
- Mitigation tạm thời: degrade, shed load, rollback, disable feature.
- Recovery criteria và handoff sang postmortem.

## Liên kết

- [[Postmortem]]
- [[Alerting]]
- [[Blast Radius]]
- [[Graceful Degradation]]
- [[Disaster Recovery]]
- [[Load Shedding]]
