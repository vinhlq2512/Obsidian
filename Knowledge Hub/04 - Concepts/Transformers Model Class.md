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
  - hugging-face
---

# Transformers Model Class

## Định nghĩa

Transformers model class là lớp Python trong Hugging Face Transformers đóng gói kiến trúc model, config, weights, forward pass và output format cho một checkpoint hoặc một downstream task.

## Cách hiểu bằng lời của tôi

Trong Hugging Face, một model không chỉ là "Transformer". Nó là một class cụ thể gắn với kiến trúc và task. Ví dụ cùng một XLM-R body có thể được dùng cho masked language modeling, sequence classification hoặc token classification bằng cách thay phần head ở trên cùng.

## Body và Head

- **Body**: phần pretrained Transformer chính, ví dụ `XLMRobertaModel`. Nó nhận `input_ids`, `attention_mask` và tạo contextual hidden states.
- **Head**: phần task-specific nằm trên body, ví dụ token classification head cho NER. Nó biến hidden states thành logits theo số nhãn cần dự đoán.

Mental model:

```text
input_ids + attention_mask
-> Transformer body
-> last_hidden_state
-> task head
-> logits
```

## Với token classification / NER

Với [[Named Entity Recognition]], model cần dự đoán nhãn cho từng token/subword, nên head không chỉ đọc một vector cấp câu như `[CLS]`.

Luồng dữ liệu:

```text
input_ids
-> XLM-R body
-> token hidden states [batch_size, sequence_length, hidden_size]
-> dropout
-> linear classifier
-> logits [batch_size, sequence_length, num_labels]
```

Nếu truyền `labels`, model có thể tính loss. Các vị trí không muốn tính loss, ví dụ special tokens hoặc subword phụ, thường được đặt label `-100`.

## AutoModel vs AutoModelFor...

- `AutoModel`: load body/base model, thường trả hidden states.
- `AutoModelForTokenClassification`: load body kèm token classification head.
- `AutoModelForSequenceClassification`: load body kèm classification head cho toàn sequence.

Điểm dễ nhầm: `AutoModel` chưa có head cho task cuối. Nếu muốn fine-tune NER, cần dùng model class có token classification head hoặc tự tạo head.

## Config và output

`config` giữ các thông tin như:

- `hidden_size`
- `num_labels`
- `id2label`
- `label2id`
- dropout probability
- tên kiến trúc/base model

Output thường là object có cấu trúc, ví dụ `TokenClassifierOutput`, gồm:

- `loss` nếu có labels.
- `logits` để dự đoán nhãn.
- `hidden_states` nếu bật output hidden states.
- `attentions` nếu bật output attentions.

## Khi áp dụng

- Khi fine-tune task mới và cần hiểu head nào đang được thêm vào body.
- Khi label set thay đổi và cần set `num_labels`, `id2label`, `label2id`.
- Khi custom model cho NER, ví dụ thêm CRF hoặc head riêng.
- Khi cần tạo [[Custom Model for Token Classification]] để kiểm soát body, head, loss và output format thay vì dùng sẵn `AutoModelForTokenClassification`.
- Khi cần [[Loading a Custom Model]] để nạp checkpoint vào class tự viết và phân biệt layer nào dùng pretrained weights, layer nào được khởi tạo mới.
- Khi debug shape: luôn kiểm tra hidden states, logits và labels có cùng chiều sequence hay không.

## Cần biết

- Body thường chứa phần pretrained weights quan trọng nhất.
- Head mới thêm có thể được khởi tạo ngẫu nhiên và cần fine-tuning.
- Với NER, head chạy trên từng token hidden state; với classification, head thường chạy trên representation cấp sequence.
- Model class chuẩn giúp `Trainer`, `from_pretrained()` và `save_pretrained()` hoạt động nhất quán.

## Liên kết

- [[Hugging Face]]
- [[Transformer]]
- [[Classification Head]]
- [[Custom Model for Token Classification]]
- [[Loading a Custom Model]]
- [[Named Entity Recognition]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
