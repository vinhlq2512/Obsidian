---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 02 - Tokens and Embeddings]]"
  - "[[Hands-On LLM - Chapter 10 - Creating Text Embedding Models]]"
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
last_updated: 2026-08-10
tags:
  - concept
  - embeddings
  - retrieval
---

# Embedding

## Định nghĩa

Embedding là vector số biểu diễn token, từ, câu, đoạn hoặc tài liệu trong không gian nhiều chiều.

## Cách hiểu bằng lời của tôi

Embedding là cách biến ý nghĩa thành tọa độ. Nếu hai text gần nhau trong embedding space, ta kỳ vọng chúng có liên quan theo tiêu chí mà model đã học.

## Cần biết

- Token embedding là input ban đầu của model.
- Word embedding là vector dense cho một word; có thể dùng pretrained models như [[Word2Vec]] để tạo feature cho text classification.
- Document embedding là vector dense cho cả document, sentence hoặc paragraph; ví dụ Doc2Vec học representation trực tiếp cho text unit lớn hơn word.
- Contextualized embedding phụ thuộc vào câu xung quanh.
- Text embedding dùng cho semantic search, clustering, classification và recommendation.
- Similarity không cố định; nó phụ thuộc objective và dữ liệu training.

## Word embeddings trong text classification

```text
Text
-> tokenization
-> lookup word embeddings
-> average word vectors
-> document/sentence feature vector
-> classifier
```

- So với [[Bag of Words]], word embeddings tạo dense low-dimensional features thay vì sparse high-dimensional vectors.
- Một cách đơn giản là average embeddings của các words trong text để tạo một vector đại diện cho cả câu/document.
- Nếu dùng pretrained embeddings, các OOV words không có trong vocabulary có thể bị bỏ qua hoặc cần xử lý riêng.
- Practical NLP dùng pretrained [[Word2Vec]] Google News model, lấy vector 300 chiều và train Logistic Regression, đạt khoảng 81% accuracy trên sentiment sentences dataset.
- Cần kiểm tra vocabulary overlap giữa domain mới và pretrained embedding vocabulary; sách nêu rule of thumb là overlap lớn hơn 80% thường cho kết quả tốt.
- Trade-off thực tế: pretrained embedding model có thể rất lớn, ví dụ khoảng 3.6GB, nên memory/load time cũng là một phần của deployment decision.

## Document embeddings trong text classification

```text
Document
-> tokenize
-> train / load document embedding model
-> infer document vector
-> classifier
```

- [[Document Embedding]] học representation cho toàn bộ sentence/paragraph/document, thay vì average các word vectors.
- Practical NLP dùng Doc2Vec cho tweet emotion classification; dữ liệu tweet cần tokenizer riêng vì ngắn, nhiều hashtag, handle, emoticon và spelling biến dạng.
- Doc2Vec cần lựa chọn hyperparameter như `vector_size`, `alpha`, `min_count`, `dm`/`dbow` và `epochs`.
- Khi infer vector cho text mới, có thể chạy nhiều steps để representation ổn định hơn.
- Kết quả ví dụ đạt F1 khoảng 0.51 trên 3 class, cho thấy embedding method không tự đảm bảo tốt nếu text quá ngắn/nhiễu hoặc feature chưa hợp task.

## Embedding lookup khi thiếu nhãn

Trong bài toán ít hoặc chưa có nhãn, embedding có thể dùng để khám phá dữ liệu trước khi train classifier.

```text
Unlabeled texts
-> Encode thành text embeddings
-> Tính similarity / clustering
-> Tìm nhóm câu gần nhau
-> Chọn representative examples để gán nhãn
```

Khi đã có vài ví dụ gán nhãn, có thể dùng nearest-neighbor:

```text
New utterance
-> Embedding
-> Tìm labeled example gần nhất
-> Dự đoán label theo neighbor
```

Điểm cần nhớ: embedding lookup không học decision boundary rõ như classifier. Nó dựa vào giả định rằng các câu cùng nhãn nằm gần nhau trong embedding space. Nếu các intent gần nghĩa hoặc embedding model không hợp domain, kết quả dễ nhiễu.

## Liên kết

- [[Semantic Search]]
- [[Contrastive Learning]]
- [[Representation Model]]
- [[Retrieval-Augmented Generation]]
- [[Few-shot Learning]]
- [[Intent Detection]]
- [[Word2Vec]]
- [[Document Embedding]]
- [[Bag of Words]]
- [[Text Classification]]
