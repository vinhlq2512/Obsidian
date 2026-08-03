---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2018 - Music Transformer - Generating Music with Long-Term Structure"
year: 2018
venue: "arXiv"
arxiv: "1809.04281v3"
source_file: "[[2018 - Music Transformer - Generating Music with Long-Term Structure - arXiv 1809.04281v3.pdf]]"
pages: 14
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

# 2018 - Music Transformer - Generating Music with Long-Term Structure - arXiv 1809.04281v3

## Nguồn

- PDF gốc: [[2018 - Music Transformer - Generating Music with Long-Term Structure - arXiv 1809.04281v3.pdf]]
- Vai trò trong CS224N: paper áp dụng Transformer cho music generation và nhấn mạnh relative attention cho cấu trúc dài hạn.

## Câu hỏi trung tâm

Transformer có thể sinh âm nhạc có cấu trúc dài hạn, lặp lại motif/phrase và xử lý timing tương đối không?

## Kiến thức cốt lõi

- Music phụ thuộc mạnh vào repetition và self-reference ở nhiều time scales.
- Relative timing quan trọng hơn absolute position trong âm nhạc.
- Paper mở rộng relative attention để capture timing và pitch relations.
- Relative attention cải thiện sample quality và perplexity trên dữ liệu âm nhạc.
- Bài này cho thấy positional representation phải phù hợp domain.

## Cơ chế / công thức / kiến trúc

```text
music events as sequence
-> self-attention
-> relative position / timing information
-> model học motif, phrase, repeated sections
```

Ý chính: attention cần biết quan hệ tương đối giữa events, không chỉ index tuyệt đối.

## Khi áp dụng

- Dùng khi đọc relative positional encoding và RoPE sau này.
- Hữu ích để thấy Transformer cần inductive bias theo modality/domain.
- Trong generation dài, coherence phụ thuộc vào khả năng truy vết cấu trúc xa.

## Kết quả / bằng chứng đáng giữ

- Abstract nói music relies heavily on repetition và self-reference.
- Source nhấn mạnh relative timing/pitch quan trọng.
- Paper nói relative attention cải thiện sample quality và perplexity.

## Cách hiểu bằng lời của tôi

Với nhạc, “token trước/sau bao xa” quan trọng như chính token. Vì vậy positional encoding không phải chi tiết phụ mà là cách model hiểu cấu trúc thời gian.

## Câu hỏi review

1. Vì sao absolute position chưa đủ cho music?
2. Relative attention giúp mô hình hoá repetition như thế nào?
3. Paper này liên hệ gì với long-context LLM?

## Liên kết

- [[Self-Attention]]
- [[Positional Embeddings]]
- [[Transformer]]
- [[CS224N]]
