---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 7
start_page: 195
end_page: 233
reading_date: 2026-08-01
planned_sessions:
  - "2026-08-01 | 195-214 | Extractive QA và cách model tìm span trả lời | 55 phút"
  - "2026-08-02 | 215-233 | Retriever-reader pipeline, evaluation và tóm tắt | 55 phút"
estimated_minutes: 80
actual_minutes:
need_review: false
tags:
  - nlp
  - question-answering
  - retrieval
---

# NLP Transformers - Chapter 07 - Question Answering

## Mục tiêu đọc

- Hiểu extractive QA và review-based QA system.
- Nắm vai trò của retriever và reader.
- Biết cách đánh giá từng phần trong QA pipeline.

## Ý chính

- Extractive QA tìm span trả lời trong context có sẵn.
- [[SubjQA]] đưa QA vào bối cảnh customer reviews: câu hỏi/câu trả lời thường chủ quan và không luôn match từ khóa trực tiếp.
- [[SQuAD]] là benchmark extractive QA quan trọng, nhưng hiệu năng cao trên SQuAD không đảm bảo model generalize tốt sang review domain.
- [[Extracting Answers from Text]] nối model output với câu trả lời cuối cùng: chọn start/end token, lọc span hợp lệ, rồi map về text gốc.
- [[Span Classification]] là cách nhìn phổ biến cho extractive QA: dự đoán token bắt đầu và token kết thúc của answer.
- [[Tokenizing Text for QA]] encode `question + context` và giữ metadata cần thiết để map answer span về text gốc.
- [[Sliding Window for QA]] xử lý context dài bằng nhiều window chồng lấn thay vì truncate mù quáng.
- [[Building a Review-Based QA System]] mở rộng QA từ một context sang nhiều review: tìm review liên quan, trích answer span, rồi trả lời kèm bằng chứng.
- Retriever chọn tài liệu liên quan, reader trích câu trả lời từ tài liệu đó.
- [[Using Haystack to Build a QA Pipeline]] cho thấy cách ghép DocumentStore, retriever, reader và answer ranking thành một hệ thống QA có thể chạy/thử nghiệm.
- [[Sparse Retriever]] tìm passage bằng overlap từ khóa; [[BM25]] là baseline phổ biến dùng IDF và length normalization.
- [[Dense Passage Retrieval]] tìm passage bằng embedding similarity giữa question và passage.
- [[Evaluating the Retriever]] dùng [[Recall@k]] và [[Mean Average Precision]] để đo passage chứa đáp án có được lấy ra và xếp hạng tốt không.
- [[Evaluating the Reader]] dùng [[Exact Match]] và [[F1 Score]] để đo answer span có khớp label không.
- [[Domain Adaptation]] cần thiết khi reader fine-tuned trên [[SQuAD]] không generalize tốt sang review domain như [[SubjQA]].
- Đánh giá QA nên tách retriever, reader và pipeline tổng thể.

## Demo thực hành

Chạy extractive QA trên context tự viết.

```python
from transformers import pipeline

qa = pipeline("question-answering")

context = """
Hugging Face provides the Transformers library for working with pretrained models.
It also provides Datasets for loading and processing datasets, and the Hub for
sharing models, datasets, and demos with the community.
"""

questions = [
    "What library is used for pretrained models?",
    "What is the Hub used for?",
]

for question in questions:
    print(qa(question=question, context=context))
```

## Khái niệm quan trọng

- [[Question Answering]]
- [[Building a Review-Based QA System]]
- [[SubjQA]]
- [[SQuAD]]
- [[Using Haystack to Build a QA Pipeline]]
- [[Sparse Retriever]]
- [[Dense Passage Retrieval]]
- [[BM25]]
- [[Evaluating the Retriever]]
- [[Recall@k]]
- [[Mean Average Precision]]
- [[Evaluating the Reader]]
- [[Exact Match]]
- [[F1 Score]]
- [[Extractive QA]]
- [[Extracting Answers from Text]]
- [[Tokenizing Text for QA]]
- [[Sliding Window for QA]]
- [[Span Classification]]
- [[Retriever]]
- [[Reader]]
- [[Domain Adaptation]]

## Active Recall

1. Extractive QA bị giới hạn bởi điều gì?
2. Retriever sai thì reader còn cứu được không?
3. Exact match và F1 trong QA đo gì?
4. Domain adaptation giúp QA pipeline như thế nào?
5. Review-based QA system khác QA trên một context ngắn ở điểm nào?
6. Vì sao extractive QA có thể được xem là span classification?
7. Vì sao cần map token span về text gốc khi extract answer?
8. Haystack giúp tách và debug những thành phần nào trong QA pipeline?
9. BM25 khác dense retrieval ở điểm nào?
10. Sparse retriever và dense passage retrieval khác nhau ở tín hiệu relevance nào?
11. Vì sao retriever đặt upper bound cho QA pipeline?
12. Vì sao nên dùng cả EM và F1 khi đánh giá reader?

## Gợi ý trả lời câu hỏi review

1. Extractive QA bị giới hạn bởi context được đưa vào model. Nếu context không chứa đáp án, bị truncate mất đáp án, hoặc câu hỏi cần tổng hợp nhiều nguồn, model khó trả lời đúng.
2. Thường là không. Reader chỉ đọc passage mà retriever đưa tới; nếu retriever không đưa passage chứa đáp án vào top-k thì reader gần như chỉ chọn một span có vẻ hợp lý nhưng sai.
3. Exact match đo câu trả lời dự đoán có khớp chính xác ground truth sau chuẩn hóa hay không. F1 đo overlap token giữa prediction và label, mềm hơn exact match.
4. Domain adaptation giúp model/reader quen với ngôn ngữ, cấu trúc và kiểu câu hỏi của domain mới, ví dụ review chủ quan trong [[SubjQA]] thay vì Wikipedia trong [[SQuAD]].
5. QA trên context ngắn chỉ cần đọc một đoạn đã cho. Review-based QA cần thêm bước tìm review/passage liên quan trước, rồi mới trích answer span.
6. Vì model dự đoán token bắt đầu và token kết thúc của answer trong context; kết quả cuối cùng là một span liên tục.
7. Vì model output là token index, còn người dùng cần answer text. Offset mapping giúp cắt đúng chuỗi từ context gốc.
8. Haystack giúp tách DocumentStore, retriever, reader, ranking và evaluation để thay component và debug từng tầng.
9. BM25 là sparse/lexical retrieval dựa vào overlap từ khóa, IDF và length normalization; dense retrieval dùng vector embeddings để bắt similarity ngữ nghĩa.
10. Sparse retriever dùng tín hiệu lexical như term overlap và term importance; dense passage retrieval dùng similarity giữa embeddings của question và passage.
11. Vì reader chỉ đọc các passage retriever đưa tới. Nếu passage chứa đáp án không nằm trong top-k, reader không có đủ bằng chứng để trích answer đúng.
12. EM strict nên dễ phạt prediction gần đúng; F1 mềm hơn vì đo overlap token nhưng có thể đánh giá cao câu sai nghĩa. Dùng cả hai giúp cân bằng.

## Checklist

- [x] Đọc xong chapter
- [ ] Chạy demo QA
- [ ] Ghi lại câu hỏi model trả lời sai
- [x] Tách concept cần dùng lại
- [x] Cập nhật tiến độ sách
