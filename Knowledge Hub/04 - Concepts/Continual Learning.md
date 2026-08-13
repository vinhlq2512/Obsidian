---
type: concept
status: developing
sources:
  - "[[Adaptive Prompting for Continual Relation Extraction]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[Adaptive Prompting for Continual Relation Extraction#Research gap]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction#Vấn đề paper giải quyết]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Vấn đề paper giải quyết]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#Vấn đề paper giải quyết]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - continual-learning
  - machine-learning
---

# Continual Learning

## Định nghĩa

Continual learning là thiết lập model học từ một chuỗi task hoặc data distributions xuất hiện theo thời gian, trong đó model phải tiếp thu kiến thức mới nhưng vẫn giữ năng lực trên phần đã học trước đó.

Khác training IID thông thường, model không được giả định rằng toàn bộ dữ liệu quá khứ luôn sẵn sàng để trộn và train lại từ đầu.

## Cách hiểu bằng lời của tôi

Continual learning giống học một giáo trình được mở khóa từng chương, nhưng sau mỗi chương tôi vẫn bị kiểm tra trên tất cả chương cũ. Nếu chỉ tối ưu bài mới, tôi dễ sửa “bộ nhớ” theo cách làm hỏng kiến thức cũ. Nếu cố khóa mọi thứ để không quên, tôi lại không học được điều mới.

Đây là bài toán cân bằng giữa:

```text
plasticity: học cái mới đủ nhanh
stability: giữ cái cũ đủ tốt
```

## Thiết lập tối thiểu

Với chuỗi task $T_1,\ldots,T_t$, tại bước $t$ model nhận dữ liệu $D_t$ và cập nhật từ trạng thái $\theta_{t-1}$ sang $\theta_t$.

Mục tiêu không chỉ là tốt trên $D_t$:

$$
\theta_t \text{ phải tốt trên } D_1,\ldots,D_t
$$

Trong nhiều setting nghiêm ngặt, dữ liệu cũ $D_{<t}$ không còn được truy cập. Trong setting khác, một memory buffer nhỏ hoặc thống kê tóm tắt được phép giữ lại. Vì vậy, trước khi so sánh hai phương pháp phải hỏi rõ **memory budget và dữ liệu cũ được phép dùng đến đâu**.

## Các dạng shift thường gặp

- **Task-incremental:** task identity được biết khi test; model có thể dùng head/module riêng theo task.
- **Class-incremental:** class/relation mới được thêm dần; test không cho task identity và model phải chọn trên toàn bộ class đã thấy.
- **Domain-incremental:** label space giữ nguyên nhưng distribution/domain thay đổi.
- **Online/streaming:** data đến liên tục, có thể không có task boundary rõ.

Bốn paper trong research line này gần class-incremental [[Continual Relation Extraction]]: relation sets mới xuất hiện theo task, còn inference phải dự đoán trong toàn bộ relation đã thấy.

## Ba nơi kiến thức có thể bị quên

1. **Representation:** encoder/prompt biến một input cũ sang vị trí mới trong latent space.
2. **Memory/prototype:** summary của class cũ không còn đại diện đúng distribution.
3. **Classifier:** decision boundary bị kéo về class mới dù representation cũ được giữ.

Điểm này giải thích vì sao một cơ chế đơn lẻ thường không đủ. WAVE/WAVE++ cô lập prompt parameters nhưng vẫn phải replay latent representations để giữ shared classifier. ConPL giữ cả samples lẫn prototypes và buộc chúng nhất quán.

## Họ phương pháp

### Replay/rehearsal

- Lưu một số raw examples cũ rồi trộn với task mới.
- Sinh synthetic inputs hoặc latent representations thay cho raw data.
- Điểm mạnh: trực tiếp nhắc model về distribution cũ.
- Rủi ro: tốn bộ nhớ, privacy, bias do buffer nhỏ, hoặc generator bị lệch.

Xem [[Replay in Continual Learning]].

### Regularization và consistency

- Phạt thay đổi parameters/outputs/representations quan trọng với task cũ.
- Giữ consistency giữa sample, prototype hoặc distributions trước và sau update.
- Rủi ro: regularization quá mạnh làm model kém plasticity.

### Parameter isolation

