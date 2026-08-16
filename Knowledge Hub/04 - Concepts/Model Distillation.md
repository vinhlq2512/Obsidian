---
type: concept
status: understood
sources:
  - "[[2026-08-05_how-big-models-teach-small-models-to-be-smart]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - model-compression
  - distillation
---

# Model Distillation

## Định nghĩa

Model Distillation (Chưng cất mô hình) là kỹ thuật nén tri thức trong đó một mô hình nhỏ (Student Model) được huấn luyện để bắt chước hành vi, phân phối xác xuất đầu ra (logits) hoặc chuỗi suy luận của một mô hình lớn, mạnh mẽ hơn (Teacher Model).

## Cách hiểu bằng lời của tôi

Giống như việc một sư phụ giỏi (Teacher LLM 400B) truyền dạy bí kíp cho học trò (Student SLM 7B). Thay vì để đệ tử tự học từ đống dữ liệu thô khổng lồ, ta dùng kết quả đầu ra và xác suất dự đoán của mô hình Teacher làm "đáp án mẫu" để Student học nhanh hơn và thông minh vượt trội so với kích thước của nó.

## Kỹ thuật chính

1. **Logit Matching (Soft Targets)**: Student học trực tiếp phân phối xác suất mềm (soft probabilities) ở lớp output của Teacher với hệ số nhiệt độ $T$ (Temperature):
   $$\mathcal{L}_{\text{distill}} = \text{KL}\left(\text{softmax}(z_T / T) \,\|\, \text{softmax}(z_S / T)\right)$$
2. **Sequence-Level Distillation**: Teacher tạo ra hàng triệu mẫu synthetic response chất lượng cao (ví dụ: Chain-of-Thought reasoning), và Student được fine-tune trên dữ liệu này.
3. **On-Policy Distillation**: Student tạo câu trả lời, Teacher chấm điểm và cung cấp feedback/correction trực tiếp cho Student điều chỉnh.

## Ứng dụng & Trade-off

- **Ưu điểm**:
  - Giảm đáng kể chi phí inference và bộ nhớ GPU (VRAM).
  - Giảm latency, cho phép chạy mô hình trên thiết bị edge hoặc thiết bị di động.
  - Giữ lại 85-95% năng lực của Teacher trên các domain cụ thể.
- **Nhược điểm**:
  - Student khó duy trì năng lực tổng quát (general reasoning) như Teacher.
  - Rủi ro kế thừa cả thiên vị (bias) và lỗi sai từ mô hình Teacher.

## Liên kết

- [[LLM Cost Optimization]]
- [[Reasoning Model]]
- [[LLM Inference Engineering]]
- [[LLM Architecture Comparison]]
