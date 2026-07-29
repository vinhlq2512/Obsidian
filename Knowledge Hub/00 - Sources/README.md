---
type: index
area: sources
created: 2026-07-23
tags:
  - sources
  - index
---

# Sources

## Mục đích

`00 - Sources` là nơi lưu tài liệu gốc: PDF, ảnh, dataset, web clip và file tham khảo. Đây không phải nơi viết note phân tích.

## Cấu trúc

- `PDFs/Books`: ebook, sách kỹ thuật, sách nghiên cứu.
- `PDFs/Papers`: paper học thuật.
- `PDFs/Docs`: tài liệu kỹ thuật, whitepaper, manual.
- `Images`: ảnh, screenshot, diagram.
- `Datasets`: CSV, JSON, sample data.
- `Web Clips`: bài viết web đã lưu.

## Quy tắc liên kết

- Note sách trong `01 - Books` nên link tới PDF gốc bằng property `source_file`.
- Note paper trong `20 - Research/Papers` nên link tới PDF gốc bằng property `pdf`.
- Không viết ghi chú dài trực tiếp trong Sources; ghi chú nên nằm trong `01 - Books`, `02 - Sections`, `04 - Concepts`, hoặc `20 - Research`.

## Ví dụ

```yaml
source_file: "[[Hands-On Large Language Models.pdf]]"
```

```yaml
pdf: "[[Attention Is All You Need.pdf]]"
```

## Graph filter gợi ý

Ẩn daily reading và sources khỏi graph tri thức:

```text
-path:"03 - Daily Reading" -path:"00 - Sources"
```

Chỉ xem sách, section, concepts và research:

```text
path:"01 - Books" OR path:"02 - Sections" OR path:"04 - Concepts" OR path:"20 - Research"
```

