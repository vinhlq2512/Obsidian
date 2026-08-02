---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
source_sections:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
first_seen: 2026-08-01
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - question-answering
---

# Extracting Answers from Text

## Định nghĩa

Extracting answers from text là bước lấy câu trả lời trực tiếp từ context bằng cách chọn một answer span trong đoạn văn bản đầu vào.

## Cách hiểu bằng lời của tôi

Trong [[Extractive QA]], model không trả lời bằng kiến thức chung hoặc tự viết lại câu. Nó đọc cặp `question + context`, chấm điểm từng token trong context, rồi cắt ra đoạn text có khả năng là câu trả lời.

```text
question + context
-> [[Tokenizer Pipeline|tokenize và giữ offset]]
-> model tạo start_logits/end_logits
-> chọn span hợp lệ
-> map token span về text gốc
-> answer
```

## Cơ chế chính

- Tokenizer cần giữ mapping giữa token và vị trí ký tự trong text gốc để có thể cắt lại câu trả lời.
- Model thường dùng [[Span Classification]]: một head dự đoán token bắt đầu, một head dự đoán token kết thúc.
- Không phải cặp start/end nào cũng hợp lệ; hệ thống cần tránh span nằm trong phần question, token đặc biệt, padding, hoặc có end trước start.
- Nếu context dài hơn giới hạn model, context được chia thành nhiều chunk/window; mỗi window sinh candidate answer, sau đó chọn candidate tốt nhất.

## Mental model

```text
Không phải:
model -> "nghĩ ra" câu trả lời

Mà là:
model -> tìm tọa độ câu trả lời trong text
```

## Ví dụ nhỏ

```text
Question: Thư viện nào dùng cho pretrained models?
Context: Hugging Face cung cấp thư viện Transformers cho pretrained models.

start token: Transformers
end token: Transformers
answer: Transformers
```

## Phần cần biết

- Bước này phụ thuộc mạnh vào việc context có thật sự chứa đáp án hay không.
- Nếu [[Retriever]] đưa sai passage, [[Reader]] có thể vẫn chọn một span có vẻ hợp lý nhưng không trả lời đúng câu hỏi.
- Với câu hỏi cần tổng hợp nhiều đoạn hoặc cần diễn đạt lại, trích span trực tiếp thường không đủ.
- Khi debug, nên kiểm tra: context được tokenize thế nào, offset có đúng không, span được chọn có nằm trong context không, và score có bị lệch vì chunking không.

## Câu hỏi review

1. Vì sao cần offset mapping khi extract answer từ text?
2. Start logits và end logits được dùng như thế nào?
3. Khi context quá dài, vì sao phải chia thành nhiều window?
4. Vì sao reader có thể trả lời sai dù model tự tin?

## Gợi ý trả lời câu hỏi review

1. Vì output của model là vị trí token, còn câu trả lời cuối cùng cần được cắt lại từ text gốc.
2. Chúng cho biết mỗi token có khả năng là điểm bắt đầu hoặc kết thúc của answer span.
3. Vì Transformer có giới hạn sequence length; mỗi window giúp model đọc một phần context vừa đủ.
4. Vì context có thể không chứa đáp án, retriever có thể đưa sai passage, hoặc span hợp lệ về mặt score nhưng không đúng ngữ nghĩa câu hỏi.

## Liên kết

- [[Question Answering]]
- [[Extractive QA]]
- [[Span Classification]]
- [[Reader]]
- [[Retriever]]
- [[Tokenizer Pipeline]]
- [[NLP Transformers - Chapter 07 - Question Answering]]
