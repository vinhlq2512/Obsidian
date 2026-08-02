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

# Causal Language Model

## Định nghĩa

Causal language model là language model dự đoán token dựa trên các token trước nó, với ràng buộc rằng token hiện tại không được nhìn các token tương lai.

## Cách hiểu bằng lời của tôi

"Causal" ở đây có nghĩa là chiều thông tin chỉ đi từ quá khứ sang hiện tại/tương lai. Khi model đang dự đoán token thứ $t$, nó chỉ được dùng prefix $x_{<t}$, không được dùng $x_{t+1}$ hay các token sau đó.

```text
được nhìn:      x1 x2 x3
đang dự đoán:           x4
không được nhìn:           x5 x6 ...
```

## Quan hệ với autoregressive

Trong text generation, [[Autoregressive Language Model]] và causal language model thường đi cùng nhau:

- **Autoregressive**: nói về cách viết xác suất/sinh từng token.
- **Causal**: nói về ràng buộc không nhìn tương lai.

GPT-style models thường là cả hai: vừa sinh autoregressive, vừa dùng causal mask trong self-attention.

## Causal mask

Trong Transformer decoder, ràng buộc causal thường được thực hiện bằng [[Attention Mask|causal mask]] dạng tam giác dưới:

```text
      key:  t1  t2  t3  t4
query
t1         1   0   0   0
t2         1   1   0   0
t3         1   1   1   0
t4         1   1   1   1
```

Token `t3` được nhìn `t1`, `t2`, `t3`, nhưng không được nhìn `t4`.

## Cần biết

- Causal LM phù hợp với [[Text Generation]] vì nó mô phỏng đúng điều kiện generation: chỉ có prefix, chưa có tương lai.
- Nếu model được nhìn token tương lai trong training, nó có thể "ăn gian" next-token prediction.
- Causal LM khác masked language model như BERT: BERT dùng cả trái và phải để đoán token bị che, nên không tự nhiên sinh từ trái sang phải bằng cùng một objective.
- Trong Hugging Face, `AutoModelForCausalLM` là class thường dùng cho GPT-style next-token generation.

## Khi áp dụng

- Dùng causal LM cho chat, completion, code generation và các bài toán sinh tiếp văn bản.
- Khi debug model sinh văn bản, kiểm tra causal mask nếu nghi ngờ model nhìn sai context hoặc loss bất thường.

## Câu hỏi review

1. Vì sao causal LM không được nhìn token tương lai?
2. Causal LM liên quan gì đến decoder-only Transformer?
3. Causal mask có hình dạng trực giác như thế nào?
4. Causal LM khác masked language model ở đâu?

## Gợi ý trả lời câu hỏi review

1. Vì lúc generation thực tế, token tương lai chưa tồn tại; nếu nhìn trước trong training thì model học sai bài toán.
2. Decoder-only Transformer dùng causal self-attention để sinh token từ trái sang phải.
3. Nó giống ma trận tam giác dưới: mỗi token chỉ nhìn chính nó và các token trước nó.
4. Causal LM dự đoán từ prefix; masked LM dùng context hai chiều để đoán token bị mask.

## Liên kết

- [[Text Generation]]
- [[Autoregressive Language Model]]
- [[Decoder]]
- [[Attention Mask]]
- [[NLP Transformers - Chapter 05 - Text Generation]]
