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
  - consensus
---

# Logical Clocks

## Định nghĩa

Logical Clocks (Đồng hồ logic) là cơ chế gán số thứ tự đơn điệu (monotonic counter) cho các sự kiện trong hệ thống phân tán để theo dõi mối quan hệ nguyên nhân - kết quả (causality / happened-before relationship) giữa chúng mà không dựa vào đồng hồ vật lý của máy tính.

## Cách hiểu bằng lời của tôi

Đồng hồ vách tường (physical wall-clock) trên các server phân tán luôn bị lệch (clock drift) do sai số phần cứng và NTP sync. Do đó, ta không thể dùng timestamp vật lý để biết sự kiện $A$ diễn ra trước hay sau sự kiện $B$. Logical Clock thay thế thời gian thực bằng việc đếm trình tự sự kiện: nếu $A$ dẫn đến $B$, thì $L(A) < L(B)$.

## Quan hệ Happened-Before ($\rightarrow$)

Leslie Lamport định nghĩa quan hệ $\rightarrow$:
1. Nếu $a$ và $b$ thuộc cùng một tiến trình và $a$ xảy ra trước $b$, thì $a \rightarrow b$.
2. Nếu $a$ là hành động gửi tin nhắn và $b$ là hành động nhận tin nhắn đó, thì $a \rightarrow b$.
3. Nếu $a \rightarrow b$ và $b \rightarrow c$, thì $a \rightarrow c$ (tính bắc cầu).
4. Nếu hai sự kiện $a$ và $b$ không có quan hệ bắc cầu với nhau, chúng được coi là song song (concurrent: $a \parallel b$).

## Biến thể phổ biến

- **[[Lamport Timestamps]]**: Cung cấp thứ tự bán phần (partial ordering) đơn giản với chi phí cực thấp (chỉ 1 số integer).
- **[[Vector Clocks]]**: Lưu mảng integer tương ứng với từng node, cho phép phát hiện chính xác các sự kiện xung đột (concurrent updates).
- **[[TrueTime]]**: Tiếp cận hybrid bằng cách kết hợp phần cứng đồng hồ nguyên tử/GPS để giới hạn độ bất định thời gian thực.

## Trade-off

- **Ưu điểm**: Đảm bảo nguyên lý causality tuyệt đối mà không cần đồng bộ đồng hồ vật lý phức tạp.
- **Nhược điểm**: Không cung cấp thông tin về thời gian thực (ví dụ: sự kiện xảy ra cách đây bao nhiêu phút/giờ).

## Liên kết

- [[Lamport Timestamps]]
- [[Vector Clocks]]
- [[TrueTime]]
- [[Distributed Systems]]
- [[Eventual Consistency]]
