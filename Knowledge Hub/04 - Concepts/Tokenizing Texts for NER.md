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
  - tokenization
---

# Tokenizing Texts for NER

## Định nghĩa

Tokenizing texts for NER là quá trình biến câu và nhãn NER ở mức word/span thành input token/subword cho Transformer, đồng thời căn chỉnh nhãn sao cho mỗi token được train đúng hoặc được bỏ qua đúng cách.

## Cách hiểu bằng lời của tôi

Với text classification, tokenize xong chỉ cần một nhãn cho cả câu. Với [[Named Entity Recognition]], mỗi word có thể có một nhãn riêng, trong khi tokenizer có thể tách word đó thành nhiều subword. Vì vậy phần khó không phải chỉ là tạo `input_ids`, mà là giữ mapping từ subword trở về word gốc.

## Luồng tổng quát

```text
words + word-level NER tags
-> tokenizer(is_split_into_words=True)
-> input_ids + attention_mask + word_ids
-> align labels theo word_ids
-> token-level labels có -100 ở vị trí cần ignore
```

## Các bước thực hiện

### 1. Chuẩn bị input dạng word list

NER dataset thường có dạng:

```text
tokens = ["Nguyễn", "Nhật", "Ánh", "sinh", "tại", "Quảng", "Nam"]
ner_tags = ["B-PER", "I-PER", "I-PER", "O", "O", "B-LOC", "I-LOC"]
```

Điểm cần nhớ: labels đang gắn với word gốc, chưa gắn với subword.

### 2. Tokenize với `is_split_into_words=True`

Khi input đã là list từ, gọi tokenizer theo kiểu:

```python
tokenized = tokenizer(
    tokens,
    is_split_into_words=True,
    truncation=True,
)
```

Tham số này báo cho tokenizer biết rằng input đã được pre-tokenized. Nếu quên tham số này, tokenizer có thể hiểu sai cấu trúc input.

### 3. Lấy `word_ids()`

Sau khi tokenize, dùng:

```python
word_ids = tokenized.word_ids()
```

`word_ids()` cho biết mỗi token/subword thuộc về word index nào.

Ví dụ mental model:

```text
tokens:     <s>  Nguyễn  Nhật  Ánh  sinh  tại  Quảng  Nam  </s>
word_ids:  None   0       1     2     3     4     5      6   None
```

Nếu một word bị tách thành nhiều subword:

```text
word:      internationalization
subwords:  inter  national  ization
word_ids:  0      0         0
```

### 4. Align labels sang token/subword

Chiến lược phổ biến:

- Special tokens có `word_id = None` -> label `-100`.
- Subword đầu tiên của mỗi word -> nhận label thật.
- Subword phụ của cùng word -> label `-100`.

Lý do: `-100` được PyTorch cross-entropy ignore, nên model không bị tính loss cho special tokens hoặc subword phụ.

### 5. Cẩn thận nếu label mọi subword

Một chiến lược khác là propagate label sang mọi subword. Khi đó cần chỉnh BIO tags:

- subword đầu tiên của entity dùng `B-...`.
- subword tiếp theo nên dùng `I-...`.

Nếu không, model có thể học sai rằng nhiều subword liên tiếp đều là điểm bắt đầu entity.

### 6. Kiểm tra thủ công vài ví dụ

Trước khi train, nên in ra:

- tokens sau tokenizer.
- `word_ids`.
- labels sau alignment.
- nhãn bị ignore `-100`.

Điểm cần nhớ: bug alignment thường không làm code crash ngay, nhưng làm model học sai ranh giới entity.

## Cần biết

- Tokenization cho NER luôn đi cùng label alignment.
- `word_ids()` hữu ích khi dùng Hugging Face fast tokenizers.
- `offset_mapping` hữu ích khi cần map prediction về character span trong text gốc.
- `-100` thường dùng để bỏ qua vị trí không tính loss.
- Với [[SentencePiece]] hoặc multilingual tokenizers, một word/tên riêng có thể bị tách thành nhiều subword hơn, nên alignment càng quan trọng.

## Liên kết

- [[Named Entity Recognition]]
- [[Tokenizer Pipeline]]
- [[SentencePiece]]
- [[Tokenization]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
