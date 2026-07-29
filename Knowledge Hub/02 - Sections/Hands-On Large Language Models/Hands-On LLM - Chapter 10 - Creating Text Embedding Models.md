---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 10
start_page: 399
end_page: 443
estimated_minutes: 110
need_review: true
tags:
  - llm
  - embeddings
  - contrastive-learning
  - loss-functions
---

# Hands-On LLM - Chapter 10 - Creating Text Embedding Models

## Mục tiêu cần hiểu

- Hiểu embedding model học notion of similarity theo mục tiêu training.
- Nắm [[Contrastive Learning]] và cách tạo positive/negative pairs.
- Biết SBERT tạo sentence embeddings hiệu quả hơn BERT gốc cho semantic similarity.
- Hiểu [[Loss Function]] và evaluation cho embedding models.
- Biết fine-tune embedding model bằng supervised data, augmented SBERT và unsupervised TSDAE.

## Định nghĩa quan trọng

- **Contrastive learning**: học bằng cách kéo các cặp giống nhau lại gần và đẩy cặp khác nhau ra xa.
- **Positive pair**: hai text nên gần nhau trong embedding space.
- **Negative pair**: hai text nên xa nhau trong embedding space.
- **SBERT**: biến thể dùng Siamese/triplet setup để tạo sentence embeddings tốt.
- **Loss function**: hàm đo model đang sai lệch bao nhiêu so với mục tiêu học; optimizer dùng giá trị này để cập nhật weights.
- **Softmax loss**: loss dùng classifier softmax để phân loại quan hệ giữa các cặp câu, ví dụ entailment, neutral, contradiction.
- **Cosine similarity loss**: loss tối ưu để cosine similarity giữa hai embedding gần với điểm similarity được gán nhãn.
- **Multiple negatives ranking loss**: loss dùng positive pairs và các in-batch negatives để kéo cặp đúng lại gần, đẩy cặp sai ra xa.
- **Hard negative**: negative example rất giống anchor nhưng không phải đáp án/cặp đúng, buộc model học biểu diễn tinh tế hơn.
- **TSDAE**: denoising autoencoder tuần tự dựa trên Transformer để domain adaptation không nhãn.
- **Domain adaptation**: điều chỉnh model cho domain cụ thể.

## Mental model

Embedding model không tự nhiên biết "giống nhau" nghĩa là gì. Similarity phụ thuộc dữ liệu và objective. Nếu train bằng cặp paraphrase, model học semantic similarity. Nếu train bằng sentiment labels, vector sẽ gần nhau theo sentiment hơn là nghĩa tổng quát.

## Phần cần biết

- Evaluation embedding thường dùng correlation với human similarity scores hoặc retrieval metrics.
- Loss function quyết định geometry của embedding space.
- Trong Chapter 10, phần nói rõ nhất về loss nằm ở mục **Loss Functions** của chương tạo text embedding models. Sách nhấn mạnh rằng chọn loss có thể làm performance thay đổi lớn: ví dụ minh họa softmax loss là baseline, cosine similarity loss tốt hơn, và multiple negatives ranking loss thường mạnh hơn nữa cho embedding/retrieval.
- Augmented SBERT dùng model mạnh hơn tạo dữ liệu bổ sung.
- TSDAE hữu ích khi có domain text nhưng thiếu labels.

## Loss Functions

### Vì sao loss quan trọng với embedding model

Loss function không chỉ là công thức tối ưu. Với embedding models, loss quyết định trực tiếp hình dạng của embedding space:

- Text nào được kéo lại gần nhau.
- Text nào bị đẩy ra xa.
- Model hiểu "similarity" theo semantic similarity, entailment, retrieval relevance, label similarity hay một tiêu chí khác.

Vì vậy, cùng một base model và cùng dữ liệu gần giống nhau, đổi loss có thể tạo ra embedding space khác hẳn. Sách minh họa điều này bằng việc training SBERT/bi-encoder trên dữ liệu NLI và đánh giá bằng STSB.

### Softmax loss

Softmax loss là cách training ban đầu của sentence-transformers. Model nhận cặp câu, tạo embedding cho từng câu, rồi kết hợp embedding của hai câu cùng phần chênh lệch giữa chúng để classifier dự đoán label quan hệ như entailment, neutral, contradiction.

- Dữ liệu phù hợp: cặp câu có nhãn phân loại rời rạc.
- Cách học: biến similarity learning thành classification task.
- Ưu điểm: dễ hiểu, hợp với dữ liệu NLI có nhãn class.
- Hạn chế: không phải lựa chọn mạnh nhất cho embedding similarity hiện đại; sách dùng nó chủ yếu như baseline minh họa.

### Cosine similarity loss

Cosine similarity loss dùng khi mỗi cặp text có một điểm similarity liên tục, thường nằm trong khoảng 0 đến 1. Model tạo embedding cho hai text, tính cosine similarity, rồi tối ưu để cosine similarity dự đoán gần với label similarity.

- Dữ liệu phù hợp: semantic textual similarity, paraphrase, cặp câu có score giống/khác theo mức độ.
- Cách học: cặp giống nhau có cosine cao, cặp khác nhau có cosine thấp.
- Ưu điểm: trực giác rõ, dễ dùng, hợp với bài toán similarity.
- Hạn chế: cần nhãn similarity dạng score hoặc phải map nhãn rời rạc sang score, ví dụ entailment = 1, neutral/contradiction = 0.

### Multiple negatives ranking loss

Multiple negatives ranking loss, còn gọi là MNR loss, InfoNCE hoặc NTXentLoss trong một số ngữ cảnh, thường dùng cho embedding retrieval. Dữ liệu gồm các positive pairs như query-answer, title-abstract, image-caption. Trong một batch, các positive pair khác được dùng như negative cho anchor hiện tại.

