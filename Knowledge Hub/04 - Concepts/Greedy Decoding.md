---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 05 - Text Generation]]"
source_sections:
  - "[[NLP Transformers - Chapter 05 - Text Generation]]"
first_seen: 2026-07-29
last_updated: 2026-08-02
tags:
  - concept
  - nlp
  - generation
  - decoding
---

# Greedy Decoding

## Định nghĩa

Greedy decoding là decoding strategy chọn token có xác suất cao nhất ở mỗi timestep khi sinh văn bản.

## Cách hiểu bằng lời của tôi

Ở mỗi bước, model tạo phân phối xác suất cho token tiếp theo. Greedy decoding không cân nhắc nhiều đường đi cùng lúc; nó chỉ chọn token đang có xác suất cao nhất ngay lúc đó, nối vào prompt, rồi lặp lại.

```text
prefix hiện tại
-> phân phối xác suất next-token
-> chọn token có xác suất cao nhất
-> prefix mới
-> lặp lại
```

## Quy trình theo nguồn

Trong Chapter 05, sách minh họa greedy search với GPT-2:

1. Lấy input prompt.
2. Chạy model để lấy logits của token cuối.
3. Dùng softmax để đổi logits thành xác suất.
4. Sắp xếp token theo xác suất giảm dần.
5. Chọn token xác suất cao nhất.
6. Nối token đó vào input sequence.
7. Lặp lại cho đến khi đủ số bước.

Trong Hugging Face `generate()`, ví dụ sách dùng `do_sample=False` để tái tạo greedy search.

## Ví dụ trực quan

Với prompt:

```text
Transformers are the
```

Greedy search có thể sinh chuỗi:

```text
Transformers are the most popular toy line in the world
```

Điểm đáng chú ý không phải chỉ là câu cuối, mà là quá trình sinh từng token một: `most`, rồi `popular`, rồi `toy`, rồi `line`, ...

## Điểm mạnh

- Đơn giản và dễ debug.
- Deterministic: cùng model, prompt và cấu hình thường cho cùng output.
- Có thể hữu ích với chuỗi ngắn khi cần output ổn định hơn đa dạng.

## Điểm yếu

- Tối ưu cục bộ: chọn token tốt nhất ở bước hiện tại, không đảm bảo chuỗi cuối tốt nhất.
- Có thể bỏ lỡ chuỗi có xác suất tổng thể cao hơn nếu chuỗi đó bắt đầu bằng token không đứng đầu ở bước đầu.
- Dễ tạo output lặp trong text generation, đặc biệt với văn bản dài hoặc cần đa dạng.

## Cần biết

- Greedy decoding là baseline quan trọng trước khi học [[Beam Search Decoding|Beam Search]], [[Top-k Sampling]] và [[Nucleus Sampling]].
- Nó minh họa rõ bản chất lặp của [[Text Generation]].
- Khi output bị lặp hoặc quá nhàm, greedy decoding là một nghi phạm đầu tiên cần kiểm tra.

## Câu hỏi review

1. Greedy decoding chọn token như thế nào ở mỗi timestep?
2. Vì sao greedy decoding deterministic?
3. Vì sao greedy decoding có thể bỏ lỡ chuỗi tốt hơn?
4. Khi nào greedy decoding dễ gây output lặp?

## Gợi ý trả lời câu hỏi review

1. Nó chọn token có xác suất cao nhất từ phân phối next-token.
2. Vì nó không sampling; cùng phân phối thì luôn chọn token đứng đầu.
3. Vì nó tối ưu từng bước cục bộ, không tìm kiếm nhiều chuỗi ứng viên để tối ưu xác suất tổng thể.
4. Khi sinh văn bản dài hoặc cần đa dạng, lựa chọn cục bộ lặp lại có thể dẫn vào vòng lặp từ/ngữ.

## Liên kết

- [[NLP Transformers - Chapter 05 - Text Generation]]
- [[Text Generation]]
- [[Autoregressive Language Model]]
- [[Causal Language Model]]
- [[Beam Search Decoding|Beam Search]]
- [[Top-k Sampling]]
- [[Nucleus Sampling]]
