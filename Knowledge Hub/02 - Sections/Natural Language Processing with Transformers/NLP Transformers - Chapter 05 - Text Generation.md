---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 5
start_page: 150
end_page: 163
reading_date: 2026-07-29
planned_sessions:
  - "2026-07-29 | 150-163 | Decoding strategies và so sánh output | 45 phút"
estimated_minutes: 45
actual_minutes:
need_review: false
tags:
  - nlp
  - text-generation
  - decoding
---

# NLP Transformers - Chapter 05 - Text Generation

## Mục tiêu đọc

- Hiểu vì sao sinh văn bản mạch lạc là khó.
- So sánh greedy search, beam search, sampling, top-k và nucleus sampling.
- Biết decoding strategy ảnh hưởng chất lượng output như thế nào.

## Ý chính

- Greedy search đơn giản nhưng dễ tạo output lặp hoặc thiếu đa dạng.
- [[Beam Search Decoding|Beam search]] tìm nhiều ứng viên hơn nhưng vẫn có thể tạo văn bản kém tự nhiên.
- Sampling, [[Top-k Sampling|top-k]] và [[Nucleus Sampling|nucleus sampling]] tăng tính đa dạng bằng cách lấy mẫu có kiểm soát.
- [[Decoding Strategies for Text Generation]] gom lại trade-off chính: greedy/beam thiên về ổn định, top-k/nucleus thiên về đa dạng có kiểm soát.

## The Challenge with Generating Coherent Text

- Với classification, model tạo logits rồi ta chọn class có xác suất cao nhất hoặc đọc phân phối class bằng softmax. Với [[Text Generation]], logits chưa phải output cuối; cần decoding để chọn token kế tiếp.
- Decoding là quá trình lặp: chọn token, nối token vào input, rồi dùng context mới để chọn token tiếp theo.
- Vì sinh từng token nên generation tốn compute/latency hơn nhiều so với một forward pass cho classification.
- Output phụ thuộc mạnh vào decoding strategy và hyperparameters. Cùng một model có thể sinh văn bản ổn định, lặp, sáng tạo hoặc mất mạch tùy cách chọn token.
- GPT-2 là một [[Autoregressive Language Model|autoregressive]]/[[Causal Language Model|causal language model]]: nó học xác suất token kế tiếp dựa trên prefix đã có.
- Cách nhìn cốt lõi:

$$
p(x_1, \dots, x_n) = \prod_t p(x_t \mid x_{<t})
$$

Mạch lạc của đoạn văn đến từ việc mỗi token mới phải hợp lý với toàn bộ prefix, nhưng mỗi lựa chọn cũng làm đổi prefix cho bước sau.

### Autoregressive vs causal

| Thuật ngữ | Nhấn vào điều gì? | Cách nhớ |
| --- | --- | --- |
| [[Autoregressive Language Model]] | Factorize xác suất chuỗi thành nhiều xác suất có điều kiện | Dự đoán token kế tiếp từ prefix |
| [[Causal Language Model]] | Chỉ được dùng quá khứ, không nhìn tương lai | Sinh từ trái sang phải bằng causal mask |

Điểm quan trọng: autoregressive là mô hình xác suất/sequential generation; causal là ràng buộc attention/context để quá trình dự đoán không ăn gian token tương lai.

## Greedy Search Decoding

- [[Greedy Decoding]] chọn token có xác suất cao nhất ở mỗi timestep.
- Đây là cách đơn giản nhất để đổi output liên tục của model thành token rời rạc.
- Pipeline theo sách:

```text
prompt
-> model tạo logits cho token cuối
-> softmax thành xác suất next-token
-> chọn token xác suất cao nhất
-> nối token vào prompt
-> lặp lại
```

- Với prompt `Transformers are the`, greedy search có thể sinh tiếp thành `Transformers are the most popular toy line in the world`.
- Điểm mạnh: dễ hiểu, deterministic, tái tạo được bằng `generate(..., do_sample=False)`.
- Điểm yếu: dễ tạo output lặp và có thể bỏ lỡ chuỗi tốt hơn về xác suất tổng thể, vì nó chỉ chọn tối ưu cục bộ ở từng bước.

