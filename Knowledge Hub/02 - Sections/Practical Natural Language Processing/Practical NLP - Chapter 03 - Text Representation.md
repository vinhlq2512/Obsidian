---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: summarized
chapter: 3
start_page: 185
end_page: 243
reading_date: 2026-08-04
planned_sessions:
  - "Tự note nền | 185-243 | Không nằm trong daily reading | 0 phút"
tags:
  - nlp
  - practical-nlp
---

# Practical NLP - Chapter 03 - Text Representation

## Mục tiêu cần hiểu

- Vì sao cần biểu diễn text thành vector.
- Khác biệt giữa sparse representation và distributed representation.
- Khi nào dùng BoW/TF-IDF, khi nào cần embedding.
- Cách đọc và đánh giá embedding visualization một cách thận trọng.

## Tóm tắt nền đã tự note

- [[Text Representation]] là bước biến text thành dạng toán học để model có thể so sánh, phân loại, truy hồi hoặc gom cụm.
- Vector space model biểu diễn từ/câu/tài liệu bằng vector. Similarity thường được hiểu qua khoảng cách hoặc cosine similarity trong không gian vector.
- One-hot, Bag of Words, Bag of N-Grams và TF-IDF là các biểu diễn sparse. Chúng đơn giản, dễ debug, mạnh cho baseline, nhưng làm mất nhiều thông tin ngữ cảnh và thứ tự.
- Distributed representation như [[Embedding]] tạo vector dense, chiều thấp hơn, học từ context và có khả năng nắm semantic similarity tốt hơn.
- Representation có thể ở nhiều mức: character, subword, word, sentence, paragraph hoặc document. Mức biểu diễn phải khớp task.
- Visualization giúp nhìn trực giác embedding space nhưng dễ gây hiểu nhầm vì phép chiếu 2D/3D có thể bóp méo quan hệ trong không gian cao chiều.
- Handcrafted features vẫn hữu ích khi có domain signal rõ, dữ liệu ít, hoặc cần giải thích dễ hơn.

## Liên kết concept

- [[Text Representation]]
- [[Tokenization]]
- [[Embedding]]
- [[Semantic Search]]
- [[Text Classification]]
- [[Topic Modeling]]

## Mental model

```text
Text
-> token/unit
-> vector representation
-> similarity / classifier / retriever / clustering
-> evaluation theo task
```

## Phần cần biết

- Representation là lớp quyết định model nhìn thấy gì từ text.
- Mỗi representation đánh đổi giữa độ đơn giản, khả năng tổng quát, chi phí tính toán và khả năng giải thích.

## Câu hỏi review

1. BoW giữ lại thông tin gì và làm mất thông tin gì?
2. TF-IDF sửa điểm yếu nào của count-based representation?
3. Word embedding khác sparse vector ở trực giác nào?

## Gợi ý trả lời câu hỏi review

- BoW giữ tần suất từ nhưng mất thứ tự và nhiều ngữ cảnh.
- TF-IDF giảm trọng số từ xuất hiện quá phổ biến và tăng tín hiệu của từ phân biệt tài liệu tốt hơn.
- Embedding đặt text vào không gian dense nơi các item gần nhau có xu hướng gần về nghĩa hoặc chức năng theo dữ liệu học được.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Practical NLP - Chapter 02 - NLP Pipeline]]
- [[Practical NLP - Chapter 04 - Text Classification]]
