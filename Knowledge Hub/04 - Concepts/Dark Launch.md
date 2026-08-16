---
type: concept
status: understood
sources:
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
source_sections:
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - deployment
  - system-design
---

# Dark Launch

## Định nghĩa

Dark Launch là strategy chạy code mới trong production nhưng không hiển thị output cho user, thường để so sánh hoặc đo hành vi hệ thống thật.

## Cách hiểu bằng lời của tôi

Dark launch phù hợp khi cần validate backend logic bằng request thật mà không thay đổi user experience. Old path vẫn trả response thật, new path chạy song song và kết quả được log, discard hoặc so sánh.

## Giới hạn

- Không validate được UI/UX vì user không thấy output.
- Cần kiểm soát side effect nếu code mới có write, gửi email, charge tiền hoặc publish event.

## Liên kết

- [[Shadow Traffic]]
- [[Feature Flag]]
- [[Shadow Testing]]
- [[Idempotency Key]]
