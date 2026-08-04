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

Trong ngữ cảnh Chapter 09 của [[Natural Language Processing with Transformers]], few-shot nằm giữa hai cực:

```text
zero-shot: chưa có ví dụ gán nhãn trực tiếp
few-shot: có vài ví dụ mỗi label
full supervised fine-tuning: có đủ dữ liệu gán nhãn để train/evaluate ổn định hơn
```

## Trong NLP

Khi ít nhãn, không nên fine-tune model lớn ngay. Cần baseline để biết tín hiệu nhãn có đủ tốt không và model có overfit không.

## Chiến lược

- Bắt đầu với baseline đơn giản.
- Dùng [[Zero-shot Classification]] nếu chưa có nhãn.
- Dùng embedding lookup hoặc nearest neighbor khi có vài ví dụ đại diện.
- Dùng [[Data Augmentation]] cẩn thận để mở rộng dữ liệu.
- Tận dụng unlabeled data qua [[Semi-supervised Learning]] nếu phù hợp.

## Khi áp dụng

Few-shot hữu ích khi:

- mỗi label chỉ có một số ít ví dụ đáng tin;
- cần prototype nhanh trước khi đầu tư gán nhãn lớn;
- muốn kiểm tra label taxonomy có phân biệt được không;
- domain mới khiến zero-shot classification chưa đủ ổn.

Few-shot không nên được hiểu là cứ fine-tune ngay với vài ví dụ. Thường nên thử theo thứ tự:

```text
Zero-shot baseline
-> Few-shot embedding lookup / nearest neighbor
-> Data augmentation hoặc prompt examples
-> Fine-tune khi có benchmark đủ tin cậy
```

## Rủi ro

- Dễ overfit vào vài ví dụ ban đầu.
- Một ví dụ sai label có ảnh hưởng lớn hơn nhiều so với setting nhiều dữ liệu.
- Evaluation nhiễu vì validation/test set nhỏ.
- Các label gần nghĩa nhau cần mô tả và ví dụ đại diện rõ hơn.

## Cách hiểu bằng lời của tôi

Few-shot không phải chỉ là "ít data", mà là tình huống mọi quyết định train/evaluate đều dễ bị nhiễu. Baseline và slice evaluation quan trọng vì vài ví dụ sai có thể làm mình tưởng model tốt hoặc tệ hơn thực tế.

Few-shot tốt nhất khi mình xem vài ví dụ như "neo nghĩa" cho label, không phải như một dataset đầy đủ. Với intent detection, vài câu mẫu giúp model hiểu `billing_issue` khác `refund_request` thế nào trong sản phẩm cụ thể.

## Câu hỏi review

1. Few-shot khác zero-shot ở đâu?
2. Vì sao không nên fine-tune ngay khi chỉ có vài ví dụ?
3. Embedding lookup dùng few-shot examples như thế nào?
4. Vì sao few-shot evaluation dễ bị nhiễu?

## Liên kết

- [[Intent Detection]]
- [[Text Classification]]
- [[Zero-shot Learning]]
- [[Zero-shot Classification]]
- [[Data Augmentation]]
