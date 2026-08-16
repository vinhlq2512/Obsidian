---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 11 - Fine-Tuning Representation Models for Classification]]"
  - "[[Hands-On LLM - Chapter 12 - Fine-Tuning Generation Models]]"
  - "[[2025-09-24_how-fine-tuning-transforms-generic-ai-models-into-specialist]]"
last_updated: 2026-08-16
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

## Fine-tuning language model vs classifier

Không phải mọi fine-tuning đều cần nhãn task ngay từ đầu.

- [[Language Model Fine-Tuning]] tiếp tục huấn luyện model bằng objective ngôn ngữ trên text thô/unlabeled text, thường để làm [[Domain Adaptation]].
- [[Classifier Fine-Tuning]] dùng dữ liệu có nhãn để học decision boundary cho task phân loại.

Trong few/no-label setting, có thể fine-tune language model trên domain corpus trước, rồi mới fine-tune classifier bằng ít labeled examples.

```text
Pretrained model
-> LM fine-tuning trên unlabeled domain text
-> Classifier fine-tuning trên ít labels
```

## Cần biết

- Fine-tuning cần dữ liệu chất lượng và metric rõ.
- Full fine-tuning cập nhật toàn bộ model, tốn compute hơn.
- PEFT/LoRA chỉ học phần adapter nhỏ, phù hợp tài nguyên hạn chế.
- [[Fine-Tuning XLM-RoBERTa]] là ví dụ fine-tuning encoder multilingual cho token classification/NER.
- Nếu chỉ thiếu kiến thức ngoài, RAG có thể tốt hơn fine-tuning.
- Với language model fine-tuning, validation có nhãn vẫn cần thiết để biết adaptation có giúp downstream task không.
- Learning rate quá lớn có thể làm model quên năng lực nền; fine-tuning tốt thường điều chỉnh nhỏ, có validation set riêng.
- Dataset ít nhưng sạch có thể giá trị hơn dataset lớn nhưng nhiễu.
- Deployment phải tính xem cần full model riêng hay adapter có thể hot-swap trên cùng base model.

## Các mục tiêu fine-tuning

- Instruction fine-tuning: dạy base model làm theo instruction thay vì chỉ tiếp tục text.
- Domain adaptation: làm model nhạy hơn với nghĩa chuyên ngành, ví dụ y tế, pháp lý, coding.
- [[Preference Learning]]: dạy model chọn response phù hợp với judgment của người dùng hoặc verifier.
- [[Parameter-Efficient Fine-Tuning]]: giảm chi phí customize bằng adapter, [[LoRA]] hoặc [[QLoRA]].

## Liên kết

- [[Parameter-Efficient Fine-Tuning]]
- [[Language Model Fine-Tuning]]
- [[Classifier Fine-Tuning]]
- [[Fine-Tuning XLM-RoBERTa]]
- [[Domain Adaptation]]
- [[Representation Model]]
- [[Generative Model]]
- [[Preference Learning]]
- [[RLHF]]
- [[DPO]]
