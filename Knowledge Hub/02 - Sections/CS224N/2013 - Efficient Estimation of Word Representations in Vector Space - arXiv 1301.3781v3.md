---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2013 - Efficient Estimation of Word Representations in Vector Space"
year: 2013
venue: "arXiv"
arxiv: "1301.3781v3"
source_file: "[[2013 - Efficient Estimation of Word Representations in Vector Space - arXiv 1301.3781v3.pdf]]"
pages: 12
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Embedding]]"
  - "[[Tokenization]]"
tags:
  - cs224n
  - paper
---

# 2013 - Efficient Estimation of Word Representations in Vector Space - arXiv 1301.3781v3

## Nguồn

- PDF gốc: [[2013 - Efficient Estimation of Word Representations in Vector Space - arXiv 1301.3781v3.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 02 - Word Vectors]]
- Concept: [[Word2Vec]], [[Embedding]]

## Vấn đề paper giải quyết

Các mô hình neural language model trước đó học word representation tốt nhưng tốn compute. Paper này hỏi: có thể học vector từ cực nhiều text với chi phí thấp hơn nhưng vẫn giữ được chất lượng semantic/syntactic không?

## Đóng góp chính

- Đề xuất các kiến trúc đơn giản và hiệu quả để học continuous word vectors từ dataset rất lớn.
- Nhấn mạnh rằng chất lượng embedding có thể đo bằng word similarity và semantic/syntactic analogy.
- Cho thấy có thể học vector chất lượng cao trên corpus 1.6B words trong thời gian dưới một ngày theo mô tả abstract.

## Cơ chế cần nhớ

[[Word2Vec]] biến representation learning thành bài toán dự đoán context. Thay vì học nghĩa bằng nhãn thủ công, model học từ thống kê xuất hiện:

```text
word trong corpus
-> context window
-> objective dự đoán center/context
-> gradient kéo vector của các từ có context tương tự lại gần nhau
```

## Vì sao quan trọng với CS224N

Lecture 02 dùng paper này như mốc chuyển từ biểu diễn từ rời rạc sang vector học được từ dữ liệu. Đây là tiền đề cho toàn bộ deep NLP: token/word không còn chỉ là ID, mà là điểm trong không gian có quan hệ hình học.

## Hạn chế / câu hỏi

- Analogy task có thể đánh giá quá hẹp.
- Word-level embedding vẫn cho mỗi word một vector tương đối tĩnh, chưa xử lý tốt polysemy như contextual embeddings sau này.
- Cần hiểu thêm negative sampling/hierarchical softmax để nắm phần efficiency đầy đủ.

## Câu hỏi review

1. Vì sao paper này nhấn mạnh computational cost?
2. Word similarity và analogy đo được gì, bỏ sót gì?
3. Word2Vec khác one-hot representation ở tầng ý nghĩa nào?
