---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]"
source_sections:
  - "[[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - tokenizer
  - pretraining
  - nlp
---

# Tokenizer Training

## Định nghĩa

`Tokenizer Training` là quá trình học một vocabulary và quy tắc tách token từ corpus mục tiêu, thay vì dùng nguyên tokenizer có sẵn của model khác.

## Vì sao quan trọng

- Tokenizer quyết định text được cắt thành đơn vị nào trước khi vào model.
- Nếu tokenizer không hợp domain, text có thể bị phân mảnh quá mức và làm representation kém hiệu quả.
- Trong training from scratch, tokenizer là một phần của kiến trúc dữ liệu chứ không chỉ là bước tiền xử lý.

## Cần biết

- Corpus dùng để train tokenizer phải đại diện cho domain mà model sẽ học.
- Tokenizer cho code, biomedical text hoặc domain nhiều ký hiệu đặc biệt thường cần thiết kế riêng.
- Tokenizer training thường đi cùng các quyết định về vocab size, special tokens và cách normalize text.

## Cách hiểu bằng lời của tôi

Tokenizer training giống như quyết định “bảng chữ cái làm việc” của model. Nếu bảng chữ cái đó không khớp domain, model sẽ phải học trên những mảnh token vụn và tốn công hơn rất nhiều.

## Liên kết

- [[Tokenization]]
- [[BPE]]
- [[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]
