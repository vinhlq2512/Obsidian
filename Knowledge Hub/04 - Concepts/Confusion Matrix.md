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
  - evaluation
---

# Confusion Matrix

## Định nghĩa

Confusion matrix là bảng so sánh label thật với label model dự đoán, cho biết model đúng/sai ở từng class như thế nào.

## Cách hiểu bằng lời của tôi

Accuracy trả lời “đúng bao nhiêu phần trăm?”. Confusion matrix trả lời câu quan trọng hơn: “đúng ở class nào, sai ở class nào, và kiểu sai đó có đáng lo không?”.

## Cơ chế

```text
Actual class
-> Predicted class
-> đếm số mẫu cho từng cặp actual/predicted
-> đọc lỗi theo từng class
```

Với binary classification, có thể đọc thành:

```text
true positive / false positive
false negative / true negative
```

Điểm cần nhớ: tên positive/negative phụ thuộc vào class mình chọn làm class quan tâm.

## Khi dùng cho text classification

- Dùng để hiểu model đang nhầm class nào với class nào.
- Hữu ích hơn accuracy khi có [[Class Imbalance]].
- Giúp quyết định nên đổi feature, đổi classifier, xử lý imbalance hay đổi metric.
- Nên đọc cùng business cost: bỏ sót class quan trọng có thể tệ hơn báo động nhầm.

## Bài học từ Practical NLP

- Dataset economic news bị lệch: non-relevant nhiều hơn relevant.
- [[Naive Bayes Classifier]] nhận diện non-relevant khá tốt nhưng relevant yếu hơn.
- Khi giảm số feature, average score giảm nhưng relevant class cải thiện mạnh hơn.
- Vì vậy không thể kết luận model tốt/xấu chỉ từ accuracy; phải đọc lỗi theo class trong confusion matrix.

## Liên kết

- [[Text Classification]]
- [[Class Imbalance]]
- [[Naive Bayes Classifier]]
- [[Bag of Words]]
