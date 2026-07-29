---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 3
start_page: 116
end_page: 157
estimated_minutes: 100
need_review: true
tags:
  - llm
  - transformer
  - attention
---

# Hands-On LLM - Chapter 03 - Looking Inside Large Language Models

## Mục tiêu cần hiểu

- Hiểu forward pass của Transformer LLM: tokenizer, embedding, stack Transformer blocks, LM head.
- Nắm cách model tạo token tiếp theo bằng probability distribution và sampling/decoding.
- Hiểu context size, parallel token processing và key-value caching.
- Nắm cấu trúc Transformer block: attention, MLP/feed-forward, residual connection, normalization.
- Biết các cải tiến gần đây: efficient attention, RoPE và biến thể kiến trúc.

## Định nghĩa quan trọng

- **Forward pass**: quá trình đưa input qua model để tạo output logits/probabilities.
- **LM head**: tầng chuyển hidden states thành phân phối xác suất trên vocabulary.
- **Decoding**: cách chọn token tiếp theo từ phân phối xác suất.
- **Context size**: số token tối đa model có thể xem trong một lần xử lý.
- **KV cache**: bộ nhớ lưu key/value của token trước để tăng tốc generation.
- **RoPE**: rotary positional embeddings, cách mã hóa vị trí bằng phép xoay trong không gian vector.

## Mental model

LLM sinh văn bản bằng vòng lặp: đọc prompt, dự đoán token tiếp theo, thêm token đó vào context, rồi lặp lại. Transformer block là nhà máy cập nhật biểu diễn token. Attention quyết định token nào nhìn token nào; MLP biến đổi thông tin; residual và normalization giúp training ổn định.

## Phần cần biết

- Generation tuần tự ở bước output, dù model có thể xử lý nhiều token input song song.
- KV cache quan trọng vì không cần tính lại attention cho toàn bộ token cũ ở mỗi bước.
- Sampling/decoding quyết định độ ổn định, sáng tạo và rủi ro của output.
- Efficient attention giúp giảm chi phí khi context dài.
- Positional embeddings cho model biết thứ tự token.

## Khi áp dụng

- Khi inference chậm, nghĩ tới context length, batch size, quantization và KV cache.
- Khi output quá lặp, kiểm tra decoding strategy.
- Khi làm long-context app, nhớ rằng context dài không đồng nghĩa model hiểu tốt toàn bộ.

## Câu hỏi review

1. Vì sao generation của decoder-only LLM là autoregressive?
2. LM head làm gì?
3. KV cache tiết kiệm chi phí ở bước nào?
4. RoPE giải quyết vấn đề gì?

## Gợi ý trả lời câu hỏi review

1. Decoder-only LLM là autoregressive vì nó sinh từng token dựa trên các token trước đó. Token mới được thêm vào context rồi model tiếp tục dự đoán token kế tiếp.
2. LM head chuyển hidden state cuối của model thành logits/probability distribution trên toàn bộ vocabulary, tức là giúp model quyết định token tiếp theo có khả năng là gì.
3. KV cache tiết kiệm chi phí trong quá trình generation bằng cách lưu key/value của các token đã xử lý, nên ở bước sinh token mới model không phải tính lại attention cho toàn bộ context cũ.
4. RoPE giúp mã hóa vị trí token vào attention theo cách phù hợp với thứ tự và khoảng cách tương đối giữa token, giúp model hiểu sequence order hiệu quả hơn.

## Liên kết

- [[Transformer]]
- [[Self-Attention]]
- [[Tokenization]]
- [[Generative Model]]