## Beam Search Decoding

- [[Beam Search Decoding]] giữ nhiều chuỗi ứng viên tốt nhất ở mỗi timestep.
- Nếu greedy chỉ đi theo một prefix duy nhất, beam search mở rộng nhiều prefix song song rồi giữ lại các prefix có tổng score cao nhất.
- Với Hugging Face `generate()`, cấu hình trong demo dùng `num_beams=5` và `early_stopping=True`.
- Điểm mạnh: ít tham lam hơn greedy, deterministic nếu không sampling, hữu ích khi cần output ổn định.
- Điểm yếu: tốn compute hơn, có thể tạo output generic hoặc kém tự nhiên nếu score ưu tiên chuỗi an toàn/lặp.

## Top-k And Nucleus Sampling

- [[Top-k Sampling]] chỉ lấy mẫu từ `k` token có xác suất cao nhất ở mỗi timestep.
- [[Nucleus Sampling]] hay top-p sampling lấy mẫu từ nhóm token nhỏ nhất có tổng xác suất đạt ngưỡng `top_p`.
- Top-k giữ số lượng token cố định; nucleus sampling giữ xác suất tích lũy cố định nên số token ứng viên có thể thay đổi theo từng bước.
- Sampling giúp output đa dạng hơn greedy/beam, nhưng nếu mở quá rộng thì dễ mất mạch hoặc chọn token nhiễu.
- Với Hugging Face `generate()`, demo dùng `do_sample=True, top_k=50` cho top-k và `do_sample=True, top_p=0.9` cho nucleus.

## Demo thực hành

So sánh nhiều decoding strategy trên cùng prompt.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

checkpoint = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

prompt = "In the future, natural language processing will"
inputs = tokenizer(prompt, return_tensors="pt")

configs = {
    "greedy": dict(max_new_tokens=40),
    "beam": dict(max_new_tokens=40, num_beams=5, early_stopping=True),
    "top_k": dict(max_new_tokens=40, do_sample=True, top_k=50),
    "nucleus": dict(max_new_tokens=40, do_sample=True, top_p=0.9),
}

for name, config in configs.items():
    output = model.generate(**inputs, **config)
    print(name, tokenizer.decode(output[0], skip_special_tokens=True))
```

## Khái niệm quan trọng

- [[Text Generation]]
- [[Autoregressive Language Model]]
- [[Causal Language Model]]
- [[Greedy Decoding]]
- [[Beam Search Decoding]]
- [[Top-k Sampling]]
- [[Nucleus Sampling]]
- [[Decoding Strategies for Text Generation]]

## Active Recall

1. Greedy search có điểm yếu gì?
2. Beam search tối ưu điều gì và có thể thất bại ra sao?
3. [[Top-k Sampling|Top-k]] khác [[Nucleus Sampling|nucleus sampling]] như thế nào?
4. Khi nào cần output đa dạng thay vì chính xác nhất?

## Gợi ý trả lời câu hỏi review

1. Greedy search chọn token xác suất cao nhất ở từng bước nên nhanh và deterministic, nhưng dễ tối ưu cục bộ và tạo output lặp.
2. Beam search giữ nhiều chuỗi ứng viên có score cao để tìm rộng hơn greedy, nhưng có thể tốn compute và sinh output generic/kém tự nhiên.
3. Top-k giữ đúng `k` token ứng viên, còn nucleus sampling giữ nhóm token có tổng xác suất đạt `top_p`, nên số token trong nucleus thay đổi theo phân phối.
4. Cần output đa dạng khi có nhiều cách trả lời hợp lý, ví dụ creative writing hoặc chatbot; với factual answer nên ưu tiên ổn định và grounding hơn.

## Checklist

- [x] Đọc xong chapter
- [ ] Chạy demo decoding
- [ ] Lưu ví dụ output tốt/xấu
- [x] Tách concept cần dùng lại
- [x] Cập nhật tiến độ sách
