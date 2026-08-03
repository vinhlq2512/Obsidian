---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: textbook-chapter
title: "SLP 2026 - Chapter 09 - Post-training - Instruction Tuning Alignment and Test-Time"
year: 2026
venue: ""
arxiv: ""
source_file: "[[SLP 2026 - Chapter 09 - Post-training - Instruction Tuning Alignment and Test-Time.pdf]]"
pages: 18
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[RLHF]]"
  - "[[DPO]]"
  - "[[Fine-tuning]]"
tags:
  - cs224n
  - textbook
---

# SLP 2026 - Chapter 09 - Post-training - Instruction Tuning Alignment and Test-Time

## Nguồn

- PDF gốc: [[SLP 2026 - Chapter 09 - Post-training - Instruction Tuning Alignment and Test-Time.pdf]]
- Vai trò trong CS224N: chapter tổng quan post-training: instruction tuning, alignment và test-time compute.

## Câu hỏi trung tâm

Sau pretraining, cần thêm bước nào để LLM trở thành assistant hữu ích và ít hại hơn?

## Kiến thức cốt lõi

- Pretrained LM chỉ học next-token prediction nên không tự động làm theo instruction tốt.
- Instruction tuning/SFT fine-tune trên instruction-response pairs.
- Preference alignment dùng human preferences qua RLHF, DPO hoặc biến thể.
- Alignment hướng model tới helpful và non-harmful behavior.
- Test-time compute dùng thêm inference computation để cải thiện chất lượng mà không đổi weight.

## Cơ chế / công thức / kiến trúc

```text
pretrained LLM
-> instruction tuning / SFT
-> preference alignment: RLHF hoặc DPO
-> test-time compute: sampling, verification, search
-> assistant behavior
```

## Khi áp dụng

- Dùng để hệ thống hoá Lecture 08, 09, 12 và 13.
- Tách rõ SFT, preference alignment và inference-time methods.
- Không xem post-training là một bước duy nhất.

## Kết quả / bằng chứng đáng giữ

- Chapter first pages nói pretrained LLM có giới hạn khi chỉ predict next word.
- Source định nghĩa instruction tuning/SFT và preference alignment/RLHF/DPO.
- Chapter title đưa test-time compute vào cùng post-training/alignment.

## Cách hiểu bằng lời của tôi

Post-training là quá trình biến khả năng ngôn ngữ thô thành hành vi có ích. Nó vừa dạy format, vừa dạy preference, vừa có thể dùng compute lúc suy luận.

## Câu hỏi review

1. Vì sao pretraining chưa đủ để model làm assistant tốt?
2. Instruction tuning và preference alignment khác nhau thế nào?
3. Test-time compute nằm ở đâu trong pipeline?

## Liên kết

- [[Instruction Fine-Tuning]]
- [[RLHF]]
- [[DPO]]
- [[Test-Time Compute]]
- [[CS224N]]
