---
type: concept
status: developing
sources:
  - "[[Adaptive Prompting for Continual Relation Extraction]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[Adaptive Prompting for Continual Relation Extraction#5. Generative replay trong latent space]]"
  - "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction#5. Generative replay trong latent space]]"
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Module 2 — Memory-enhanced learning]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#5. GPT-3.5 memory augmentation]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - continual-learning
  - replay
  - memory
---

# Replay in Continual Learning

## Định nghĩa

Replay trong continual learning là đưa tín hiệu đại diện cho dữ liệu/task cũ trở lại quá trình học task mới, để gradient hiện tại không chỉ tối ưu cho distribution mới.

Tín hiệu replay có thể là raw examples, exemplars đã chọn, prototypes, generated text hoặc synthetic latent representations.

## Cách hiểu bằng lời của tôi

Khi học task mới, model cần một “lời nhắc” đủ đại diện cho cái cũ. Replay khác nhau chủ yếu ở việc lời nhắc được lưu dưới dạng nào và còn bao nhiêu thông tin:

```text
raw samples -> nhiều chi tiết, privacy/storage cao
selected exemplars -> ít hơn nhưng coverage phụ thuộc cách chọn
prototypes -> rất gọn, mất multimodality
generated samples -> linh hoạt, phụ thuộc generator
latent distributions -> không giữ text, phụ thuộc representation/modeling assumption
```

## Các dạng replay trong bốn paper

### Episodic memory

ConPL lưu vital samples cùng refined prototypes. Hai loại thông tin bổ sung nhau:

- sample giữ instances cụ thể;
- prototype giữ summary ở class level.

Consistency losses giúp cả hai không bị representation drift làm mất giá trị.

### Memory augmentation

CPL dùng ChatGPT tạo các câu đa dạng từ memory samples. Mục tiêu là mở rộng support của buffer nhỏ để model không overfit vài exemplars.

Điểm cần nhớ: đây vẫn là replay dựa trên raw memory samples; việc gửi sample vào external generator còn tạo privacy/reproducibility questions.

### Latent generative replay

WAVE-CRE/WAVE++ mô hình hóa representation của mỗi relation bằng Gaussian:

$$
z_r\sim\mathcal N(\mu_r,\Sigma)
$$

Synthetic $z_r$ được dùng train lại shared classifier trên old relations. Raw sentences không được lưu, nhưng mean/covariance và prompt/model parameters vẫn là memory.

## Replay bảo vệ phần nào?

| Replay signal | Phần được bảo vệ trực tiếp | Không tự bảo vệ được |
|---|---|---|
| Raw/generated input | Encoder + classifier nếu train end-to-end | Quality phụ thuộc buffer/generator |
| Prototype | Class geometry/classifier | Within-class modes bị nén |
| Latent samples | Classifier/decision boundary | Encoder/prompt drift trước latent layer |
| Output/logit replay | Behavior cũ | Internal representation có thể đổi |

WAVE++ freeze backbone/prompt pools cũ rồi dùng latent replay cho classifier: hai cơ chế bảo vệ hai tầng khác nhau.

## Memory và privacy không phải nhị phân

Không nên chỉ gắn nhãn `rehearsal-free` rồi bỏ qua memory assumptions. Cần ghi rõ:

- có lưu raw text/entity pairs không;
- lưu bao nhiêu vectors/prototypes/statistics mỗi relation/task;
- memory tăng tuyến tính hay bậc cao theo số task;
- representations có thể bị inversion/membership inference không;
- external LLM có nhận raw examples không;
- generator có được train bằng dữ liệu cũ không.

Không lưu raw data **giảm** một số rủi ro nhưng không tự tạo formal privacy guarantee.

## Trade-off

### Buffer nhỏ

- Rẻ, đơn giản.
- Dễ sampling bias và overfit exemplars.

### Prototype

- Rất gọn và giải thích được.
- Một centroid không mô hình hóa multimodal class tốt.

### Text generation

- Tăng lexical/context diversity.
- Có thể hallucinate hoặc đổi relation label/direction.

### Gaussian latent replay

- Không cần decode text và train classifier nhanh.
- Phụ thuộc Gaussian assumption; covariance storage/inversion có thể đắt; synthetic latent không sửa lỗi encoder.

## Thiết kế generator/replay cần kiểm tra

1. **Fidelity:** sample sinh có đúng class không?
2. **Diversity:** có phủ mode mới hay chỉ paraphrase bề mặt?
3. **Balance:** số replay samples giữa old/new classes có công bằng không?
4. **Calibration:** synthetic distribution có scale/covariance giống real representation không?
5. **Privacy:** summary/generator có rò rỉ sample gốc không?
6. **Scaling:** memory và sampling cost tăng thế nào theo số class/task?

## Evidence quan trọng từ WAVE++

Bỏ generative replay làm stage-$T_{10}$ accuracy giảm:

- FewRel: 87,7 → 62,1.
- TACRED: 82,5 → 60,3.

Điều này cho thấy shared classifier là nguồn forgetting lớn trong setup, nhưng không chứng minh Gaussian replay luôn tốt nhất: ablation chỉ so “có/không” trong cùng framework. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=20|PDF, tr. 20]]

## Câu hỏi review

1. Replay khác parameter isolation thế nào?
2. Vì sao latent replay không thể tự sửa encoder drift?
3. Prototype và exemplar mang hai loại thông tin gì?
4. “Rehearsal-free” có đồng nghĩa zero-memory không?
5. LLM memory augmentation có failure modes nào?

## Gợi ý trả lời

1. Replay đưa tín hiệu task cũ vào objective; isolation ngăn task mới sửa parameters cũ.
2. Nó sample sau encoder và chỉ train downstream classifier; mapping input→latent cũ không được tái kiểm tra.
3. Exemplar giữ chi tiết instance; prototype tóm tắt center/class-level structure.
4. Không; method vẫn có thể lưu prompts, prototypes hoặc distribution statistics.
5. Sai label/direction, diversity giả, hallucination, privacy và khó tái lập theo model version.

## Liên kết

- [[Continual Learning]]
- [[Catastrophic Forgetting]]
- [[Continual Relation Extraction]]
- [[Prototype Learning]]
- [[Data Augmentation]]
- [[Generative Model]]
- [[Knowledge Distillation]]
