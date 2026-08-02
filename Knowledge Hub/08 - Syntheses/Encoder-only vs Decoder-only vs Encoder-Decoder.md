---
type: synthesis
status: evolving
concepts:
  - "[[Transformer]]"
  - "[[Bidirectional Attention]]"
  - "[[Decoder]]"
  - "[[Encoder-Decoder Architecture]]"
  - "[[Cross-Attention]]"
  - "[[Attention Mask]]"
sources:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
  - "[[27-07-2026]]"
questions:
  - "[[When to Use Representation Model Instead of Generative Model]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - synthesis
  - transformer
  - architecture
---

# Encoder-only vs Decoder-only vs Encoder-Decoder

## Câu hỏi trung tâm

- Khi chọn Transformer architecture, nên nhớ khác biệt theo cơ chế attention và loại task như thế nào?

## Mental model

```text
Encoder-only    -> đọc toàn bộ input -> understanding / representation
Decoder-only    -> chỉ nhìn prefix   -> generation / next-token prediction
Encoder-decoder -> encoder đọc input, decoder viết output -> sequence-to-sequence
```

## Bảng so sánh

| Nhóm | Cách nhìn context | Cơ chế chính | Ví dụ | Task phù hợp |
| --- | --- | --- | --- | --- |
| Encoder-only | Nhìn cả trái và phải | [[Bidirectional Attention]] | BERT, RoBERTa, DistilBERT | Classification, NER, semantic understanding |
| Decoder-only | Chỉ nhìn quá khứ/prefix | [[Attention Mask|Causal mask]] | GPT family | Text generation, chat, completion |
| Encoder-decoder | Encoder đọc input, decoder sinh output | [[Cross-Attention]] | T5, BART | Translation, summarization, seq2seq |

## Tổng hợp của tôi

- Tên model là ví dụ; điều cần nhớ là architecture quyết định model được phép nhìn context nào.
- Encoder-only mạnh cho understanding vì token nhìn được toàn bộ input.
- Decoder-only mạnh cho generation vì training/inference đều xoay quanh dự đoán token kế tiếp.
- Encoder-decoder phù hợp khi output là một sequence mới dựa trên input khác, vì decoder có cross-attention để nhìn encoder output.

## Điểm dễ nhầm

- Cùng là sinh văn bản, decoder-only và encoder-decoder không giống nhau: decoder-only sinh từ prefix, còn encoder-decoder sinh có điều kiện trên input đã được encoder đọc.
- [[Attention Mask]] không chỉ dùng cho padding; causal mask là thứ giữ decoder không nhìn token tương lai.

## Nguồn

- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
- [[27-07-2026]]
- [[Transformer]]
- [[Encoder-Decoder Architecture]]

## Liên kết

- [[Transformers]]
- [[Representation Model vs Generative Model vs RAG]]

