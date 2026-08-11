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

# Active Learning

## Định nghĩa

Active learning là chiến lược chọn những data points đáng gán nhãn nhất để cải thiện model khi ngân sách annotation bị giới hạn.

## Cách hiểu bằng lời của tôi

Không phải mẫu nào cũng dạy model nhiều như nhau. Nếu phải nhờ người gán nhãn ít mẫu, nên ưu tiên những mẫu model đang phân vân, vì chúng thường nằm gần vùng quyết định khó.

## Workflow

```text
Labeled data ít
-> train classifier ban đầu
-> predict trên unlabeled/new data
-> chọn mẫu model không chắc chắn
-> human annotate
-> thêm vào training set
-> retrain
-> lặp lại
```

- Practical NLP dùng active learning cho tình huống text classification có ít labeled data hoặc dữ liệu bị lệch class, trong khi annotation thủ công quá tốn thời gian.
- Câu hỏi trung tâm: nếu có 1,000 data points nhưng chỉ gán nhãn được 100, nên chọn 100 điểm nào?
- Sách nhấn mạnh các điểm model ít tự tin thường đóng góp nhiều hơn cho chất lượng classifier.
- Prodigy là ví dụ tool được sách nhắc để hỗ trợ active learning cho text classification.

## Rủi ro

- Nếu uncertainty của model ban đầu kém tin cậy, vòng lặp có thể chọn mẫu không thật sự hữu ích.
- Human annotation vẫn là nút thắt chi phí và chất lượng.
- Cần theo dõi performance trên evaluation set cố định, không chỉ nhìn số mẫu đã gán nhãn.

## Liên kết

- [[Text Classification]]
- [[Few-shot Learning]]
- [[Weak Supervision]]
- [[Domain Adaptation]]
- [[Class Imbalance]]
