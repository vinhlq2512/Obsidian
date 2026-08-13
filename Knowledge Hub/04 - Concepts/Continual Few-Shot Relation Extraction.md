---
type: concept
status: developing
sources:
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Bài toán NK-CRE]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#Continual Few-Shot Relation Extraction là gì?]]"
first_seen: 2026-08-13
last_updated: 2026-08-13
created_at: 2026-08-13
updated_at: 2026-08-13
tags:
  - concept
  - continual-learning
  - few-shot
  - relation-extraction
---

# Continual Few-Shot Relation Extraction

## Định nghĩa

Continual Few-Shot Relation Extraction (CFRE) kết hợp hai ràng buộc:

1. Relation classes xuất hiện dần như [[Continual Relation Extraction]].
2. Mỗi relation mới chỉ có rất ít labeled examples như [[Few-shot Learning]].

Model vì thế phải đồng thời tránh [[Catastrophic Forgetting]] trên relation cũ và tránh overfitting trên vài examples của relation mới.

## Cách hiểu bằng lời của tôi

CRE thường đã khó vì model không được quên. CFRE còn khó hơn vì mỗi lần học cái mới, tín hiệu quá ít để xác định đúng “hình dạng” của class:

```text
ít examples mới
-> prototype/decision boundary ước lượng nhiễu
-> dễ overfit
-> update nhiễu còn làm hỏng class cũ
```

## NK-CRE là gì?

ConPL đề xuất N-way-K-shot CRE (NK-CRE): mỗi task có $N$ relation và **mỗi relation ở mọi task**, kể cả task đầu tiên, chỉ có $K$ training examples.

Đây là điểm khác quan trọng với một số protocol CFRE trước đó: task đầu có nhiều data, còn chỉ các task sau là few-shot. Nếu test set chứa nhiều relation từ task đầu, protocol đó có thể cho kết quả lạc quan hơn về “true continual few-shot”. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1|ConPL PDF, tr. 1]] [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=2|ConPL PDF, tr. 2]]

## Hai failure modes tương tác

### Overfitting relation mới

- Model học surface patterns của vài câu thay vì semantics của relation.
- Prototype bị lệch vì sample mean có variance lớn.
- Hard negatives/relations gần nghĩa bị nhập nhằng.

### Forgetting relation cũ

- Memory buffer nhỏ không phủ distribution cũ.
- Rehearsal trên vài memory samples làm model overfit chính buffer.
- Prototype cũ drift khi representation encoder đổi.

Vì hai failure modes gắn nhau, giải pháp thường kết hợp semantic anchors, contrastive loss, prototype/memory và augmentation.

## Hai hướng trong paper

### ConPL: giữ hình học prototype nhất quán

- Dự đoán bằng relation prototypes.
- Chọn vital samples và refined prototypes thành multi-information episodic memory.
- Dùng classification/distribution consistency để samples và prototypes cũ không lệch quá xa.
- Dùng focal loss để tập trung vào classes/samples khó.

### CPL: khai thác PLM và làm giàu memory

- Thiết kế prompt representation để PLM sinh feature tổng quát hơn cho old/new relations.
- Margin-based contrastive loss tập trung vào hard samples/negatives.
- Dùng ChatGPT sinh biến thể cho memory examples nhằm giảm overfitting do buffer quá nhỏ.

## Evaluation checklist

- Task đầu có thật sự $K$-shot không?
- $N$, $K$, số task và số relation tổng là bao nhiêu?
- Buffer size tính trên relation hay toàn hệ thống?
- Synthetic examples có được tính vào memory/compute budget không?
- Datasets có cân bằng không; có `no_relation` không?
- Kết quả trung bình qua bao nhiêu task orders/seeds?
- Báo average accuracy, old/new accuracy và forgetting riêng không?
- Baselines có dùng cùng backbone/prompt/augmentation không?

## Rủi ro khi dùng LLM augmentation

- Entity markers hoặc relation direction có thể bị đổi.
- Câu sinh trôi khỏi target label nhưng vẫn được gán nhãn cũ.
- LLM tạo lexical patterns lặp lại, cho diversity bề mặt chứ không phải semantic diversity.
- Chi phí và version của external LLM ảnh hưởng reproducibility.
- Synthetic examples không loại bỏ privacy concern nếu prompt chứa raw memory sample.

Xem [[Data Augmentation]].

## Tổng hợp của tôi

CFRE nên được coi như bài toán **ước lượng class geometry dưới data scarcity và distribution shift**. Prototype, prompt và augmentation là ba cách bù thông tin thiếu:

```text
prototype  -> nén class thành điểm neo
prompt     -> kéo prior knowledge từ PLM
augmentation -> mở rộng support quan sát được
```

Nhưng cả ba đều có thể tạo bias. Vì vậy cần ablation và kiểm tra error slices, không chỉ nhìn average accuracy.

## Câu hỏi review

1. Vì sao CFRE không chỉ là CRE với dataset nhỏ hơn?
2. NK-CRE sửa điểm chưa thực tế nào của protocol trước?
3. Tại sao replay buffer nhỏ vừa giúp nhớ vừa gây overfit?
4. Prototype distortion ảnh hưởng relation cũ thế nào?
5. LLM augmentation cần kiểm tra những lỗi nhãn nào?

## Gợi ý trả lời

1. Few-shot làm cả ước lượng class mới và evaluation nhiễu hơn, đồng thời khuếch đại forgetting.
2. Nó buộc task đầu cũng K-shot, tránh một base task lớn làm kết quả dễ hơn.
3. Buffer nhắc model về class cũ nhưng coverage hẹp khiến model fit vào vài samples đại diện.
4. Prototype không còn nằm gần distribution class cũ nên sample cũ bị hút sang relation khác.
5. Relation direction, entity roles/types, label semantics, factual/plausibility và diversity thực.

## Liên kết

- [[Continual Relation Extraction]]
- [[Continual Learning]]
- [[Few-shot Learning]]
- [[Catastrophic Forgetting]]
- [[Prototype Learning]]
- [[Contrastive Learning]]
- [[Data Augmentation]]
- [[Replay in Continual Learning]]
