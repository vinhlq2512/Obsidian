---
type: concept
status: seed
sources:
  - "[[2026-05-20_how-netflix-is-using-multimodal-ai-to-power-video-search]]"
source_sections:
  - "[[2026-05-20_how-netflix-is-using-multimodal-ai-to-power-video-search]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - multimodal
  - search
  - ai
---

# Multimodal Annotation Fusion

## Định nghĩa

[[Multimodal Annotation Fusion]] là bước hợp nhất output từ nhiều model/modalities thành một representation chung có thể index và query.

## Cách hiểu bằng lời của tôi

Trong video search, mỗi model nhìn footage theo cách khác nhau: character model trả label, scene model trả embedding, dialogue model trả transcript có timestamp. Nếu không fuse chúng vào cùng mốc thời gian, query kiểu "nhân vật X ở địa điểm Y nói câu Z" sẽ rất khó chạy nhanh.

## Cơ chế từ nguồn Netflix

```text
raw model outputs
-> map interval liên tục thành bucket thời gian
-> intersect annotation trong cùng bucket
-> ghi record fused theo asset + second
-> index parent/child document để query cross-annotation
```

## Quyết định thiết kế

- Bucket nhỏ tăng precision nhưng tăng số record.
- Fusion offline giữ ingestion nhẹ và query nhanh, đổi lại freshness kém hơn.
- Update record theo bucket giúp thêm model mới mà không tạo duplicate timeline.
- Parent/child index giúp exact label, transcript và vector embedding cùng nằm trong một context truy vấn.

## Liên kết

- [[Multimodal Search]]
- [[Hybrid Retrieval]]
- [[Vector Search Infrastructure]]
- [[Cassandra]]
- [[AI Search]]