- Adapter, prompt hoặc module riêng cho từng task.
- Freeze module cũ để tránh interference trực tiếp.
- Rủi ro: model/module tăng theo số task và phải biết/chọn đúng module khi test.

### Prototype và representation methods

- Tóm tắt mỗi class bằng prototype hoặc distribution.
- Phân loại bằng khoảng cách và giữ hình học latent space ổn định.
- Rủi ro: centroid đơn có thể che khuất multimodality; prototype drift gây quên.

### Prompt-based continual learning

- Giữ backbone pretrained bị freeze, chỉ học prompts nhỏ.
- Dùng [[Prompt Pool]] để route input tới prompt/expert phù hợp.
- Rủi ro: shared prompt bị ghi đè hoặc [[Task Identity Inference]] sai ở test.

## Đánh giá

Không nên chỉ báo accuracy ở task cuối cùng. Tối thiểu cần:

- **Average accuracy ở stage $t$:** hiệu năng trên toàn bộ task/class đã thấy.
- **Forgetting:** mức giảm của một task từ điểm tốt nhất trước đó đến hiện tại.
- **Forward transfer/plasticity:** model học task mới tốt đến đâu.
- **Nhiều task orders/seeds:** kết quả continual learning nhạy với thứ tự task.
- **Memory, train time, inference latency:** một phương pháp có thể đổi chi phí train lấy inference hoặc ngược lại.
- **Protocol parity:** cùng backbone, memory budget, số samples/relation và cách chia task.

Một thước đo forgetting trực giác cho task $i$ sau stage $t$:

$$
F_{i,t}=\max_{k<t} a_{i,k}-a_{i,t}
$$

trong đó $a_{i,k}$ là accuracy trên task $i$ sau khi học đến stage $k$.

## Các source bổ sung cho nhau thế nào?

### ConPL

Nhìn continual learning qua **prototype distortion và episodic memory**: cần giữ sample/prototype nhất quán trong class space, đặc biệt ở few-shot setting.

### CPL

Nhấn mạnh hai vấn đề đồng thời: [[Catastrophic Forgetting]] và overfitting khi mỗi relation có rất ít examples; dùng prompt representation, margin-based contrastive objective và LLM augmentation.

### WAVE-CRE/WAVE++

Nhìn bài toán qua **parameter isolation + task identity + classifier consolidation**. Prompt pools giữ task-specific knowledge; latent replay bảo vệ shared classifier; WAVE++ thêm cascade voting và label descriptions.

## Tổng hợp của tôi

Một continual learner tốt phải trả lời bốn câu hỏi độc lập:

1. Kiến thức cũ được lưu ở đâu: examples, prototypes, distributions hay parameters?
2. Phần nào được phép đổi khi task mới đến?
3. Model biết dùng module/knowledge nào khi inference bằng cách nào?
4. Protocol đo forgetting có công bằng về memory và task boundaries không?

Nếu một paper chỉ giải quyết một trong bốn câu hỏi, phần còn lại thường xuất hiện như failure mode trong ablation.

## Câu hỏi review

1. Continual learning khác incremental fine-tuning bình thường ở tiêu chí nào?
2. Stability-plasticity dilemma là gì?
3. Vì sao freeze task-specific prompts chưa đủ ngăn shared classifier quên?
4. Class-incremental khó hơn task-incremental ở điểm nào?
5. Vì sao phải báo memory budget và task order khi so sánh?

## Gợi ý trả lời

1. Model phải giữ hiệu năng trên toàn bộ phần đã học, không chỉ thích nghi với batch mới nhất.
2. Học nhanh làm parameters đổi và dễ quên; giữ quá chặt lại cản việc học kiến thức mới.
3. Classifier vẫn update bằng labels mới và decision boundary có thể nghiêng về task mới.
4. Test không cung cấp task identity nên model vừa phải suy task/module, vừa phân class.
5. Replay nhiều hơn và task order dễ hơn có thể tạo lợi thế không đến từ thuật toán cốt lõi.

## Liên kết

- [[Catastrophic Forgetting]]
- [[Continual Relation Extraction]]
- [[Continual Few-Shot Relation Extraction]]
- [[Replay in Continual Learning]]
- [[Prompt Pool]]
- [[Prototype Learning]]
- [[Task Identity Inference]]
- [[Fine-tuning]]
