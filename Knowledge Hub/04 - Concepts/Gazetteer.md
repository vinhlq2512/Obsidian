---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 05 - Information Extraction]]"
first_seen: 2026-08-10
last_updated: 2026-08-10
tags:
  - concept
  - nlp
  - ner
---

# Gazetteer

## Định nghĩa

Gazetteer là một collection lớn các tên đã biết, thường là person, organization hoặc location names, dùng để lookup nhanh entities trong text.

## Cách hiểu bằng lời của tôi

Gazetteer giống một cuốn danh bạ entity theo domain. Nếu text chứa nhiều tên mình đã biết sẵn, chỉ cần dò bảng là có thể khởi động NER rất nhanh.

## Khi nào dùng

- Khi chưa có NER system sẵn.
- Khi domain có danh sách entity tương đối ổn định.
- Khi coverage của entity known names trong dữ liệu đủ cao.

## Hạn chế

- Khó xử lý tên mới chưa có trong danh sách.
- Cần cơ chế update database định kỳ.
- Cần quản lý aliases hoặc variations như `USA` và `United States`.
- Khả năng tổng quát hóa thấp hơn model học từ context.

## Trong NER

- Practical NLP xem gazetteer là cách bắt đầu đơn giản nhất để xây [[Named Entity Recognition]].
- Đây là bước trước rule-based NER hoặc ML-based [[Sequence Labeling]] khi cần generalization tốt hơn.

## Liên kết

- [[Named Entity Recognition]]
- [[Sequence Labeling]]
- [[Information Extraction]]
