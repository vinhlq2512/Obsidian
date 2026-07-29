---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 4
start_page: 160
end_page: 190
estimated_minutes: 75
need_review: true
tags:
  - llm
  - classification
---

# Hands-On LLM - Chapter 04 - Text Classification

## Mục tiêu cần hiểu

- Biết các cách dùng language models cho text classification.
- Phân biệt classification bằng representation model, embeddings và generative model.
- Nắm vai trò của task-specific model, supervised classifier và zero/few-shot prompting.
- Biết vì sao cần so sánh với baseline cổ điển như TF-IDF + logistic regression.

## Định nghĩa quan trọng

- **Text classification**: gán nhãn cho một đoạn text.
- **Task-specific model**: model đã fine-tune cho một tác vụ cụ thể.
- **Supervised classification**: huấn luyện với dữ liệu có nhãn.
- **Zero-shot classification**: phân loại không cần ví dụ huấn luyện trực tiếp cho nhãn mới.
- **Text-to-text model**: model chuyển input text thành output text, có thể dùng cho classification bằng cách sinh nhãn.

## Mental model

Classification có thể được xem là chọn nhãn phù hợp nhất cho text. Representation model biến text thành vector rồi classifier quyết định nhãn. Generative model nhận prompt mô tả nhãn và sinh câu trả lời. Cách nào tốt hơn phụ thuộc dữ liệu, chi phí, latency và yêu cầu kiểm soát.

## Phần cần biết

- Representation models thường nhanh, rẻ và ổn định hơn cho classification production.
- Generative models linh hoạt hơn khi nhãn thay đổi hoặc thiếu dữ liệu huấn luyện.
- Embedding-based classification hữu ích khi muốn tận dụng semantic similarity.
- Task-specific models có thể mạnh nhưng ít linh hoạt nếu domain/label thay đổi.

## Khi áp dụng

- Nếu có nhiều dữ liệu nhãn: fine-tune representation model hoặc train classifier trên embeddings.
- Nếu không có dữ liệu nhãn: thử generative prompting hoặc zero-shot classification.
- Nếu cần latency thấp: tránh model generation lớn nếu representation model đủ tốt.

## Câu hỏi review

1. Khi nào classification bằng embedding đủ tốt?
2. Vì sao generative model có thể phân loại dù không fine-tune?
3. Baseline cổ điển giúp kiểm tra điều gì?
4. Trade-off giữa model nhỏ task-specific và LLM API là gì?

## Gợi ý trả lời câu hỏi review

1. Classification bằng embedding đủ tốt khi nhãn chủ yếu phụ thuộc vào semantic similarity, dữ liệu không quá phức tạp, embedding model phù hợp domain, và classifier đơn giản đạt metric chấp nhận được.
2. Generative model có thể phân loại vì nó đã học nhiều pattern ngôn ngữ trong pretraining và có thể làm theo instruction trong prompt. Ta mô tả nhãn, tiêu chí và format output để model sinh nhãn phù hợp.
3. Baseline cổ điển kiểm tra mức khó thật của bài toán và tránh dùng LLM quá mức. Nếu TF-IDF + logistic regression đã rất tốt, LLM lớn có thể không đáng chi phí.
4. Model nhỏ task-specific thường nhanh, rẻ, ổn định và dễ deploy hơn nhưng kém linh hoạt. LLM API linh hoạt, ít setup và xử lý zero/few-shot tốt hơn, nhưng tốn chi phí, latency cao hơn và phụ thuộc nhà cung cấp.

## Liên kết

- [[Representation Model]]
- [[Generative Model]]
- [[Embedding]]
- [[Fine-tuning]]
