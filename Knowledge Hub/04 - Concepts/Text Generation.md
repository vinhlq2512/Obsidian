---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 05 - Text Generation]]"
tags:
  - concept
  - nlp
  - generation
  - decoding
---

# Text Generation

## Định nghĩa

Text generation là bài toán sinh văn bản bằng cách để language model dự đoán token tiếp theo dựa trên context/prefix đã có, rồi lặp lại quá trình đó cho đến khi đạt độ dài mong muốn hoặc gặp token kết thúc.

## Cách hiểu bằng lời của tôi

Model không sinh cả đoạn văn trong một lần. Ở mỗi bước, nó tạo logits cho toàn bộ vocabulary. Decoding strategy biến logits đó thành một token cụ thể. Token mới được nối vào context, rồi model dự đoán tiếp.

```text
prompt
-> model dự đoán phân phối token kế tiếp
-> decoding chọn token
-> nối token vào prompt
-> lặp lại
```

## Vì sao sinh văn bản mạch lạc khó?

- **Iterative decoding**: output càng dài thì càng cần nhiều bước forward, nên chi phí cao hơn classification.
- **Lỗi tích lũy**: token chọn ở bước trước trở thành context cho bước sau; một lựa chọn kém có thể kéo đoạn văn đi lệch.
- **Chất lượng phụ thuộc decoding**: cùng một model nhưng greedy, beam search, top-k hoặc nucleus sampling có thể tạo output rất khác nhau.
- **Trade-off chất lượng và đa dạng**: output quá tham lam dễ lặp/nhàm; output quá ngẫu nhiên dễ mất mạch.

## Công thức trực giác

Với causal/autoregressive generation:

$$
p(x_1, \dots, x_n) = \prod_{t=1}^{n} p(x_t \mid x_{<t})
$$

Nghĩa là xác suất của cả chuỗi được tách thành nhiều dự đoán nhỏ: mỗi token được dự đoán từ các token trước nó.

## Cần biết

- [[Decoder|Decoder-only models]] như GPT phù hợp với next-token generation vì dùng causal attention.
- [[Autoregressive Language Model]] mô hình hóa chuỗi bằng nhiều bước dự đoán token kế tiếp.
- [[Causal Language Model]] dùng ràng buộc causal để token hiện tại không nhìn token tương lai.
- [[Attention Mask|Causal mask]] giúp token hiện tại không nhìn token tương lai.
- Decoding strategy là phần quyết định token nào được chọn từ phân phối xác suất.
- [[Greedy Decoding]] là strategy đơn giản nhất: chọn token có xác suất cao nhất ở mỗi bước.
- [[Beam Search Decoding|Beam search]] giữ nhiều chuỗi ứng viên tốt nhất để tránh tối ưu quá cục bộ như greedy.
- [[Top-k Sampling]] và [[Nucleus Sampling]] tăng đa dạng bằng cách lấy mẫu trong một tập token ứng viên đã được giới hạn.
- [[Decoding Strategies for Text Generation]] gom các trade-off chính giữa ổn định, đa dạng, compute và rủi ro lặp/mất mạch.
- Khi debug output xấu, cần xem cả prompt, model, decoding method và hyperparameters.

## Khi áp dụng

- Dùng cho chat, completion, creative writing, code generation, summarization dạng abstractive và nhiều tác vụ cần sinh chuỗi tự nhiên.
- Với câu trả lời factual, thường cần decoding ổn định hơn và có thể cần grounding như [[Retrieval-Augmented Generation]].
- Với sáng tạo nội dung, có thể tăng đa dạng bằng sampling có kiểm soát.

## Câu hỏi review

1. Vì sao text generation không giống classification?
2. Iterative decoding làm tăng chi phí như thế nào?
3. Vì sao decoding strategy ảnh hưởng chất lượng output?
4. Khi nào output bị lặp hoặc mất mạch?
5. Công thức autoregressive generation nói điều gì?

## Gợi ý trả lời câu hỏi review

1. Classification thường chọn nhãn từ logits trong một lần; text generation phải chọn từng token và lặp lại.
2. Mỗi token mới thường cần thêm một bước dự đoán, nên output dài làm tăng compute/latency.
3. Vì logits chỉ là phân phối xác suất; cách chọn token từ phân phối đó quyết định chuỗi cuối cùng.
4. Lặp có thể do decoding quá tham lam hoặc model/prompt dẫn vào vòng lặp; mất mạch có thể do sampling quá rộng hoặc context yếu.
5. Cả chuỗi được xem như tích của nhiều xác suất có điều kiện, mỗi token phụ thuộc vào prefix trước đó.

## Liên kết

- [[NLP Transformers - Chapter 05 - Text Generation]]
- [[Generative Model]]
- [[Autoregressive Language Model]]
- [[Causal Language Model]]
- [[Greedy Decoding]]
- [[Beam Search Decoding]]
- [[Top-k Sampling]]
- [[Nucleus Sampling]]
- [[Decoding Strategies for Text Generation]]
- [[Decoder]]
- [[Attention Mask]]
- [[Prompt Engineering]]
- [[Retrieval-Augmented Generation]]
