---
type: concept
status: understood
sources:
  - "[[2026-07-14_how-llms-learn-to-be-helpful-rlhf-vs-dpo]]"
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - alignment
  - security
---

# Model Alignment

## Định nghĩa

Model Alignment (Căn chỉnh mô hình) là quá trình tinh chỉnh các mô hình trí tuệ nhân tạo (đặc biệt là LLM) để hành vi, giá trị và đầu ra của mô hình phù hợp với ý định, sự an toàn và kỳ vọng của con người (Helpful, Honest, Harmless - HHH).

## Cách hiểu bằng lời của tôi

Mô hình pre-training ban đầu chỉ học nhiệm vụ tiếp theo (next-token prediction) từ toàn bộ internet, nên nó có thể tạo ra thông tin độc hại, sai sự thật hoặc vô nghĩa. Alignment là quá trình "dạy lễ nghĩa và kỹ năng trả lời" cho mô hình để nó trở thành một trợ lý hữu ích và an toàn.

## Các giai đoạn Alignment

```text
Base Pre-trained LLM
-> Supervised Fine-Tuning (SFT / Instruction Tuning)
-> Preference Alignment (RLHF / DPO / KTO)
-> Safety Guardrails & Red-Teaming Filter
-> Aligned Production Assistant
```

1. **Instruction Fine-Tuning (SFT)**: Huấn luyện trên các cặp câu hỏi - câu trả lời chất lượng cao do con người hoặc AI chọn lọc.
2. **Preference Learning**: Dùng dữ liệu so sánh $y_{\text{win}}$ / $y_{\text{lose}}$ để điều chỉnh hành vi theo mong muốn (qua [[Direct Preference Optimization|DPO]], RLHF, hay KTO).
3. **Red-Teaming & Safety Guardrails**: Kiểm thử các kịch bản jailbreak, tấn công prompt injection và cài đặt các bộ lọc an toàn đầu vào/đầu ra.

## Trade-off

- **Alignment Tax**: Đôi khi căn chỉnh quá mức làm giảm khả năng sáng tạo hoặc năng lực xử lý bài toán logic phức tạp của mô hình (Over-refusal: từ chối cả những câu hỏi hợp lệ).
- **Catastrophic Forgetting**: Quá trình alignment có thể làm suy giảm một số tri thức nguyên bản học được ở giai đoạn Pre-training.

## Liên kết

- [[Direct Preference Optimization]]
- [[Preference Learning]]
- [[LLM Security]]
- [[Prompt Injection]]
- [[Safe Outputs Pipeline]]
