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

# Nucleus Sampling

## Định nghĩa

Nucleus sampling, hay top-p sampling, là decoding strategy lấy mẫu token tiếp theo từ nhóm token nhỏ nhất có tổng xác suất đạt ít nhất `p`.

## Cách hiểu bằng lời của tôi

Top-k hỏi: "Giữ bao nhiêu token?"

Nucleus sampling hỏi: "Giữ đủ bao nhiêu xác suất?"

Nếu `top_p = 0.9`, model sắp xếp token theo xác suất giảm dần, rồi lấy nhóm token đầu tiên sao cho tổng xác suất của nhóm đó đạt khoảng 90%. Sau đó model sampling trong nhóm này.

```text
logits toàn vocabulary
-> softmax thành xác suất
-> sắp token theo xác suất giảm dần
-> giữ nhóm token có tổng xác suất >= top_p
-> chuẩn hóa lại xác suất trong nhóm
-> sampling token tiếp theo
```

## Vì sao cần nucleus sampling?

- Phân phối next-token không phải lúc nào cũng có cùng độ rộng.
- Có bước model rất chắc chắn: chỉ vài token hợp lý.
- Có bước model mở hơn: nhiều token đều hợp lý.
- Nucleus sampling thích nghi theo phân phối đó bằng cách để số token ứng viên thay đổi theo `top_p`.

## Ví dụ trực quan

Nếu phân phối rất sắc:

| Token | Xác suất |
| --- | ---: |
| `yes` | 0.85 |
| `no` | 0.08 |
| `maybe` | 0.03 |

Với `top_p = 0.9`, nucleus có thể chỉ giữ `yes` và `no`.

Nếu phân phối rộng hơn:

| Token | Xác suất |
| --- | ---: |
| `beautiful` | 0.18 |
| `strange` | 0.15 |
| `quiet` | 0.12 |
| `bright` | 0.10 |
| `old` | 0.08 |

Với cùng `top_p = 0.9`, nucleus sẽ cần giữ nhiều token hơn để đạt tổng xác suất 90%.

## Điểm mạnh

- Linh hoạt hơn [[Top-k Sampling]] vì số token ứng viên thay đổi theo phân phối.
- Tăng đa dạng nhưng vẫn giới hạn sampling vào vùng xác suất cao.
- Hữu ích cho creative writing, chatbot hoặc generation cần tự nhiên hơn greedy/beam.

## Điểm yếu

- Vẫn có thể mất mạch nếu `top_p` quá cao hoặc temperature quá lớn.
- Nếu `top_p` quá thấp, output có thể gần giống greedy và thiếu đa dạng.
- Khó debug hơn greedy vì output có yếu tố ngẫu nhiên.

## Hyperparameters cần biết

- `top_p`: ngưỡng tổng xác suất của nucleus.
- `temperature`: điều chỉnh độ ngẫu nhiên trước khi sampling.
- `do_sample=True`: cần bật sampling trong Hugging Face.

Ví dụ Hugging Face:

```python
output = model.generate(
    **inputs,
    max_new_tokens=40,
    do_sample=True,
    top_p=0.9,
)
```

## So sánh với top-k

| Strategy | Tập ứng viên | Khi phân phối sắc | Khi phân phối rộng |
| --- | --- | --- | --- |
| [[Top-k Sampling]] | Luôn giữ `k` token | Có thể giữ quá nhiều token | Có thể giữ quá ít token |
| Nucleus sampling | Giữ token đến khi đạt `top_p` | Tập ứng viên nhỏ | Tập ứng viên lớn hơn |

## Khi áp dụng

- Khi muốn output đa dạng và tự nhiên hơn greedy/beam.
- Khi không muốn cố định số lượng token ứng viên như top-k.
- Khi cần kiểm soát rủi ro sampling bằng một ngưỡng xác suất.

## Câu hỏi review

1. Nucleus sampling chọn tập token ứng viên như thế nào?
2. Vì sao nucleus sampling linh hoạt hơn top-k?
3. `top_p` quá cao hoặc quá thấp gây vấn đề gì?
4. Khi nào nên dùng nucleus sampling thay vì beam search?

## Gợi ý trả lời câu hỏi review

1. Nó lấy nhóm token có xác suất cao nhất sao cho tổng xác suất đạt ngưỡng `top_p`, rồi sampling trong nhóm đó.
2. Vì số token ứng viên thay đổi theo độ sắc/rộng của phân phối.
3. Quá cao thì dễ đưa nhiều token nhiễu vào; quá thấp thì output thiếu đa dạng.
4. Khi cần output tự nhiên/sáng tạo hơn và chấp nhận yếu tố ngẫu nhiên có kiểm soát.

## Liên kết

- [[NLP Transformers - Chapter 05 - Text Generation]]
- [[Text Generation]]
- [[Top-k Sampling]]
- [[Greedy Decoding]]
- [[Beam Search Decoding]]

