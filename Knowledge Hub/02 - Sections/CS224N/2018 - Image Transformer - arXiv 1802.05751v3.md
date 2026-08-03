---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2018 - Image Transformer"
year: 2018
venue: "arXiv"
arxiv: "1802.05751v3"
source_file: "[[2018 - Image Transformer - arXiv 1802.05751v3.pdf]]"
pages: 10
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
tags:
  - cs224n
  - paper
---

# 2018 - Image Transformer - arXiv 1802.05751v3

## Nguồn

- PDF gốc: [[2018 - Image Transformer - arXiv 1802.05751v3.pdf]]
- Vai trò trong CS224N: paper mở rộng Transformer/self-attention sang image generation autoregressive.

## Câu hỏi trung tâm

Self-attention có thể thay convolution/recurrent models trong image generation không, và làm sao xử lý cost lớn của ảnh?

## Kiến thức cốt lõi

- Image generation có thể được cast thành autoregressive sequence generation trên pixels/patches.
- Paper dùng Transformer cho image generation với likelihood tractable.
- Local self-attention hạn chế phạm vi attention để xử lý ảnh lớn hơn trong thực tế.
- Self-attention tạo receptive field lớn hơn CNN thông thường theo mỗi layer.
- Paper cho thấy Transformer không chỉ dành cho text.

## Cơ chế / công thức / kiến trúc

```text
image -> sequence of pixels / positions
-> autoregressive factorization
-> locally restricted multi-head self-attention
-> predict next pixel/token
```

Local attention là trade-off: giảm cost so với full attention nhưng vẫn giữ khả năng mô hình hoá dependency rộng hơn convolution local thuần.

## Khi áp dụng

- Dùng để hiểu lịch sử Transformer chuyển sang multimodal/vision.
- Khi sequence length rất lớn, cần sparse/local attention hoặc kiến trúc hiệu quả hơn.
- Không nên áp full attention ngây thơ cho ảnh độ phân giải lớn.

## Kết quả / bằng chứng đáng giữ

- Abstract nói self-attention được generalize sang image generation.
- Source nhấn mạnh locally restricted self-attention để tăng kích thước ảnh xử lý được.
- Paper báo cáo generative models outperform các baseline thời điểm đó.

## Cách hiểu bằng lời của tôi

Image Transformer là ví dụ đầu cho tư duy “mọi thứ có thể là sequence”, nhưng cũng phơi bày ngay vấn đề quadratic cost.

## Câu hỏi review

1. Vì sao image generation có thể xem như autoregressive sequence generation?
2. Local self-attention giải quyết cost như thế nào?
3. Paper này liên hệ gì với multimodal LLM hiện đại?

## Liên kết

- [[Transformer]]
- [[Self-Attention]]
- [[Multimodal LLM]]
- [[CS224N]]
