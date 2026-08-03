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
  - few-shot
  - nlp
---

# Few-shot Learning

## Định nghĩa

Few-shot learning là thiết lập học khi mỗi class/task chỉ có rất ít ví dụ gán nhãn.

## Trong NLP

Khi ít nhãn, không nên fine-tune model lớn ngay. Cần baseline để biết tín hiệu nhãn có đủ tốt không và model có overfit không.

## Chiến lược

- Bắt đầu với baseline đơn giản.
- Dùng [[Zero-shot Classification]] nếu chưa có nhãn.
- Dùng embedding lookup hoặc nearest neighbor khi có vài ví dụ đại diện.
- Dùng [[Data Augmentation]] cẩn thận để mở rộng dữ liệu.
- Tận dụng unlabeled data qua [[Semi-supervised Learning]] nếu phù hợp.

## Cách hiểu bằng lời của tôi

Few-shot không phải chỉ là "ít data", mà là tình huống mọi quyết định train/evaluate đều dễ bị nhiễu. Baseline và slice evaluation quan trọng vì vài ví dụ sai có thể làm mình tưởng model tốt hoặc tệ hơn thực tế.

## Liên kết

- [[Intent Detection]]
- [[Text Classification]]
- [[Zero-shot Classification]]
- [[Data Augmentation]]

