---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 5
start_page: 192
end_page: 233
estimated_minutes: 100
need_review: true
tags:
  - llm
  - clustering
  - topic-modeling
---

# Hands-On LLM - Chapter 05 - Text Clustering and Topic Modeling

## Mục tiêu cần hiểu

- Hiểu pipeline clustering text: embed documents, reduce dimensions, cluster, inspect clusters.
- Nắm topic modeling là bước diễn giải cluster thành chủ đề có tên/keywords.
- Biết BERTopic là framework modular kết hợp embeddings, dimensionality reduction, clustering và representation.
- Hiểu vai trò của generative models trong việc đặt tên hoặc mô tả topic.

## Định nghĩa quan trọng

- **Text clustering**: nhóm tài liệu giống nhau mà không cần nhãn.
- **Dimensionality reduction**: giảm số chiều embedding để clustering dễ hơn.
- **Topic modeling**: tìm/chú giải các chủ đề ẩn trong tập tài liệu.
- **BERTopic**: pipeline topic modeling hiện đại dựa trên embeddings và clustering.
- **Cluster inspection**: đọc mẫu tài liệu trong cluster để hiểu cluster đại diện cho gì.

## Mental model

Embedding đưa tài liệu vào không gian vector. Dimensionality reduction làm không gian này dễ phân cụm hơn. Clustering tạo nhóm. Topic modeling biến nhóm thành kiến thức có thể đọc được bằng keywords, representative documents hoặc mô tả sinh bởi LLM.

## Phần cần biết

- Clustering không có "đáp án đúng" duy nhất; cần inspect thủ công.
- Tham số clustering ảnh hưởng số lượng và độ lớn cluster.
- Topic label tốt phải vừa ngắn vừa đại diện cho tài liệu trong nhóm.
- Generative model có thể giúp mô tả topic, nhưng vẫn cần kiểm chứng.

## Khi áp dụng

- Dùng cho khám phá corpus lớn: paper abstracts, tickets, feedback, logs, documents.
- Dùng topic modeling để tạo taxonomy ban đầu, không xem đó là ground truth.
- Luôn lưu representative documents cho mỗi topic để kiểm tra chất lượng.

## Câu hỏi review

1. Vì sao cần giảm chiều embedding trước khi clustering?
2. Clustering khác classification ở điểm nào?
3. Topic modeling thêm tầng ý nghĩa nào lên clustering?
4. Vì sao cần inspect clusters?

## Gợi ý trả lời câu hỏi review

1. Cần giảm chiều vì embedding gốc thường có số chiều lớn, nhiều nhiễu và khó cluster hiệu quả. Dimensionality reduction giúp giữ cấu trúc chính, giảm noise và làm thuật toán clustering ổn định hơn.
2. Clustering là unsupervised: model tự nhóm dữ liệu chưa có nhãn. Classification là supervised hoặc rule-based: model gán dữ liệu vào nhãn đã định nghĩa trước.
3. Topic modeling biến cluster thành chủ đề có thể hiểu được bằng keywords, representative documents, labels hoặc mô tả. Nó chuyển nhóm vector thành tri thức đọc được.
4. Cần inspect vì cluster có thể nhiễu, nhập nhiều chủ đề vào một nhóm, hoặc tách một chủ đề thành nhiều nhóm. Đọc representative documents giúp kiểm tra cluster có ý nghĩa thật không.

## Liên kết

- [[Embedding]]
- [[Topic Modeling]]
- [[Semantic Search]]
- [[Generative Model]]
