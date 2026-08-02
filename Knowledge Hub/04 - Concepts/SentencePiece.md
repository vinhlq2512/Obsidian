---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - nlp
  - tokenization
---

# SentencePiece

## Định nghĩa

SentencePiece là một tokenizer subword học cách chia text thành các mảnh nhỏ hơn từ dữ liệu thô, thường dùng trong các mô hình NLP đa ngôn ngữ như XLM-R hoặc T5.

## Cách hiểu bằng lời của tôi

Thay vì giả định text đã được tách thành từ bằng khoảng trắng, SentencePiece xem input như một chuỗi ký tự và tự học các mảnh subword thường gặp. Điều này giúp tokenizer hoạt động ổn hơn trên nhiều ngôn ngữ, kể cả những ngôn ngữ không dùng dấu cách giống tiếng Anh.

## Mental model

```text
raw text -> normalize -> học subword pieces -> token IDs
```

Một từ có thể thành một token, nhiều subword token, hoặc đôi khi gần với ký tự nếu từ đó hiếm.

## Vì sao quan trọng trong multilingual NER

- Multilingual model cần tokenizer dùng được cho nhiều ngôn ngữ và nhiều hệ chữ.
- Subword giúp xử lý từ hiếm, tên riêng, biến thể hình thái và từ chưa từng thấy.
- Trong NER, label ban đầu thường nằm ở mức word/span, còn model nhận input ở mức subword, nên cần bước align label.
- Nếu một entity bị tách thành quá nhiều subword, model có thể khó học ranh giới entity hơn.

## Khi áp dụng

- Dùng khi train hoặc dùng model có tokenizer SentencePiece.
- Luôn kiểm tra output tokenization trước khi xử lý token-level task như [[Named Entity Recognition]].
- Khi fine-tune NER, cần quyết định chiến lược gán nhãn cho subword: chỉ label subword đầu, propagate label, hoặc ignore phần subword phụ.

## Cần biết

- SentencePiece là cách tokenization, không phải bản thân model Transformer.
- Nó thường được dùng trong pipeline của [[Multilingual Transformer]] vì phù hợp với text đa ngôn ngữ.
- Tokenization ảnh hưởng trực tiếp đến độ dài input, chi phí tính toán, alignment nhãn và chất lượng downstream task.

## Liên kết

- [[Tokenization]]
- [[Multilingual Transformer]]
- [[Named Entity Recognition]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
