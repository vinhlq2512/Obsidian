---
type: concept
status: developing
sources:
  - "[[2026-07-28_why-doordash-instacart-and-uber-eats-integrated-llms-into-se]]"
  - "[[2026-05-05_how-instacart-built-a-search-for-billions-of-products]]"
  - "[[2026-05-27_how-airtable-built-the-search-layer-behind-their-ai-features]]"
  - "[[2026-04-27_how-amazon-uses-llms-to-recommend-products]]"
  - "[[2026-05-20_how-netflix-is-using-multimodal-ai-to-power-video-search]]"
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - llm
  - recommendation
---

# AI Search

## Định nghĩa

AI search là hệ thống tìm kiếm dùng model học máy hoặc LLM để hiểu intent, tạo representation, mở rộng/chuẩn hóa query, retrieve candidate và hỗ trợ ranking.

## Cách hiểu bằng lời của tôi

Search hiện đại không chỉ hỏi "có từ này trong document không". Nó phải hiểu người dùng muốn gì, catalog đang có gì, item nào còn available, constraint nào là hard filter, tín hiệu nào là soft preference, rồi trả kết quả đủ nhanh để user không rời đi.

## Các lớp thường gặp

- Query understanding: parse intent, entity, constraint, synonym, rewrite.
- Candidate generation: keyword search, [[Semantic Search]], graph retrieval hoặc ANN.
- Guardrail: giới hạn output bằng taxonomy, similarity filter hoặc business rule.
- Ranking: kết hợp relevance, availability, personalization và conversion signal.
- Feedback loop: dùng click/purchase/complaint/zero-result để cải thiện.

## Từ ByteByteGo

DoorDash, Instacart và Uber Eats cùng dùng LLM cho search nhưng đặt LLM ở các độ sâu khác nhau. DoorDash dùng LLM để enrich graph và parse query có ràng buộc; Instacart dùng LLM cho query understanding, head query cache và tail query real-time; Uber Eats đưa fine-tuned LLM vào embedding backbone của retrieval.

Netflix video search cho thấy AI search có thể bắt đầu từ dữ liệu phi văn bản. Hệ thống chạy nhiều model chuyên biệt trên video để nhận diện nhân vật, scene, dialogue và object, rồi fusion các annotation theo bucket thời gian trước khi index vào Elasticsearch. Search runtime sau đó kết hợp keyword matching, vector search, threshold, phrase slop, fuzzy matching và post-processing để tái tạo scene phù hợp.

Feed retrieval case của LinkedIn/Meta/YouTube cho thấy search/recommendation còn là bài toán chọn proxy đúng. Nếu retrieval tối ưu engagement thô, clickbait có lợi thế kiến trúc. Semantic retrieval đổi proxy sang meaning, còn ranking funnel hoặc generative retrieval là các cách khác nhau để trả chi phí compute.

## Liên kết

- [[Query Understanding]]
- [[Semantic Search]]
- [[Semantic Retrieval]]
- [[Feed Retrieval]]
- [[Vector Search Infrastructure]]
- [[Two-Tower Retrieval]]
- [[Commonsense Knowledge Graph]]
- [[Product Recommendation System]]
- [[Multimodal Search]]
