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
  - consistency
---

# External Consistency

## Định nghĩa

External Consistency (Tính nhất quán bên ngoài / Strict Serializability) là cấp độ nhất quán mạnh nhất trong các hệ thống cơ sở dữ liệu phân tán. Nó đảm bảo rằng nếu một giao dịch $T_1$ hoàn tất (commit) trước khi giao dịch $T_2$ bắt đầu theo thời gian thực (real-world wall-clock time), thì mọi client trong hệ thống đều phải thấy hiệu ứng của $T_1$ trước $T_2$.

## Ý nghĩa & Cơ chế

- **Strict Serializability**: Kết hợp cả tính chất Serializability (ACID) và Linearizability.
- **Triển khai**: Để đạt External Consistency trên quy mô toàn cầu (như Google Spanner), hệ thống sử dụng phần cứng đồng hồ nguyên tử và GPS cùng API [[TrueTime]] để áp dụng quy tắc Commit Wait, đảm bảo không có hai giao dịch nào bị đảo ngược thứ tự thời gian thực.

## Trade-off

- Latency của thao tác ghi bị ảnh hưởng bởi độ bất định thời gian ($\epsilon$) của phần cứng.
- Chi phí hạ tầng và vận hành phần cứng đồng bộ thời gian rất cao.

## Liên kết

- [[TrueTime]]
- [[Linearizability]]
- [[Serializability]]
- [[Strict Serializability]]
