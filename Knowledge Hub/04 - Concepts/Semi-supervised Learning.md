---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
source_sections:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - weak-supervision
  - nlp
---

# Semi-supervised Learning

## Định nghĩa

Semi-supervised learning là thiết lập học kết hợp một lượng nhỏ dữ liệu có nhãn với lượng lớn dữ liệu chưa gán nhãn.

## Vì sao quan trọng

Trong nhiều bài toán NLP thực tế, unlabeled text rẻ hơn labeled data rất nhiều. Chapter 09 nhấn mạnh rằng unlabeled data vẫn có thể hữu ích khi thiếu nhãn.

## Khi chưa có labeled data

Nếu hoàn toàn chưa có nhãn, unlabeled data chưa đủ để supervised fine-tuning, nhưng vẫn giúp hiểu bài toán:

- đọc sample thật để phát hiện intent/topic tự nhiên;
- dùng [[Embedding]] để clustering và tìm nhóm câu gần nhau;
- chọn các sample đại diện để gán nhãn thủ công trước;
- dùng [[Zero-shot Classification]] để tạo baseline hoặc pseudo-label ban đầu;
- sau khi có một ít nhãn thật, mới chuyển dần sang semi-supervised learning.

Workflow:

```text
Unlabeled corpus
-> Explore / cluster / zero-shot label
-> Human labels cho một tập nhỏ
-> Pseudo-label hoặc semi-supervised training
-> Evaluate bằng labeled set thật
```

Điểm cần cẩn thận: pseudo-label từ model có thể khuếch đại lỗi. Nếu model zero-shot nhầm có hệ thống, training tiếp trên pseudo-label đó sẽ làm lỗi ổn định hơn chứ không tự biến thành đúng.

## Cách hiểu bằng lời của tôi

Không có nhãn không có nghĩa là không có tín hiệu. Unlabeled data có thể giúp model hiểu domain, phân phối câu thật, hoặc tạo nhãn giả để mở rộng training.

Nhưng unlabeled data không thay thế ground truth. Mình vẫn cần một tập nhỏ có nhãn thật để biết pseudo-label hoặc clustering có đáng tin không.

## Liên kết

- [[Few-shot Learning]]
- [[Intent Detection]]
- [[Text Classification]]
- [[Zero-shot Classification]]
- [[Embedding]]
