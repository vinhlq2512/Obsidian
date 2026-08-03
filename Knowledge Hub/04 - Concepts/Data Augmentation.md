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
  - data
  - nlp
---

# Data Augmentation

## Định nghĩa

Data augmentation là kỹ thuật tạo thêm biến thể dữ liệu từ dữ liệu hiện có để tăng độ phủ của training set.

## Trong NLP ít nhãn

Với [[Intent Detection]] hoặc [[Text Classification]], augmentation có thể tạo thêm các cách diễn đạt khác nhau cho cùng một nhãn.

## Rủi ro

- Làm đổi label nếu biến đổi câu quá mạnh.
- Tạo dữ liệu không tự nhiên.
- Khuếch đại bias hoặc lỗi trong dữ liệu gốc.

## Cách hiểu bằng lời của tôi

Augmentation hữu ích khi nó tạo thêm cách nói hợp lý cho cùng một ý. Nếu nó làm câu đổi nghĩa, nó không còn là tăng dữ liệu mà là thêm nhiễu.

## Liên kết

- [[Few-shot Learning]]
- [[Intent Detection]]
- [[Text Classification]]

