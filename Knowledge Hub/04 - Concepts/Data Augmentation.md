---
type: concept
status: developing
sources:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#5. GPT-3.5 memory augmentation]]"
first_seen: 2026-08-03
last_updated: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - data
  - nlp
---

# Data Augmentation

## Định nghĩa

Data augmentation là kỹ thuật tạo thêm biến thể dữ liệu từ dữ liệu hiện có để tăng độ phủ của training set.

## Trong NLP ít nhãn

Với [[Intent Detection]] hoặc [[Text Classification]], augmentation có thể tạo thêm các cách diễn đạt khác nhau cho cùng một nhãn.

## Rủi ro

- Làm đổi label nếu biến đổi câu quá mạnh.
- Tạo dữ liệu không tự nhiên.
- Khuếch đại bias hoặc lỗi trong dữ liệu gốc.

## Cách hiểu bằng lời của tôi

Augmentation hữu ích khi nó tạo thêm cách nói hợp lý cho cùng một ý. Nếu nó làm câu đổi nghĩa, nó không còn là tăng dữ liệu mà là thêm nhiễu.

## LLM-based augmentation cho relation extraction

CPL dùng GPT-3.5-turbo để mở rộng episodic memory nhỏ:

1. Chọn một exemplar thật đại diện cho relation.
2. Đưa relation name, semantic description, context và head/tail entities vào prompt.
3. Sinh structured examples mới.
4. Replay real exemplar + generated examples bằng contrastive objective.

Demonstration rất quan trọng: chỉ relation name/description không đủ đảm bảo câu sinh có đúng relation giữa **đúng head-tail pair**. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=8|CPL PDF, tr. 8]]

## Augmentation không phải càng nhiều càng tốt

Trong CPL:

- 2 generated samples/relation tốt nhất trên FewRel.
- 5 tốt nhất trên TACRED.
- Tăng đến 10 làm performance giảm.

Ablation bỏ generation ở $T_8$:

- FewRel: giảm 0,72 điểm.
- TACRED: giảm 6,76 điểm.

Hiệu quả phụ thuộc dataset; synthetic noise và diversity kém có thể lấn át lợi ích khi sinh quá nhiều. [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=7|CPL PDF, tr. 7]] [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors.pdf#page=8|CPL PDF, tr. 8]]

## Checklist kiểm tra synthetic RE examples

- Head/tail entity có xuất hiện đúng span không?
- Direction có đúng không: `parent_of(A,B)` khác `child_of(A,B)`.
- Entity types có hợp relation không?
- Câu có thật sự entail relation hay chỉ chứa từ liên quan?
- Label có giữ nguyên sau paraphrase không?
- Lexical/syntactic diversity có thật hay chỉ thay tên riêng?
- Có duplicate train/test hoặc memorization không?
- Generator version, temperature và prompt có được lưu để tái lập không?

## Data augmentation trong continual learning

Augmentation có thể mở rộng coverage của replay buffer, nhưng không biến method thành rehearsal-free nếu prompt vẫn chứa raw exemplars. Cần tính cả:

- memory của exemplar thật;
- số synthetic examples và replay compute;
- API/token cost;
- privacy khi gửi dữ liệu sang external model;
- training time tăng theo số relation đã thấy.

## Khi dùng

- Label semantics rõ và có thể kiểm tra tự động.
- Có exemplar tốt để condition generator.
- Human/validator hoặc filtering model kiểm tra entailment/direction.
- Ablation xác nhận lợi ích theo dataset và shot count.

Không nên dùng synthetic volume như thay thế mù cho quality. Một tập nhỏ đúng nhãn thường tốt hơn nhiều câu đa dạng bề mặt nhưng sai relation.

## Câu hỏi review

1. Vì sao relation description alone chưa đủ condition generator?
2. Tại sao synthetic sample count có optimum thay vì tăng đơn điệu?
3. Augmentation replay có còn là rehearsal-based không?
4. Những lỗi nào đặc thù cho relation extraction?

## Gợi ý trả lời

1. Generator cần demonstration để hiểu context và vai trò head-tail cụ thể.
2. Noise, duplication và distribution mismatch tăng khi sinh quá nhiều.
3. Có, nếu vẫn lưu/dùng real exemplars hoặc dữ liệu lịch sử để condition.
4. Đảo direction, sai entity roles/types, câu không entail relation và label drift.

## Liên kết

- [[Few-shot Learning]]
- [[Intent Detection]]
- [[Text Classification]]
- [[Continual Few-Shot Relation Extraction]]
- [[Replay in Continual Learning]]
- [[Contrastive Learning]]
- [[Large Language Model]]
