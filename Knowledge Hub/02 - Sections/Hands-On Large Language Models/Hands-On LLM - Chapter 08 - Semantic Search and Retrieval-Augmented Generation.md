---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 8
start_page: 316
end_page: 358
estimated_minutes: 105
need_review: true
tags:
  - llm
  - semantic-search
  - rag
---

# Hands-On LLM - Chapter 08 - Semantic Search and Retrieval-Augmented Generation

## Mục tiêu cần hiểu

- Hiểu [[Semantic Search]] dùng embeddings để tìm tài liệu theo nghĩa thay vì keyword thuần.
- Nắm dense retrieval, chunking, vector database và similarity search.
- Biết reranking dùng model mạnh hơn để sắp xếp lại candidate results.
- Hiểu [[Retrieval-Augmented Generation]] nối retrieval với generation để tạo câu trả lời grounded.
- Nắm retrieval metrics và RAG evaluation ở mức hệ thống.

## Định nghĩa quan trọng

- **Dense retrieval**: retrieval bằng vector dense embedding.
- **Chunking**: chia tài liệu thành đoạn nhỏ trước khi embedding.
- **Vector database**: nơi lưu embedding vectors và metadata để tìm nearest neighbors.
- **Reranking**: sắp xếp lại kết quả retrieval bằng model chuyên đánh giá query-document relevance.
- **RAG**: pipeline lấy context liên quan rồi đưa vào LLM để sinh câu trả lời.
- **Grounded generation**: sinh câu trả lời dựa trên tài liệu được truy xuất.

## Mental model

RAG là cách cho LLM "mở sách" trước khi trả lời. Retriever chọn trang liên quan, reranker chọn đoạn tốt nhất, generator viết câu trả lời dựa trên đoạn đó. Chất lượng RAG phụ thuộc nhiều vào retrieval hơn người mới thường nghĩ.

## Phần cần biết

- Chunk quá dài làm retrieval kém chính xác; chunk quá ngắn mất ngữ cảnh.
- Dense retrieval tìm theo nghĩa nhưng có thể bỏ lỡ từ khóa chính xác.
- Reranking cải thiện top results nhưng tăng latency.
- Evaluation phải tách retrieval quality và generation quality.
- RAG không tự đảm bảo đúng; vẫn cần citation, grounding và kiểm chứng.

## Khi áp dụng

- Dùng semantic search khi người dùng hỏi bằng ngôn ngữ tự nhiên.
- Dùng RAG khi kiến thức thay đổi, private, dài hoặc không nằm trong model.
- Thêm reranker khi kết quả top-k nhiều nhiễu.
- Log query, retrieved chunks và answer để debug.

## Câu hỏi review

1. Semantic search khác keyword search ở đâu?
2. Vì sao chunking là quyết định thiết kế quan trọng?
3. Reranker cải thiện phần nào của pipeline?
4. Đánh giá RAG cần đo những gì?

## Gợi ý trả lời câu hỏi review

1. Keyword search tìm theo từ khóa xuất hiện trong tài liệu. Semantic search embed query và documents rồi tìm theo ý nghĩa, nên có thể tìm được kết quả liên quan dù dùng từ khác.
2. Chunking quan trọng vì nó quyết định đơn vị được embed và retrieve. Chunk quá dài gây loãng thông tin, chunk quá ngắn mất ngữ cảnh. Chunk tốt giúp retriever lấy đúng đoạn đủ thông tin.
3. Reranker cải thiện bước xếp hạng sau retrieval. Retriever lấy candidate nhanh, reranker đánh giá query-document relevance kỹ hơn để đưa đoạn tốt nhất lên đầu.
4. Đánh giá RAG cần đo retrieval quality như recall@k/MRR/nDCG, generation quality như correctness/helpfulness, grounding/faithfulness, citation accuracy, latency, cost và khả năng trả lời "không biết" khi thiếu context.

## Liên kết

- [[Semantic Search]]
- [[Retrieval-Augmented Generation]]
- [[Embedding]]
- [[Vector Database]]
