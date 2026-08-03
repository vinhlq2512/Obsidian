---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2020 - Contextual Word Representations - A Contextual Introduction"
year: 2020
venue: "arXiv"
arxiv: "1902.06006v3"
source_file: "[[2020 - Contextual Word Representations - A Contextual Introduction - arXiv 1902.06006v3.pdf]]"
pages: 15
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Embedding]]"
  - "[[Tokenization]]"
tags:
  - cs224n
  - paper
---

# 2020 - Contextual Word Representations - A Contextual Introduction - arXiv 1902.06006v3

## Nguồn

- PDF gốc: [[2020 - Contextual Word Representations - A Contextual Introduction - arXiv 1902.06006v3.pdf]]
- Vai trò trong CS224N: bài đọc giải thích chuyển đổi từ static embeddings sang contextual representations.

## Câu hỏi trung tâm

Vì sao một từ cần representation thay đổi theo context thay vì một vector cố định?

## Kiến thức cốt lõi

- Static embeddings như Word2Vec/GloVe gán mỗi word type một vector.
- Contextual representations tạo vector cho từng token occurrence trong câu.
- Một từ đa nghĩa có thể có representation khác nhau tùy context.
- Transformer/BERT làm contextualization bằng self-attention.
- Đây là cầu nối khái niệm từ word vectors sang pretrained language models.

## Cơ chế / công thức / kiến trúc

```text
word type: bank -> static vector duy nhất
word occurrence trong câu -> contextual vector phụ thuộc các token xung quanh
self-attention/RNN -> trộn context -> representation mới
```

## Khi áp dụng

- Dùng khi giải thích vì sao BERT mạnh hơn static embeddings cho NLU.
- Hữu ích khi phân biệt embedding layer ban đầu với hidden states contextualized.
- Cần nhớ contextual representation thường gắn với token, layer và context cụ thể.

## Kết quả / bằng chứng đáng giữ

- Title nêu contextual word representations.
- CS224N dùng nó sau embedding để chuẩn bị cho Transformer/BERT.
- Concept này giải thích hạn chế polysemy của static embeddings.

## Cách hiểu bằng lời của tôi

Static embedding trả lời “từ này thường nghĩa là gì”; contextual representation trả lời “lần xuất hiện này của từ này đang nghĩa là gì trong câu này”.

## Câu hỏi review

1. Static và contextual embeddings khác nhau ở đơn vị biểu diễn nào?
2. Self-attention tạo contextualization bằng cách nào?
3. Vì sao polysemy làm static embedding yếu?

## Liên kết

- [[Embedding]]
- [[Self-Attention]]
- [[Bidirectional Attention]]
- [[Transformer]]
- [[CS224N]]
