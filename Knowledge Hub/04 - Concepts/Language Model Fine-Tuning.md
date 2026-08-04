---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
source_sections:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - fine-tuning
  - language-model
  - domain-adaptation
---

# Language Model Fine-Tuning

## Định nghĩa

Language model fine-tuning là quá trình tiếp tục huấn luyện một pretrained language model trên text của domain mục tiêu bằng objective ngôn ngữ, thường chưa cần nhãn task thủ công.

Trong Chapter 09, ý chính là: nếu thiếu labeled data nhưng có nhiều text thô cùng domain, ta có thể fine-tune language model trước để model thích nghi với domain, rồi mới fine-tune classifier khi có nhãn.

## Khác classifier fine-tuning

| Loại fine-tuning | Dữ liệu cần | Mục tiêu học | Khi dùng |
|---|---|---|---|
| Language model fine-tuning | Text thô/unlabeled text | Học ngôn ngữ, thuật ngữ và phân phối domain | Khi có nhiều text nhưng ít nhãn |
| Classifier fine-tuning | Text + label | Học mapping từ input sang label | Khi có đủ nhãn và metric rõ |

Mental model:

```text
Pretrained LM chung
-> Fine-tune trên unlabeled domain text
-> Domain-adapted LM
-> Fine-tune classifier bằng ít labeled examples
```

## Vì sao hữu ích khi thiếu nhãn

Unlabeled text không nói trực tiếp class nào đúng, nhưng vẫn cho model thấy:

- thuật ngữ domain;
- phong cách câu thật;
- phân phối lỗi/ngôn ngữ người dùng;
- cụm từ thường gặp;
- quan hệ ngữ nghĩa trong domain.

Vì vậy language model fine-tuning là một dạng [[Domain Adaptation]]: model học "ngôn ngữ của domain" trước khi học task cụ thể.

## Objective

Objective phụ thuộc loại model:

- encoder/BERT-style model thường dùng [[Masked Language Modeling]];
- decoder/GPT-style model thường dùng [[Causal Language Model|causal language modeling]] hoặc next-token prediction.

Điểm quan trọng: objective tự tạo nhãn từ text, nên có thể dùng unlabeled corpus.

## Rủi ro

- Nếu domain corpus nhỏ hoặc nhiễu, model có thể overfit vào pattern hẹp.
- Nếu corpus lệch với data production, adaptation có thể làm downstream kém hơn.
- Fine-tune quá mạnh có thể làm model quên bớt năng lực tổng quát đã học từ pretraining.
- Vẫn cần labeled validation set để biết domain-adapted model có giúp classifier thật không.

## Cách hiểu bằng lời của tôi

Language model fine-tuning giống như cho model đọc thêm tài liệu nội bộ trước khi bắt nó phân loại. Nó chưa dạy model nhãn nào đúng, nhưng giúp model quen với cách domain đó nói chuyện.

Với bài toán ít nhãn, đây là bước trung gian hợp lý: dùng text chưa nhãn để giảm khoảng cách domain, rồi dùng vài nhãn thật để học decision boundary.

## Câu hỏi review

1. Language model fine-tuning khác classifier fine-tuning ở đâu?
2. Vì sao language model fine-tuning có thể dùng unlabeled data?
3. Khi nào bước này hữu ích hơn fine-tune classifier ngay?
4. Rủi ro của domain-adaptive language model fine-tuning là gì?

## Liên kết

- [[Fine-tuning]]
- [[Pretraining]]
- [[Domain Adaptation]]
- [[Masked Language Modeling]]
- [[Causal Language Model]]
- [[Semi-supervised Learning]]
- [[Few-shot Learning]]
- [[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]
