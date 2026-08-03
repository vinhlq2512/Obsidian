---
type: concept
status: seed
sources:
  - "[[CS224N 2026 - Lecture 07 - Pretraining]]"
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
source_sections:
  - "[[CS224N 2026 - Lecture 07 - Pretraining]]"
  - "[[NLP Transformers - Chapter 08 - Making Transformers Efficient in Production]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - pretraining
  - transformer
  - llm
---

# Pretraining

## Định nghĩa

Pretraining là giai đoạn huấn luyện model trên dữ liệu lớn trước khi đưa model vào một downstream task cụ thể.

Trong NLP/LLM, dữ liệu pretraining thường là text thô hoặc dữ liệu tự giám sát. Model không cần nhãn thủ công cho từng task; objective tự tạo tín hiệu học từ chính dữ liệu.

## Mục tiêu

Pretraining giúp model học:

- thống kê ngôn ngữ;
- cú pháp và ngữ nghĩa;
- biểu diễn từ/câu/ngữ cảnh;
- tri thức nền xuất hiện trong corpus;
- khả năng dự đoán token hoặc phần bị che.

Sau pretraining, model thường được dùng tiếp qua [[Fine-tuning]], instruction tuning, prompting, hoặc các kỹ thuật thích nghi tham số như [[LoRA]] / [[QLoRA]].

## Objective phổ biến

Với encoder như BERT:

- dùng [[Masked Language Modeling]];
- che một số token;
- yêu cầu model dự đoán token bị che từ ngữ cảnh hai chiều.

Với decoder/generative model:

- dùng next-token prediction;
- model dự đoán token tiếp theo từ các token trước đó;
- đây là nền của [[Autoregressive Language Model]].

## Pretraining và transfer learning

Pretraining tạo năng lực tổng quát. Downstream adaptation biến năng lực đó thành hành vi cụ thể.

```text
Large corpus
-> Pretraining objective
-> Base pretrained model
-> Fine-tuning / prompting / alignment
-> Task behavior
```

Nếu không có pretraining, mỗi task phải học từ đầu với dữ liệu gán nhãn ít hơn rất nhiều. Đây là lý do [[Transfer Learning]] trở thành trung tâm của Transformer hiện đại.

## Pretraining và knowledge distillation

Trong [[Knowledge Distillation]], pretraining cũng có thể là nơi truyền năng lực từ teacher sang student.

Thay vì chỉ distill sau khi teacher đã fine-tune cho một task, ta có thể dùng teacher pretrained lớn chạy trên unlabeled corpus và sinh logits/soft targets. Student nhỏ học từ pretraining objective gốc cộng với distillation loss, thường dùng [[KL Divergence]] để khớp phân phối của teacher.

```text
Teacher pretrained lớn
-> Unlabeled corpus
-> Soft targets / logits
-> Student pretrained nhỏ hơn
-> Fine-tune downstream
```

Điểm mạnh là student nhận được tín hiệu mềm và giàu thông tin hơn nhãn tự giám sát đơn thuần. Điểm yếu là phải chạy teacher trên lượng dữ liệu lớn, nên chi phí tiền xử lý/training có thể cao.

## Cách hiểu bằng lời của tôi

Pretraining là lúc model học "nền ngôn ngữ" trước khi học làm một việc cụ thể. Fine-tuning giống như dạy nghề, còn pretraining giống như dạy ngôn ngữ, pattern và tri thức nền.

Pretraining distillation là phiên bản nén của giai đoạn này: dùng model lớn làm teacher để tạo một base model nhỏ hơn, sau đó mới đem base model đó đi fine-tune hoặc deploy.

## Câu hỏi review

1. Pretraining khác fine-tuning ở dữ liệu và mục tiêu như thế nào?
2. Vì sao pretraining có thể dùng dữ liệu chưa gán nhãn?
3. Masked language modeling và next-token prediction khác nhau ở đâu?
4. Pretraining hỗ trợ transfer learning như thế nào?
5. Knowledge distillation for pretraining truyền cái gì từ teacher sang student?

## Liên kết

- [[Fine-tuning]]
- [[Transfer Learning]]
- [[Masked Language Modeling]]
- [[Autoregressive Language Model]]
- [[Knowledge Distillation]]
- [[KL Divergence]]
