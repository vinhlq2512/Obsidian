---
type: concept
status: seed
sources:
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
source_sections:
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - debugging
---

# Runbook Automation

## Định nghĩa

[[Runbook Automation]] là việc chuyển các bước điều tra hoặc mitigation lặp lại trong runbook thành workflow tự chạy, có guardrail và kết quả có cấu trúc.

## Cách hiểu bằng lời của tôi

Runbook tốt không nên chỉ là checklist cho người mệt lúc nửa đêm. Những bước kéo dashboard, lấy log, so baseline, kiểm tra deploy/config và gợi ý mitigation có thể được tự động hóa để engineer tập trung vào phán đoán cuối.

## Trade-off

- Giảm context gathering trong incident.
- Giúp engineer mới đi nhanh hơn.
- Cần maintenance khi hệ thống, metric hoặc dependency thay đổi.
- Mitigation nguy hiểm vẫn nên có human approval.

## Liên kết

- [[Debugging as Code]]
- [[Incident Response]]
- [[Root Cause Analysis]]
- [[Alerting]]
- [[Automated Root Cause Analysis]]
