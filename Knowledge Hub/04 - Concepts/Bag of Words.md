---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 03 - Text Representation]]"
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-10
last_updated: 2026-08-10
tags:
  - concept
  - nlp
  - representation
---

# Bag of Words

## Định nghĩa

Bag of Words là cách biểu diễn text thành vector dựa trên các từ trong vocabulary, thường bằng số lần mỗi từ xuất hiện trong document.

## Cách hiểu bằng lời của tôi

BoW xem document như một “túi từ”: từ nào có mặt và xuất hiện bao nhiêu lần thì được ghi lại, còn thứ tự từ và ngữ cảnh câu bị bỏ qua.

## Cơ chế

```text
Raw text
-> preprocessing
-> vocabulary
-> document-term vector
-> classifier / model cổ điển
```

- Trong scikit-learn, `CountVectorizer` là một implementation phổ biến của BoW.
- Mỗi document trở thành một vector có chiều bằng vocabulary.
- Giá trị trong vector thường là count của từng từ trong document.
- Khi áp dụng cho nhiều document, ta có document-term matrix.

## Khi dùng cho text classification

- BoW là baseline tốt vì đơn giản, dễ debug và chạy được với classifier cổ điển như [[Naive Bayes Classifier]], Logistic Regression hoặc SVM.
- Nếu vocabulary quá lớn, vector rất sparse: phần lớn vị trí bằng 0.
- Feature hiếm có thể trở thành noise và làm classifier khó học.
- Có thể giới hạn số feature, ví dụ `max_features`, để giảm sparsity và noise.

## Trade-off

- Giữ được tín hiệu lexical trực tiếp: từ nào xuất hiện và xuất hiện nhiều hay ít.
- Mất thứ tự từ, ngữ cảnh và quan hệ ngữ nghĩa sâu.
- Dễ giải thích hơn embedding, nhưng kém linh hoạt hơn khi cần bắt nghĩa tương đương hoặc paraphrase.

## Liên kết

- [[Text Representation]]
- [[Text Classification]]
- [[Class Imbalance]]
- [[Naive Bayes Classifier]]
