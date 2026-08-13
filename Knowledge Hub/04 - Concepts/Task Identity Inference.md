---
type: concept
status: seed
sources:
  - "[[Adaptive Prompting for Continual Relation Extraction]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
source_sections:
  - "[[Adaptive Prompting for Continual Relation Extraction#6. Task predictor và relation classifier]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction#4. Cascade voting cho task identity]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - continual-learning
  - routing
  - task-inference
---

# Task Identity Inference

## Định nghĩa

Task Identity Inference (TII) là bước suy ra input tại inference thuộc task/distribution nào khi task label không được cung cấp. Với hệ có task-specific heads, prompts hoặc experts, TII quyết định module nào được dùng trước khi dự đoán label cuối.

## Vì sao quan trọng?

Trong class-incremental setting, xác suất dự đoán đúng có thể phân rã:

$$
P(\hat y=y\mid x)
=P(\hat y\in R_t\mid x)
\cdot P(\hat y=y\mid \hat y\in R_t,x)
$$

- TII: $P(\hat y\in R_t\mid x)$.
- Within-task prediction: $P(\hat y=y\mid \hat y\in R_t,x)$.

Chọn sai task khiến một classifier rất tốt bên trong task vẫn thất bại. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=4|WAVE++ PDF, tr. 4]]

## Cách hiểu bằng lời của tôi

Nếu knowledge được cất trong nhiều ngăn, TII là bước tìm đúng ngăn. Forgetting đôi khi không phải knowledge bị xóa; model chỉ mở nhầm ngăn.

```text
input -> suy task -> chọn prompt/expert/head -> dự đoán label
```

## Các cách suy task

### Task classifier trực tiếp

Train MLP từ unprompted feature tới task ID.

- Ưu: inference một lần, đơn giản.
- Nhược: task index là thứ tự hành chính, không nhất thiết là semantic class; classifier có thể drift/quên.

### Relation-level predictor rồi map về task

WAVE-CRE cho predictor output trên toàn bộ relations, sau đó map predicted relation về task/prompt pool. Relation labels có semantics cụ thể hơn task IDs.

Predictor được củng cố bằng Gaussian replay của query representations cũ, nhưng vẫn là trainable shared component có thể lệch.

### Distance/distribution-based inference

WAVE++ lưu Gaussian statistics của prompted representations. Mỗi pool đánh giá input bằng minimum Mahalanobis distance tới relation distributions của từng task:

$$
Score_t^i(x)=\min_{r\in R_t}
(z^i-\mu_{r,t}^i)^\top(\Sigma_t^i)^{-1}(z^i-\mu_{r,t}^i)
$$

Pool bỏ phiếu cho task có score nhỏ nhất. Cách này không train task classifier nhưng cần distribution storage và nhiều inference computations.

### Oracle task identity

Cung cấp task ID thật ở test. Đây là task-incremental evaluation và thường dễ hơn; hữu ích như diagnostic upper bound nhưng không nên lẫn với class-incremental result.

## Cascade voting của WAVE++

1. BERT không prompt ($P_0$) và pool đầu tiên ($P_1$) bỏ phiếu.
2. Nếu đồng ý, trả kết quả ngay.
3. Nếu khác, thêm một số pools hợp lệ vào vote, giới hạn bởi $m=2$.
4. Task majority vote quyết định prompt pool cuối.

Ý tưởng “cascade” tiết kiệm hơn thử mọi pool cho mọi input, nhưng vẫn tăng inference latency so với MLP predictor. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=12|WAVE++ PDF, tr. 12]] [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=14|WAVE++ PDF, tr. 14]]

## Kết quả từ WAVE++

Task prediction accuracy ở $T_{10}$:

| Dataset | WAVE-CRE MLP | WAVE++ cascade voting |
|---|---:|---:|
| FewRel | 85,4 | 88,3 |
| TACRED | 79,2 | 84,8 |

Nhưng inference latency tăng từ 28,7/29,8 ms lên 40,5/41,2 ms trên TACRED/FewRel. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=19|WAVE++ PDF, tr. 19]] [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=30|WAVE++ PDF, tr. 30]]

## Failure modes

- Task boundaries không tồn tại rõ trong data thật.
- Relation distributions overlap giữa task.
- Covariance ước lượng kém hoặc singular.
- Query/representation drift làm stored distributions stale.
- Task mới làm prediction range của pools không đồng nhất.
- Sai task gây prompt mismatch nhưng final classifier đôi khi vẫn đoán đúng relation do semantic anchors.
- Number of pools lớn làm latency/memory tăng.

## Đánh giá đúng

- TII accuracy theo từng learning stage.
- Final relation accuracy khi TII đúng và khi TII sai.
- Oracle-task accuracy để tách lỗi routing khỏi WTP.
- Confusion matrix giữa tasks.
- Latency/memory theo số task.
- Calibration/unknown detection khi input không thuộc task đã biết.
- Robustness khi task order hoặc domain thay đổi.

## Câu hỏi review

1. TII khác relation classification thế nào?
2. Vì sao task-classifier theo task index có thể thiếu semantics?
3. WAVE-CRE và WAVE++ suy task khác nhau ra sao?
4. Mahalanobis distance dùng covariance để làm gì?
5. Oracle-task evaluation cho biết điều gì?

## Gợi ý trả lời

1. TII chọn nhóm/module; relation classifier chọn label cuối.
2. Task ID chỉ phản ánh thứ tự/batch, các relations trong một task có thể không đồng nhất nghĩa.
3. WAVE-CRE train MLP relation predictor; WAVE++ dùng distribution scores và cascade voting không train predictor.
4. Chuẩn hóa khoảng cách theo direction/scale variance của latent distribution.
5. Upper bound khi routing hoàn hảo và giúp cô lập lỗi WTP.

## Liên kết

- [[Continual Learning]]
- [[Continual Relation Extraction]]
- [[Prompt Pool]]
- [[Mixture of Experts]]
- [[Catastrophic Forgetting]]
- [[Classification Head]]
- [[Confusion Matrix]]
