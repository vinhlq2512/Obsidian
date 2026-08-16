---
type: concept
status: understood
sources:
  - "[[2026-07-04_proof-of-human-how-to-verify-a-person-is-real-and-unique]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - security
  - distributed-systems
---

# Sybil Resistance

## Định nghĩa

Sybil Resistance (Khả năng kháng tấn công Sybil) là đặc tính của một hệ thống phân tán hoặc mạng lưới máy tính ngăn chặn một thực thể đơn lẻ giả danh tạo ra hàng loạt bản thể/tài khoản ảo (Sybil identities) để thao túng quyền quyết định, băng thông hoặc tài nguyên của hệ thống.

## Cơ chế chống Sybil

Các kiến trúc mạng phân tán sử dụng các cơ chế tài nguyên hoặc danh tính để chống Sybil:

1. **Proof of Work (PoW)**: Yêu cầu đóng góp năng lực tính toán phần cứng (hashrate).
2. **Proof of Stake (PoS)**: Yêu cầu đặt cọc giá trị kinh tế (tokens/coins).
3. **Proof of Personhood (PoP)**: Yêu cầu xác minh danh tính con người duy nhất bằng sinh trắc học hoặc ZKP.
4. **Rate Limiting & Cost Barriers**: Tăng chi phí tài chính/thời gian khi tạo tài khoản mới.

## Trade-off

- Tăng rào cản tham gia gia nhập hệ thống (User Onboarding Friction).
- Đòi hỏi sự đánh đổi giữa tính phi tập trung và tính xác thực danh tính.

## Liên kết

- [[Proof of Personhood]]
- [[Distributed Systems]]
- [[Rate Limiting]]
