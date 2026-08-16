---
type: concept
status: developing
sources:
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - retrieval
  - recommendation
  - feed
---

# Feed Retrieval

## Định nghĩa

Feed retrieval là tầng lấy một tập candidate nhỏ từ corpus rất lớn trước khi ranking đắt tiền sắp xếp nội dung trong feed.

## Cách hiểu bằng lời của tôi

Feed không thể score hàng trăm triệu post bằng model nặng trong vài trăm mili-giây. Retrieval là bước rẻ và rộng: giảm toàn bộ corpus xuống khoảng vài trăm hoặc vài nghìn candidate, rồi ranking mới dùng compute đắt hơn.

## Vì sao clickbait liên quan đến retrieval

Nếu retrieval tối ưu theo engagement thô, nó sẽ học đưa lên những nội dung tạo click/comment dễ nhất, kể cả khi nội dung đó không thật sự có giá trị. Chặn clickbait bằng rule chỉ xử lý triệu chứng; sửa retrieval metric mới đụng vào gốc.

## Liên kết

- [[Semantic Retrieval]]
- [[Recommendation Funnel]]
- [[Product Recommendation System]]
- [[AI Search]]
- [[Two-Tower Retrieval]]
