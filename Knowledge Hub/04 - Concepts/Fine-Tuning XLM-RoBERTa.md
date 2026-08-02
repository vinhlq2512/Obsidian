---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - nlp
  - ner
  - fine-tuning
  - multilingual
---

# Fine-Tuning XLM-RoBERTa

## Định nghĩa

Fine-tuning XLM-RoBERTa là quá trình tiếp tục huấn luyện XLM-R pretrained multilingual model trên dataset cụ thể, ví dụ NER, để model học mapping từ multilingual token representations sang nhãn task-specific.

## Cách hiểu bằng lời của tôi

XLM-R đã học representation đa ngôn ngữ từ pretraining. Khi fine-tune cho [[Named Entity Recognition]], mình thêm token classification head lên từng token hidden state và train model bằng dữ liệu có nhãn thực thể. Fine-tuning dạy model biến năng lực hiểu ngôn ngữ chung thành khả năng nhận diện `PER`, `ORG`, `LOC` theo label set của mình.

## Luồng tổng quát

```text
NER dataset
-> tokenizer XLM-R + label alignment
-> XLM-R body + token classification head
-> Trainer
-> seqeval metrics
-> fine-tuned checkpoint
```

## Các bước thực hiện

### 1. Chuẩn bị labels và mapping

Cần xác định label set:

- `label2id`
- `id2label`
- `num_labels`

Ví dụ:

```text
O, B-PER, I-PER, B-ORG, I-ORG, B-LOC, I-LOC
```

Mapping này phải nhất quán giữa dataset, model config, metric và pipeline inference.

### 2. Load tokenizer và model checkpoint

Dùng tokenizer và checkpoint khớp nhau, ví dụ XLM-R:

```text
xlm-roberta-base
```

Nếu dùng model class có sẵn, chọn `AutoModelForTokenClassification`. Nếu cần logic riêng, dùng [[Custom Model for Token Classification]] rồi load bằng [[Loading a Custom Model]].

### 3. Tokenize và align labels

Với NER, tokenization không đủ; cần align word-level labels sang subword labels.

Luồng quan trọng:

```text
tokens + ner_tags
-> tokenizer(is_split_into_words=True)
-> word_ids()
-> labels có -100 cho special tokens/subword phụ
```

Xem chi tiết ở [[Tokenizing Texts for NER]].

### 4. Tạo data collator

Token classification cần padding đồng bộ cho input và labels. Data collator nên padding:

- `input_ids`
- `attention_mask`
- `labels`

Với Hugging Face, thường dùng:

```text
DataCollatorForTokenClassification
```

Điểm cần nhớ: labels phải được padding bằng `-100` ở vị trí không tính loss.

### 5. Định nghĩa metrics

Với NER, dùng [[Performance Measures for NER]]:

- precision
- recall
- F1
- accuracy

Thường dùng `seqeval`: bỏ các label `-100`, map ID về label string, rồi tính entity-level metrics.

### 6. Cấu hình Trainer

`TrainingArguments` kiểm soát:

- learning rate
- batch size
- số epoch
- weight decay
- evaluation strategy
- logging
- checkpoint saving
- push to hub nếu cần

Với XLM-R, cần để ý VRAM vì multilingual encoder lớn hơn nhiều model nhỏ như DistilBERT.

### 7. Train, evaluate, save

Sau khi train:

- kiểm tra validation F1.
- xem per-entity-type score.
- nếu multilingual, xem per-language score.
- chạy thử vài câu thật.
- làm [[Error Analysis for NER]] để đọc lỗi ranh giới, type, false positive/negative và lỗi theo ngôn ngữ.
- lưu model và tokenizer bằng `save_pretrained()`.

## Cần biết

- Fine-tuning cập nhật token classification head và thường cập nhật cả XLM-R body.
- Dataset label alignment sai sẽ làm model học sai dù code training chạy bình thường.
- F1 tổng có thể che lỗi ở entity type hiếm hoặc ngôn ngữ ít tài nguyên.
- Fine-tuned model trên một ngôn ngữ có thể dùng để thử [[Zero-shot Learning|zero-shot transfer]] sang ngôn ngữ khác.
- Sau fine-tuning, error analysis thường quan trọng hơn việc chỉ tăng epoch hoặc đổi checkpoint.
- Khi ít GPU, có thể giảm batch size, dùng gradient accumulation, mixed precision hoặc model nhỏ hơn.

## Liên kết

- [[Fine-tuning]]
- [[Multilingual Transformer]]
- [[Tokenizing Texts for NER]]
- [[Custom Model for Token Classification]]
- [[Loading a Custom Model]]
- [[Performance Measures for NER]]
- [[Error Analysis for NER]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
