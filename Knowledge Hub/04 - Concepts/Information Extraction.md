---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 05 - Information Extraction]]"
first_seen: 2026-08-11
last_updated: 2026-08-11
tags:
  - concept
  - nlp
  - information-extraction
---

# Information Extraction

## Định nghĩa

Information extraction là nhóm tác vụ NLP trích thông tin liên quan từ văn bản, ví dụ entities, events, relations hoặc fields có thể đưa vào dữ liệu có cấu trúc.

## Cách hiểu bằng lời của tôi

IE là bước biến text phi cấu trúc thành những mẩu dữ liệu máy có thể dùng tiếp: tag để search, slot cho chatbot, event để theo dõi, hoặc field để nhập vào hệ thống.

## Vì sao khó

- Database/table có schema rõ, còn text tự nhiên thường là free-flowing text không có vị trí cố định cho từng loại thông tin.
- Một số thông tin có pattern cố định như phone number, date hoặc address có thể trích bằng rule/regex.
- Thông tin như person, organization, location, event hoặc relation giữa entities thường cần NLP processing sâu hơn.

## Ứng dụng

```text
News / social posts / forms / user queries
-> extract entities, events, fields, relations
-> search, recommendation, chatbot, monitoring, workflow
```

- **News tagging**: trích people, organizations, locations và events để hỗ trợ search/recommendation.
- **Chatbots**: trích thông tin cụ thể trong câu hỏi, ví dụ location và object of interest.
- **Social media**: trích thông tin time-sensitive như traffic updates hoặc disaster relief efforts.
- **Forms and receipts**: kết hợp OCR để đọc text từ ảnh với IE để lấy field có ý nghĩa.

## Các task chính

```text
Keyword/keyphrase
-> entity mention
-> entity identity
-> relation
-> event / temporal information
-> template slot
```

- [[Keyphrase Extraction]] tìm keyword/keyphrase biểu diễn chủ đề chính của text.
- [[Named Entity Recognition]] nhận diện span/entity type như person, organization, location hoặc event.
- [[Entity Linking]] phân biệt entity mention đang nói tới thực thể cụ thể nào trong thế giới hoặc knowledge base.
- [[Relation Extraction]] trích quan hệ giữa entities.
- [[Event Extraction]] nhận diện event và có thể liên kết nhiều text nói về cùng event.
- [[Template Filling]] đưa thông tin đã trích vào một schema/slot cố định.

## Pipeline tổng quát

IE thường dùng [[Information Extraction Pipeline]] với nhiều mức phân tích:

```text
Raw text
-> sentence segmentation
-> word tokenization
-> POS tagging
-> syntactic parsing / NER
-> coreference resolution / entity disambiguation
-> relation extraction / event extraction
```

- IE thường NLP-intensive hơn [[Text Classification]] vì nhiều task cần output ở mức span, entity, relation hoặc event.
- Không phải task nào cũng cần đủ mọi bước: [[Keyphrase Extraction]] là nhóm cần ít preprocessing hơn, còn relation/event/entity disambiguation thường cần cấu trúc sâu hơn.
- Độ chính xác của pipeline IE phụ thuộc cả model task-specific lẫn chất lượng preprocessing trước đó.

## Trade-off triển khai

- IE thường cần annotation mịn hơn [[Text Classification]], ví dụ span, identity, relation hoặc slot.
- Task càng sâu thì càng phụ thuộc vào preprocessing như POS tagging, coreference resolution và model task-specific.
- Trong industry, IE thường là hybrid system kết hợp rule-based và learning-based approaches vì domain rất quan trọng.
- Precision, recall và F1 là nhóm metric phổ biến để đánh giá IE task.

## Liên kết

- [[Named Entity Recognition]]
- [[Keyphrase Extraction]]
- [[Entity Linking]]
- [[Relation Extraction]]
- [[Event Extraction]]
- [[Template Filling]]
- [[Information Extraction Pipeline]]
- [[Text Classification]]
- [[NLP Pipeline]]
- [[Extractive QA]]
