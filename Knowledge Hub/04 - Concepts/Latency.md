---
type: concept
status: developing
sources:
  - "[[2025-01-23_top-strategies-to-reduce-latency]]"
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
  - "[[2025-09-09_how-netflix-tudum-supports-20-million-users-with-cqrs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - performance
  - reliability
---

# Latency

## Định nghĩa

Latency là độ trễ từ lúc bắt đầu một request/operation đến khi nhận được kết quả hoặc phản hồi.

## Cách hiểu bằng lời của tôi

Latency là thời gian user hoặc service phải chờ. Nó khác bandwidth và throughput: bandwidth là sức chứa đường truyền, throughput là lượng xử lý thực tế, còn latency là độ trễ cảm nhận trên từng operation.

## Các nguồn latency

- Network latency: khoảng cách vật lý, routing, congestion, packet loss.
- Server latency: thời gian xử lý request, query database, gọi dependency.
- Client-side latency: render, JavaScript blocking, device chậm hoặc asset quá lớn.
- Tail latency: p95/p99 tăng do overload, lock, queue hoặc dependency chậm.

## Vì sao liên quan đến reliability

Latency spike có thể bị đọc thành failure. Khi timeout và retry bật lên, một vấn đề performance có thể biến thành [[Retry Storm]], [[Cascading Failure]] hoặc [[Metastable Failure]].

## Khi deadline rất ngắn

Trong live streaming, latency không chỉ ảnh hưởng cảm nhận user mà còn quyết định segment có còn hữu ích hay không. Nguồn Netflix Live Origin mô tả retry budget khoảng vài giây và yêu cầu write rất nhanh; vì vậy read surge từ CDN phải được tách khỏi publishing path. Trong Tudum, latency của preview lại đến từ read path nhiều hop và cache refresh lệch nhịp, nên tối ưu nằm ở việc đưa read model vào memory của service.

## Liên kết

- [[Timeout]]
- [[Observability]]
- [[Service Level Indicator]]
- [[Caching Strategy]]
- [[Content Delivery Network]]
- [[Database Indexing]]
- [[Live Streaming Origin]]
- [[In-Memory Read Model]]
