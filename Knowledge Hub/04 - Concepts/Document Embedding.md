---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-10
last_updated: 2026-08-10
tags:
  - concept
  - nlp
  - representation
---

# Document Embedding

## Định nghĩa

Document embedding là vector dense biểu diễn trực tiếp một document, sentence hoặc paragraph trong không gian số.

## Cách hiểu bằng lời của tôi

Word embedding học tọa độ cho từng từ rồi mình phải gom lại. Document embedding cố học tọa độ cho cả đoạn text như một đơn vị, để classifier nhận luôn một vector đại diện cho document.

## Cơ chế với Doc2Vec

```text
Document / sentence / paragraph
-> tokenize
-> TaggedDocument
-> train Doc2Vec
-> infer_vector cho text mới
-> classifier
```

- `TaggedDocument` biểu diễn document như list token kèm một tag/id.
- Doc2Vec có các lựa chọn như `vector_size`, `alpha`, `min_count`, `dm`/`dbow` và `epochs`.
- `dm` là distributed memory; `dbow` là distributed bag of words.
- Khi infer vector cho text mới, có thể chạy nhiều steps để representation ổn định hơn.

## Khi dùng cho text classification

- Dùng khi muốn học representation trực tiếp cho document thay vì average [[Embedding|word embeddings]].
- Có thể dùng document vectors làm feature cho classifier như [[Logistic Regression]].
- Với dữ liệu như tweets, preprocessing rất quan trọng vì text ngắn, nhiều hashtag, handle, emoticon và spelling biến dạng.

## Bài học từ Practical NLP

- Ví dụ dùng Doc2Vec cho tweet emotion classification với ba label: neutral, worry, happiness.
- Kết quả F1 khoảng 0.51, khá kém dù dataset không quá nhỏ.
- Một cách diễn giải là tweets có rất ít thông tin mỗi mẫu và ngôn ngữ nhiễu, nên representation cần problem-specific hơn hoặc cần tuning kỹ hơn.
- Trade-off deployment: phải lưu model đã học representation. Doc2Vec thường không cồng kềnh như fastText nhưng cũng không train nhanh bằng fastText.

## Liên kết

- [[Embedding]]
- [[Text Representation]]
- [[Text Classification]]
- [[Logistic Regression]]
- [[Word2Vec]]
