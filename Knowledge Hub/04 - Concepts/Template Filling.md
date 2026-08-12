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
---

# Template Filling

## Định nghĩa

Template filling là task điền các slot của một template/schema cố định bằng thông tin trích được từ text hoặc dữ liệu đầu vào.

## Cách hiểu bằng lời của tôi

Nếu extraction lấy ra các mẩu thông tin, template filling đặt các mẩu đó vào đúng ô để hệ thống có một record chuẩn.

## Khi dùng

```text
Extracted data
-> slot 1
-> slot 2
-> slot 3
-> structured template
```

- Practical NLP nêu ví dụ weather reports hoặc flight announcements: output thường theo template chuẩn, chỉ một số slot thay đổi.
- Template filling hợp khi domain có schema tương đối ổn định và các trường cần điền được biết trước.
- Task này nối [[Information Extraction]] với workflow sinh báo cáo, thông báo hoặc record có cấu trúc.

## Cách làm

- Sách mô tả template filling như một bài toán supervised ML hai giai đoạn.
- Bước 1: xác định trong sentence có template đó hay không.
- Bước 2: xác định slot fillers cho template, với classifier riêng cho từng slot.
- Work đang tiếp tục về việc tự động induce template.

## Giới hạn

- Đây là bài toán specialized, domain-dependent.
- Sách nói không biết có off-the-shelf service provider phổ biến nào cho task này.
- Kết quả tốt nhất thường xuất hiện khi schema đã ổn định và dữ liệu đầu vào tương đối chuẩn.

## Liên kết

- [[Information Extraction]]
- [[Event Extraction]]
- [[Temporal Information Extraction]]
- [[Relation Extraction]]
