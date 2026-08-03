---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2019 - The Lottery Ticket Hypothesis - Finding Sparse Trainable Neural Networks"
year: 2019
venue: "arXiv"
arxiv: "1803.03635v5"
source_file: "[[2019 - The Lottery Ticket Hypothesis - Finding Sparse Trainable Neural Networks - arXiv 1803.03635v5.pdf]]"
pages: 42
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Feed-Forward Layer]]"
  - "[[Loss Function]]"
tags:
  - cs224n
  - paper
---

# 2019 - The Lottery Ticket Hypothesis - Finding Sparse Trainable Neural Networks - arXiv 1803.03635v5

## Nguồn

- PDF gốc: [[2019 - The Lottery Ticket Hypothesis - Finding Sparse Trainable Neural Networks - arXiv 1803.03635v5.pdf]]
- Vai trò trong CS224N: paper nền cho pruning/subnetwork trong efficient adaptation.

## Câu hỏi trung tâm

Trong một mạng dense ngẫu nhiên có tồn tại subnetworks nhỏ có thể train tốt như mạng lớn không?

## Kiến thức cốt lõi

- Lottery Ticket Hypothesis cho rằng dense network chứa winning tickets: subnetworks sparse train được hiệu quả khi khởi tạo đúng.
- Pruning không chỉ là nén model sau train; nó đặt câu hỏi về phần tham số thật sự cần thiết.
- Khởi tạo ban đầu của subnetwork có vai trò quan trọng.
- Paper ảnh hưởng tới nghiên cứu sparsity, pruning và efficient training.
- Trong CS224N, nó liên hệ với lecture efficient adaptation và subnetwork methods.

## Cơ chế / công thức / kiến trúc

```text
train dense network
-> prune weights ít quan trọng
-> reset surviving weights về initialization ban đầu
-> train subnetwork
-> nếu đạt performance tốt: winning ticket
```

## Khi áp dụng

- Dùng khi nghiên cứu model compression hoặc sparse adaptation.
- Không đồng nhất pruning inference với tìm winning tickets trong training.
- Cần chú ý chi phí tìm ticket có thể lớn.

## Kết quả / bằng chứng đáng giữ

- Title nêu finding sparse trainable neural networks.
- Lecture 09 đặt pruning/subnetwork cạnh PEFT methods.
- Paper là nguồn lịch sử quan trọng cho suy nghĩ về redundancy trong neural networks.

## Cách hiểu bằng lời của tôi

Lottery ticket nói rằng trong mạng lớn có thể có mạng nhỏ “đúng chỗ” đã nằm sẵn. Vấn đề là tìm nó và giữ initialization phù hợp.

## Câu hỏi review

1. Winning ticket là gì?
2. Reset initialization có ý nghĩa gì?
3. Pruning liên hệ gì với efficient adaptation?

## Liên kết

- [[Parameter-Efficient Fine-Tuning]]
- [[Fine-tuning]]
- [[Large Language Model]]
- [[CS224N]]
