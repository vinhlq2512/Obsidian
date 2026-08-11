---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-11
last_updated: 2026-08-11
tags:
  - concept
  - machine-learning
  - nlp
---

# Weak Supervision

## Định nghĩa

Weak supervision là cách tạo nhãn huấn luyện bằng tín hiệu gián tiếp, rule, pattern hoặc labeling functions thay vì gán nhãn thủ công từng ví dụ một cách đầy đủ.

## Cách hiểu bằng lời của tôi

Khi chưa có dataset có nhãn, mình có thể dùng hiểu biết nghiệp vụ để viết các rule tạo nhãn tạm. Nhãn này không hoàn hảo, nhưng đủ để khởi động classifier và mở rộng dữ liệu trước khi đầu tư gán nhãn lớn.

## Khi dùng cho text classification

```text
Unlabeled texts
-> rule / pattern / labeling function
-> noisy labels
-> classifier ban đầu
-> human evaluation / refinement
```

- Practical NLP gọi hướng này là bootstrapping hoặc weak supervision trong tình huống chưa có training data.
- Ví dụ complaint routing: billing request có thể chứa từ liên quan tới `bill` hoặc số tiền; delivery request có thể chứa từ liên quan tới shipping hoặc delay.
- Các pattern này tạo annotated dataset nhỏ và có thể nhiễu, rồi dùng để train classifier hoặc annotate dữ liệu lớn hơn.
- Snorkel là ví dụ công cụ được sách nhắc tới để triển khai weak supervision cho classification.

## Rủi ro

- Rule có thể encode bias hoặc bỏ sót cách diễn đạt không nằm trong pattern.
- Noisy labels có thể làm classifier học lỗi của rule thay vì học task thật.
- Vẫn cần một tập evaluation có nhãn đáng tin để kiểm tra chất lượng.

## Liên kết

- [[Text Classification]]
- [[Semi-supervised Learning]]
- [[Few-shot Learning]]
- [[NLP Pipeline]]
