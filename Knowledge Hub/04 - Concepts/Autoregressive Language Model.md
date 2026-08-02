---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 05 - Text Generation]]"
tags:
  - concept
  - nlp
  - generation
  - language-model
---

# Autoregressive Language Model

## Định nghĩa

Autoregressive language model là language model mô hình hóa một chuỗi bằng cách dự đoán từng token dựa trên các token đứng trước nó.

## Cách hiểu bằng lời của tôi

Model không cần đoán cả đoạn văn một lần. Nó chỉ cần trả lời câu hỏi lặp lại: "với prefix hiện tại, token tiếp theo hợp lý là gì?" Sau khi chọn token mới, token đó trở thành một phần của prefix cho bước kế tiếp.

```text
prefix: Transformers are the
-> dự đoán token kế tiếp: most
prefix mới: Transformers are the most
-> dự đoán token kế tiếp: ...
```

## Công thức trực giác

Xác suất của cả chuỗi được factorize thành tích các xác suất có điều kiện:

$$
p(x_1, \dots, x_n) = \prod_{t=1}^{n} p(x_t \mid x_{<t})
$$

Trong đó $x_{<t}$ là toàn bộ prefix trước token $x_t$.

## Ví dụ trực quan

Với câu:

```text
I love natural language processing
```

Model học các bước kiểu:

```text
p(I)
p(love | I)
p(natural | I love)
p(language | I love natural)
p(processing | I love natural language)
```

## Cần biết

- Autoregressive nhấn vào **cách phân rã xác suất và sinh tuần tự**.
- Trong LLM hiện đại, autoregressive generation thường đi cùng [[Decoder|decoder-only models]] như GPT.
- Mỗi token mới có thể ảnh hưởng toàn bộ phần sinh sau đó, nên lỗi có thể tích lũy.
- Decoding strategy quyết định cách chọn token từ phân phối xác suất ở mỗi bước.
- Autoregressive không tự nói attention được nhìn gì; phần "không nhìn tương lai" thường được nói bằng [[Causal Language Model]] hoặc [[Attention Mask|causal mask]].

## Khi áp dụng

- Dùng để hiểu text generation, chat, completion và code generation.
- Khi đọc paper/model card, nếu thấy "autoregressive LM", hãy nghĩ ngay đến next-token prediction và sinh từ prefix.

## Câu hỏi review

1. Autoregressive language model dự đoán gì ở mỗi bước?
2. Vì sao xác suất chuỗi có thể viết thành tích các xác suất có điều kiện?
3. Token sinh sai ở bước đầu có thể ảnh hưởng các bước sau thế nào?
4. Autoregressive khác gì với masked language modeling của BERT?

## Gợi ý trả lời câu hỏi review

1. Nó dự đoán token tiếp theo dựa trên prefix đã có.
2. Vì chain rule cho phép factorize xác suất của chuỗi thành các xác suất điều kiện theo thứ tự.
3. Token sai trở thành một phần của prefix, làm context cho các dự đoán sau bị lệch.
4. Autoregressive dự đoán từ trái sang phải bằng prefix; BERT thường dùng context hai chiều để dự đoán token bị mask.

## Liên kết

- [[Text Generation]]
- [[Causal Language Model]]
- [[Decoder]]
- [[Attention Mask]]
- [[NLP Transformers - Chapter 05 - Text Generation]]
