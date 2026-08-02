---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - nlp
  - ner
  - evaluation
---

# Performance Measures for NER

## Định nghĩa

Performance measures for NER là các metric dùng để đánh giá model nhận diện thực thể, thường tập trung vào precision, recall và F1 ở mức entity span thay vì chỉ token-level accuracy.

## Cách hiểu bằng lời của tôi

NER không chỉ cần biết token nào có nhãn nào, mà cần nhận đúng cả cụm thực thể và loại thực thể. Nếu model dự đoán sai ranh giới hoặc sai type, kết quả nên bị xem là lỗi, dù một vài token riêng lẻ có thể trông đúng.

## Vì sao không chỉ dùng accuracy

Trong NER, phần lớn token thường là `O`, nghĩa là không thuộc entity nào. Nếu dùng accuracy đơn thuần, model có thể đạt điểm cao bằng cách đoán nhiều token là `O`, nhưng vẫn bỏ sót các entity quan trọng.

Vì vậy nên dùng:

- precision
- recall
- F1
- per-entity-type scores
- per-language scores nếu là multilingual NER

## Precision

Precision đo độ đúng của những entity mà model đã dự đoán.

```text
precision = true_positive / (true_positive + false_positive)
```

Cách hiểu: trong tất cả entity model nói là có, bao nhiêu entity thật sự đúng.

Precision thấp thường nghĩa là model hay nhận nhầm non-entity thành entity, hoặc gán sai type.

## Recall

Recall đo khả năng tìm đủ entity thật.

```text
recall = true_positive / (true_positive + false_negative)
```

Cách hiểu: trong tất cả entity thật có trong dữ liệu, model tìm được bao nhiêu.

Recall thấp thường nghĩa là model bỏ sót entity.

## F1

F1 cân bằng precision và recall.

```text
F1 = 2 * precision * recall / (precision + recall)
```

F1 hữu ích để so sánh model, nhưng không thay thế error analysis. Hai model có F1 gần nhau vẫn có thể lỗi rất khác nhau: một model precision cao recall thấp, model kia recall cao precision thấp.

## Entity-level evaluation

Với entity-level evaluation, một dự đoán thường chỉ được xem là đúng khi:

- ranh giới entity đúng.
- entity type đúng.
- sequence BIO/BILOU hợp lệ.

Ví dụ gold:

```text
Nguyễn/B-PER Nhật/I-PER Ánh/I-PER sinh/O tại/O Quảng/B-LOC Nam/I-LOC
```

Nếu model dự đoán `Nguyễn Nhật` là `PER` nhưng bỏ mất `Ánh`, thì entity `PER` này sai ở ranh giới.

## Seqeval

`seqeval` là thư viện thường dùng để tính metric cho sequence labeling như NER.

Luồng tính metric:

```text
prediction logits
-> argmax thành label IDs
-> bỏ các vị trí label = -100
-> map IDs về label strings
-> seqeval precision/recall/F1/accuracy
```

Điểm cần nhớ: phải bỏ `-100` trước khi đưa vào metric, vì đó là vị trí special tokens hoặc subword phụ không nên tính.

## Với multilingual NER

Ngoài điểm tổng, nên xem:

- F1 theo từng ngôn ngữ.
- F1 theo từng entity type.
- lỗi ranh giới entity.
- lỗi type entity.
- lỗi do tokenizer tách subword.

Điểm trung bình có thể che vấn đề: model tốt ở source language nhưng yếu ở target language, hoặc tốt với `PER` nhưng kém với `ORG`.

## Cần biết

- Accuracy dễ gây hiểu nhầm trong NER vì nhãn `O` quá nhiều.
- Precision cao không có nghĩa model tìm đủ entity.
- Recall cao không có nghĩa mọi entity dự đoán đều đáng tin.
- F1 là metric tổng tốt để so sánh, nhưng phải đi kèm per-class/per-language analysis.
- [[Error Analysis for NER]] là bước đọc ví dụ sai để giải thích vì sao precision/recall/F1 cao hoặc thấp.
- Với [[Tokenizing Texts for NER]], alignment sai sẽ làm metric xấu hoặc khó diễn giải.

## Liên kết

- [[Named Entity Recognition]]
- [[Error Analysis for NER]]
- [[Tokenizing Texts for NER]]
- [[Custom Model for Token Classification]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
