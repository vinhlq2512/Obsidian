---
type: concept
status: developing
sources:
  - "[[2026-03-26_how-to-implement-api-security]]"
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
  - "[[2023-04-12_authentication-methods-passwordless-mfa-sso-oauth-part-2]]"
  - "[[2026-01-27_how-google-manages-trillions-of-authorizations-with-zanzibar]]"
  - "[[2026-02-24_how-uber-reinvented-access-control-for-microservices]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - api
---

# Authorization

## Định nghĩa

Authorization là quá trình kiểm tra caller đã xác thực có quyền thực hiện action cụ thể trên resource cụ thể hay không.

## Cách hiểu bằng lời của tôi

Một user đăng nhập hợp lệ vẫn không được đọc đơn hàng của user khác. Authentication mở cửa vào hệ thống; authorization kiểm từng căn phòng.

## Cần biết

- Broken Object Level Authorization xảy ra khi API chỉ kiểm login nhưng không kiểm quyền trên object ID.
- Least privilege giới hạn blast radius khi credential bị lộ.
- RBAC gán quyền qua role; ABAC dùng thuộc tính caller/resource/context để quyết định linh hoạt hơn.
- ReBAC dùng quan hệ giữa user, group và object để diễn đạt sharing/inheritance.
- Hệ authorization ở scale lớn cần kiểm soát freshness, cache, quota và isolation giữa client.
- Authorization phải nằm server-side và được kiểm cho từng resource/action nhạy cảm.

## Liên kết

- [[API Security]]
- [[Authentication]]
- [[OAuth 2.0]]
- [[API Gateway]]
- [[Excessive Agency]]
- [[Fine-Grained Authorization]]
- [[Attribute-Based Access Control]]
- [[Relationship-Based Access Control]]
- [[Google Zanzibar]]
