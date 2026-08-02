---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 10 - Creating Text Embedding Models]]"
tags:
  - concept
  - machine-learning
  - embeddings
  - loss-functions
---

# Loss Function

## Định nghĩa

Loss function là hàm đo mức sai lệch giữa output hiện tại của model và mục tiêu học. Trong training, optimizer cố gắng giảm loss bằng cách cập nhật weights.

## Cách hiểu bằng lời của tôi

Loss giống như tín hiệu phản hồi cho model biết "sai ở đâu và sai bao nhiêu". Với embedding model, loss đặc biệt quan trọng vì nó quyết định hình dạng của embedding space: cặp nào nên gần nhau, cặp nào nên xa nhau, và "giống nhau" nghĩa là gì.

## Trong Hands-On Large Language Models

Sách nói rõ nhất về loss functions ở Chapter 10, trong phần tạo text embedding models. Phần này tập trung vào các loss dùng cho sentence-transformers/SBERT và contrastive learning.

Các loss chính được nhắc tới:

- Softmax loss.
- Cosine similarity loss.
- Multiple negatives ranking loss.

Sách cũng nhắc rằng còn nhiều loss khác trong `sentence-transformers`, ví dụ MarginMSE, nhưng không đi sâu.

## Định nghĩa các loss chính

### Softmax loss

Softmax loss biến bài toán so sánh cặp câu thành bài toán classification. Model tạo embedding cho hai câu, kết hợp hai embedding và phần khác biệt giữa chúng, rồi classifier dự đoán nhãn quan hệ như entailment, neutral, contradiction.

- Dữ liệu hợp: cặp câu có nhãn rời rạc.
- Mục tiêu: dự đoán đúng class quan hệ.
- Vai trò trong sách: baseline lịch sử của sentence-transformers, không phải lựa chọn mạnh nhất cho embedding similarity hiện đại.

### Cosine similarity loss

Cosine similarity loss tối ưu để cosine similarity giữa hai embedding gần với score similarity được gán nhãn.

- Dữ liệu hợp: cặp text có điểm giống nhau, thường 0 đến 1.
- Mục tiêu: text giống nhau có cosine cao, text khác nhau có cosine thấp.
- Khi dùng: semantic textual similarity, paraphrase scoring, dữ liệu có similarity labels.

### Multiple negatives ranking loss

Multiple negatives ranking loss, viết tắt là MNR loss, dùng anchor-positive pairs và tận dụng các positive pairs khác trong cùng batch làm negatives.

- Dữ liệu hợp: query-answer, title-abstract, image-caption, hoặc bất kỳ anchor-positive pairs nào.
- Mục tiêu: với một anchor, positive đúng phải có similarity cao hơn các negatives trong batch.
- Cơ chế: tính similarity giữa anchor và các candidate, rồi tối ưu như một classification/ranking task bằng cross-entropy.
- Khi dùng: semantic search, dense retrieval, embedding retrieval.

### InfoNCE và NTXentLoss

InfoNCE và NTXentLoss là các tên/biến thể thường được liên hệ với MNR loss trong contrastive learning. Ý tưởng chung là đưa positive lên cao hơn nhiều negative candidates.

### Hard negative

Hard negative là negative example rất gần với anchor nhưng vẫn sai. Nó tốt hơn easy negative vì buộc model học khác biệt tinh tế.

Ví dụ: nếu anchor là câu hỏi về dân số Amsterdam, hard negative cũng nói về Amsterdam/dân số nhưng trả lời sai hoặc đánh tráo thành phố.

## Cần biết

- Loss phải khớp với mục tiêu sản phẩm: retrieval, semantic similarity, classification hay preference.
- Loss khác nhau tạo ra embedding space khác nhau.
- MNR loss thường hưởng lợi từ batch size lớn vì có nhiều in-batch negatives hơn.
- Hard negatives thường cải thiện retrieval vì làm nhiệm vụ khó hơn và giảm học shortcut.
- Metric/evaluator cũng phải khớp với loss; ví dụ STSB dùng similarity correlation, retrieval dùng Recall@k, MRR, nDCG.

## Khi áp dụng

- Dùng cosine similarity loss khi có cặp text và score similarity.
- Dùng MNR loss khi có anchor-positive pairs và muốn tối ưu retrieval/ranking.
- Dùng softmax loss khi dữ liệu tự nhiên là cặp text với nhãn quan hệ rời rạc, hoặc khi cần baseline đơn giản.
- Tạo hard negatives khi model retrieval nhầm các tài liệu có vẻ liên quan nhưng sai đáp án.

## Câu hỏi review

1. Loss function ảnh hưởng embedding space như thế nào?
2. Cosine similarity loss cần loại nhãn gì?
3. MNR loss tận dụng in-batch negatives ra sao?
4. Vì sao hard negatives thường giúp model retrieval tốt hơn?

## Gợi ý trả lời câu hỏi review

1. Loss function quyết định cặp embedding nào bị kéo gần hoặc đẩy xa, nên nó định nghĩa tiêu chí similarity mà model học.
2. Cosine similarity loss cần nhãn similarity dạng score, thường trong khoảng 0 đến 1.
3. MNR loss lấy positive pair của sample khác trong cùng batch làm negative candidates cho anchor hiện tại.
4. Hard negatives gần với anchor nhưng sai, nên model phải học ranh giới tinh tế hơn thay vì chỉ phân biệt các ví dụ quá dễ.

## Liên kết

- [[Hands-On LLM - Chapter 10 - Creating Text Embedding Models]]
- [[Embedding]]
- [[Contrastive Learning]]
- [[Semantic Search]]
- [[Fine-tuning]]
