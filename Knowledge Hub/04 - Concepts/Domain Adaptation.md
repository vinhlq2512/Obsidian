---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
source_sections:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
first_seen: 2026-08-01
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - transfer-learning
---

# Domain Adaptation

## Định nghĩa

Domain adaptation là quá trình điều chỉnh model hoặc pipeline để hoạt động tốt hơn trên một domain cụ thể khác với dữ liệu gốc mà model được huấn luyện.

## Cách hiểu bằng lời của tôi

Model pretrained có hiểu ngôn ngữ chung, nhưng domain thật có thuật ngữ, cách viết, kiểu câu hỏi và kiểu đáp án riêng. Domain adaptation giúp giảm khoảng cách đó.

## Cần biết

- Trong QA, domain adaptation có thể cần dữ liệu câu hỏi/câu trả lời cùng domain.
- Với review-based QA, ngôn ngữ review thường ngắn, chủ quan, nhiều nhiễu và không giống văn bản Wikipedia/SQuAD.
- Có thể cần fine-tune reader, cải thiện retriever, hoặc chuẩn hóa dữ liệu review.
- Reader fine-tuned trên [[SQuAD]] có thể đạt metric tốt trên Wikipedia-style QA nhưng giảm mạnh trên [[SubjQA]] vì khác domain và mức độ chủ quan.
- Với retriever, dense model cũng có thể cần fine-tune/domain adaptation nếu embedding similarity học từ domain khác không phản ánh đúng relevance trong review.
- Trong few/no-label classification, [[Language Model Fine-Tuning]] trên unlabeled domain text là một cách domain adaptation trước khi học classifier bằng ít nhãn.

## Language model fine-tuning cho domain adaptation

```text
General pretrained LM
-> Unlabeled domain corpus
-> Fine-tune bằng objective language modeling
-> Domain-adapted LM
-> Downstream classifier / QA / retriever
```

Điểm hay là unlabeled domain corpus thường rẻ hơn labeled data. Model có thể học thuật ngữ, style và phân phối câu của domain trước khi cần nhãn task cụ thể.

Điểm cần kiểm tra: adaptation chỉ đáng giữ nếu downstream metric tốt hơn trên validation set có nhãn thật.

## Khi áp dụng

- Khi [[Evaluating the Reader]] cho thấy [[Exact Match]] và [[F1 Score]] thấp trên domain mới.
- Khi [[Dense Passage Retrieval]] không cải thiện [[Recall@k]] so với baseline [[BM25]].
- Khi user-generated content khác nhiều với dữ liệu pretraining/fine-tuning ban đầu.

## Liên kết

- [[Transfer Learning]]
- [[Fine-tuning]]
- [[Language Model Fine-Tuning]]
- [[Question Answering]]
- [[Building a Review-Based QA System]]
- [[SubjQA]]
- [[SQuAD]]
- [[Evaluating the Reader]]
- [[Dense Passage Retrieval]]
- [[NLP Transformers - Chapter 07 - Question Answering]]
