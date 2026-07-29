---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: planned
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

## Active Recall

1. Khi nào train từ đầu hợp lý hơn fine-tune?
2. Corpus cho pretraining cần kiểm soát những rủi ro nào?
3. Tokenizer riêng giúp gì cho domain đặc thù?
4. Pretraining objective ảnh hưởng output cuối như thế nào?

## Checklist

- [ ] Đọc xong chapter
- [ ] Chạy demo tokenizer
- [ ] Viết lại pipeline train từ đầu bằng 5 bước
- [ ] Tách concept cần dùng lại
- [ ] Cập nhật tiến độ sách
