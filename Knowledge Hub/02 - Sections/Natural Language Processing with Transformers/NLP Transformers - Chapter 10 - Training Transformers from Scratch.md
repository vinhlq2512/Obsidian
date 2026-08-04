---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 10
start_page: 326
end_page: 392
reading_date: 2026-08-07
planned_sessions:
  - "2026-08-07 | 326-358 | Khi nào train từ đầu, corpus và tokenizer | 60 phút"
  - "2026-08-08 | 359-392 | Pretraining loop, chi phí và tóm tắt quyết định | 60 phút"
estimated_minutes: 120
actual_minutes:
need_review: false
tags:
  - nlp
  - pretraining
  - tokenizer
---

# NLP Transformers - Chapter 10 - Training Transformers from Scratch

## Mục tiêu đọc

- Hiểu khi nào cần train từ đầu thay vì fine-tune.
- Nắm cách xây dựng corpus lớn và tokenizer riêng.
- Biết các bước pretraining model ở mức kiến trúc và training loop.

## Ý chính

- Train từ đầu cần dữ liệu lớn, compute lớn và mục tiêu rõ ràng.
- Tokenizer ảnh hưởng trực tiếp đến khả năng biểu diễn domain-specific text.
- Pretraining objectives quyết định model học loại thông tin nào từ corpus.

## Khi nào nên train từ đầu?

Train from scratch chỉ hợp lý khi:

- pretrained models sẵn có không khớp domain hoặc ngôn ngữ;
- tokenizer hiện có phân mảnh domain text quá tệ;
- mục tiêu là xây foundation model riêng chứ không chỉ giải một downstream task.

Nếu chỉ cần hiệu quả tốt trên một task cụ thể, fine-tuning thường rẻ và thực tế hơn nhiều.

## Corpus và tokenizer

Chapter này nhấn mạnh rằng corpus không chỉ cần lớn mà còn phải:

- đủ sạch;
- đủ đại diện cho domain;
- tránh quá nhiều duplicate hoặc text rác;
- phù hợp với tokenizer mà mình sẽ train.

[[Tokenizer Training]] là phần quan trọng vì tokenizer quyết định model “nhìn” text theo những mảnh nào.

## Pretraining objectives và training loop

- [[Language Modeling]] là lõi của pretraining.
- Encoder-style models thường gắn với [[Masked Language Modeling]].
- Decoder-style models thường gắn với [[Causal Language Model|causal language modeling]].
- [[Training Loop]] ở quy mô này không chỉ là code loop đơn giản mà còn là bài toán throughput, checkpointing, batching, streaming và compute budget.

## Checklist quyết định

```text
Có model pretrained phù hợp chưa?
-> Có: ưu tiên fine-tuning
-> Chưa: kiểm tra domain gap lớn đến mức nào

Có đủ corpus sạch và compute không?
-> Không: chưa nên train từ đầu
-> Có: cân nhắc tokenizer + objective + training loop
```

## Demo thực hành

Train tokenizer nhỏ trên corpus toy.

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer

corpus = [
    "transformers are useful for natural language processing",
    "tokenizers split text into tokens",
    "domain specific data can need a custom tokenizer",
]

with open("toy_corpus.txt", "w") as f:
    for line in corpus:
        f.write(line + "\n")

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()
trainer = BpeTrainer(vocab_size=50, special_tokens=["[UNK]", "[PAD]"])

tokenizer.train(["toy_corpus.txt"], trainer)
encoded = tokenizer.encode("transformers tokenize domain text")

print(encoded.tokens)
```

## Khái niệm quan trọng

- [[Pretraining]]
- [[Tokenizer Training]]
- [[BPE]]
- [[Language Modeling]]
- [[Training Loop]]
- [[Working with Large Datasets]]

## Active Recall

1. Khi nào train từ đầu hợp lý hơn fine-tune?
2. Corpus cho pretraining cần kiểm soát những rủi ro nào?
3. Tokenizer riêng giúp gì cho domain đặc thù?
4. Pretraining objective ảnh hưởng output cuối như thế nào?

## Checklist

- [x] Đọc xong chapter
- [ ] Chạy demo tokenizer
- [x] Viết lại pipeline train từ đầu bằng 5 bước
- [x] Tách concept cần dùng lại
- [x] Cập nhật tiến độ sách
