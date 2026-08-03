---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 07 - Pretraining"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 07 - Pretraining.pdf]]"
pages: 56
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Transfer Learning]]"
  - "[[Large Language Model]]"
tags:
  - cs224n
  - lecture
---
# CS224N 2026 - Lecture 07 - Pretraining

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 07 - Pretraining.pdf]]
- Vai trò trong khoá: giải thích pretraining, subword modeling và ba họ pretrained Transformer.
- Paper đọc kèm: [[2018 - BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding - arXiv 1810.04805v2]], [[2020 - Language Models are Few-Shot Learners - arXiv 2005.14165v4]], [[2016 - Neural Machine Translation of Rare Words with Subword Units - arXiv 1508.07909v5]].

## Mục tiêu cần hiểu

- Vì sao pretraining dùng dữ liệu không nhãn ở scale lớn.
- Subword modeling giải quyết OOV và vocabulary coverage ra sao.
- Encoder, decoder và encoder-decoder được pretrain bằng objective khác nhau.
- In-context learning xuất hiện khi model decoder rất lớn học từ prompt mà không update trọng số.

## Ý chính

- Pretraining tận dụng dữ liệu thô lớn vì labeled data không scale đủ.
- Subword tokenization cho phép xử lý từ hiếm, biến thể, typo và từ mới bằng các mảnh token đã biết.
- Encoder pretraining thường học bidirectional representation qua masked language modeling.
- Decoder pretraining học next-token prediction, tạo nền cho generation và in-context learning.
- Encoder-decoder pretraining học biến đổi input sang output, hợp với seq2seq như summarization/translation.

## [[BPE|Byte Pair Encoding]]

[[BPE]] bắt đầu từ vocabulary ký tự, rồi lặp lại:

```text
đếm cặp token liền nhau phổ biến nhất
-> merge cặp đó thành token mới
-> cập nhật corpus đã segment
-> lặp đến khi đạt vocab size
```

Hệ quả:

- Từ phổ biến có thể thành một token.
- Từ hiếm bị tách thành nhiều subword.
- Không cần map mọi từ lạ thành `UNK`.

## Ba hướng pretraining

| Kiến trúc | Objective điển hình | Năng lực chính |
| --- | --- | --- |
| Encoder | Masked language modeling | hiểu input hai chiều |
| Decoder | Next-token prediction | sinh văn bản autoregressive |
| Encoder-decoder | denoising/seq2seq | chuyển đổi chuỗi |

## Cách hiểu bằng lời của tôi

Pretraining là cách biến Internet thành giáo viên yếu nhưng cực lớn. Model không cần nhãn thủ công; objective tự tạo nhãn từ text. Sau pretraining, model đã có representation/ngôn ngữ nền, rồi downstream chỉ cần fine-tune, prompt hoặc adapt.

## Câu hỏi review

1. Vì sao pretraining không dùng labeled data làm nguồn chính?
2. [[BPE]] khác word-level tokenization ở điểm nào?
3. Encoder pretraining và decoder pretraining tối ưu objective gì?
4. In-context learning khác fine-tuning như thế nào?

## Liên kết

- [[Tokenization]]
- [[SentencePiece]]
- [[Transfer Learning]]
- [[Bidirectional Attention]]
- [[Autoregressive Language Model]]
- [[Large Language Model]]
- [[CS224N]]
