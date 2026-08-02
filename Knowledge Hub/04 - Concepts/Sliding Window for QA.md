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
  - tokenization
---

# Sliding Window for QA

## Định nghĩa

Sliding window for QA là kỹ thuật chia context dài thành nhiều window chồng lấn để model extractive QA có thể đọc từng phần mà không vượt giới hạn sequence length.

## Cách hiểu bằng lời của tôi

Không thể cứ cắt bỏ cuối context như text classification, vì answer có thể nằm ở cuối đoạn. Sliding window giống cách kéo một khung đọc qua context: mỗi khung giữ nguyên question và chứa một phần context.

```text
question + long context
-> window 1: question + context part 1
-> window 2: question + overlapping context part 2
-> window 3: question + overlapping context part 3
-> chọn answer tốt nhất từ các window
```

## Tham số quan trọng

- `max_length` hoặc `max_seq_length`: số token tối đa trong mỗi input window.
- `stride` hoặc `doc_stride`: số token overlap giữa các window.
- `return_overflowing_tokens`: bật chế độ trả về nhiều window khi context quá dài.

## Vì sao cần overlap

Answer có thể nằm ngay ranh giới giữa hai window. Nếu không có overlap, một answer span có thể bị cắt đôi và reader không thấy đủ context để trích đúng.

## Điểm cần cẩn thận

- Window càng nhiều thì recall answer có thể tốt hơn, nhưng latency tăng.
- Stride quá nhỏ có thể cắt mất answer ở biên; stride quá lớn làm trùng lặp nhiều và tốn compute.
- Khi nhiều window trả về cùng answer, pipeline cần xếp hạng hoặc loại duplicate.

## Câu hỏi review

1. Vì sao truncation đơn giản nguy hiểm trong QA?
2. `doc_stride` giải quyết vấn đề gì?
3. Sliding window đánh đổi recall và latency như thế nào?

## Gợi ý trả lời câu hỏi review

1. Vì answer có thể nằm ở phần context bị cắt bỏ.
2. Nó tạo overlap giữa các window để giảm nguy cơ cắt đôi answer hoặc mất context quanh answer.
3. Nhiều window/overlap lớn giúp ít mất answer hơn nhưng phải chạy model nhiều lần hơn.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Question Answering]]
- [[Tokenizing Text for QA]]
- [[Extractive QA]]
- [[Extracting Answers from Text]]
- [[Reader]]
