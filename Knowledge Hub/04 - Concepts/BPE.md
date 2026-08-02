---
type: concept
status: developing
sources:
  - "[[CS224N 2026 - Lecture 07 - Pretraining]]"
  - "[[CS224N 2026 - Lecture 14 - Tokenization and Multilinguality]]"
  - "[[2016 - Neural Machine Translation of Rare Words with Subword Units - arXiv 1508.07909v5]]"
source_sections:
  - "[[CS224N 2026 - Lecture 14 - Tokenization and Multilinguality]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
tags:
  - concept
  - tokenization
  - cs224n
---

# BPE

## Định nghĩa

BPE, hay Byte Pair Encoding, là phương pháp học vocabulary subword bằng cách lặp lại thao tác merge cặp token liền nhau xuất hiện phổ biến nhất trong corpus.

## Cách hiểu bằng lời của tôi

BPE là cách thoả hiệp giữa character-level và word-level tokenization. Từ phổ biến có thể được giữ thành token lớn; từ hiếm bị tách thành nhiều mảnh nhỏ hơn thay vì trở thành `UNK`.

## Thuật toán

```text
khởi tạo vocabulary bằng ký tự/byte
-> đếm các cặp token liền nhau
-> merge cặp phổ biến nhất thành token mới
-> cập nhật segmentation
-> lặp đến khi đạt vocab size
```

## Trade-off

- Giảm out-of-vocabulary vì từ mới vẫn có thể tách thành subword.
- Vocabulary hữu hạn nên phù hợp với [[Large Language Model]].
- Segment không nhất thiết trùng với morpheme hoặc đơn vị nghĩa.
- Có thể bất công giữa ngôn ngữ nếu corpus/vocabulary thiên về một số ngôn ngữ.

## Liên kết

- [[Tokenization]]
- [[SentencePiece]]
- [[Multilingual Transformer]]
- [[CS224N]]
