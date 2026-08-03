---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2016 - Neural Machine Translation of Rare Words with Subword Units"
year: 2016
venue: "arXiv"
arxiv: "1508.07909v5"
source_file: "[[2016 - Neural Machine Translation of Rare Words with Subword Units - arXiv 1508.07909v5.pdf]]"
pages: 11
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

# 2016 - Neural Machine Translation of Rare Words with Subword Units - arXiv 1508.07909v5

## Nguồn

- PDF gốc: [[2016 - Neural Machine Translation of Rare Words with Subword Units - arXiv 1508.07909v5.pdf]]
- Vai trò trong CS224N: paper nền cho [[BPE]] và subword tokenization trong NMT/LLM.

## Câu hỏi trung tâm

Làm thế nào NMT xử lý rare words và open vocabulary mà không cần dictionary backoff phức tạp?

## Kiến thức cốt lõi

- NMT dùng fixed vocabulary nhưng dịch thuật là open-vocabulary problem.
- Paper encode rare/unknown words thành sequences of subword units.
- BPE được chuyển từ compression sang word segmentation.
- Subword giúp xử lý names, compounds, cognates và morphology.
- Đây là nền trực tiếp cho tokenization hiện đại trong LLM.

## Cơ chế / công thức / kiến trúc

```text
training text
-> học BPE merges
-> rare word được tách thành subword units
-> encoder-decoder NMT xử lý chuỗi subword
-> output subword được ghép lại thành word
```

Mấu chốt: vocabulary cố định nhưng có thể biểu diễn từ mới bằng chuỗi token nhỏ hơn.

## Khi áp dụng

- Dùng khi thiết kế tokenizer cho ngôn ngữ nhiều morphology hoặc từ mới.
- Hữu ích khi hiểu vì sao LLM không dùng word-level vocabulary thuần.
- Cần nhớ subword không luôn trùng với đơn vị nghĩa.

## Kết quả / bằng chứng đáng giữ

- Abstract nói rare/unknown words được encode as sequences of subword units.
- Source nêu BPE cho phép open vocabulary với fixed-size vocabulary.
- Paper so sánh cách này với large vocabularies và back-off dictionaries.

## Cách hiểu bằng lời của tôi

Subword tokenization là mẹo rất thực tế: không cần biết mọi từ trước, chỉ cần biết đủ mảnh để lắp lại từ mới.

## Câu hỏi review

1. Vì sao fixed word vocabulary gây lỗi với rare words?
2. BPE giúp open-vocabulary translation như thế nào?
3. Subword units tốt hơn dictionary backoff ở điểm nào?

## Liên kết

- [[BPE]]
- [[Tokenization]]
- [[SentencePiece]]
- [[Encoder-Decoder Architecture]]
- [[CS224N]]
