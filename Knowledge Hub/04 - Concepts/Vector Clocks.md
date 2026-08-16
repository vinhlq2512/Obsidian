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
---

# Vector Clocks

## Định nghĩa

Vector Clocks là phần mở rộng của [[Lamport Timestamps]] trong đó mỗi tiến trình $P_i$ duy trì một mảng (vector) $V_i$ kích thước $N$ (với $N$ là số lượng tiến trình trong hệ thống). Kỹ thuật này cho phép phát hiện chính xác mối quan hệ nguyên nhân - kết quả (causality) và các sự kiện ghi song song xung đột (concurrent updates / causal conflicts).

## Quy tắc cập nhật

Cho hệ thống gồm $N$ tiến trình:

1. **Ban đầu**: $V_i[k] = 0$ với mọi $k \in [1, N]$.
2. **Sự kiện nội bộ**: $P_i$ tăng giá trị bản thân: $V_i[i] = V_i[i] + 1$.
3. **Gửi tin nhắn**: $P_i$ tăng $V_i[i] = V_i[i] + 1$ và gửi kèm vector $V_i$ trong tin nhắn $m$.
4. **Nhận tin nhắn**: Khi $P_j$ nhận tin nhắn chứa vector $V_m$:
   - Với mọi $k \in [1, N]$: $V_j[k] = \max(V_j[k], V_m[k])$.
   - Tăng phần tử bản thân: $V_j[j] = V_j[j] + 1$.

## So sánh Vector & Phát hiện Xung đột

Cho hai vector $V_A$ và $V_B$:
- $V_A \le V_B$ nếu $V_A[k] \le V_B[k]$ với mọi $k$.
- $V_A < V_B$ nếu $V_A \le V_B$ và tồn tại ít nhất một $k$ mà $V_A[k] < V_B[k]$ (tức $A \rightarrow B$).
- **Concurrent Conflict**: Nếu $V_A \not< V_B$ và $V_B \not< V_A$, hai sự kiện là song song ($A \parallel B$). Hệ thống phát hiện xung đột và yêu cầu ứng dụng tự resolve (ví dụ: Amazon Dynamo sibling resolution).

## Trade-off

- **Ưu điểm**: Phát hiện 100% sự kiện xung đột và causality hai chiều ($V_A < V_B \iff A \rightarrow B$).
- **Nhược điểm**: Kích thước vector tăng tuyến tính theo số lượng node $N$, gây tốn băng thông và bộ nhớ khi $N$ lên tới hàng nghìn node.

## Liên kết

- [[Logical Clocks]]
- [[Lamport Timestamps]]
- [[Distributed Key-Value Store]]
- [[Eventual Consistency]]
