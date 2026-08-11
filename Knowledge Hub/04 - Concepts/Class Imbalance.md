---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-10
last_updated: 2026-08-11
tags:
  - concept
  - machine-learning
  - evaluation
---

# Class Imbalance

## Định nghĩa

Class imbalance là tình huống dữ liệu classification có số mẫu giữa các class lệch mạnh, ví dụ class A chiếm 80% còn class B chỉ chiếm 20%.

## Cách hiểu bằng lời của tôi

Khi class bị lệch, model rất dễ học cách “chọn class đông” để có điểm accuracy nhìn có vẻ cao. Vấn đề là class ít mẫu thường lại là class mình quan tâm nhất.

## Vì sao quan trọng

- Accuracy có thể đánh lừa: nếu 80% dữ liệu là non-relevant, model đoán tất cả là non-relevant vẫn đạt khoảng 80% accuracy nhưng gần như vô dụng cho relevant class.
- Cần đọc lỗi theo từng class bằng [[Confusion Matrix|confusion matrix]], precision, recall và F1 khi phù hợp.
- Classifier có thể bị kéo về majority class nếu training data không được xử lý.

## Cách xử lý thường gặp

- Oversampling class ít mẫu.
- Undersampling class nhiều mẫu.
- Dùng class weight, ví dụ `class_weight="balanced"` trong một số classifier như [[Logistic Regression]].
- Thu thập thêm dữ liệu cho class ít mẫu nếu có thể.
- Chọn metric phản ánh đúng chi phí sai của use case.
- Practical NLP nhấn mạnh balanced training data là lời khuyên production quan trọng: khi category không được đại diện tương đối đều, classifier dễ trở thành biased classifier.
- Các hướng xử lý trong sách gồm collecting more data, resampling và weight balancing.

## Liên kết

- [[Text Classification]]
- [[NLP Pipeline]]
- [[Confusion Matrix]]
- [[Logistic Regression]]
- [[Active Learning]]
