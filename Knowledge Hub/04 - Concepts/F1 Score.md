---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
source_sections:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - evaluation
  - question-answering
---

# F1 Score

## Định nghĩa

F1 score là harmonic mean của precision và recall. Trong extractive QA, F1 thường đo overlap token giữa predicted answer và ground truth answer.

## Cách hiểu bằng lời của tôi

F1 mềm hơn [[Exact Match]]. Nếu model trả lời gần đúng nhưng thêm/thiếu vài token, F1 vẫn cho điểm một phần.

```text
prediction: "about 6000 hours"
label:      "6000 hours"
F1: cao hơn 0 vì có overlap "6000 hours"
```

## Công thức

```text
F1 = 2 * precision * recall / (precision + recall)
```

Trong QA:

- `precision`: bao nhiêu token trong prediction cũng có trong label.
- `recall`: bao nhiêu token trong label được prediction bắt được.

## Điểm cần cẩn thận

- F1 có thể cho điểm khá tốt cho câu trả lời vẫn sai về nghĩa.
- Ví dụ prediction overlap số nhưng sai đơn vị vẫn có thể nhận điểm khác 0.
- Vì vậy nên theo dõi F1 cùng [[Exact Match]].

## Khi áp dụng

- Dùng để đánh giá [[Reader]] trong [[Extractive QA]].
- Hữu ích khi có nhiều cách chọn span gần đúng.
- Dùng cùng EM để cân bằng giữa metric strict và metric mềm.

## Câu hỏi review

1. F1 trong extractive QA đo gì?
2. Vì sao F1 mềm hơn Exact Match?
3. Vì sao không nên chỉ nhìn F1?

## Gợi ý trả lời câu hỏi review

1. Nó đo overlap token giữa prediction và label.
2. Vì prediction không cần khớp tuyệt đối vẫn được điểm nếu có token đúng.
3. Vì overlap token không luôn đồng nghĩa với câu trả lời đúng về nghĩa.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Evaluating the Reader]]
- [[Exact Match]]
- [[Reader]]
- [[Extractive QA]]
