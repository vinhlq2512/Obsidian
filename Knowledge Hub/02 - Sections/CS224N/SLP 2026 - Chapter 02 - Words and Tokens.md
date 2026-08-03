---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: textbook-chapter
title: "SLP 2026 - Chapter 02 - Words and Tokens"
year: 2026
venue: ""
arxiv: ""
source_file: "[[SLP 2026 - Chapter 02 - Words and Tokens.pdf]]"
pages: 36
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Embedding]]"
  - "[[Tokenization]]"
tags:
  - cs224n
  - textbook
---

# SLP 2026 - Chapter 02 - Words and Tokens

## Nguồn

- PDF gốc: [[SLP 2026 - Chapter 02 - Words and Tokens.pdf]]
- Vai trò trong CS224N: chapter nền về words, tokens, tokenization và xử lý text trước khi vào LM.

## Câu hỏi trung tâm

“Word” và “token” khác nhau thế nào, và vì sao tokenization là quyết định nền tảng trong NLP?

## Kiến thức cốt lõi

- Định nghĩa word phụ thuộc task: punctuation, spoken disfluency, contractions và morphology làm việc đếm word không đơn giản.
- Utterance trong spoken language có hiện tượng như fillers, fragments, repairs.
- Tokenizer biến text thành units mà model xử lý được.
- Punctuation và boundary markers có thể mang thông tin cú pháp/ngữ nghĩa.
- Chapter đặt nền cho Lecture 14 về tokenization hiện đại.

## Cơ chế / công thức / kiến trúc

```text
raw text / speech transcript
-> chuẩn hoá nếu cần
-> tách words/tokens
-> xử lý punctuation, contractions, morphology
-> sequence tokens cho downstream model
```

Điểm chính: tokenization không phải bước trung lập; nó định nghĩa input mà model thấy.

## Khi áp dụng

- Dùng trước khi học BPE/SentencePiece.
- Khi làm multilingual NLP, đừng giả định whitespace words là universal.
- Đối với spoken text, cần xử lý disfluencies và utterance boundaries.

## Kết quả / bằng chứng đáng giữ

- Chapter mở bằng ELIZA để cho thấy pattern matching trên words là NLP sơ khai.
- Trang 2 thảo luận số lượng words thay đổi nếu tính punctuation.
- Source nêu spoken language tạo complication khi định nghĩa words.

## Cách hiểu bằng lời của tôi

Token là giao diện giữa ngôn ngữ người và mô hình. Nếu giao diện này sai, mọi tầng sau đều học trên một phiên bản méo của text.

## Câu hỏi review

1. Vì sao đếm words trong một câu không luôn rõ ràng?
2. Token khác word ở điểm nào?
3. Punctuation có nên là token không?

## Liên kết

- [[Tokenization]]
- [[BPE]]
- [[SentencePiece]]
- [[CS224N]]
