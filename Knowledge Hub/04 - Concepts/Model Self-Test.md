---
type: concept
status: seed
sources:
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
source_sections:
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - testing
---

# Model Self-Test

## Định nghĩa

[[Model Self-Test]] là test data và expected output được lưu cùng model để platform tự kiểm tra model mỗi khi load hoặc khi code/dependency thay đổi.

## Cách hiểu bằng lời của tôi

Model production có thể bị hỏng vì library upgrade, container image mới hoặc thay đổi preprocessing. Self-test là smoke test gắn với model artifact: nếu input mẫu không còn cho output kỳ vọng, platform phát hiện trước khi request thật bị ảnh hưởng.

## Liên kết

- [[AI Model Serving]]
- [[Model Shadowing]]
- [[Behavioral Compatibility]]
- [[Deployment Pipeline]]
- [[Regression Testing]]
