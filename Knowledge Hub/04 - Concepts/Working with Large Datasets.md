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
  - datasets
  - data-engineering
  - hugging-face
  - nlp
---

# Working with Large Datasets

## Định nghĩa

`Working with Large Datasets` là bài toán xử lý tập dữ liệu quá lớn để đọc hết vào RAM hoặc quá tốn thời gian nếu tokenize, shuffle, map và train theo cách ngây thơ.

## Vì sao quan trọng

- Trong few-shot hoặc semi-supervised learning, ta thường có **ít nhãn nhưng rất nhiều unlabeled text**.
- Giá trị không nằm ở việc “có nhiều file” mà ở khả năng biến lượng text lớn đó thành tín hiệu huấn luyện hữu ích.
- Nếu pipeline dữ liệu chậm hoặc ngốn RAM, bottleneck không còn là model mà là I/O, preprocessing và batching.

## Cần biết

- Không phải mọi dữ liệu lớn đều nên dùng hết; chất lượng và độ khớp domain quan trọng hơn số lượng thô.
- Nên ưu tiên pipeline có thể:
  - đọc theo từng phần hoặc streaming;
  - tokenize theo batch với `map(..., batched=True)`;
  - cache kết quả preprocessing để tránh làm lại;
  - lọc dữ liệu rác, duplicate và mẫu quá dài trước khi train.
- Với [[Hugging Face]], `Datasets` giúp xử lý dataset theo kiểu Arrow-backed, memory mapping và transform theo batch thay vì ép mọi thứ thành list trong Python.

## Mental model

```text
Raw large corpus
-> lọc / deduplicate / giới hạn độ dài
-> tokenize theo batch
-> lưu cache / shard / stream
-> train hoặc LM fine-tuning
-> lấy representation / pseudo-label / downstream classifier
```

## Khi áp dụng

- Có hàng trăm nghìn đến hàng triệu câu unlabeled trong cùng domain.
- Muốn làm [[Language Model Fine-Tuning]] trước khi fine-tune classifier.
- Muốn khai thác corpus lớn cho [[Semi-supervised Learning]] hoặc pseudo-labeling.
- Dataset không vừa RAM hoặc preprocessing quá chậm nếu chạy tuần tự.

## Rủi ro thực tế

- Dữ liệu lớn nhưng nhiễu có thể làm model học lệch domain.
- Tokenization là điểm nghẽn nếu không batch tốt.
- Shuffle toàn bộ dataset lớn có thể đắt về RAM/I/O.
- Pseudo-labeling trên dữ liệu lớn có thể khuếch đại lỗi nếu confidence filtering yếu.

## Cách hiểu bằng lời của tôi

Tập dữ liệu lớn không tự động làm model tốt hơn. Nó chỉ hữu ích khi mình có pipeline đủ tốt để đọc, lọc, tokenize và biến đống text đó thành tín hiệu sạch. Nếu không, mình chỉ đang đổi bài toán “thiếu nhãn” thành bài toán “tắc dữ liệu”.

## Câu hỏi review

1. Vì sao trong few-shot setting, unlabeled corpus lớn vẫn rất đáng giá?
2. Vì sao dữ liệu lớn nhưng lệch domain hoặc nhiều rác có thể gây hại?
3. `map(..., batched=True)` giải quyết bottleneck nào?
4. Khi nào nên nghĩ tới streaming hoặc shard dataset?

## Liên kết

- [[Hugging Face]]
- [[Language Model Fine-Tuning]]
- [[Semi-supervised Learning]]
- [[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]
