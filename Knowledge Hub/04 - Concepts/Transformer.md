---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 03 - Looking Inside Large Language Models]]"
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - transformer
  - llm
---

# Transformer

## Định nghĩa

Transformer là kiến trúc neural network dựa trên attention, dùng để xử lý sequence và là nền tảng của nhiều language models hiện đại.

## Cách hiểu bằng lời của tôi

Transformer cập nhật biểu diễn của từng token bằng cách cho token đó nhìn các token liên quan trong context. Nó không cần xử lý tuần tự như RNN, nên train song song hiệu quả hơn.

## Cần biết

- Thành phần chính: attention, feed-forward/MLP, residual connections, normalization, positional embeddings.
- Encoder-only phù hợp understanding/classification.
- Decoder-only phù hợp text generation.
- Encoder-decoder phù hợp sequence-to-sequence như translation hoặc summarization.
- Transformer gốc được thiết kế cho sequence-to-sequence tasks như machine translation, nhưng encoder và decoder block sau đó được dùng riêng thành các model family độc lập.
- Phần lớn Transformer models có thể gom vào ba nhóm: encoder-only, decoder-only, encoder-decoder.
- [[Multilingual Transformer]] là hướng dùng cùng một Transformer đã pretrain trên nhiều ngôn ngữ để hỗ trợ transfer giữa các ngôn ngữ.

## Ba nhóm Transformer chính

| Nhóm | Cách hoạt động | Model ví dụ | Task phù hợp |
| --- | --- | --- | --- |
| Encoder-only | Đọc toàn bộ input và tạo representation | BERT, RoBERTa, DistilBERT | Classification, NER, semantic understanding |
| Decoder-only | Sinh token tiếp theo từ context bên trái | GPT | Chat, completion, text generation |
| Encoder-decoder | Encoder đọc input, decoder sinh output | T5, BART | Translation, summarization, seq2seq |

Mental model ngắn: encoder để hiểu, decoder để sinh, encoder-decoder để chuyển đổi chuỗi.

## Liên kết

- [[Self-Attention]]
- [[Bidirectional Attention]]
- [[Decoder]]
- [[Encoder-Decoder Architecture]]
- [[Tokenization]]
- [[Embedding]]
- [[Positional Embeddings]]
- [[Generative Model]]
- [[Multilingual Transformer]]