- Dữ liệu phù hợp: cặp anchor-positive, ví dụ câu hỏi và câu trả lời đúng.
- Cách học: với một anchor, model phải xếp positive đúng cao hơn các negative trong batch.
- Cơ chế chính: tính similarity giữa anchor và nhiều candidate, rồi dùng cross-entropy để tối ưu việc chọn đúng positive.
- Ưu điểm: rất hiệu quả cho retrieval/semantic search vì tận dụng in-batch negatives.
- Hạn chế: nếu negatives quá dễ, model học ít. Hard negatives thường giúp model tốt hơn vì buộc nó phân biệt những trường hợp gần giống nhưng sai.
- Ghi nhớ thực dụng: batch size lớn thường giúp MNR loss tốt hơn vì mỗi anchor có nhiều candidate negative hơn.

### Hard negatives

Hard negative là ví dụ âm gần với anchor về chủ đề hoặc surface form nhưng không phải cặp đúng. Trong retrieval, hard negative tốt hơn easy negative vì nó ép model học ranh giới liên quan/không liên quan tinh hơn.

Ví dụ: với câu hỏi "Có bao nhiêu người sống ở Amsterdam?", một hard negative tốt cũng nói về Amsterdam và dân số nhưng trả lời sai hoặc nói về thành phố khác. Nếu negative hoàn toàn không liên quan, model chỉ cần học dấu hiệu thô là đã phân biệt được.

### Bảng so sánh nhanh

| Loss | Input phù hợp | Mục tiêu học | Khi dùng |
| --- | --- | --- | --- |
| Softmax loss | Cặp câu có nhãn class | Dự đoán class quan hệ giữa hai câu | Baseline hoặc dữ liệu NLI dạng label rời rạc |
| Cosine similarity loss | Cặp câu có similarity score | Làm cosine similarity khớp score | Semantic textual similarity |
| MNR loss | Anchor-positive pairs | Xếp positive đúng cao hơn negatives | Retrieval, semantic search, embedding ranking |

## Ý nghĩa kết quả trong sách

- Softmax loss cho kết quả baseline thấp hơn trên STSB.
- Cosine similarity loss cải thiện rõ vì nó khớp trực tiếp với semantic similarity.
- MNR loss tiếp tục tốt hơn trong ví dụ của sách vì objective gần với ranking/retrieval hơn.
- Bài học chính: khi fine-tune embedding model, đừng chỉ chọn model; phải chọn đúng dữ liệu, đúng loss và đúng evaluator.

## Khi áp dụng

- Fine-tune embedding model khi off-the-shelf embeddings retrieval kém trên domain riêng.
- Trước khi fine-tune, cần xác định "similarity" trong bài toán là gì.
- Tạo validation set nhỏ nhưng chất lượng cao để tránh tối ưu mù.
- Dùng cosine similarity loss nếu có cặp câu kèm score similarity.
- Dùng MNR loss nếu dữ liệu tự nhiên là query-document, question-answer, title-abstract, image-caption hoặc anchor-positive pairs.
- Tạo hard negatives nếu retrieval đang nhầm các tài liệu rất giống nhau.

## Câu hỏi review

1. Contrastive learning cần positive/negative examples để làm gì?
2. SBERT cải thiện điều gì so với dùng BERT embedding trực tiếp?
3. Similarity theo semantic và similarity theo label khác nhau thế nào?
4. Khi nào TSDAE phù hợp?
5. Loss function ảnh hưởng embedding space như thế nào?
6. Softmax loss, cosine similarity loss và MNR loss khác nhau ở input/mục tiêu nào?
7. Vì sao MNR loss thường hưởng lợi từ batch size lớn?
8. Hard negative khác easy negative ở đâu?

## Gợi ý trả lời câu hỏi review

1. Positive/negative examples dạy model geometry của embedding space: cặp liên quan nên gần nhau, cặp không liên quan nên xa nhau. Không có chúng, model không biết "giống nhau" nghĩa là gì cho bài toán cụ thể.
2. SBERT cải thiện việc tạo sentence embeddings bằng cách huấn luyện BERT trong setup phù hợp cho similarity/retrieval. Thay vì so sánh cross-encoder chậm hoặc dùng embedding thô kém ổn định, SBERT tạo vector câu có thể so sánh nhanh.
3. Similarity theo semantic nghĩa là hai text gần nhau vì cùng nghĩa/chủ đề. Similarity theo label nghĩa là chúng gần nhau vì cùng nhãn task, dù nội dung ngữ nghĩa có thể khác.
4. TSDAE phù hợp khi có nhiều text không nhãn trong domain riêng và muốn domain adaptation cho embedding model mà chưa có dữ liệu labeled pairs chất lượng.
5. Loss function quyết định cặp nào bị kéo gần, cặp nào bị đẩy xa, và model tối ưu similarity theo tiêu chí nào. Vì vậy nó định hình geometry của embedding space.
6. Softmax loss dùng cặp câu có nhãn class và học dự đoán quan hệ. Cosine similarity loss dùng cặp câu có score similarity và học cosine khớp score. MNR loss dùng anchor-positive pairs và học xếp positive đúng cao hơn negatives.
7. Batch size lớn tạo nhiều in-batch negatives hơn, làm bài toán khó hơn và cho tín hiệu ranking giàu hơn.
8. Easy negative thường không liên quan rõ ràng nên dễ phân biệt. Hard negative gần chủ đề hoặc gần bề mặt với anchor nhưng sai, nên ép model học nuance tốt hơn.

## Liên kết

- [[Embedding]]
- [[Contrastive Learning]]
- [[Loss Function]]
- [[Semantic Search]]
- [[Fine-tuning]]
