---
type: concept
status: seed
sources:
  - "[[2025-07-29_how-salesforce-cut-model-onboarding-time-by-75percent]]"
source_sections:
  - "[[2025-07-29_how-salesforce-cut-model-onboarding-time-by-75percent]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - cloud
---

# Managed Model Serving Integration

## Định nghĩa

[[Managed Model Serving Integration]] là pattern tích hợp managed model platform vào serving architecture hiện có bằng wrapper/adaptor để giảm hạ tầng tự vận hành mà vẫn giữ contract cũ.

## Cách hiểu bằng lời của tôi

Salesforce dùng Bedrock CMI để giảm friction GPU/provisioning, nhưng không bắt product team đổi prediction workflow. SageMaker trở thành lớp pre/post-processing mỏng forward sang Bedrock, giúp backend mới nằm sau interface quen thuộc.

## Trade-off

- Giảm thời gian onboarding và GPU lifecycle work.
- Cần validate security, scaling behavior, error handling và observability của vendor.
- Wrapper giữ backward compatibility nhưng thêm một lớp vận hành.

## Liên kết

- [[Model Onboarding]]
- [[AI Model Serving]]
- [[Serverless Architecture]]
- [[Backward Compatibility]]
- [[Vendor Lock-In]]
