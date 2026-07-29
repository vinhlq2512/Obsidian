---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 1
start_page: 23
end_page: 64
estimated_minutes: 90
need_review: true
tags:
  - llm
  - language-ai
---

# Hands-On LLM - Chapter 01 - An Introduction to Large Language Models

## Mục tiêu cần hiểu

- Hiểu [[Language AI]] là lĩnh vực xây dựng hệ thống có khả năng hiểu, xử lý và sinh ngôn ngữ tự nhiên.
- Nắm lịch sử ngắn của Language AI: bag-of-words, dense embeddings, attention, Transformer, encoder-only models, decoder-only models và làn sóng generative AI.
- Phân biệt [[Representation Model]] và [[Generative Model]].
- Hiểu vì sao định nghĩa "large" trong [[Large Language Model]] là tương đối và thay đổi theo thời gian.
- Biết các cách tương tác với LLM: proprietary/private models, open models và open source frameworks.

## Định nghĩa quan trọng

- **Language AI**: nhánh của AI tập trung vào công nghệ hiểu, xử lý và tạo ra ngôn ngữ con người.
- **Bag-of-words**: biểu diễn văn bản bằng tần suất/tồn tại của từ, bỏ qua thứ tự và ngữ cảnh.
- **Dense embedding**: vector dày đặc biểu diễn ý nghĩa, giúp đo độ tương đồng giữa từ/câu/tài liệu.
- **Representation model**: model tạo biểu diễn hữu ích cho tác vụ như classification, clustering, retrieval.
- **Generative model**: model sinh token mới, thường dùng cho chat, writing, summarization, code generation.
- **LLM**: language model có năng lực rộng, thường có quy mô lớn, nhưng kích thước không phải tiêu chí duy nhất.

## Mental model

Sách đặt nền bằng một trục tiến hóa: từ biểu diễn thô của text sang biểu diễn ngữ nghĩa, rồi sang mô hình có attention và Transformer. Khi model chỉ biểu diễn text tốt, nó rất mạnh cho tìm kiếm, phân loại và clustering. Khi model học sinh token kế tiếp tốt, nó trở thành nền tảng cho chat, reasoning, summarization và công cụ viết.

## Phần cần biết

- Bag-of-words dễ dùng nhưng mất thứ tự, ngữ cảnh và nghĩa tinh tế.
- Embeddings cho phép so sánh text bằng khoảng cách vector.
- Attention giúp model chọn phần input liên quan thay vì nén mọi thứ vào một vector cố định.
- Encoder-only models như BERT mạnh về understanding.
- Decoder-only models như GPT mạnh về generation.
- LLM hữu ích vì một model có thể được điều khiển bằng prompt và áp dụng cho nhiều tác vụ.

## Khi áp dụng vào developer workflow

- Dùng representation model khi cần search, clustering, classification hoặc reranking.
- Dùng generative model khi cần sinh text/code, tóm tắt, giải thích hoặc hội thoại.
- Ưu tiên open models khi cần kiểm soát dữ liệu/chi phí/hạ tầng.
- Ưu tiên proprietary models khi cần chất lượng cao nhanh và không muốn vận hành model.

## Câu hỏi review

1. Vì sao bag-of-words không đủ để biểu diễn ngữ nghĩa?
2. Representation model khác generative model ở output và use case nào?
3. Một model có nhỏ hơn nhưng mạnh hơn model lớn hơn thì có còn nên gọi là LLM không?
4. Khi nào nên dùng model API thay vì open model tự host?

## Gợi ý trả lời câu hỏi review

1. Bag-of-words không đủ vì nó chỉ đếm hoặc đánh dấu từ xuất hiện, gần như bỏ qua thứ tự, ngữ cảnh, đa nghĩa và quan hệ giữa các từ. Hai câu dùng cùng từ nhưng nghĩa khác nhau có thể bị biểu diễn gần giống nhau.
2. Representation model thường trả về vector/embedding hoặc hidden representation để dùng cho classification, retrieval, clustering, reranking. Generative model trả về token/text mới, phù hợp chat, summarization, code generation, reasoning hoặc viết nội dung.
3. Có thể vẫn gọi là LLM nếu model có năng lực ngôn ngữ rộng và tổng quát. "Large" là nhãn tương đối; năng lực, dữ liệu huấn luyện, kiến trúc và use case quan trọng hơn chỉ số tham số.
4. Nên dùng model API khi cần chất lượng nhanh, không muốn vận hành hạ tầng, không có GPU, hoặc cần model frontier. Nên tự host open model khi cần kiểm soát dữ liệu, chi phí dài hạn, độ trễ nội bộ, customization hoặc yêu cầu privacy.

## Liên kết

- [[Language AI]]
- [[Large Language Model]]
- [[Representation Model]]
- [[Generative Model]]
- [[Embedding]]
- [[Transformer]]
