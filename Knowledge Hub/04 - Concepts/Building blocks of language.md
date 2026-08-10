---
type: concept
status: seed
sources:
  - "[[Practical NLP - Chapter 01 - NLP A Primer]]"
source_sections:
  - "[[Practical NLP - Chapter 01 - NLP A Primer]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - linguistics
---

# Building blocks of language

## Định nghĩa

Ngôn ngữ của con người là một hệ thống giao tiếp có cấu trúc, bao gồm nhiều khối xây dựng (building blocks) kết hợp với nhau. Trong xử lý ngôn ngữ tự nhiên (NLP), việc hiểu các khối này giúp ta mô hình hóa ngôn ngữ. Có 4 khối chính:

1. **Phonemes (Âm vị)**: Đơn vị âm thanh nhỏ nhất trong ngôn ngữ. Bản thân chúng không có ý nghĩa nhưng khi kết hợp lại sẽ tạo ra ý nghĩa. Đặc biệt quan trọng cho Speech Recognition và Text-to-Speech.
2. **Morphemes và Lexemes (Hình vị và Từ vị)**: 
   - *Morpheme* là đơn vị nhỏ nhất mang ý nghĩa (ví dụ: tiền tố "multi-", hoặc hậu tố "-able"). Không phải morpheme nào cũng là một từ độc lập.
   - *Lexeme* là các biến thể cấu trúc của cùng một hình vị (ví dụ: "run", "running"). Hình thái học (morphological analysis) dùng để phân tích từ ra các khối này, ứng dụng trong Tokenization, Stemming.
3. **Syntax (Cú pháp)**: Bộ quy tắc để kết hợp các từ, cụm từ thành câu đúng ngữ pháp. Cú pháp thường được biểu diễn dạng cây phân tích (Parse tree). Quan trọng cho Parsing, Entity Extraction.
4. **Context (Ngữ cảnh)**: Cách các phần của ngôn ngữ kết hợp để truyền đạt ý nghĩa cụ thể.
   - *Semantics*: Nghĩa trực tiếp của từ/câu.
   - *Pragmatics*: Nghĩa ngầm định dựa trên kiến thức xã hội, thế giới quan. Cần thiết cho các task phức tạp như Sarcasm detection, Topic modeling.

## Cách hiểu bằng lời của tôi

Ngôn ngữ không chỉ là các "từ" xếp cạnh nhau, mà là một cấu trúc nhiều tầng: từ âm thanh (Phonemes) -> ghép thành các thành phần có nghĩa (Morphemes) -> ghép thành câu theo quy tắc (Syntax) -> và đặt trong một hoàn cảnh cụ thể (Context). Máy tính gặp khó khăn nhất ở tầng Context vì nó đòi hỏi kiến thức nền (World knowledge) - thứ con người tích lũy từ cuộc sống.

## Cần biết

- NLP systems hiện đại đôi khi không cần mô hình hóa tường minh toàn bộ các khối này (ví dụ: Deep Learning có thể học thẳng từ Text/BPE tokens), nhưng hiểu về các khối này giúp giải thích tại sao mô hình gặp lỗi ở những khía cạnh nhất định.

## Liên kết

- [[Language AI]]
- [[Tokenization]]
- [[BPE]]
