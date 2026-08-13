---
type: concept
status: developing
sources:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
  - "[[Practical Natural Language Processing]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Bài toán NK-CRE]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#Continual Few-Shot Relation Extraction là gì?]]"
first_seen: 2026-08-03
last_updated: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - few-shot
  - nlp
---

# Few-shot Learning

## Định nghĩa

Few-shot learning là thiết lập học khi mỗi class/task chỉ có rất ít ví dụ gán nhãn.

Trong ngữ cảnh Chapter 09 của [[01 - Books/Natural Language Processing with Transformers|Natural Language Processing with Transformers]], few-shot nằm giữa hai cực:

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
- Dùng [[Active Learning]] để ưu tiên gán nhãn những mẫu model đang không chắc chắn.
- Dùng [[Domain Adaptation]] khi có nhiều dữ liệu/unlabeled text ở target domain nhưng ít nhãn.

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

## Few-shot trong continual learning

[[Continual Few-Shot Relation Extraction]] cho thấy “ít data” và “học liên tục” khuếch đại lẫn nhau:

- prototype của class mới được ước lượng từ rất ít points nên có variance cao;
- update nhiễu từ class mới làm class cũ dễ quên hơn;
- replay buffer mỗi class nhỏ nên model có thể overfit memory;
- relation gần nghĩa cần hard-negative/contrastive objective;
- task đầu có nhiều data có thể làm benchmark trông dễ hơn thực tế.

ConPL vì vậy đề xuất NK-CRE: mọi task, kể cả task đầu, đều N-way K-shot. Khi đọc một benchmark few-shot continual, cần kiểm tra riêng số examples của base task thay vì chỉ nhìn tên setting.

## Ba cách bù tín hiệu khi K nhỏ

```text
[[Prototype Learning]] -> nén class thành điểm neo
[[Prompt Tuning]] -> khai thác prior của pretrained model
[[Data Augmentation]] -> mở rộng support quan sát được
```

Mỗi cách đều có bias: prototype che multimodality, prompt phụ thuộc template/init, augmentation có thể đổi nhãn. Kết hợp không tự đảm bảo tốt; cần ablation theo dataset và shot count.

## Câu hỏi review

1. Few-shot khác zero-shot ở đâu?
2. Vì sao không nên fine-tune ngay khi chỉ có vài ví dụ?
3. Embedding lookup dùng few-shot examples như thế nào?
4. Vì sao few-shot evaluation dễ bị nhiễu?
5. Vì sao task đầu nhiều data làm continual few-shot benchmark lạc quan?
6. Prototype, prompt và augmentation bù thiếu data theo ba cách khác nhau ra sao?

## Liên kết

- [[Intent Detection]]
- [[Text Classification]]
- [[Zero-shot Learning]]
- [[Zero-shot Classification]]
- [[Data Augmentation]]
- [[Active Learning]]
- [[Domain Adaptation]]
- [[Continual Few-Shot Relation Extraction]]
- [[Continual Learning]]
- [[Prototype Learning]]
- [[Prompt Tuning]]
- [[Catastrophic Forgetting]]
