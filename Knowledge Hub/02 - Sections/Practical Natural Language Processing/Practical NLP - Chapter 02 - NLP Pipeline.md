---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: summarized
chapter: 2
start_page: 106
end_page: 180
reading_date: 2026-08-04
planned_sessions:
  - "Tự note nền | 106-180 | Không nằm trong daily reading | 0 phút"
tags:
  - nlp
  - practical-nlp
---

# Practical NLP - Chapter 02 - NLP Pipeline

## Mục tiêu cần hiểu

- Các pha chính của pipeline NLP từ lấy dữ liệu đến deployment.
- Cleanup, preprocessing và feature engineering ảnh hưởng tới model như thế nào.
- Vì sao evaluation, monitoring và model updating là một phần của hệ thống chứ không phải việc phụ.

## Tóm tắt nền đã tự note

- [[NLP Pipeline]] bắt đầu từ data acquisition: dữ liệu có thể đến từ web, log, ticket, review, document hoặc API. Chất lượng nguồn quyết định trần hiệu năng của hệ thống.
- Text extraction và cleanup xử lý HTML, encoding, Unicode, lỗi chính tả và lỗi hệ thống. Đây không phải bước máy móc: mỗi quyết định cleanup có thể xóa tín hiệu quan trọng.
- Preprocessing gồm normalization, tokenization, stopword/stemming/lemmatization khi phù hợp, và các bước nâng cao theo task. Với DL pipeline, nhiều bước cổ điển có thể được thay bằng tokenizer/model-specific processing.
- Feature engineering nối text với model. Classical NLP/ML thường cần feature rõ; DL pipeline học representation nhiều hơn từ dữ liệu nhưng vẫn cần kiểm soát input, label và distribution.
- Modeling nên đi từ heuristic/baseline đơn giản đến model phức tạp hơn. Baseline giúp biết lỗi đến từ dữ liệu, label, task formulation hay capacity của model.
- Evaluation gồm intrinsic evaluation cho component và extrinsic evaluation cho tác động sản phẩm. Sau deployment cần monitoring, model updating và xử lý drift.
- Case study COTA của Uber minh họa pipeline NLP như hệ thống ranking/decision hỗ trợ customer care, không chỉ là một classifier cô lập.

## Liên kết concept

- [[NLP Pipeline]]
- [[Tokenization]]
- [[Text Representation]]
- [[Embedding]]
- [[Model Benchmarking]]

## Mental model

```text
Raw text
-> acquisition
-> extraction / cleanup
-> preprocessing
-> representation / features
-> baseline
-> model
-> evaluation
-> deployment
-> monitoring
-> update loop
```

## Phần cần biết

- Chapter này là xương sống cho các chapter sau: mỗi task NLP thực tế đều quay về pipeline này.
- Khi đọc Part II, luôn hỏi: task này thay đổi bước nào trong pipeline chung?

## Câu hỏi review

1. Intrinsic evaluation và extrinsic evaluation khác nhau ở điểm nào?
2. Vì sao preprocessing không nên được xem là bước cơ học?
3. Monitoring trong NLP cần theo dõi những thay đổi nào của dữ liệu/người dùng?

## Gợi ý trả lời câu hỏi review

- Intrinsic đo component/model theo metric nội bộ; extrinsic đo hệ thống trong mục tiêu cuối như giảm ticket time, tăng search success hoặc giảm escalation.
- Preprocessing là quyết định thông tin: xóa punctuation, lowercase, normalize slang hoặc sửa lỗi chính tả đều có thể làm mất tín hiệu tùy task.
- Monitoring cần theo dõi data drift, label drift, user behavior, lỗi theo slice, latency, cost và phản hồi người dùng.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Practical NLP - Chapter 01 - NLP A Primer]]
- [[Practical NLP - Chapter 03 - Text Representation]]
