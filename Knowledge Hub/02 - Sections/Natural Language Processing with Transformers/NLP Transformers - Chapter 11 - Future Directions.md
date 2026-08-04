---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
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

## Scaling và multimodal

[[Scaling Laws]] cho một khung suy nghĩ thực dụng: model mạnh hơn thường đi cùng data và compute lớn hơn, nhưng chi phí vận hành cũng leo thang. Chapter này không chỉ nhìn vào “model lớn hơn” mà còn nhìn vào “kiến trúc thông minh hơn” và “mở rộng sang modality khác”.

[[Vision Transformer]] cho thấy nếu ảnh được chia thành patch embeddings, Transformer vẫn hoạt động tốt trên dữ liệu không phải text. Từ đó, [[Multimodal Transformer]] trở thành bước tiếp theo tự nhiên: attention được dùng để trộn tín hiệu từ text, ảnh, bảng hoặc âm thanh.

## Sparse Attention

[[Sparse Attention]] là hướng giảm chi phí attention bằng cách không cho mọi token nhìn toàn bộ sequence như [[Self-Attention]] chuẩn.

Ý tưởng trực giác:

```text
Full attention
-> mọi token tương tác với mọi token
-> mạnh nhưng quadratic theo sequence length

Sparse attention
-> chỉ giữ một tập kết nối attention quan trọng
-> rẻ hơn, đặc biệt với context dài
```

Các pattern điển hình:

- local/sliding-window: chú ý chủ yếu vùng lân cận;
- thêm một số global tokens để giữ tín hiệu toàn cục;
- block hoặc strided patterns để mở rộng coverage mà không quay lại full attention.

Trade-off quan trọng:

- giảm memory và compute;
- nhưng có thể bỏ lỡ tương tác xa nếu pattern quá cứng hoặc không hợp bài toán.

Điểm cần nhớ: sparse attention không phủ nhận attention chuẩn, mà là một cách **thiết kế attention pattern thông minh hơn** để xử lý sequence dài.

## Linearized Attention

[[Linearized Attention]] là hướng khác để giảm chi phí attention. Thay vì bỏ bớt kết nối như [[Sparse Attention]], hướng này cố **đổi cách tính attention** để không cần materialize toàn bộ attention matrix.

Ý tưởng trực giác:

```text
Full attention
-> tính mọi cặp token-token
-> tạo ma trận attention lớn

Linearized attention
-> sắp xếp lại phép tính hoặc dùng biến đổi phù hợp
-> giảm bottleneck do attention matrix
```

Điểm cần phân biệt:

- sparse attention: giảm chi phí bằng pattern thưa;
- linearized attention: giảm chi phí bằng phép tính thay thế/approximate hiệu quả hơn.

Trade-off:

- hứa hẹn tốt hơn cho sequence dài;
- nhưng có thể phải đánh đổi một phần fidelity của attention chuẩn tùy cách xấp xỉ.

Nói ngắn gọn: nếu sparse attention là “chọn lọc token nào được nhìn”, thì linearized attention là “viết lại bài toán attention cho rẻ hơn”.

## Demo thực hành

Tạo research note so sánh các hướng phát triển thay vì train model nặng.

```markdown
| Hướng | Vấn đề giải quyết | Ví dụ ứng dụng | Câu hỏi cần đọc thêm |
| --- | --- | --- | --- |
| Scaling laws | Dự đoán hiệu quả khi tăng model/data/compute | Lập kế hoạch train model | Khi nào scaling hết hiệu quả? |
| Sparse attention | Giảm chi phí sequence dài | Long document QA | Mất thông tin toàn cục ra sao? |
| Linearized attention | Giảm bottleneck attention matrix | Long-context modeling | Xấp xỉ này làm mất gì so với attention chuẩn? |
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
3. Linearized attention khác sparse attention ở điểm nào?
4. Vì sao Transformer dùng được ngoài text?
5. Hướng nào liên quan nhất tới mục tiêu học của tôi?

## Checklist

- [x] Đọc xong chapter
- [ ] Tạo research note ngắn
- [x] Chọn 3 concept muốn đọc sâu hơn
- [x] Tổng kết toàn bộ sách
- [x] Cập nhật trạng thái sách
