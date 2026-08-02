---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
source_sections:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
first_seen: 2026-08-01
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - question-answering
---

# Span Classification

## Định nghĩa

Span classification là bài toán chọn một đoạn liên tục trong input bằng cách dự đoán vị trí bắt đầu và vị trí kết thúc của đoạn đó. Trong QA, nó là cơ chế lõi của [[Extracting Answers from Text]].

## Cách hiểu bằng lời của tôi

Trong [[Extractive QA]], model không sinh câu trả lời mới. Nó biến mỗi token trong context thành một ứng viên "có thể là điểm bắt đầu" và "có thể là điểm kết thúc", rồi chọn cặp vị trí có score tốt nhất.

```text
question + context
-> encoder tạo hidden states cho từng token
-> start classifier chấm điểm token bắt đầu
-> end classifier chấm điểm token kết thúc
-> chọn answer span trong context
```

## Phần cần biết

- Đây là một dạng classification trên từng token, nhưng kết quả cuối cùng là một span gồm nhiều token liên tiếp.
- Trong QA, thường có hai vector logit: `start_logits` và `end_logits`.
- Cần loại các span không hợp lệ, ví dụ end đứng trước start hoặc span nằm trong phần question/special tokens.
- Với context dài, cùng một câu hỏi có thể chạy qua nhiều window; sau đó hệ thống chọn span có score cao nhất.
- Span classification phù hợp khi câu trả lời xuất hiện nguyên văn trong context, nhưng kém phù hợp khi cần tổng hợp nhiều nguồn hoặc diễn đạt lại.
- Sau khi chọn span ở mức token, cần dùng offset mapping từ [[Tokenizer Pipeline]] để cắt lại answer trong text gốc.

## Ví dụ nhỏ

```text
Question: Transformers dùng thư viện nào?
Context: Hugging Face cung cấp thư viện Transformers cho pretrained models.

start -> "Transformers"
end   -> "Transformers"
answer span -> "Transformers"
```

## Khi áp dụng

- Dùng cho [[Extractive QA]] khi muốn trích câu trả lời từ context đã cho.
- Trong hệ thống nhiều tài liệu, [[Retriever]] tìm passage trước, còn [[Reader]] dùng span classification để trích đáp án.
- Khi debug QA model, nên xem cả score của start token, end token và span được chọn.

## Câu hỏi review

1. Vì sao extractive QA thường được xem như bài toán span classification?
2. `start_logits` và `end_logits` đại diện cho điều gì?
3. Khi nào span được chọn có thể không hợp lệ?
4. Span classification khác text generation ở điểm nào?

## Gợi ý trả lời câu hỏi review

1. Vì model chọn một đoạn có sẵn trong context bằng cách dự đoán token bắt đầu và token kết thúc.
2. Chúng là điểm số cho khả năng mỗi token là vị trí bắt đầu hoặc kết thúc của câu trả lời.
3. Khi end trước start, span nằm ngoài context, quá dài, hoặc rơi vào token đặc biệt.
4. Span classification trích nguyên văn từ input; text generation tự tạo chuỗi output mới.

## Liên kết

- [[Question Answering]]
- [[Extracting Answers from Text]]
- [[Extractive QA]]
- [[Reader]]
- [[Retriever]]
- [[Tokenizer Pipeline]]
- [[NLP Transformers - Chapter 07 - Question Answering]]
