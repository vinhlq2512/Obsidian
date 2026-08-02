---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 05 - Text Generation]]"
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
---

# Beam Search Decoding

## Định nghĩa

Beam search decoding là decoding strategy giữ lại nhiều chuỗi ứng viên tốt nhất ở mỗi timestep, thay vì chỉ giữ một chuỗi như [[Greedy Decoding]].

## Cách hiểu bằng lời của tôi

Greedy decoding giống như đi theo một đường duy nhất: mỗi bước chọn token có xác suất cao nhất rồi không quay lại. Beam search thì giữ nhiều đường đi song song. Nếu `num_beams = 5`, model giữ 5 prefix ứng viên đang có điểm tốt nhất, mở rộng từng prefix bằng token tiếp theo, rồi lại chọn 5 prefix tốt nhất cho bước sau.

Mental model:

```text
prefix ban đầu
-> mở rộng thành nhiều token ứng viên
-> giữ top-k chuỗi ứng viên
-> mở rộng từng chuỗi
-> giữ top-k chuỗi mới
-> lặp đến khi đủ dài hoặc gặp EOS
```

## Vì sao cần beam search?

- [[Greedy Decoding]] tối ưu cục bộ: token tốt nhất ở bước hiện tại chưa chắc dẫn đến chuỗi tốt nhất cuối cùng.
- Beam search tìm kiếm rộng hơn bằng cách giữ nhiều prefix có khả năng tốt.
- Nó hữu ích khi cần output ổn định, có xác suất cao và ít ngẫu nhiên hơn sampling.

## Công thức trực giác

Với một chuỗi ứng viên $y_{1:t}$, score thường dựa trên tổng log-probability:

```text
score(y_1:t) = log p(y_1 | x) + log p(y_2 | x, y_1) + ... + log p(y_t | x, y_<t)
```

Beam search giữ lại các chuỗi có score cao nhất sau mỗi bước mở rộng.

Điểm cần nhớ: dùng log-probability để cộng điểm dễ hơn nhân nhiều xác suất nhỏ.

## Ví dụ trực quan

Giả sử prompt:

```text
Transformers are the
```

Greedy có thể chọn ngay token tốt nhất ở bước đầu, ví dụ `most`, rồi chỉ đi tiếp theo nhánh đó.

Beam search giữ nhiều khả năng:

```text
Transformers are the most
Transformers are the best
Transformers are the foundation
Transformers are the core
Transformers are the key
```

Sau đó nó mở rộng từng chuỗi và chọn lại các chuỗi có tổng score tốt nhất.

## Điểm mạnh

- Ít tham lam hơn greedy decoding.
- Deterministic nếu không sampling.
- Thường tạo output ổn định hơn cho các task cần câu trả lời có cấu trúc hoặc seq2seq như translation/summarization.

## Điểm yếu

- Tốn compute và memory hơn vì phải giữ nhiều beams.
- Có thể tạo output kém tự nhiên hoặc lặp nếu score ưu tiên chuỗi quá an toàn.
- Beam width lớn hơn không luôn tốt hơn; có thể làm output dài dòng hoặc quá generic.
- Vì tối ưu likelihood, beam search không tự đảm bảo tính đa dạng.

## Hyperparameters cần biết

- `num_beams`: số chuỗi ứng viên giữ lại.
- `early_stopping`: dừng khi các beam tốt nhất đã hoàn thành.
- `length_penalty`: điều chỉnh thiên hướng sinh chuỗi ngắn/dài.
- `no_repeat_ngram_size`: giảm lặp n-gram trong output.

Ví dụ Hugging Face:

```python
output = model.generate(
    **inputs,
    max_new_tokens=40,
    num_beams=5,
    early_stopping=True,
)
```

## So sánh nhanh

| Strategy | Cách chọn token | Mạnh ở | Dễ lỗi ở |
| --- | --- | --- | --- |
| [[Greedy Decoding]] | Chọn token tốt nhất từng bước | Đơn giản, nhanh, deterministic | Tối ưu cục bộ, dễ lặp |
| Beam search | Giữ nhiều chuỗi tốt nhất | Ổn định, tìm kiếm rộng hơn greedy | Tốn compute, có thể generic |
| Sampling | Lấy mẫu từ phân phối | Đa dạng, sáng tạo | Dễ mất mạch nếu quá rộng |

## Khi áp dụng

- Khi cần output ổn định hơn sampling.
- Khi task có câu trả lời tương đối hẹp, ví dụ translation hoặc summarization.
- Khi greedy decoding quá tham lam và bỏ lỡ chuỗi tốt hơn.

Không nên mặc định dùng beam search cho mọi chat/creative writing, vì output có thể an toàn, ít đa dạng hoặc hơi máy móc.

## Câu hỏi review

1. Beam search khác greedy decoding ở điểm nào?
2. `num_beams` ảnh hưởng compute và chất lượng thế nào?
3. Vì sao beam search vẫn có thể tạo output lặp hoặc kém tự nhiên?
4. Khi nào nên dùng beam search thay vì sampling?

## Gợi ý trả lời câu hỏi review

1. Greedy giữ một chuỗi duy nhất; beam search giữ nhiều chuỗi ứng viên và chọn chuỗi có score tốt nhất.
2. `num_beams` càng lớn thì tìm kiếm rộng hơn nhưng tốn compute/memory hơn, và không đảm bảo output tốt hơn.
3. Vì nó tối ưu likelihood/score, nên có thể ưu tiên chuỗi an toàn, generic hoặc lặp.
4. Khi cần output ổn định, ít ngẫu nhiên và task có không gian đáp án tương đối hẹp.

## Liên kết

- [[NLP Transformers - Chapter 05 - Text Generation]]
- [[Text Generation]]
- [[Greedy Decoding]]
- [[Autoregressive Language Model]]
- [[Causal Language Model]]

