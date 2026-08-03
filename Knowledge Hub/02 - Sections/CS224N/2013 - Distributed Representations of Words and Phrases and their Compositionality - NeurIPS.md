---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2013 - Distributed Representations of Words and Phrases and their Compositionality"
year: 2013
venue: "NeurIPS"
arxiv: ""
source_file: "[[2013 - Distributed Representations of Words and Phrases and their Compositionality - NeurIPS.pdf]]"
pages: 9
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

# 2013 - Distributed Representations of Words and Phrases and their Compositionality - NeurIPS

## Nguồn

- PDF gốc: [[2013 - Distributed Representations of Words and Phrases and their Compositionality - NeurIPS.pdf]]
- Vai trò trong CS224N: paper mở rộng [[Word2Vec]] với subsampling, negative sampling và phrase representations.

## Câu hỏi trung tâm

Làm thế nào cải thiện chất lượng và tốc độ học distributed representations cho từ và cụm từ?

## Kiến thức cốt lõi

- Continuous Skip-gram học vector tốt bằng cách dự đoán nearby words.
- Subsampling frequent words giúp tăng tốc và cải thiện representation cho từ ít gặp.
- Negative sampling là lựa chọn đơn giản hơn hierarchical softmax để train nhanh.
- Phrase representations xử lý những cụm có nghĩa không phải tổng đơn giản của từng từ.
- Paper củng cố ý tưởng rằng vector space có thể mã hoá quan hệ semantic/syntactic có cấu trúc.

## Cơ chế / công thức / kiến trúc

```text
corpus
-> tạo center/context pairs
-> bỏ bớt từ quá phổ biến bằng subsampling
-> train skip-gram với negative sampling
-> học vector cho word và phrase
```

Negative sampling biến bài toán softmax toàn vocabulary thành nhiều bài toán phân biệt context thật với negative examples.

## Khi áp dụng

- Dùng khi cần hiểu vì sao word2vec train được trên corpus rất lớn.
- Dùng để đọc các paper embedding sau này so sánh local prediction vs count-based statistics.
- Cẩn thận với phrase detection: không phải mọi cụm đều compositional.

## Kết quả / bằng chứng đáng giữ

- Abstract nêu extensions cải thiện quality và training speed.
- Source nói subsampling frequent words tạo speedup đáng kể và giúp vector regular hơn.
- Source mô tả negative sampling như alternative đơn giản cho hierarchical softmax.

## Cách hiểu bằng lời của tôi

Paper này là bản word2vec thực dụng hơn: không chỉ ý tưởng center/context, mà còn các trick làm nó đủ nhanh và đủ tốt để dùng ở scale lớn.

## Câu hỏi review

1. Subsampling frequent words giải quyết vấn đề gì?
2. Negative sampling thay đổi bài toán train như thế nào?
3. Vì sao phrase representation cần thiết?

## Liên kết

- [[Word2Vec]]
- [[Embedding]]
- [[Loss Function]]
- [[GloVe]]
- [[CS224N]]
