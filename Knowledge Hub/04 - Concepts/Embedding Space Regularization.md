---
type: concept
status: seed
sources:
  - "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
source_sections:
  - "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Module 3 — Consistent learning]]"
  - "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction#Prototype distortion và forgetting]]"
  - "[[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors#Research gap]]"
first_seen: 2026-08-18
last_updated: 2026-08-18
tags:
  - concept
  - embeddings
  - continual-learning
  - regularization
---

# Embedding Space Regularization

## Định nghĩa ngắn

Embedding space regularization là nhóm kỹ thuật thêm ràng buộc vào quá trình học để hình học của [[Embedding|embedding space]] không bị trôi quá mạnh khi model học task mới. Thay vì chỉ regularize trực tiếp trọng số model, nó regularize vị trí, khoảng cách, similarity hoặc distribution của các vector biểu diễn.

Trong [[04 - Concepts/Continual Learning|Continual Learning]], mục tiêu thường là giữ representation của class/task cũ vẫn kích hoạt đúng sau khi model cập nhật bằng dữ liệu mới.

## Diễn giải học tập

Cách hiểu gọn: nếu mỗi class là một vùng trong không gian vector, thì học task mới có thể làm cả bản đồ bị méo. Embedding space regularization cố giữ vài cấu trúc quan trọng của bản đồ này:

- sample cũ vẫn gần class anchor cũ;
- các class gần nghĩa vẫn có ranh giới đủ rõ;
- quan hệ tương đối giữa một sample và các prototype không bị đảo lộn;
- encoder mới không phá hoàn toàn embedding geometry mà task cũ đang dựa vào.

Với ConPL, paper không đặt tên method chính là embedding space regularization. Paper nhắc ERDA là baseline dùng embedding space regularization và data augmentation. Tuy vậy, một cách diễn giải có thể là các loss consistency của ConPL cũng thuộc họ tư duy này, vì chúng trực tiếp ràng buộc quan hệ giữa sample embeddings và prototype embeddings. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=6|ConPL PDF, tr. 6]]

## Cơ chế

### Ràng buộc điểm với prototype

ConPL dùng classification consistency để kéo embedding của memory sample về prototype đúng:

$$
L_{cc}=\sum_{(x_i,y_i)\in\hat S^{k-1}}\|f_\theta(x_i)-p_i\|
$$

Ràng buộc này bảo vệ quan hệ **sample - own prototype**. Nếu encoder học task mới làm sample cũ trôi xa prototype cũ, loss này tạo lực kéo ngược lại. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4|ConPL PDF, tr. 4]]

### Ràng buộc distribution trong prototype space

ConPL dùng distribution consistency:

$$
L_{dc}=\sum_{(x_i,y_i)\in\hat S^k}
\left\|
d(f_\theta(x_i),\hat P^k)-d(p_i,\hat P^k)
\right\|
$$

Ở đây model không chỉ giữ sample gần prototype đúng, mà còn giữ vector similarity của sample tới toàn bộ prototype memory gần với vector similarity của prototype đúng tới toàn bộ prototype memory. Nói cách khác, nó bảo vệ **hình học tương đối** của class space. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|ConPL PDF, tr. 5]]

## Vì sao quan trọng

Trong continual relation extraction, nhiều relation có ngữ cảnh rất gần nhau, ví dụ `father`, `mother`, `spouse`. Nếu embedding space bị méo sau task mới, old relation có thể không mất hoàn toàn trong trọng số model nhưng vị trí vector của nó không còn phân biệt tốt. Khi đó [[Catastrophic Forgetting]] xuất hiện như lỗi hình học: class cũ không còn được kích hoạt hoặc bị nhầm với class gần nghĩa.

ConPL đo prototype distortion bằng cosine similarity giữa embedding của cùng một relation qua các task và quan sát distortion cao thường đi cùng forgetting cao. Paper không báo hệ số tương quan, nên đây là bằng chứng reported/observed ở mức xu hướng, chưa phải kết luận nhân quả. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=11|ConPL PDF, tr. 11]]

## Khi áp dụng

- [[04 - Concepts/Continual Learning|Continual Learning]] có encoder chung bị cập nhật qua nhiều task.
- Few-shot classification dùng prototype hoặc nearest-class-mean.
- Relation/intent/entity classes gần nghĩa và dễ bị confusion.
- Memory nhỏ, nên cần giữ thêm latent geometry chứ không chỉ replay raw examples.
- Cần regularize representation nhưng vẫn cho model đủ plasticity để học class mới.

## Trade-off và failure modes

- Regularization quá mạnh có thể làm model khó học relation mới.
- Một prototype cho mỗi class có thể không đủ nếu class đa mode.
- Nếu prototype memory đã stale, kéo sample về prototype cũ có thể giữ lại bias sai.
- Metric như cosine similarity phải được dùng nhất quán; nhầm giữa distance và similarity dễ làm diễn giải sai objective.
- Loss consistency có thể đóng góp nhỏ khi classifier đã dùng prototype memory mạnh; trong ablation của ConPL, bỏ $L_{cc}$ và $L_{dc}$ riêng lẻ giảm ít hơn nhiều so với bỏ hard-negative loss $L_{fc}$. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8|ConPL PDF, tr. 8]]

## Liên quan

- [[Embedding]]
- [[Prototype Learning]]
- [[Catastrophic Forgetting]]
- [[04 - Concepts/Continual Learning|Continual Learning]]
- [[Continual Relation Extraction]]
- [[Continual Few-Shot Relation Extraction]]
- [[Replay in Continual Learning]]
- [[Contrastive Learning]]

## Nguồn đã dùng

- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]: dùng để hiểu $L_{cc}$, $L_{dc}$, prototype distortion và mối liên hệ với forgetting.
- [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]: ghi nhận embedding-space regularization là một hướng prior work trong CFRE.

## Câu hỏi review

1. Embedding space regularization khác weight regularization ở đâu?
2. Vì sao giữ sample gần prototype đúng chưa đủ để giữ toàn bộ class geometry?
3. Trong ConPL, $L_{cc}$ và $L_{dc}$ bảo vệ hai loại consistency nào?
4. Prototype distortion liên quan gì tới catastrophic forgetting?
5. Khi nào regularization lên embedding space có thể gây hại?

## Gợi ý trả lời câu hỏi review

1. Weight regularization hạn chế trực tiếp tham số; embedding space regularization hạn chế vị trí/quan hệ của vector biểu diễn hoặc output distribution.
2. Vì sample có thể vẫn gần own prototype nhưng quan hệ với các prototype khác bị đổi, làm ranh giới giữa các class gần nghĩa xấu đi.
3. $L_{cc}$ giữ consistency giữa memory sample và prototype đúng; $L_{dc}$ giữ consistency của vector similarity tới toàn bộ prototype memory.
4. Prototype distortion là dấu hiệu class anchor cũ bị trôi; khi anchor trôi, model dễ nhầm hoặc không kích hoạt class cũ.
5. Khi task mới thật sự cần thay đổi representation hoặc prototype cũ không còn đại diện tốt, regularization quá mạnh sẽ giảm plasticity.
