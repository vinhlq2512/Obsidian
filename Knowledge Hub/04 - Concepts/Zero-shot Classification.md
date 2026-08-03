---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
source_sections:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - zero-shot
  - text-classification
  - nlp
---

# Zero-shot Classification

## Định nghĩa

Zero-shot classification là cách phân loại văn bản vào các nhãn chưa có dữ liệu train trực tiếp cho task đó.

## Cơ chế trực giác

Model nhận text và danh sách candidate labels, rồi ước lượng label nào phù hợp nhất.

```text
Text
Candidate labels
-> Zero-shot classifier
-> Ranking labels theo score
```

## Khi dùng

- Khi chưa có dữ liệu gán nhãn.
- Khi cần baseline nhanh trước khi xây dataset.
- Khi muốn kiểm tra taxonomy nhãn có hợp lý không.

## Hạn chế

- Phụ thuộc mạnh vào cách đặt tên label.
- Có thể nhầm nếu label mơ hồ hoặc chồng lấn.
- Không thay thế evaluation bằng dữ liệu thật.

## Liên kết

- [[Few-shot Learning]]
- [[Intent Detection]]
- [[Text Classification]]

