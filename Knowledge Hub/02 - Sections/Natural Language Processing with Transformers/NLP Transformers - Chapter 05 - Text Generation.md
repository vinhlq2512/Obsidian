---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: planned
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
- Beam search tìm nhiều ứng viên hơn nhưng vẫn có thể tạo văn bản kém tự nhiên.
- Sampling, top-k và nucleus sampling tăng tính đa dạng bằng cách lấy mẫu có kiểm soát.

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
- [[Greedy Decoding]]
- [[Beam Search]]
- [[Top-k Sampling]]
- [[Nucleus Sampling]]

## Active Recall

1. Greedy search có điểm yếu gì?
2. Beam search tối ưu điều gì và có thể thất bại ra sao?
3. Top-k khác nucleus sampling như thế nào?
4. Khi nào cần output đa dạng thay vì chính xác nhất?

## Checklist

- [ ] Đọc xong chapter
- [ ] Chạy demo decoding
- [ ] Lưu ví dụ output tốt/xấu
- [ ] Tách concept cần dùng lại
- [ ] Cập nhật tiến độ sách
