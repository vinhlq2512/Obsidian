---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - nlp
  - transformer
  - token-classification
  - hugging-face
---

# Custom Model for Token Classification

## Định nghĩa

Custom model for token classification là model class tự định nghĩa để dự đoán nhãn cho từng token/subword, thường bằng cách dùng pretrained Transformer body và thêm token classification head riêng.

## Cách hiểu bằng lời của tôi

Thay vì chỉ gọi `AutoModelForTokenClassification`, mình tự viết class để thấy rõ model chạy như thế nào: input đi vào Transformer body, hidden state của từng token đi qua dropout và linear classifier, rồi model trả logits cho từng token. Cách này hữu ích khi cần thay head, thêm logic loss, hoặc debug sâu hơn.

## Luồng tổng quát

```text
input_ids + attention_mask
-> pretrained Transformer body
-> last_hidden_state [batch_size, sequence_length, hidden_size]
-> dropout
-> linear classifier hidden_size -> num_labels
-> logits [batch_size, sequence_length, num_labels]
-> loss nếu có labels
```

## Các bước thực hiện

### 1. Chọn pretrained body

Dùng body phù hợp với checkpoint, ví dụ `XLMRobertaModel` cho XLM-R. Body chịu trách nhiệm tạo contextual representation cho từng token.

Điểm cần nhớ: body phải khớp với tokenizer và checkpoint. Không nên dùng tokenizer của model này với body của model khác nếu không có lý do rõ ràng.

### 2. Khai báo config và labels

Config nên chứa:

- `num_labels`: số nhãn NER/token classification.
- `id2label`: ánh xạ id sang tên nhãn.
- `label2id`: ánh xạ tên nhãn sang id.
- dropout probability nếu head dùng dropout.

Config giúp `Trainer`, `pipeline()` và `save_pretrained()` hiểu model đang dự đoán nhãn gì.

### 3. Thêm token classification head

Head phổ biến:

```text
dropout
-> linear layer hidden_size -> num_labels
```

Khác với sequence classification, token classification head chạy trên hidden state của từng token, không chỉ token đầu tiên.

### 4. Viết `forward()`

`forward()` thường nhận:

- `input_ids`
- `attention_mask`
- `labels`
- các tham số phụ như `token_type_ids`, `output_attentions`, `output_hidden_states`

Trong `forward()`:

1. Gọi Transformer body để lấy `last_hidden_state`.
2. Đưa hidden states qua dropout.
3. Đưa qua classifier để tạo logits.
4. Nếu có labels, tính loss.
5. Trả output chuẩn, ví dụ `TokenClassifierOutput`.

### 5. Tính loss đúng cho NER

Với NER, labels có shape:

```text
[batch_size, sequence_length]
```

Logits có shape:

```text
[batch_size, sequence_length, num_labels]
```

Khi tính cross-entropy, thường flatten:

```text
logits -> [batch_size * sequence_length, num_labels]
labels -> [batch_size * sequence_length]
```

Các vị trí không muốn tính loss, như special tokens hoặc subword phụ, thường dùng label `-100` để loss function ignore.

### 6. Trả output chuẩn

Output nên giữ dạng Hugging Face-friendly:

- `loss`
- `logits`
- `hidden_states`
- `attentions`

Điều này giúp model tương thích với `Trainer`, evaluation loop và pipeline.

## Lỗi dễ gặp

- `num_labels` không khớp với label set.
- `id2label` và `label2id` bị đảo hoặc thiếu nhãn.
- Logits và labels lệch `sequence_length` do tokenizer/label alignment sai.
- Quên ignore special tokens hoặc subword phụ bằng `-100`.
- Dùng `AutoModel` rồi quên thêm head nên chỉ có hidden states, chưa có logits.

## Cần biết

- Custom model cho token classification là cách làm rõ anatomy của [[Transformers Model Class]].
- Với [[Named Entity Recognition]], chất lượng phụ thuộc nhiều vào cả token-label alignment lẫn head/loss.
- Head mới thường khởi tạo ngẫu nhiên, nên cần fine-tune.
- [[Loading a Custom Model]] là bước nạp pretrained body vào class custom bằng `from_pretrained()` và kiểm tra những layer nào được load hoặc khởi tạo mới.
- Nếu không cần custom logic, `AutoModelForTokenClassification` thường đủ tốt và ít rủi ro hơn.

## Liên kết

- [[Transformers Model Class]]
- [[Loading a Custom Model]]
- [[Classification Head]]
- [[Named Entity Recognition]]
- [[Tokenizer Pipeline]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
