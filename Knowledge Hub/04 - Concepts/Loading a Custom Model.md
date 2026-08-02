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

# Loading a Custom Model

## Định nghĩa

Loading a custom model là quá trình nạp pretrained checkpoint vào một model class tự định nghĩa, sao cho phần body dùng lại weights đã học còn phần head/task-specific được khởi tạo hoặc nạp theo checkpoint phù hợp.

## Cách hiểu bằng lời của tôi

Custom model class chỉ mô tả kiến trúc và `forward()`. Để model thật sự có tri thức pretraining, mình cần load weights từ checkpoint bằng `from_pretrained()`. Nếu class custom có layer mới, ví dụ token classification head cho NER, layer đó có thể chưa có weights trong checkpoint và sẽ được khởi tạo mới.

## Luồng tổng quát

```text
checkpoint name/path
-> load config
-> set num_labels, id2label, label2id
-> CustomModel.from_pretrained(checkpoint, config=config)
-> pretrained body + initialized/custom head
```

## Các bước thực hiện

### 1. Load hoặc tạo config

Config giữ thông tin kiến trúc và metadata cho task:

- `num_labels`
- `id2label`
- `label2id`
- dropout
- model type/base architecture

Với NER, cần set label mapping trước khi load model để head có đúng số logits.

### 2. Gọi `from_pretrained()` trên custom class

Thay vì:

```python
AutoModelForTokenClassification.from_pretrained(checkpoint)
```

mình gọi custom class:

```python
model = CustomModelForTokenClassification.from_pretrained(
    checkpoint,
    config=config,
)
```

Ý nghĩa: Hugging Face đọc checkpoint, khớp tên parameters, nạp weights vào những layer có cùng tên/shape, và khởi tạo những layer mới nếu checkpoint chưa có.

### 3. Hiểu cảnh báo khi load weights

Cảnh báo thường gặp:

```text
Some weights were not initialized from the model checkpoint
```

Với custom token classification, cảnh báo này thường không đáng sợ nếu nó chỉ nói về head mới. Head mới chưa được pretrain cho label set của mình, nên cần fine-tune.

Cảnh báo đáng chú ý hơn là:

- body weights không load được nhiều layer.
- shape mismatch ngoài phần head.
- `num_labels` không khớp với checkpoint đang load lại.

### 4. Fine-tune sau khi load

Sau khi load:

- pretrained body đã có representation tổng quát.
- token classification head có thể còn random.
- cần train/fine-tune trên dataset NER để head học mapping từ hidden states sang labels.

Với [[Named Entity Recognition]], cũng cần chắc rằng labels đã align đúng với token/subword trước khi train.

### 5. Lưu và load lại model custom

Sau khi train, lưu:

```python
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
```

Khi load lại, cần có:

- code định nghĩa custom model class.
- config đã lưu.
- checkpoint weights đã lưu.
- tokenizer tương ứng.

Nếu muốn load tự động bằng Auto classes ở môi trường khác, cần đăng ký custom architecture/auto class đúng cách; nếu không, Python sẽ không biết class custom nằm ở đâu.

## Cần biết

- `from_pretrained()` không chỉ tạo object; nó nạp weights từ checkpoint vào model architecture.
- `config` quyết định head có bao nhiêu nhãn và label mapping hiển thị thế nào.
- Cảnh báo về head mới thường bình thường khi task label set khác checkpoint gốc.
- Tokenizer phải đi cùng checkpoint/model; tokenizer lệch có thể làm input IDs không còn đúng nghĩa.
- Với [[Custom Model for Token Classification]], loading đúng giúp mình tận dụng pretrained body thay vì train từ đầu.

## Lỗi dễ gặp

- Quên truyền `config` có `num_labels` đúng.
- Dùng nhầm checkpoint không khớp với body architecture.
- Tưởng cảnh báo head mới là lỗi nghiêm trọng, trong khi nó chỉ báo head cần fine-tune.
- Lưu model nhưng quên lưu tokenizer.
- Load lại custom model ở môi trường không có class definition.

## Liên kết

- [[Custom Model for Token Classification]]
- [[Transformers Model Class]]
- [[Hugging Face]]
- [[Named Entity Recognition]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
