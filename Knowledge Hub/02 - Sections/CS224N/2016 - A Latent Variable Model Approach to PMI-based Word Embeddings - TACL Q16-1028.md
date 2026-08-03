---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2016 - A Latent Variable Model Approach to PMI-based Word Embeddings"
year: 2016
venue: "TACL"
arxiv: ""
source_file: "[[2016 - A Latent Variable Model Approach to PMI-based Word Embeddings - TACL Q16-1028.pdf]]"
pages: 16
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

# 2016 - A Latent Variable Model Approach to PMI-based Word Embeddings - TACL Q16-1028

## Nguồn

- PDF gốc: [[2016 - A Latent Variable Model Approach to PMI-based Word Embeddings - TACL Q16-1028.pdf]]
- Vai trò trong CS224N: paper lý thuyết giải thích vì sao PMI, word2vec và GloVe có liên hệ với low-rank word statistics.

## Câu hỏi trung tâm

Vì sao PMI matrix có thể được xấp xỉ bởi low-rank word vectors và điều đó nói gì về embedding?

## Kiến thức cốt lõi

- Paper đề xuất generative latent variable model cho text.
- Từ model này, tác giả suy ra biểu thức closed-form cho word statistics.
- Kết quả cung cấp lý giải lý thuyết cho PMI-based embeddings, word2vec và GloVe.
- Quan hệ gần đúng $<v_w, v_{w\prime}> pprox PMI(w,w\prime)$ là điểm trung tâm.
- Paper làm rõ vì sao embedding dimension thấp vẫn có thể chứa nhiều thông tin thống kê.

## Cơ chế / công thức / kiến trúc

Công thức cần nhớ:

$$
\langle v_w, v_{w'} angle pprox PMI(w,w')
$$

Trực giác: nếu xác suất hai từ đồng xuất hiện cao hơn mức độc lập, PMI cao; embedding học sao cho dot product phản ánh liên hệ đó.

## Khi áp dụng

- Dùng để nối count-based distributional semantics với neural embeddings.
- Hữu ích khi cần giải thích vì sao dot product trong embedding có nghĩa thống kê.
- Không cần nắm toàn bộ proof ở lần đọc đầu, nhưng cần giữ mental model PMI thấp chiều.

## Kết quả / bằng chứng đáng giữ

- Abstract nói paper đưa ra generative model và closed-form expressions cho word statistics.
- Source nhấn mạnh PMI matrix được xấp xỉ bằng low-rank matrix.
- Paper giải thích các lựa chọn hyperparameter/reweighting trong các embedding methods.

## Cách hiểu bằng lời của tôi

Embedding không phải phép màu. Một phần sức mạnh của nó đến từ việc nén ma trận đồng xuất hiện khổng lồ vào không gian thấp chiều nhưng vẫn giữ được cấu trúc PMI quan trọng.

## Câu hỏi review

1. PMI đo quan hệ gì giữa hai từ?
2. Vì sao low-rank approximation quan trọng với embedding?
3. Paper này nối PMI với word2vec/GloVe như thế nào?

## Liên kết

- [[Embedding]]
- [[Word2Vec]]
- [[GloVe]]
- [[CS224N]]
