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

# Lamport Timestamps

## Định nghĩa

Lamport Timestamps là thuật toán đồng hồ logic đơn giản do Leslie Lamport đề xuất năm 1978. Thuật toán gán một số nguyên đơn điệu $C(e)$ cho mỗi sự kiện $e$ nhằm tạo ra thứ tự bán phần (partial ordering) hoặc thứ tự toàn phần (total ordering) duy nhất giữa các sự kiện trong hệ thống phân tán.

## Quy tắc hoạt động

Mỗi tiến trình $P_i$ duy trì một bộ đếm số nguyên $C_i$, ban đầu bằng 0:

1. **Sự kiện nội bộ (Internal Event)**: Trước khi thực hiện sự kiện nội bộ, $P_i$ tăng bộ đếm: $C_i = C_i + 1$.
2. **Gửi tin nhắn (Send Message)**: $P_i$ tăng $C_i = C_i + 1$ và gắn giá trị $C_i$ vào tin nhắn $m$.
3. **Nhận tin nhắn (Receive Message)**: Khi $P_j$ nhận tin nhắn $m$ chứa timestamp $t_m$, $P_j$ cập nhật bộ đếm: $C_j = \max(C_j, t_m) + 1$.

```text
Process A:  (C=1) -> Send (C=2) -----------\
                                            \
Process B:               Receive (C=max(0,2)+1=3) -> Local (C=4)
```

## Tính chất

- **Causal Order**: Nếu $a \rightarrow b$, thì $C(a) < C(b)$.
- **Không có chiều ngược lại**: Nếu $C(a) < C(b)$, ta **không thể** kết luận $a \rightarrow b$ (vì $a$ và $b$ có thể là hai sự kiện độc lập/concurrent). Để khắc phục điểm này, hệ thống cần dùng [[Vector Clocks]].

## Liên kết

- [[Logical Clocks]]
- [[Vector Clocks]]
- [[Distributed Systems]]
