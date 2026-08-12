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

# Entity Linking

## Định nghĩa

Entity linking là task nối một entity mention trong text với thực thể cụ thể tương ứng trong knowledge base hoặc thế giới thực.

Named entity disambiguation (NED) là bước gán unique identity cho mention. Khi kết hợp [[Named Entity Recognition]] với NED, sách gọi tổng thể này là named entity linking (NEL).

## Cách hiểu bằng lời của tôi

NER chỉ nói “Apple” là một organization. Entity linking phải nói rõ đó là Apple Inc., không phải trái táo hay một tổ chức khác có chữ Apple.

Một mention string tự nó chưa đủ tin cậy. `Lincoln` có thể là người, xe hoặc địa danh; `Washington` có thể là người, bang, thành phố hoặc organization trong một số context. Entity linking dùng context quanh mention và knowledge base để biến chuỗi chữ thành một thực thể có identity ổn định.

## Trong IE

```text
text
-> NER tìm mention/span + type
-> disambiguation bằng context
-> linked entity trong knowledge base
```

- Practical NLP gộp named entity disambiguation and linking như một task IE sau NER.
- Task này cần context quanh mention để phân biệt các thực thể có cùng tên hoặc tên gần giống nhau.
- Entity linking làm entity trở thành dữ liệu có thể query và nối vào knowledge base.
- Khi đã link được identity, downstream task như [[Relation Extraction]], [[Question Answering]] hoặc knowledge graph construction có thể nối đúng các thực thể thay vì chỉ nối surface strings.

## Điều kiện triển khai

- Cần output từ [[Named Entity Recognition]] hoặc một bước phát hiện mention tương đương.
- Thường cần linguistic context sâu hơn POS tagging, ví dụ parsing để biết subject/verb/object.
- Có thể cần coreference resolution để gom nhiều reference cùng trỏ tới một entity, ví dụ `Albert Einstein`, `Einstein`, `the scientist`.
- Cần một knowledge base hoặc encyclopedic resource để chọn entity đích, ví dụ Wikipedia/DBpedia hoặc KB nội bộ.
- Nếu train model supervised, cần annotated dataset đủ lớn và đánh giá bằng precision, recall, F1.

## Trade-off

- NEL chuyên biệt hơn KPE/NER nên tự xây in-house thường đắt hơn.
- Dịch vụ có sẵn như Azure Text Analytics hoặc DBpedia Spotlight có thể là điểm bắt đầu nhanh.
- Điểm yếu là tên mới, domain-specific terms và việc khó kiểm soát preprocessing/internal behavior của third-party services.
- Chỉ nên thêm NEL vào pipeline khi use case cần unique identity; nếu chỉ cần biết có entity type nào xuất hiện, [[Named Entity Recognition]] có thể đủ.

## Liên kết

- [[Information Extraction]]
- [[Named Entity Recognition]]
- [[Relation Extraction]]
- [[Question Answering]]
