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
  - identity
---

# Proof of Personhood

## Định nghĩa

Proof of Personhood (Xác minh tư cách con người) là tập hợp các cơ chế kỹ thuật nhằm chứng minh một tài khoản thuộc về một con người thực sự, duy nhất (unique human) trong thế giới số mà không cần tiết lộ danh tính cá nhân nhạy cảm (PII).

## Cách hiểu bằng lời của tôi

Trong kỷ nguyên AI tạo ra hàng tỷ bot và clone account tự động, các phương pháp truyền thống như email/phone hay CAPTCHA đều bị qua mặt dễ dàng. Proof of Personhood giải bài toán: "Làm sao biết bạn là con người thực sự và duy nhất trên trái đất mà không ép bạn phải nộp CMND/Hộ chiếu công khai?".

## Phương pháp triển khai

```text
User Physical Presence
-> Iris/Biometric Scan (Hardware device like Orb)
-> Cryptographic Hash & Iris Code Generation
-> Zero-Knowledge Proof (ZKP) Generation
-> World ID (On-chain/Off-chain Anonymous Verification)
```

1. **Biometric Hardware Verification**: Dùng thiết bị chuyên dụng (như Worldcoin Orb) quét mống mắt (iris) để tạo mống mắt băm ngẫu nhiên. Sau khi tạo hash, ảnh sinh trắc học gốc bị xóa lập tức.
2. **Zero-Knowledge Proofs (ZKP)**: Người dùng chứng minh mình sở hữu một mống mắt hợp lệ trong tập dữ liệu mà không tiết lộ mã mống mắt hay danh tính cá nhân.
3. **Social Graph / Web of Trust**: Xác minh dựa trên mạng lưới tin cậy xã hội (ví dụ: BrightID, Gitcoin Passport).

## Ứng dụng & Trade-off

- **Ứng dụng**: Phân phối thu nhập cơ bản toàn cầu (UBI), bỏ phiếu chống gian lận (Sybil-resistant voting), chống sybil bot trong airdrop và mạng xã hội.
- **Trade-off**:
  - Quyền riêng tư vs Tiện ích: Nguy cơ lo ngại về bảo mật dữ liệu sinh trắc học.
  - Chi phí thiết bị phần cứng lớn.

## Liên kết

- [[Sybil Resistance]]
- [[Authentication]]
- [[LLM Security]]
