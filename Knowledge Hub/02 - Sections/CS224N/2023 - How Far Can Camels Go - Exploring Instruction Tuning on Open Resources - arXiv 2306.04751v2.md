---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2023 - How Far Can Camels Go - Exploring Instruction Tuning on Open Resources"
year: 2023
venue: "arXiv"
arxiv: "2306.04751v2"
source_file: "[[2023 - How Far Can Camels Go - Exploring Instruction Tuning on Open Resources - arXiv 2306.04751v2.pdf]]"
pages: 23
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Fine-tuning]]"
  - "[[RLHF]]"
tags:
  - cs224n
  - paper
---

# 2023 - How Far Can Camels Go - Exploring Instruction Tuning on Open Resources - arXiv 2306.04751v2

## Nguồn

- PDF gốc: [[2023 - How Far Can Camels Go - Exploring Instruction Tuning on Open Resources - arXiv 2306.04751v2.pdf]]
- Vai trò trong CS224N: paper về instruction tuning bằng open resources và giới hạn của dữ liệu mở.

## Câu hỏi trung tâm

Open resources có thể đưa instruction-tuned models đi xa đến đâu so với hệ thống đóng và data proprietary?

## Kiến thức cốt lõi

- Instruction tuning chất lượng phụ thuộc mạnh vào nguồn dữ liệu và filtering.
- Open datasets giúp democratize LLM development nhưng có giới hạn về coverage/quality.
- Tên Camels gợi cụm model/data open instruction tuning.
- Paper thuộc trục post-training và open-source alignment.
- Cần phân biệt cải thiện do base model, data mixture, training recipe hay evaluation setup.

## Cơ chế / công thức / kiến trúc

```text
base LM
-> open instruction datasets
-> supervised fine-tuning / alignment recipe
-> evaluate instruction following
-> phân tích giới hạn open resources
```

## Khi áp dụng

- Dùng khi xây model nội bộ/open-source bằng dữ liệu công khai.
- Cần audit data quality, duplication và benchmark leakage.
- Không chỉ thêm nhiều instruction; cần chọn instruction hữu ích.

## Kết quả / bằng chứng đáng giữ

- Title nói exploring instruction tuning on open resources.
- Lecture 08/09 đặt instruction data và human preference data ở trung tâm post-training.
- Paper bổ sung góc nhìn open-source vào post-training.

## Cách hiểu bằng lời của tôi

Open instruction tuning là bài toán chất lượng dữ liệu nhiều hơn số lượng dữ liệu. Data mở giúp bắt đầu, nhưng không tự đảm bảo assistant tốt.

## Câu hỏi review

1. Open resources có lợi thế và giới hạn gì?
2. Vì sao cần audit instruction data?
3. Khi so sánh model, cần tách ảnh hưởng của base model và data như thế nào?

## Liên kết

- [[Instruction Fine-Tuning]]
- [[Fine-tuning]]
- [[Large Language Model]]
- [[CS224N]]
