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
  - machine-learning
  - classification
---

# Naive Bayes Classifier

## Định nghĩa

Naive Bayes Classifier là classifier xác suất dùng Bayes theorem để dự đoán class của một văn bản dựa trên các feature quan sát được trong training data.

## Cách hiểu bằng lời của tôi

Naive Bayes hỏi: “Nếu document thuộc class này, các từ/feature mình đang thấy có khả năng xuất hiện đến mức nào?” Sau đó nó so sánh các class và chọn class có xác suất lớn nhất.

## Cơ chế

```text
Text
-> [[Bag of Words|BoW]] / document-term vector
-> ước lượng P(feature | class)
-> kết hợp xác suất feature cho từng class
-> chọn class có xác suất lớn nhất
```

Trong ví dụ của Practical NLP, `MultinomialNB` nhận feature vector từ `CountVectorizer` rồi train trên label relevant/non-relevant.

## Công thức trực giác

```text
score(class) ~= P(class) * product(P(feature_i | class))
```

- `P(class)`: class đó xuất hiện nhiều hay ít trong training data.
- `P(feature_i | class)`: feature/từ đó thường xuất hiện trong class này đến mức nào.
- Class có score lớn nhất là prediction cuối.

## Khi dùng trong text classification

- Dùng tốt làm baseline vì đơn giản, nhanh và hợp với sparse features như [[Bag of Words]].
- Giúp kiểm tra pipeline trước khi thử Logistic Regression, SVM hoặc model phức tạp hơn.
- Nếu kết quả kém, lỗi có thể đến từ feature quá sparse, [[Class Imbalance]], preprocessing hoặc metric chưa khớp use case.

## Bài học từ Practical NLP

- Trong dataset economic news, Naive Bayes nhận diện non-relevant tốt hơn relevant.
- Khi giảm số feature, average performance có thể giảm nhưng relevant class được cải thiện mạnh.
- Vì vậy cần đọc [[Confusion Matrix|confusion matrix]] theo từng class, không chỉ nhìn accuracy trung bình.

## Liên kết

- [[Text Classification]]
- [[Bag of Words]]
- [[Class Imbalance]]
- [[Text Representation]]
- [[Confusion Matrix]]
