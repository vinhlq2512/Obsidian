---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 05 - Information Extraction]]"
first_seen: 2026-08-11
last_updated: 2026-08-11
tags:
  - concept
  - nlp
  - information-extraction
  - weak-supervision
---

# Distant Supervision

## Định nghĩa

Distant supervision là cách tạo dữ liệu huấn luyện cho relation extraction bằng cách dùng một knowledge base hoặc database lớn để tự động gán nhãn cho các câu có chứa cặp thực thể phù hợp.

## Cách hiểu bằng lời của tôi

Thay vì ngồi gán thủ công từng câu có `person` và `organization`, mình lấy một database như Wikipedia hoặc Freebase làm “nguồn sự thật” rồi tự động match ra hàng nghìn ví dụ relation. Nhãn sinh ra sẽ nhiễu hơn gán thủ công, nhưng đủ để khởi động một supervised model.

## Trong RE

```text
knowledge base / database lớn
-> match entity pair với relation đã biết
-> tạo noisy training examples
-> train supervised RE model
```

- Practical NLP mô tả distant supervision như một mở rộng của weak supervision cho relation extraction.
- Ví dụ, nếu Wikipedia infobox cho biết `person X` là `employee of` `organization Y`, những sentence chứa cả hai entity có thể được xem như ví dụ huấn luyện cho relation đó.
- Cách này hữu ích khi relation schema đã rõ nhưng không có đủ dữ liệu gán nhãn thủ công.

## Vì sao hữu ích

- Tạo được tập huấn luyện lớn nhanh hơn manual labeling.
- Hợp với relation extraction vì relation thường có thể soi ngược từ knowledge base có cấu trúc.
- Có thể làm cầu nối giữa open data/KB và supervised learning.

## Hạn chế

- Nhãn tạo ra là noisy, vì câu chứa cùng entity pair chưa chắc luôn diễn đạt đúng relation đó.
- Chất lượng phụ thuộc vào độ phủ và độ sạch của knowledge base.
- Distant supervision thường không giải quyết được vấn đề relation schema phụ thuộc domain.
- Vẫn cần kiểm tra, lọc hoặc kết hợp với weak supervision / pattern / human review.

## Liên kết

- [[Relation Extraction]]
- [[Weak Supervision]]
- [[Information Extraction]]
