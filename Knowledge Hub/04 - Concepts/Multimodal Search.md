---
type: concept
status: developing
sources:
  - "[[2026-05-20_how-netflix-is-using-multimodal-ai-to-power-video-search]]"
  - "[[2026-07-07_chatgpt-vs-gemini-vs-claude-how-they-differ]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - multimodal
  - ai
---

# Multimodal Search

## Định nghĩa

Multimodal search là hệ thống tìm kiếm trên nhiều dạng dữ liệu như text, image, audio hoặc video, trong đó mỗi modality được biến thành metadata, transcript, embedding hoặc annotation để truy vấn chung.

## Cách hiểu bằng lời của tôi

Nếu search truyền thống xem document là text, multimodal search xem một video hay asset như một chuỗi bằng chứng: ai xuất hiện, cảnh nào đang diễn ra, dialogue nói gì, object nào có mặt, thời điểm nào khớp với query. Điểm khó là gom các bằng chứng có format và độ dài thời gian khác nhau thành một index có thể query nhanh.

## Cơ chế từ ByteByteGo

Netflix video search dùng pipeline ba lớp:

- Annotation ingestion: nhiều model chuyên biệt đọc footage và sinh output khác nhau như character, scene embedding, transcript và object.
- Temporal fusion: gom annotation theo bucket thời gian, ví dụ từng giây, để những tín hiệu cùng đoạn video có thể được truy vấn cùng nhau. Xem [[Multimodal Annotation Fusion]].
- Search index: lưu nested document trong Elasticsearch để runtime query có thể kết hợp keyword, vector similarity, confidence threshold và fuzzy matching.

## Trade-off

- Fusion offline làm dữ liệu bớt tươi ngay lập tức, nhưng giữ ingestion và query latency ổn định.
- Ensemble nhiều model chuyên biệt dễ debug và kiểm soát hơn, nhưng tạo bài toán hợp nhất schema/thời gian.
- Một foundation model native multimodal có thể đơn giản hóa pipeline, nhưng production vẫn phải chứng minh latency, quality và khả năng giải thích.

## Liên kết

- [[AI Search]]
- [[Semantic Search]]
- [[Vector Search Infrastructure]]
- [[Multimodal LLM]]
- [[Foundation Model for Recommendation]]
- [[Multimodal Annotation Fusion]]
- [[Hybrid Retrieval]]
