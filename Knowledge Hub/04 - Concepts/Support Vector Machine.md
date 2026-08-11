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

# Support Vector Machine

## Định nghĩa

Support Vector Machine, viết tắt là SVM, là discriminative classifier tìm một hyperplane để tách các class với margin lớn nhất có thể.

## Cách hiểu bằng lời của tôi

SVM không chỉ muốn vẽ một đường phân chia class. Nó muốn vẽ đường phân chia “có khoảng đệm rộng”, để các điểm hai bên cách ranh giới càng an toàn càng tốt.

## Cơ chế

```text
Feature vector
-> tìm hyperplane tách class
-> tối đa hóa margin
-> dự đoán class theo phía của hyperplane
```

- Trong text classification, feature vector có thể đến từ [[Bag of Words]] hoặc representation sparse khác.
- SVM là discriminative classifier giống [[Logistic Regression]].
- Điểm khác sách nhấn mạnh: SVM nhắm tới hyperplane có margin lớn, còn Logistic Regression học weight/probability distribution.
- SVM có thể học non-linear separation, nhưng thường train lâu hơn.

## Khi dùng trong text classification

- Dùng như một classifier cổ điển để so sánh với [[Naive Bayes Classifier]] và [[Logistic Regression]].
- Hợp để thử khi baseline đơn giản chưa đủ, nhưng phải kiểm soát số feature nếu training chậm.
- Có thể dùng class weight, ví dụ `class_weight="balanced"`, khi dữ liệu bị [[Class Imbalance]].

## Bài học từ Practical NLP

- Sách dùng `LinearSVC(class_weight="balanced")` trong ví dụ economic news.
- Vì SVM train lâu hơn, ví dụ giảm `CountVectorizer(max_features=1000)` thay vì 5,000.
- SVM cải thiện relevant class so với Logistic Regression, nhưng Naive Bayes với feature set nhỏ vẫn tốt nhất trong nhóm thử nghiệm nhỏ.
- Vì vậy, SVM là một giả thuyết model cần kiểm chứng bằng [[Confusion Matrix]], không phải lựa chọn mặc định luôn tốt hơn.

## Liên kết

- [[Text Classification]]
- [[Logistic Regression]]
- [[Naive Bayes Classifier]]
- [[Bag of Words]]
- [[Class Imbalance]]
- [[Confusion Matrix]]
