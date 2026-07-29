---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 12
start_page: 487
end_page: 533
estimated_minutes: 120
need_review: true
tags:
  - llm
  - fine-tuning
  - alignment
---

# Hands-On LLM - Chapter 12 - Fine-Tuning Generation Models

## Mục tiêu cần hiểu

- Hiểu ba bước training phổ biến của generative LLM: pretraining, supervised fine-tuning và preference tuning.
- Phân biệt full fine-tuning và [[Parameter-Efficient Fine-Tuning]].
- Nắm QLoRA: quantization + LoRA để fine-tune model lớn với ít tài nguyên hơn.
- Hiểu cách đánh giá generative models bằng metrics, benchmarks, leaderboards, automated và human evaluation.
- Nắm [[RLHF]], reward model và [[DPO]] như các phương pháp alignment/preference tuning.

## Định nghĩa quan trọng

- **Pretraining**: huấn luyện model trên corpus lớn để học language modeling tổng quát.
- **Supervised fine-tuning (SFT)**: huấn luyện model sinh câu trả lời mong muốn từ instruction-output pairs.
- **PEFT**: fine-tune một lượng nhỏ tham số thay vì toàn bộ model.
- **LoRA**: thêm low-rank adapters vào model để học update nhỏ.
- **QLoRA**: dùng quantized base model kết hợp LoRA để giảm memory.
- **Reward model**: model chấm điểm output theo preference.
- **RLHF**: dùng feedback/preference của con người để align model.
- **DPO**: tối ưu preference trực tiếp không cần vòng RL phức tạp như PPO.

## Mental model

Pretraining dạy model "ngôn ngữ". SFT dạy model "làm theo instruction". Preference tuning dạy model "chọn câu trả lời người dùng thích hơn". PEFT/QLoRA làm quá trình này rẻ hơn bằng cách chỉ học phần adapter nhỏ.

## Phần cần biết

- Full fine-tuning mạnh nhưng tốn memory/compute và dễ làm model quên năng lực cũ.
- PEFT phù hợp khi cần customize model với tài nguyên hạn chế.
- Instruction data cần template rõ để model học format hội thoại.
- Evaluation generative khó vì nhiều câu trả lời có thể đúng.
- Human evaluation vẫn quan trọng cho chất lượng, safety và preference.
- DPO đơn giản hóa alignment bằng preferred/rejected pairs.

## Khi áp dụng

- Dùng prompt/RAG trước nếu vấn đề chỉ là thiếu context.
- Dùng SFT khi cần model học format, style hoặc task behavior ổn định.
- Dùng PEFT/QLoRA khi muốn fine-tune model lớn trên GPU hạn chế.
- Dùng preference tuning khi vấn đề là chất lượng lựa chọn output, helpfulness hoặc alignment.

## Câu hỏi review

1. Pretraining, SFT và preference tuning khác nhau ở dữ liệu và mục tiêu nào?
2. LoRA giảm chi phí fine-tuning bằng cách nào?
3. Vì sao đánh giá generative model khó hơn classification?
4. DPO khác RLHF truyền thống ở đâu?

## Gợi ý trả lời câu hỏi review

1. Pretraining dùng corpus lớn và objective language modeling để học ngôn ngữ tổng quát. SFT dùng instruction-output pairs để dạy model làm theo yêu cầu. Preference tuning dùng dữ liệu so sánh preferred/rejected để model chọn output phù hợp preference hơn.
2. LoRA giữ weights gốc gần như cố định và thêm các low-rank adapter nhỏ vào một số layer. Khi train chỉ cập nhật adapter, nên giảm memory, compute và kích thước checkpoint.
3. Generative model khó đánh giá hơn vì một prompt có thể có nhiều câu trả lời đúng, chất lượng gồm nhiều chiều như correctness, helpfulness, faithfulness, style, safety và format. Classification thường có nhãn rõ để so sánh trực tiếp.
4. RLHF truyền thống thường train reward model rồi dùng reinforcement learning để tối ưu policy. DPO dùng trực tiếp cặp preferred/rejected để tối ưu model theo preference, đơn giản hơn và tránh nhiều phức tạp của RL loop.

## Liên kết

- [[Fine-tuning]]
- [[Parameter-Efficient Fine-Tuning]]
- [[RLHF]]
- [[DPO]]
- [[Generative Model]]
