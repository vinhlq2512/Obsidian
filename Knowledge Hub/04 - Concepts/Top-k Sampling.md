---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 05 - Text Generation]]"
  - "[[Hands-On LLM - Chapter 06 - Prompt Engineering]]"
source_sections:
  - "[[NLP Transformers - Chapter 05 - Text Generation]]"
first_seen: 2026-07-29
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - generation
  - decoding
  - sampling
---

# Top-k Sampling

## Định nghĩa

Top-k sampling là decoding strategy chỉ lấy mẫu token tiếp theo từ `k` token có xác suất cao nhất, thay vì lấy mẫu từ toàn bộ vocabulary.

## Cách hiểu bằng lời của tôi

Model vẫn tạo phân phối xác suất cho toàn bộ vocabulary, nhưng top-k cắt bỏ phần đuôi quá thấp. Sau đó nó chỉ random trong nhóm ứng viên tốt nhất.

Nếu `top_k = 50`, mỗi bước sinh text sẽ:

```text
logits toàn vocabulary
-> chọn 50 token có xác suất cao nhất
-> chuẩn hóa lại xác suất trong nhóm 50 token
-> sampling token tiếp theo
-> nối token vào prefix
-> lặp lại
```

## Vì sao cần top-k?

- [[Greedy Decoding]] quá tham lam vì luôn chọn token xác suất cao nhất.
- [[Beam Search Decoding]] tìm rộng hơn greedy nhưng vẫn ưu tiên chuỗi có score cao, dễ generic.
- Top-k sampling cho phép output đa dạng hơn, nhưng vẫn tránh lấy token quá vô lý ở đuôi phân phối.

## Ví dụ trực quan

Giả sử prompt:

```text
The weather today is
```

Model có thể cho các token tiếp theo:

| Token | Xác suất |
| --- | ---: |
| `sunny` | 0.30 |
| `warm` | 0.20 |
| `cold` | 0.12 |
| `rainy` | 0.10 |
| `beautiful` | 0.08 |
| `quantum` | 0.001 |

Nếu `top_k = 5`, token `quantum` bị loại khỏi tập sampling. Model vẫn có thể chọn `sunny`, `warm`, `cold`, `rainy` hoặc `beautiful`, nên output có đa dạng nhưng không quá lạc.

## Điểm mạnh

- Tăng tính đa dạng so với greedy/beam.
- Dễ hiểu và dễ cấu hình.
- Giảm khả năng chọn token rất thấp xác suất.

## Điểm yếu

- `k` cố định nên không thích nghi với độ sắc của phân phối.
- Nếu phân phối rất chắc chắn, giữ quá nhiều token có thể đưa thêm nhiễu.
- Nếu phân phối rất rộng, `k` quá nhỏ có thể loại token hợp lý.
- Output vẫn có thể mất mạch nếu sampling quá rộng hoặc temperature quá cao.

## Hyperparameters cần biết

- `top_k`: số token ứng viên được giữ lại.
- `temperature`: điều chỉnh độ sắc/phẳng của phân phối trước khi sampling.
- `do_sample=True`: trong Hugging Face, cần bật sampling để top-k có tác dụng.

Ví dụ Hugging Face:

```python
output = model.generate(
    **inputs,
    max_new_tokens=40,
    do_sample=True,
    top_k=50,
)
```

## So sánh với nucleus sampling

- Top-k giữ số lượng token cố định.
- [[Nucleus Sampling]] giữ số lượng token động sao cho tổng xác suất đạt ngưỡng `top_p`.

Mental model:

```text
top-k: giữ đúng k lựa chọn tốt nhất
top-p: giữ đủ lựa chọn để phủ p xác suất
```

## Khi áp dụng

- Khi muốn output bớt nhàm/lặp hơn greedy.
- Khi cần sáng tạo có kiểm soát.
- Khi muốn một baseline sampling đơn giản trước khi thử [[Nucleus Sampling]].

## Câu hỏi review

1. Top-k sampling khác greedy decoding ở đâu?
2. Vì sao top-k vẫn cần `do_sample=True`?
3. Top-k khác nucleus sampling ở điểm nào?
4. `top_k` quá nhỏ hoặc quá lớn gây rủi ro gì?

## Gợi ý trả lời câu hỏi review

1. Greedy chọn token xác suất cao nhất; top-k lấy mẫu trong nhóm `k` token xác suất cao nhất.
2. Vì top-k chỉ lọc ứng viên; nếu không sampling thì model vẫn có thể chọn token top-1.
3. Top-k giữ số token cố định, còn nucleus sampling giữ tập token theo tổng xác suất.
4. Quá nhỏ thì thiếu đa dạng; quá lớn thì có thể đưa token nhiễu vào tập sampling.

## Liên kết

- [[NLP Transformers - Chapter 05 - Text Generation]]
- [[Text Generation]]
- [[Greedy Decoding]]
- [[Beam Search Decoding]]
- [[Nucleus Sampling]]

