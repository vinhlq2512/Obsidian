---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - nlp
  - multilingual
  - transfer-learning
---

# Cross-Lingual Transfer

## Định nghĩa

Cross-lingual transfer là khả năng chuyển tri thức hoặc năng lực học được từ một ngôn ngữ nguồn sang một ngôn ngữ đích, thường để giảm nhu cầu dữ liệu gán nhãn ở ngôn ngữ đích.

## Cách hiểu bằng lời của tôi

Nếu mình có nhiều dữ liệu NER tiếng Anh nhưng ít dữ liệu tiếng Việt, cross-lingual transfer hỏi rằng: model đã học từ tiếng Anh có giúp nhận diện thực thể trong tiếng Việt không? Với [[Multilingual Transformer]] như XLM-R, hy vọng là representation đa ngôn ngữ đủ chia sẻ để một phần năng lực này chuyển được.

## Mental model

```text
source language có nhãn
-> fine-tune multilingual model
-> evaluate/predict trên target language
-> phân tích transfer theo metric và lỗi
```

## Trong multilingual NER

Ví dụ:

- Fine-tune XLM-R trên NER tiếng Anh.
- Dùng cùng model để predict NER tiếng Việt.
- Đánh giá `PER`, `ORG`, `LOC` bằng entity-level F1.
- Làm [[Error Analysis for NER]] để xem model lỗi do ranh giới, type, tokenizer hay domain.

## Zero-shot vs target adaptation

- **Zero-shot cross-lingual transfer**: không dùng dữ liệu gán nhãn của target language khi fine-tune. Fine-tune trên source language, predict trực tiếp trên target language.
- **Few-shot/target adaptation**: có một ít dữ liệu target language để fine-tune thêm, tune hyperparameters hoặc đánh giá tốt hơn.

Zero-shot hữu ích khi target language gần như không có nhãn. Target adaptation thường tốt hơn nếu có thể lấy một ít nhãn chất lượng.

## Vì sao có thể hoạt động

Cross-lingual transfer dựa vào:

- multilingual pretraining.
- shared tokenizer hoặc subword vocabulary.
- shared model parameters.
- pattern ngôn ngữ và entity context có phần giống nhau.
- label schema giống nhau giữa source và target.

Ví dụ, tên người hoặc địa danh thường xuất hiện trong những ngữ cảnh có tín hiệu tương tự, dù ngôn ngữ khác nhau.

## Vì sao có thể thất bại

- Tokenizer tách target language thành quá nhiều subword.
- Source và target khác domain.
- Entity surface form khác nhiều.
- Label guideline không nhất quán giữa các ngôn ngữ.
- Ngôn ngữ target ít xuất hiện trong pretraining.
- Script, morphology hoặc word order khác làm representation kém chia sẻ.

## Cần biết

- Cross-lingual transfer không đồng nghĩa với translation; model không nhất thiết dịch câu, mà dùng representation chung để xử lý task.
- Điểm trung bình có thể che lỗi: cần xem theo ngôn ngữ và entity type.
- [[Zero-shot Learning]] là một dạng quan trọng của cross-lingual transfer khi không dùng nhãn target language.
- [[Fine-Tuning XLM-RoBERTa]] là workflow thực tế để thử cross-lingual transfer cho NER.
- Thành công của transfer cần được kiểm chứng bằng [[Performance Measures for NER]] và error analysis.

## Liên kết

- [[Transfer Learning]]
- [[Multilingual Transformer]]
- [[Zero-shot Learning]]
- [[Fine-Tuning XLM-RoBERTa]]
- [[Performance Measures for NER]]
- [[Error Analysis for NER]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
