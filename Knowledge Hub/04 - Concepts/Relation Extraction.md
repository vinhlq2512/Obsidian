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

# Relation Extraction

## Định nghĩa

Relation extraction là task trích quan hệ giữa các entities được nhắc trong text.

## Cách hiểu bằng lời của tôi

NER tìm các “điểm”; relation extraction nối các điểm đó bằng một cạnh có nghĩa. Ví dụ không chỉ biết `Luca Maestri` và `Apple`, mà biết quan hệ `finance chief of`.

Nếu [[Entity Linking]] giúp xác định đúng node trong knowledge base, thì relation extraction quyết định giữa các node đó có cạnh nào. Output có thể được xem như triple hoặc record:

```text
(entity_1, relation, entity_2)
```

## Trong IE

```text
entity A
entity B
context
-> relation label / relation record
```

- Practical NLP dùng ví dụ: `Luca Maestri` là finance chief của `Apple`.
- Relation extraction cần nhiều thông tin hơn NER vì phải hiểu mối liên hệ giữa nhiều entity trong cùng context.
- Đây là bước quan trọng để biến text thành structured records hoặc knowledge graph.
- RE hữu ích cho knowledge base, search và [[Question Answering]] vì nó không chỉ lưu entity, mà lưu cách các entity liên quan với nhau.

## Vì sao khó

- Phải hiểu words nối giữa entities và sense của cách dùng trong sentence.
- Phải quyết định “relation” nào đáng trích, trong khi relation schema phụ thuộc domain.
- Medical domain, financial domain, news và social media có thể cần các relation set rất khác nhau.
- RE phụ thuộc các bước trước như [[Named Entity Recognition]], [[Entity Linking]], parsing và coreference resolution; lỗi upstream có thể làm sai relation downstream.

## Hướng tiếp cận

### Pattern-based

- Dùng handcrafted patterns hoặc regular expressions để bắt relation cụ thể.
- Ví dụ pattern kiểu `PER, [something] of ORG` có thể gợi ý relation “is-a-part-of” giữa person và organization.
- Ưu điểm: precision cao nếu pattern đúng.
- Nhược điểm: coverage thấp, khó phủ hết relation và biến thể ngôn ngữ trong domain.

### Supervised classification

Sách mô tả supervised RE như hai bước:

```text
entity pair
-> related / not related
-> relation label nếu related
```

- Bước 1 là binary classification: hai entities có liên quan không?
- Bước 2 là multiclass classification: nếu có, relation là loại nào?
- Feature có thể là context quanh entity, syntactic structure như `NP VP NP`, handcrafted features, embeddings hoặc neural architecture.

### Weak/distant supervision

- Bootstrapping bắt đầu từ seed patterns nhỏ, rồi dùng sentences match pattern để học thêm patterns mới.
- [[Distant Supervision]] dùng database lớn như Wikipedia/Freebase để tạo nhiều examples relation tự động.
- [[Weak Supervision]] phù hợp khi thiếu labeled data nhưng có rules, seed patterns hoặc external knowledge base để tạo noisy labels.

### Open IE

- Open IE không cần relation list cố định hoặc training data.
- Output thường là tuple dạng `<verb, argument1, argument2, ...>`.
- Ưu điểm là bắt được relation mở.
- Nhược điểm là phải map tuple tự do về schema chuẩn nếu muốn dùng trong database/knowledge graph.

## Trade-off triển khai

- Pretrained/service-based RE có thể nhanh để thử, nhưng thường bị giới hạn bởi preset relation list.
- Model hoặc API chạy tốt trên Wikipedia chưa chắc chạy tốt trên general news hoặc social media.
- Practical NLP khuyên bắt đầu bằng pattern-based approach và thêm weak supervision khi supervised pretrained model không hợp domain.

## Liên kết

- [[Information Extraction]]
- [[Named Entity Recognition]]
- [[Entity Linking]]
- [[Information Extraction Pipeline]]
- [[Weak Supervision]]
- [[Distant Supervision]]
- [[Question Answering]]
