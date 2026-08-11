---
type: concept
status: seed
sources:
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-11
last_updated: 2026-08-11
tags:
  - concept
  - machine-learning
  - classification
---

# Ensemble Learning

## Định nghĩa

Ensemble learning là cách kết hợp nhiều model để tạo dự đoán cuối cùng thay vì dựa vào một model đơn lẻ.

## Cách hiểu bằng lời của tôi

Mỗi classifier có kiểu sai riêng. Ensemble cố gắng gom nhiều góc nhìn lại để lỗi của một model không quyết định toàn bộ hệ thống.

## Khi dùng cho text classification

```text
Text
-> classifier A
-> classifier B
-> classifier C
-> combine predictions
-> final class
```

- Practical NLP gọi hướng này là "use the wisdom of many" trong phần practical advice.
- Một cách combine đơn giản là majority voting: class được nhiều classifiers chọn nhất trở thành prediction cuối.
- Ensembling hữu ích vì không có thuật toán text classification nào luôn tốt nhất trên mọi dataset.

## Rủi ro

- Ensemble phức tạp hơn để deploy, monitor và debug so với một model đơn giản.
- Nếu các model sai giống nhau vì cùng bias dữ liệu, ensemble không tự sửa được lỗi nền.
- Cần so sánh với strong baseline để biết phần phức tạp thêm có đáng không.

## Liên kết

- [[Text Classification]]
- [[Model Benchmarking]]
- [[Class Imbalance]]
- [[Ticket Routing]]
