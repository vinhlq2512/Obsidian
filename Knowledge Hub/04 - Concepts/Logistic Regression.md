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

# Logistic Regression

## Định nghĩa

Logistic Regression là discriminative classifier học trọng số cho các feature để dự đoán class hoặc xác suất class.

## Cách hiểu bằng lời của tôi

Nếu [[Naive Bayes Classifier]] hỏi “feature này thường xuất hiện trong class nào?”, Logistic Regression hỏi “feature này nên đẩy quyết định về class nào, mạnh đến mức nào?”.

## Cơ chế

```text
Feature vector
-> học weight cho từng feature
-> tạo linear separator giữa các class
-> dự đoán xác suất / class
```

- Với text classification, feature vector có thể đến từ [[Bag of Words]] hoặc representation sparse khác.
- Mỗi feature có weight thể hiện mức đóng góp vào quyết định classification.
- Sách gọi Logistic Regression là discriminative classifier, đối lập với Naive Bayes là generative classifier.

## Khi dùng trong text classification

- Dùng làm baseline mạnh trong nghiên cứu và MVP thực tế.
- Dễ so sánh với Naive Bayes, [[Support Vector Machine|SVM]] và các model phức tạp hơn.
- Có thể dùng `class_weight="balanced"` khi dữ liệu bị [[Class Imbalance]].

## Bài học từ Practical NLP

- Trong ví dụ economic news, Logistic Regression dùng feature vector 5,000 chiều từ bước Naive Bayes trước đó.
- `class_weight="balanced"` tăng trọng số cho class ít mẫu theo tỷ lệ ngược với số sample của class.
- Accuracy khoảng 73.7% và kém Naive Bayes trên dataset này.
- Vì vậy, Logistic Regression không tự động tốt hơn baseline đơn giản; cần đọc [[Confusion Matrix]] và so sánh theo lỗi quan trọng của use case.

## Liên kết

- [[Text Classification]]
- [[Naive Bayes Classifier]]
- [[Class Imbalance]]
- [[Confusion Matrix]]
- [[Bag of Words]]
- [[Support Vector Machine]]
