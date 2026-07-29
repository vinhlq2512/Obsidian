---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: planned
chapter: 11
start_page: 393
end_page: 416
reading_date: 2026-08-09
planned_sessions:
  - "2026-08-09 | 393-416 | Scaling, efficient attention, multimodal và tổng kết sách | 60 phút"
estimated_minutes: 60
actual_minutes:
need_review: false
tags:
  - nlp
  - future-directions
  - multimodal
---

# NLP Transformers - Chapter 11 - Future Directions

## Mục tiêu đọc

- Hiểu các hướng phát triển sau Transformer text truyền thống.
- Nắm scaling laws, sparse attention, linearized attention.
- Biết Transformer mở rộng sang vision, tables, speech và multimodal như thế nào.

## Ý chính

- Scaling giúp model mạnh hơn nhưng đi kèm chi phí, dữ liệu và rủi ro vận hành.
- Sparse và linearized attention cố gắng giảm chi phí attention trên sequence dài.
- Transformer không chỉ dùng cho text mà còn là kiến trúc chung cho nhiều modality.

## Demo thực hành

Tạo research note so sánh các hướng phát triển thay vì train model nặng.

```markdown
| Hướng | Vấn đề giải quyết | Ví dụ ứng dụng | Câu hỏi cần đọc thêm |
| --- | --- | --- | --- |
| Scaling laws | Dự đoán hiệu quả khi tăng model/data/compute | Lập kế hoạch train model | Khi nào scaling hết hiệu quả? |
| Sparse attention | Giảm chi phí sequence dài | Long document QA | Mất thông tin toàn cục ra sao? |
| Multimodal | Kết hợp text với ảnh/âm thanh | Image captioning, VQA | Fusion nên làm ở layer nào? |
```

## Khái niệm quan trọng

- [[Scaling Laws]]
- [[Sparse Attention]]
- [[Linearized Attention]]
- [[Vision Transformer]]
- [[Multimodal Transformer]]

## Active Recall

1. Scaling laws giúp ra quyết định gì?
2. Sparse attention đánh đổi điều gì để giảm chi phí?
3. Vì sao Transformer dùng được ngoài text?
4. Hướng nào liên quan nhất tới mục tiêu học của tôi?

## Checklist

- [ ] Đọc xong chapter
- [ ] Tạo research note ngắn
- [ ] Chọn 3 concept muốn đọc sâu hơn
- [ ] Tổng kết toàn bộ sách
- [ ] Cập nhật trạng thái sách
