---
type: concept
status: understood
sources:
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2023-09-21_a-crash-course-in-redis]]"
source_sections:
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2023-09-21_a-crash-course-in-redis]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-structures
  - redis
---

# Redis Sorted Set

## Định nghĩa

Redis Sorted Set là data structure giữ member duy nhất kèm score, cho phép query theo rank hoặc range với latency thấp.

## Cách hiểu bằng lời của tôi

Sorted Set biến bài toán leaderboard thành primitive sẵn có: update score, lấy top N, lấy rank của user. Redis dùng cấu trúc như hash table và skip list để vừa lookup member vừa duy trì thứ tự theo score.

## Khi dùng

- Leaderboard game hoặc social app.
- Ranking top item theo doanh số, điểm, lượt tương tác.
- Rate/window tracking đơn giản khi cần sort theo timestamp hoặc score.

## Giới hạn

- Nếu update cực lớn với hàng chục triệu user đồng thời, chi phí duy trì thứ tự có thể thành bottleneck và cần thiết kế chuyên biệt hơn.

## Liên kết

- [[Redis]]
- [[Ranking]]
- leaderboard
- [[Redis Data Structures]]
