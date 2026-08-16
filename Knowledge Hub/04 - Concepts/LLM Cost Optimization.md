---
type: concept
status: understood
sources:
  - "[[2026-06-08_token-spend-out-of-control-the-case-for-smarter-routing]]"
  - "[[2026-08-04_why-an-llms-memory-gets-expensive-and-how-to-fix-it]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - cost-optimization
  - inference
---

# LLM Cost Optimization

## Định nghĩa

LLM Cost Optimization (Tối ưu hóa chi phí LLM) là tổng hợp các phương pháp kiến trúc, điều phối truy vấn (routing), caching và quản lý bộ nhớ nhằm tối thiểu hóa chi phí hạ tầng (GPU hosting hoặc API token spend) khi vận hành các ứng dụng AI ở quy mô sản xuất.

## Chiến lược tối ưu hóa

```text
User Request
-> Semantic Cache Hit? -> Return Cached Answer (Zero LLM Cost)
-> Smart Model Router (Analyze Intent & Complexity)
   |- Simple Query -> Small / Open-Weight Model (SLM)
   |- Complex Query -> Frontier LLM (GPT-4o/Claude 3.5 Sonnet)
-> Apply [[Context Compression]] -> Send Compact Prompt
```

1. **Semantic Caching**: Lưu trữ các câu trả lời cho các câu hỏi có độ tương đồng ngữ nghĩa (embedding similarity) cao. Khi có câu hỏi tương tự, hệ thống trả kết quả ngay từ cache mà không gọi LLM.
2. **Model Routing**: Phân loại độ phức tạp của câu hỏi ở gateway. Đưa các task đơn giản (như phân loại, trích xuất thông tin) cho mô hình nhỏ (SLM) và chỉ gọi mô hình Frontier đắt tiền cho các task suy luận khó.
3. **[[Context Compression]]**: Loại bỏ token thừa và tóm tắt prompt trước khi gửi API.
4. **Offloading & Model Distillation**: Chuyển các task lặp đi lặp lại sang mô hình nhỏ được fine-tune/distill riêng cho công ty.

## Trade-off

- Cần cân bằng giữa tiết kiệm chi phí và chất lượng câu trả lời (Response Accuracy).
- Tăng độ phức tạp của hệ thống điều hướng (Router latency và Semantic Cache lookup overhead).

## Liên kết

- [[Model Router]]
- [[Context Compression]]
- [[Model Distillation]]
- [[Production LLM System Design]]
