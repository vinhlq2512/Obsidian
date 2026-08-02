---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 11 - Fine-Tuning Representation Models for Classification]]"
  - "[[Hands-On LLM - Chapter 12 - Fine-Tuning Generation Models]]"
tags:
  - concept
  - fine-tuning
  - llm
---

# Fine-tuning

## Định nghĩa

Fine-tuning là quá trình tiếp tục huấn luyện pretrained model trên dữ liệu của task hoặc domain cụ thể.

## Cách hiểu bằng lời của tôi

Pretraining cho model kiến thức/ngôn ngữ nền. Fine-tuning dạy model dùng nền đó cho hành vi cụ thể: phân loại nhãn, nhận diện thực thể, trả lời theo format, hoặc làm theo instruction.

## Cần biết

- Fine-tuning cần dữ liệu chất lượng và metric rõ.
- Full fine-tuning cập nhật toàn bộ model, tốn compute hơn.
- PEFT/LoRA chỉ học phần adapter nhỏ, phù hợp tài nguyên hạn chế.
- [[Fine-Tuning XLM-RoBERTa]] là ví dụ fine-tuning encoder multilingual cho token classification/NER.
- Nếu chỉ thiếu kiến thức ngoài, RAG có thể tốt hơn fine-tuning.

## Liên kết

- [[Parameter-Efficient Fine-Tuning]]
- [[Fine-Tuning XLM-RoBERTa]]
- [[Representation Model]]
- [[Generative Model]]
- [[DPO]]
