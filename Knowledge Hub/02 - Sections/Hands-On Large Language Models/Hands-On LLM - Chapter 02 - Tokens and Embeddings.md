---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 2
start_page: 67
end_page: 113
estimated_minutes: 110
need_review: true
tags:
  - llm
  - tokenization
  - embeddings
---

# Hands-On LLM - Chapter 02 - Tokens and Embeddings

## Mục tiêu cần hiểu

- Hiểu [[Tokenization]] biến text thành token IDs để model xử lý.
- Phân biệt word, subword, character và byte tokens.
- Nắm tokenizer properties: vocabulary, special tokens, cased/uncased behavior, unknown tokens và token boundary.
- Hiểu [[Embedding]] ở nhiều mức: token embedding, contextualized word embedding, sentence/document embedding.
- Biết embeddings cũng dùng được ngoài NLP, ví dụ recommendation systems.

## Định nghĩa quan trọng

- **Token**: đơn vị text mà model nhìn thấy, có thể là từ, mảnh từ, ký tự hoặc byte.
- **Tokenizer**: thành phần chuyển text thành chuỗi token IDs và chuyển IDs ngược lại thành text.
- **Vocabulary**: tập token mà tokenizer biết.
- **Special tokens**: token điều khiển như beginning/end of sequence, padding, mask hoặc classification token.
- **Token embedding**: vector gắn với một token trong vocabulary.
- **Contextualized embedding**: embedding của token sau khi đi qua model, phụ thuộc vào ngữ cảnh.
- **Text embedding**: vector biểu diễn cả câu, đoạn hoặc tài liệu.

## Mental model

Tokenizer là "cửa vào" của model. Model không đọc chữ trực tiếp; nó đọc số. Embedding table biến token ID thành vector ban đầu. Sau đó Transformer cập nhật vector này dựa trên context, tạo ra biểu diễn giàu nghĩa hơn.

## Phần cần biết

- Subword tokenization cân bằng giữa vocabulary size và khả năng xử lý từ hiếm.
- Byte-level tokenization có thể xử lý nhiều ký tự lạ nhưng sequence có thể dài hơn.
- Hai tokenizer khác nhau có thể chia cùng một câu thành số lượng token rất khác nhau.
- Contextualized embeddings giải quyết vấn đề một từ có nhiều nghĩa trong nhiều ngữ cảnh.
- Sentence/document embeddings phục vụ semantic search, clustering, recommendation và retrieval.

## Khi áp dụng

- Luôn kiểm tra số token, không chỉ số ký tự hoặc số từ.
- Khi thiết kế prompt dài, context window bị tiêu thụ theo token.
- Khi dùng embedding model cho search, cần chọn model phù hợp ngôn ngữ và domain.
- Với văn bản code hoặc đa ngôn ngữ, tokenizer behavior ảnh hưởng rất mạnh tới chi phí và chất lượng.

## Câu hỏi review

1. Vì sao cùng một text có thể tạo số token khác nhau giữa các model?
2. Token embedding khác sentence embedding thế nào?
3. Contextualized embedding giải quyết vấn đề gì của word embedding tĩnh?
4. Khi nào byte tokenization có lợi?

## Gợi ý trả lời câu hỏi review

1. Vì mỗi model có tokenizer riêng: vocabulary khác nhau, thuật toán tách token khác nhau, special tokens khác nhau và cách xử lý khoảng trắng/ký tự lạ khác nhau. Cùng một câu có thể thành ít token với tokenizer này nhưng nhiều token với tokenizer khác.
2. Token embedding biểu diễn một token riêng lẻ trong vocabulary hoặc trong context. Sentence embedding biểu diễn ý nghĩa của cả câu/đoạn/tài liệu, thường dùng để so sánh semantic similarity hoặc retrieval.
3. Contextualized embedding giải quyết chuyện một từ có nhiều nghĩa. Ví dụ cùng một token có thể mang nghĩa khác nhau tùy câu; embedding sau Transformer sẽ thay đổi theo ngữ cảnh xung quanh.
4. Byte tokenization có lợi khi cần xử lý văn bản đa ngôn ngữ, ký tự hiếm, emoji, code hoặc input lạ mà không muốn gặp unknown token. Đổi lại, chuỗi token có thể dài hơn.

## Liên kết

- [[Tokenization]]
- [[Embedding]]
- [[Semantic Search]]
- [[Large Language Model]]
