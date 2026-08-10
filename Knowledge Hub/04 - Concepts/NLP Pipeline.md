---
type: concept
status: seed
sources:
  - "[[Practical NLP - Chapter 02 - NLP Pipeline]]"
source_sections:
  - "[[Practical NLP - Chapter 02 - NLP Pipeline]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - nlp
  - ml-engineering
---

# NLP Pipeline

## Định nghĩa

NLP pipeline là chuỗi bước biến raw text thành output có ích cho một task hoặc sản phẩm NLP.

## Cách hiểu bằng lời của tôi

Pipeline là phần làm cho NLP thành hệ thống thật: lấy dữ liệu, làm sạch, biến text thành representation, train/evaluate model, deploy, theo dõi lỗi và cập nhật khi dữ liệu thay đổi.

## Mental model

```text
Raw text
-> acquisition
-> extraction / cleanup
-> preprocessing
-> representation / features
-> modeling
-> evaluation
-> deployment
-> monitoring
-> update loop
```

## Cần biết

- Pipeline phụ thuộc task; không có preprocessing chung đúng cho mọi bài toán.
- Baseline đơn giản giúp kiểm tra dữ liệu và label trước khi tăng độ phức tạp của model.
- Evaluation cần đo cả component lẫn tác động cuối trong workflow sản phẩm.
- Monitoring quan trọng vì ngôn ngữ, người dùng và domain có thể drift theo thời gian.

## Liên kết

- [[Practical NLP - Chapter 02 - NLP Pipeline]]
- [[Tokenization]]
- [[Text Representation]]
- [[Model Benchmarking]]
