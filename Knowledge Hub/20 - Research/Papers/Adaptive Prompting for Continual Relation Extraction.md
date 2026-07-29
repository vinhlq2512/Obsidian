---
type: paper
status: unread
title: "Adaptive Prompting for Continual Relation Extraction: A Within-Task Variance Perspective"
authors:
  - Minh Le
  - Tien Ngoc Luu
  - An Nguyen The
  - Thanh-Thien Le
  - Trang Nguyen
  - Tung Thanh Nguyen
  - Linh Ngo Van
  - Thien Huu Nguyen
year: 2025
venue: "Proceedings of the AAAI Conference on Artificial Intelligence, 39(23), 24384-24392"
url: "https://ojs.aaai.org/index.php/AAAI/article/view/34616"
pdf:
zotero_key:
citekey:
doi: "10.1609/aaai.v39i23.34616"
arxiv: "2412.08285"
topic:
  - continual relation extraction
  - prompt learning
  - continual learning
priority: medium
reading_status: not-started
rating:
related_concepts:
  - "[[Prompt Engineering]]"
  - "[[Fine-tuning]]"
  - "[[Large Language Model]]"
tags:
  - paper
---

# Adaptive Prompting for Continual Relation Extraction

## Tóm tắt một câu

- Paper đề xuất một phương pháp adaptive prompting cho Continual Relation Extraction nhằm giảm catastrophic forgetting mà không cần lưu replay buffer rõ ràng.

## Nguồn

- PDF gốc:
- URL: [AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/34616)
- DOI: `10.1609/aaai.v39i23.34616`
- arXiv: `2412.08285`
- Zotero key:
- Citekey:

## Vấn đề paper giải quyết

- Continual Relation Extraction cần học các task quan hệ mới mà không quên kiến thức cũ.
- Các phương pháp rehearsal thường dùng memory buffer, nhưng cách này có thể tốn bộ nhớ, vướng dữ liệu riêng tư, hoặc không phù hợp với setting rehearsal-free.
- Các phương pháp prompt-based hiện có còn gặp vấn đề chọn prompt chưa chính xác, chưa xử lý tốt forgetting trong shared parameters, và chưa nắm bắt đủ variance giữa task lẫn trong từng task.

## Đóng góp chính

- Đề xuất dùng prompt pool cho mỗi task để mô hình hóa variance bên trong task.
- Khai thác liên hệ giữa prefix tuning và mixture of experts để cải thiện adaptive prompting.
- Dùng generative model để củng cố kiến thức cũ trong shared parameters mà không cần lưu dữ liệu cũ trực tiếp.

## Phương pháp

- Cần đọc kỹ phần method để xác định:
  - Prompt pool được tổ chức theo task như thế nào.
  - Cơ chế chọn hoặc phối hợp prompt hoạt động ra sao.
  - Generative consolidation được huấn luyện và dùng ở bước nào.

## Kết quả quan trọng

- Theo abstract, phương pháp đạt kết quả tốt hơn các baseline prompt-based và rehearsal-free trong Continual Relation Extraction.
- Cần kiểm tra bảng kết quả chính, dataset sử dụng và metric đánh giá.

## Hạn chế

- Chưa đọc chi tiết experimental setup.
- Cần kiểm tra chi phí huấn luyện, số lượng prompt/expert, và độ nhạy với task order.

## Tôi hiểu được gì

- Paper này nằm ở giao điểm giữa [[Prompt Engineering]], [[Fine-tuning]], continual learning và relation extraction.
- Điểm đáng chú ý là paper không chỉ thêm prompt, mà cố gắng mô hình hóa variance trong từng task.

## Liên quan đến

- [[Prompt Engineering]]
- [[Fine-tuning]]
- [[Large Language Model]]
- [[Zotero Integration Workflow]]

## Cần đọc tiếp

- [ ] Introduction để hiểu gap của các prompt-based CRE methods.
- [ ] Method để nắm prompt pool và generative consolidation.
- [ ] Experiment để xem baseline, dataset và ablation.
- [ ] Related work để tách concept về Continual Relation Extraction nếu cần dùng lại.

## Trích dẫn đáng giữ

> 
