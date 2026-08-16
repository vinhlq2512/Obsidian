---
type: concept
status: understood
sources:
  - "[[2026-04-18_ep211-how-the-jvm-works]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - java
  - runtime
---

# JVM Architecture

## Định nghĩa

JVM (Java Virtual Machine) là môi trường thực thi ảo hóa chuyển đổi Java Bytecode (`.class`) thành mã máy bản địa (native machine code) tương thích với hệ điều hành và phần cứng bên dưới.

## Cách hiểu bằng lời của tôi

JVM là "trái tim" của khẩu hiệu "Write Once, Run Anywhere". Thay vì biên dịch trực tiếp sang x86 hay ARM assembly, Java compiler dịch source code thành Bytecode. JVM trên từng platform sẽ nạp, xác thực, thông dịch và biên dịch JIT Bytecode đó thành mã máy tối ưu.

## Cấu trúc thành phần

```text
Java Source (.java) -> javac -> Bytecode (.class)
-> ClassLoader Subsystem (Loading, Linking, Initialization)
-> Runtime Data Areas (Heap, Stack, Method Area/Metaspace, PC Registers)
-> Execution Engine (Interpreter + JIT Compiler + Garbage Collector)
```

- **ClassLoader**: Nạp các file `.class` vào bộ nhớ khi cần.
- **Heap Memory**: Nơi chứa toàn bộ Object được khởi tạo. Phân chia thành Young Generation (Eden, Survivor spaces) và Old Generation.
- **Metaspace**: Lưu trữ metadata của Class (thay thế PermGen từ Java 8 trở đi), tự động mở rộng theo bộ nhớ OS.
- **JIT Compiler (Just-In-Time)**: Phát hiện "hot code" (đoạn mã chạy thường xuyên) và biên dịch trực tiếp sang native machine code để tăng hiệu năng cận kề C/C++.
- **Garbage Collector (GC)**: Tự động thu hồi bộ nhớ của các object không còn được tham chiếu (ví dụ: G1, ZGC, Shenandoah).

## Trade-off

- **Warm-up Time**: JVM cần thời gian khởi động và warm-up JIT compiler trước khi đạt đỉnh hiệu năng.
- **Memory Overhead**: Bộ nhớ dành cho JVM Runtime và GC metadata lớn hơn so với binary tĩnh (Go, Rust, C++).
- **GC Pauses**: Dù các GC hiện đại như ZGC giảm pause time xuống dưới 1ms, Stop-The-World pauses vẫn là yếu tố cần tính toán trong hệ thống realtime.

## Liên kết

- [[Java Virtual Threads]]
- [[Generational Garbage Collection]]
- [[Netflix Java Runtime Architecture]]
- [[Virtualization]]
