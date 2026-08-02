---
type: synthesis
status: evolving
concepts:
  - "[[Text Generation]]"
  - "[[Greedy Decoding]]"
  - "[[Beam Search Decoding]]"
  - "[[Top-k Sampling]]"
  - "[[Nucleus Sampling]]"
  - "[[Autoregressive Language Model]]"
  - "[[Causal Language Model]]"
sources:
  - "[[NLP Transformers - Chapter 05 - Text Generation]]"
questions: []
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - synthesis
  - nlp
  - text-generation
  - decoding
---

# Decoding Strategies for Text Generation

## Câu hỏi trung tâm

- Khi model đã trả về phân phối xác suất next-token, nên chọn token tiếp theo bằng chiến lược nào?

## Mental model

```text
prompt
-> model tạo logits cho token kế tiếp
-> softmax thành xác suất trên vocabulary
-> decoding strategy chọn token
-> nối token vào prefix
-> lặp lại cho đến khi đủ dài hoặc gặp EOS
```

## Vì sao decoding quan trọng?

- [[Text Generation]] không kết thúc ở một forward pass như classification.
- Mỗi token được chọn sẽ trở thành context cho bước tiếp theo.
- Vì vậy decoding strategy quyết định output ổn định, lặp, generic, đa dạng hay dễ mất mạch.

## So sánh nhanh

| Strategy | Cách chọn | Tính chất | Khi nên dùng | Rủi ro |
| --- | --- | --- | --- | --- |
| [[Greedy Decoding]] | Chọn token xác suất cao nhất từng bước | Nhanh, deterministic | Baseline, output ngắn, debug | Tối ưu cục bộ, dễ lặp |
| [[Beam Search Decoding]] | Giữ nhiều chuỗi ứng viên có score cao | Deterministic, tìm rộng hơn greedy | Translation/summarization hoặc output có cấu trúc | Tốn compute, dễ generic |
| [[Top-k Sampling]] | Sampling trong `k` token xác suất cao nhất | Đa dạng có giới hạn | Creative generation có kiểm soát | `k` cố định, có thể quá hẹp/quá rộng |
| [[Nucleus Sampling]] | Sampling trong nhóm token có tổng xác suất đạt `top_p` | Linh hoạt theo phân phối | Chat/creative writing tự nhiên hơn | `top_p` cao dễ nhiễu, thấp dễ nhàm |

## Tổng hợp của tôi

- Greedy và beam thiên về ổn định: phù hợp khi muốn output ít ngẫu nhiên.
- Sampling thiên về đa dạng: phù hợp khi output có nhiều cách nói đúng.
- Top-k giới hạn bằng số lượng token, còn nucleus/top-p giới hạn bằng khối lượng xác suất.
- Khi output bị lặp hoặc quá an toàn, cần nghi ngờ decoding quá tham lam.
- Khi output mất mạch hoặc bốc token lạ, cần nghi ngờ sampling quá rộng hoặc temperature quá cao.

## Khi áp dụng

- Factual answer: ưu tiên decoding ổn định, temperature thấp, có thể cần grounding như [[Retrieval-Augmented Generation]].
- Creative writing/chatbot: sampling có kiểm soát thường tự nhiên hơn greedy/beam.
- Summarization/translation: beam search có thể hữu ích vì output cần bám input và ít ngẫu nhiên.
- Debug generation: bắt đầu từ greedy để có baseline deterministic, sau đó thử beam/top-k/top-p.

## Nguồn

- [[NLP Transformers - Chapter 05 - Text Generation]]
- [[Text Generation]]
- [[Greedy Decoding]]
- [[Beam Search Decoding]]
- [[Top-k Sampling]]
- [[Nucleus Sampling]]

## Liên kết

- [[NLP]]
- [[LLM]]

