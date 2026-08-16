---
type: concept
status: seed
sources:
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
source_sections:
  - "[[2026-05-12_how-figma-upgraded-data-pipeline-from-multi-day-latency-to-r]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
---

# Snapshot Bootstrap

## Định nghĩa

[[Snapshot Bootstrap]] là bước tạo bản sao ban đầu của một dataset trước khi pipeline incremental hoặc CDC tiếp tục cập nhật các thay đổi mới.

## Cách hiểu bằng lời của tôi

CDC chỉ biết các event sau khi mình bắt đầu nghe. Nếu warehouse đang rỗng, stream thay đổi không thể tự dựng lại toàn bộ trạng thái hiện tại. Vì vậy phải có snapshot làm nền, rồi merge các event xảy ra quanh thời điểm snapshot để không mất dữ liệu.

## Cơ chế

```text
chọn thời điểm snapshot
-> export trạng thái bảng ra storage tạm
-> bắt CDC từ offset trước hoặc bằng thời điểm snapshot
-> load snapshot vào bảng đích
-> merge event CDC, chấp nhận duplicate nhưng không chấp nhận gap
```

## Điểm dễ sai

- Bắt CDC quá muộn làm mất thay đổi xảy ra trong lúc snapshot chạy.
- Không có idempotent merge khiến event trùng làm sai số liệu.
- Validation dùng cùng đường pipeline với production có thể bỏ sót bug chung.

## Liên kết

- [[Change Data Capture]]
- [[Write-Ahead Log]]
- [[Event Stream]]
- [[Data Pipeline Validation]]
- [[Data Freshness]]
