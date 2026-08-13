---
type: concept
status: seed
sources:
  - "[[Adaptive Prompting for Continual Relation Extraction]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
source_sections:
  - "[[Adaptive Prompting for Continual Relation Extraction#2. Task-specific prompt pool]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction#2. Task-specific prompt pool]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - prompting
  - continual-learning
  - routing
---

# Prompt Pool

## Định nghĩa

Prompt pool là một tập learned prompts kèm keys, cho phép hệ thống chọn động một hoặc nhiều prompts phù hợp với từng input thay vì dùng một prompt cố định cho toàn bộ task/dataset.

Một pool có dạng:

$$
\mathcal P=\{(k_1,P_1),\ldots,(k_M,P_M)\}
$$

trong đó $k_i$ là prompt key và $P_i$ là prompt parameters.

## Cách hiểu bằng lời của tôi

Một prompt cố định giống dùng cùng một chuyên gia cho mọi ví dụ. Prompt pool giống danh sách chuyên gia nhỏ: query của input quyết định gọi ai.

```text
input x -> query q(x)
q(x) so với prompt keys
-> chọn top-K prompts
-> chèn prompts vào model
```

## Routing

Với similarity/distance $\gamma$ giữa query và keys, chọn tập $K_x$:

$$
K_x=TopK\{\gamma(q(x),k_i)\}_{i=1}^{M}
$$

Phải ghi rõ convention:

- cosine **similarity**: chọn giá trị lớn nhất;
- cosine **distance** hoặc negative similarity: chọn giá trị nhỏ nhất.

WAVE-CRE ghi `argmin` nhưng gọi $\gamma$ là cosine similarity, tạo ambiguity ký hiệu. Khi implement cần kiểm tra code thay vì sao chép công thức máy móc.

## Shared pool và task-specific pools

### Shared pool

Một pool dùng cho mọi task.

- Ưu: parameter growth thấp hơn, có thể chia sẻ knowledge.
- Nhược: task mới update prompts từng phục vụ task cũ; input từ task khác nhau có thể route vào cùng experts và giảm cross-task separation.

### Task-specific pools

Mỗi task $t$ có $\mathcal P^t$ riêng.

- Ưu: cô lập task-specific knowledge, giảm interference.
- Nhược: parameters/memory tăng theo task; inference phải chọn đúng pool.

WAVE/WAVE++ dùng task-specific pool để tăng cross-task variance, rồi dùng nhiều prompts trong mỗi pool để mô hình hóa within-task variance.

## Within-task variance

Một task/relation group không đồng nhất: contexts, entity types và linguistic patterns có nhiều mode. Một prompt cố định chỉ tạo cùng prefix offsets cho mọi sample.

Nhiều prompts được route theo $q(x)$ cho phép chuyên môn hóa:

```text
prompt A -> pattern/domain mode A
prompt B -> pattern/domain mode B
prompt C -> ambiguous/hard cases
```

Paper không đo variance trực tiếp; evidence là prompt-pool ablation. Trên WAVE++, pool tăng stage-$T_{10}$ accuracy 1,3 điểm ở FewRel và 1,4 điểm ở TACRED so với một prompt/task. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=18|WAVE++ PDF, tr. 18]]

## Prompt length và expert granularity

Theo lens [[Prefix Tuning]]–[[Mixture of Experts]]:

- prompt dài $L>1$: một key điều khiển nhiều prefix experts;
- prompt $L=1$: mỗi expert có key riêng;
- giữ tổng selected experts cố định, $L=1$ tăng routing granularity.

Điều này không đảm bảo luôn tốt hơn: key riêng tăng flexibility nhưng cũng tăng routing decisions và nguy cơ experts phân mảnh.

## Training objective

Ngoài task loss, prompt-pool methods thường có key/query alignment loss để các input chọn đúng prompts:

$$
\mathcal L=\mathcal L_{task}+\lambda\mathcal L_{pool}
$$

Nếu keys và prompts cùng được update, cần tránh collapse: mọi query chọn cùng prompt hoặc một số prompts không bao giờ được dùng. Có thể theo dõi utilization, load balance và entropy của routing.

## Failure modes

- **Prompt collapse:** nhiều input chọn cùng vài prompts.
- **Dead prompts:** prompts không bao giờ được route tới nên không học.
- **Cross-task overwrite:** shared prompts bị task mới sửa.
- **Task/pool mismatch:** chọn sai task pool khi test.
- **Boundary-spanning:** một expert vô tình phục vụ distributions không tương thích.
- **Unbounded growth:** mỗi task thêm pool làm memory tăng tuyến tính.
- **Query drift:** query encoder đổi làm mapping tới keys cũ mất ổn định.

## Evaluation checklist

- Accuracy với task ID oracle so với task ID predicted.
- Prompt utilization và số experts thật sự được dùng.
- Sensitivity theo $M,K,L$.
- Parameter/memory growth theo số task.
- Inference latency do thử/vote nhiều pools.
- Kết quả khi task boundaries hoặc relation sets overlap.
- Robustness khi input chọn sai pool.

## Câu hỏi review

1. Prompt pool giải quyết điểm yếu nào của một prompt cố định?
2. Shared pool và task-specific pools đổi trade-off gì?
3. Vì sao task-specific pool tạo thêm task identity problem?
4. $L=1$ có ý nghĩa gì theo MoE lens?
5. Làm sao phát hiện prompt collapse?

## Gợi ý trả lời

1. Cho phép input-dependent specialization và nắm nhiều modes.
2. Shared pool chia sẻ/rẻ hơn nhưng dễ interference; task pools cô lập tốt hơn nhưng tăng memory và cần routing.
3. Test không biết task nên phải tự chọn pool trước khi dùng prompt.
4. Mỗi prefix expert có key riêng và được chọn độc lập.
5. Đo histogram utilization, routing entropy và tỷ lệ prompts không bao giờ được chọn.

## Liên kết

- [[Prefix Tuning]]
- [[Mixture of Experts]]
- [[Continual Learning]]
- [[Continual Relation Extraction]]
- [[Task Identity Inference]]
- [[Catastrophic Forgetting]]
