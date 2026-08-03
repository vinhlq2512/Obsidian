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
  - text-classification
  - nlp
  - few-shot
---

# Intent Detection

## Định nghĩa

Intent detection là một dạng [[Text Classification]] trong đó model nhận một câu người dùng và dự đoán ý định phía sau câu đó.

Ví dụ:

```text
"I forgot my password"
-> reset_password

"Where is my order?"
-> track_order
```

## Vì sao dùng làm case study

Trong Chapter 09, intent detection là case study tốt cho bài toán ít nhãn vì:

- Nhãn thường là các intent cụ thể của sản phẩm.
- Mỗi intent có thể có rất ít ví dụ thật.
- Câu người dùng đa dạng về cách diễn đạt nhưng cùng mang một ý định.
- Cần baseline trước khi quyết định fine-tune Transformer.

## Cơ chế bài toán

```text
Utterance của user
-> Encoder hoặc embedding model
-> Classifier / nearest-neighbor / zero-shot head
-> Intent label
```

## Khi ít hoặc không có nhãn

Các hướng thường thử trước:

- [[Zero-shot Classification]]: dùng nhãn intent như candidate labels.
- [[Few-shot Learning]]: bắt đầu với vài ví dụ mỗi intent.
- Embedding lookup: tìm utterance gần nhất trong embedding space.
- [[Data Augmentation]]: tạo thêm biến thể câu hỏi cho từng intent.
- [[Semi-supervised Learning]]: tận dụng unlabeled utterances nếu có.

## Cách hiểu bằng lời của tôi

Intent detection là bài toán "người dùng đang muốn làm gì?". Điểm khó không chỉ là hiểu câu, mà là ánh xạ câu đó vào taxonomy intent đúng của sản phẩm, trong khi dữ liệu gán nhãn thường ít và không phủ hết cách người dùng nói thật.

## Câu hỏi review

1. Intent detection khác sentiment classification ở đâu?
2. Vì sao intent detection dễ rơi vào bài toán ít nhãn?
3. Khi chưa có nhiều nhãn, baseline nào nên thử trước?
4. Embedding lookup hữu ích như thế nào cho intent detection?

## Liên kết

- [[Text Classification]]
- [[Few-shot Learning]]
- [[Zero-shot Classification]]
- [[Data Augmentation]]
- [[Semi-supervised Learning]]
- [[Embedding]]

