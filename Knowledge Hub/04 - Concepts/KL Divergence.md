---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
source_sections:
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - probability
  - loss-function
  - transformer
---

# KL Divergence

## Định nghĩa

Kullback-Leibler divergence, hay KL divergence, là thước đo mức khác nhau giữa hai phân phối xác suất.

Trong [[Knowledge Distillation]], KL divergence thường dùng để đo student distribution khác teacher distribution bao nhiêu.

## Công thức

Với hai phân phối rời rạc $P$ và $Q$ trên cùng tập outcome:

$$
D_{KL}(P || Q) = \sum_i P(i)\log\frac{P(i)}{Q(i)}
$$

## Thành phần

- $P(i)$: xác suất của outcome $i$ theo phân phối tham chiếu, ví dụ teacher.
- $Q(i)$: xác suất của outcome $i$ theo phân phối cần học, ví dụ student.
- $D_{KL}(P || Q)$: mức student lệch khỏi teacher nếu đặt $P$ là teacher distribution.

## Trực giác

KL divergence hỏi: nếu teacher tin vào phân phối $P$, student dùng phân phối $Q$ thì student "lệch" khỏi teacher bao nhiêu?

Nếu $P$ và $Q$ giống nhau, KL divergence bằng 0. Nếu $Q$ gán xác suất thấp cho outcome mà $P$ cho là quan trọng, KL divergence tăng.

## Lưu ý quan trọng

KL divergence không đối xứng:

$$
D_{KL}(P || Q) \neq D_{KL}(Q || P)
$$

Vì vậy cần chú ý chiều. Trong distillation, thường muốn student bắt chước teacher, nên đọc là đo khoảng cách từ teacher distribution sang student distribution.

## Trong knowledge distillation

```text
Teacher logits
-> softmax với temperature
-> teacher probability distribution P

Student logits
-> softmax với temperature
-> student probability distribution Q

Distillation loss
-> KL divergence giữa P và Q
```

Mục tiêu training là giảm KL divergence để phân phối dự đoán của student gần với teacher hơn.

## Cách hiểu bằng lời của tôi

KL divergence là cách nói bằng số rằng hai model đang "tin" khác nhau đến mức nào. Trong distillation, teacher không chỉ đưa nhãn đúng, mà đưa cả phân phối niềm tin; student học bằng cách làm phân phối của mình giống teacher hơn.

## Câu hỏi review

1. KL divergence đo sự khác nhau giữa hai thứ gì?
2. Vì sao KL divergence phù hợp với soft labels trong knowledge distillation?
3. Vì sao phải chú ý chiều $D_{KL}(P || Q)$?
4. Khi $P$ và $Q$ giống hệt nhau thì KL divergence bằng bao nhiêu?

## Liên kết

- [[Knowledge Distillation]]
- [[Loss Function]]
- [[Model Benchmarking]]

