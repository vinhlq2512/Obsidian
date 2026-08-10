---
type: concept
status: seed
sources:
  - "[[Practical NLP - Chapter 03 - Text Representation]]"
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 03 - Text Representation]]"
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-04
last_updated: 2026-08-10
tags:
  - concept
  - nlp
  - representation
---

# Text Representation

## Định nghĩa

Text representation là cách biểu diễn token, câu, đoạn hoặc tài liệu thành vector/số để thuật toán có thể xử lý.

## Cách hiểu bằng lời của tôi

Model không xử lý chữ trực tiếp. Representation là lăng kính biến text thành tín hiệu toán học. Nếu lăng kính mất thông tin quan trọng, model phía sau dù mạnh vẫn khó làm đúng task.

## Các nhóm chính

- Sparse representation: one-hot, [[Bag of Words]], Bag of N-Grams, TF-IDF.
- Dense/distributed representation: [[Embedding]] ở mức word, subword, sentence hoặc document.
- Handcrafted features: feature do người thiết kế dựa trên domain signal.

## Cần biết

- Sparse vector dễ debug và làm baseline tốt, nhưng thường mất thứ tự/ngữ cảnh.
- Với text classification, sparse representation như [[Bag of Words]] có thể tạo document-term matrix cho classifier cổ điển. Điểm cần kiểm soát là vocabulary quá lớn làm vector rất sparse và nhiều feature hiếm thành noise.
- [[Embedding]] nén thông tin vào vector dense, hữu ích cho similarity, retrieval, clustering và classification.
- Representation phải khớp task: document classification, NER, search và QA có nhu cầu khác nhau.
- Visualization chỉ là công cụ trực giác; không nên xem plot 2D như bằng chứng đầy đủ về embedding space.

## Liên kết

- [[Practical NLP - Chapter 03 - Text Representation]]
- [[Tokenization]]
- [[Bag of Words]]
- [[Embedding]]
- [[Semantic Search]]
- [[Text Classification]]
- [[Topic Modeling]]
