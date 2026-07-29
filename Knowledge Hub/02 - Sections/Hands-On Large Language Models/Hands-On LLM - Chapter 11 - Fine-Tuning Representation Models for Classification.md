---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 11
start_page: 446
end_page: 485
estimated_minutes: 95
need_review: true
tags:
  - llm
  - fine-tuning
  - classification
---

# Hands-On LLM - Chapter 11 - Fine-Tuning Representation Models for Classification

## Mục tiêu cần hiểu

- Hiểu supervised fine-tuning pretrained BERT cho classification.
- Biết freezing layers là cách giảm chi phí và rủi ro overfitting.
- Nắm SetFit cho few-shot classification.
- Hiểu continued pretraining bằng masked language modeling.
- Biết fine-tune representation model cho named-entity recognition.

## Định nghĩa quan trọng

- **Fine-tuning**: tiếp tục huấn luyện pretrained model trên task/domain cụ thể.
- **Freezing layers**: giữ nguyên một số layer để chỉ train phần còn lại.
- **Few-shot classification**: phân loại với rất ít ví dụ có nhãn.
- **SetFit**: phương pháp fine-tune sentence transformer hiệu quả với ít nhãn.
- **Masked language modeling**: che token rồi huấn luyện model dự đoán token bị che.
- **Named-entity recognition**: gán nhãn thực thể cho token/span.

## Mental model

Representation model đã học ngôn ngữ tổng quát. Fine-tuning dạy model dùng biểu diễn đó cho nhãn cụ thể. Nếu dữ liệu ít, full fine-tuning có thể quá mạnh và dễ overfit; cần freezing, SetFit hoặc continued pretraining để thích nghi mềm hơn.

## Phần cần biết

- Supervised fine-tuning cần split dữ liệu, metric và error analysis.
- Freezing layers tiết kiệm compute nhưng có thể giảm khả năng thích nghi.
- SetFit tận dụng contrastive learning để học tốt từ ít example.
- Continued pretraining giúp model quen domain trước khi học task.
- NER cần align labels với subtokens.

## Khi áp dụng

- Dùng BERT/encoder model cho classification khi cần latency thấp và output ổn định.
- Dùng SetFit khi có rất ít nhãn.
- Dùng continued pretraining nếu domain vocabulary/style khác dữ liệu gốc.
- Với NER, kiểm tra kỹ mapping giữa token và label.

## Câu hỏi review

1. Fine-tuning khác continued pretraining thế nào?
2. Freezing layers có trade-off gì?
3. SetFit phù hợp hơn full fine-tuning trong trường hợp nào?
4. Vì sao NER phức tạp hơn sequence classification?

## Gợi ý trả lời câu hỏi review

1. Fine-tuning huấn luyện model trên task có nhãn hoặc objective task-specific. Continued pretraining tiếp tục huấn luyện bằng objective nền như masked language modeling trên domain text để model quen domain trước, chưa nhất thiết học nhãn task.
2. Freezing layers giảm compute, memory và rủi ro overfitting, nhưng cũng giảm khả năng model thích nghi sâu với task/domain mới. Freeze quá nhiều có thể làm performance thấp.
3. SetFit phù hợp khi có rất ít dữ liệu nhãn, cần huấn luyện nhanh, và task là sentence/text classification. Nó tận dụng contrastive learning để học từ ít ví dụ hiệu quả hơn full fine-tuning nặng.
4. NER phức tạp hơn vì output nằm ở token/span level, không phải một nhãn cho cả sequence. Cần align label với token/subword, xử lý special tokens, scheme BIO/BILOU và entity boundaries.

## Liên kết

- [[Fine-tuning]]
- [[Representation Model]]
- [[Contrastive Learning]]
- [[Named Entity Recognition]]
