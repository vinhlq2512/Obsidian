---
type: concept
status: developing
sources:
  - "[[CS224N 2026 - Lecture 02 - Word Vectors]]"
  - "[[CS224N 2023 - Notes 01 - Introduction and Word2Vec - Draft]]"
  - "[[2013 - Efficient Estimation of Word Representations in Vector Space - arXiv 1301.3781v3]]"
source_sections:
  - "[[CS224N 2026 - Lecture 02 - Word Vectors]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
tags:
  - concept
  - nlp
  - cs224n
---

# Word2Vec

## Định nghĩa

Word2Vec là họ mô hình học [[Embedding|word embeddings]] bằng cách dự đoán quan hệ giữa một từ trung tâm và các từ xuất hiện quanh nó trong corpus.

## Cách hiểu bằng lời của tôi

Word2Vec biến câu hỏi "từ này nghĩa là gì?" thành câu hỏi dễ train hơn: "từ này thường xuất hiện cùng những từ nào?". Nếu hai từ xuất hiện trong ngữ cảnh giống nhau, training sẽ kéo vector của chúng về gần nhau.

## Cơ chế

Với skip-gram, model nhận center word $c$ và dự đoán outside/context word $o$:

$$
P(o|c) = \frac{\exp(u_o^T v_c)}{\sum_{w \in V}\exp(u_w^T v_c)}
$$

- $v_c$: vector của center word.
- $u_o$: vector output của context word.
- $u_o^T v_c$: điểm tương thích giữa center và context.
- Softmax biến score thành xác suất trên vocabulary.

## Điều cần biết

- Word2Vec dựa trên distributional semantics: từ có nghĩa tương tự thường xuất hiện trong context tương tự.
- Analogy tuyến tính là một dấu hiệu thú vị nhưng không đủ để kết luận embedding tốt cho task thật.
- Intrinsic evaluation nhanh, còn extrinsic evaluation mới kiểm tra giá trị trong downstream task.

## Liên kết

- [[Embedding]]
- [[Tokenization]]
- [[Loss Function]]
- [[CS224N]]
