---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-11
last_updated: 2026-08-11
tags:
  - concept
  - nlp
  - classification
---

# Ticket Routing

## Định nghĩa

Ticket routing là bài toán tự động phân loại ticket hoặc request rồi chuyển tới người, team hoặc workflow phù hợp.

## Cách hiểu bằng lời của tôi

Đây là [[Text Classification]] ở dạng sản phẩm vận hành. Label không chỉ là nhãn để báo cáo; label quyết định ticket đi đâu, ai xử lý, và lỗi phân loại sẽ ảnh hưởng trực tiếp tới thời gian phản hồi.

## Workflow khi thiếu nhãn

```text
Ticket history chưa có label cần dùng
-> baseline từ API / public dataset / weak supervision
-> deploy nhỏ hoặc thử nghiệm
-> thu explicit + implicit feedback
-> active learning chọn ticket cần gán nhãn
-> cải thiện classifier
```

- Practical NLP dùng corporate ticketing làm case study: công ty cần phát hiện medical-related issues để route tới medical counsel hoặc hospital, nhưng ticket cũ chưa có label health-related.
- Một baseline có thể đến từ API/library public và mapping category ngoài vào taxonomy nội bộ.
- Một baseline khác có thể đến từ public dataset như 20 Newsgroups, dùng `sci.med` làm positive class.
- [[Weak Supervision]] có thể tạo nhãn khởi động bằng rule, ví dụ ticket chứa từ như `fever`, `diarrhea`, `headache`, `nausea`.
- [[Active Learning]] giúp chọn ticket descriptions đáng hỏi human annotators khi ngân sách gán nhãn hạn chế.

## Feedback loop

- Explicit feedback: người nhận ticket nói ticket relevant hoặc không relevant.
- Implicit feedback: response time, response rate hoặc các biến vận hành khác cho thấy route có thể đang đúng/sai.
- Khi dữ liệu tích lũy đủ hơn, có thể thử model phức tạp hơn; trước đó, baseline và feedback loop thường quan trọng hơn chọn architecture lớn.

## Liên kết

- [[Text Classification]]
- [[Weak Supervision]]
- [[Active Learning]]
- [[Domain Adaptation]]
- [[Few-shot Learning]]
