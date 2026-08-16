---
type: concept
status: understood
sources:
  - "[[2026-07-23_a-beginners-guide-to-clocks-causality-and-ordering-in-distri]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - distributed-systems
  - database
---

# TrueTime

## Định nghĩa

TrueTime là API đồng bộ thời gian phân tán do Google thiết kế cho cơ sở dữ liệu Spanner. API này không chỉ trả về một mốc thời gian duy nhất mà trả về một khoảng thời gian $[t_{\text{earliest}}, t_{\text{latest}}]$ đại diện cho khoảng độ bất định thời gian thực (time uncertainty bound $\epsilon$).

## Cơ chế hoạt động

```text
TrueTime API -> [t_earliest, t_latest]
trong đó: t_latest - t_earliest = 2 * epsilon (thường epsilon < 7ms)
```

- **Phần cứng chuyên dụng**: Google trang bị kết hợp cả Master Clock bằng **Đồng hồ nguyên tử (Atomic Clocks)** và **Đầu thu GPS** tại mỗi data center để giảm giá trị $\epsilon$ xuống mức cực nhỏ (vài millisecond).
- **Commit Wait Rule**: Để đảm bảo tính nhất quán Strict Serializability trên quy mô toàn cầu, khi giao dịch $T_1$ commit tại $t_{\text{absolute}}$, node phải chờ đúng khoảng thời gian $2\epsilon$ trước khi cho phép giao dịch $T_2$ đọc dữ liệu. Việc chờ này đảm bảo $T_2$ luôn thấy timestamp của $T_1$ xảy ra hoàn toàn trong quá khứ.

## Ý nghĩa trong Distributed Databases

TrueTime cho phép Google Spanner đạt được tính nhất quán [[Strict Serializability]] và [[External Consistency]] trên quy mô toàn cầu mà không cần sự trợ giúp của một đợt giao tiếp giữa các datacenter để thỏa thuận thứ tự timestamp.

## Trade-off

- **Ưu điểm**: Đạt tính nhất quán cao nhất thế giới (External Consistency) với hiệu năng truy vấn đọc vượt trội.
- **Nhược điểm**: Đòi hỏi hạ tầng phần cứng đắt đỏ (GPS + Atomic Clock) và cam kết vận hành cực kỳ nghiêm ngặt; nếu $\epsilon$ phồng to do sự cố phần cứng, latency ghi của hệ thống sẽ tăng theo.

## Liên kết

- [[Logical Clocks]]
- [[Strict Serializability]]
- [[Consensus]]
- [[Distributed Systems]]
