---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - nlp
  - tokenization
---

# Tokenizer Pipeline

## Định nghĩa

Tokenizer pipeline là chuỗi bước biến văn bản thô thành token IDs và metadata đi kèm để model Transformer có thể xử lý.

## Cách hiểu bằng lời của tôi

Tokenizer không chỉ đơn giản là "cắt chữ". Nó là một pipeline có nhiều quyết định nhỏ: chuẩn hóa text, chia sơ bộ, tách thành subword/token, rồi thêm special tokens và thông tin phụ. Với token-level task như [[Named Entity Recognition]], từng quyết định trong pipeline ảnh hưởng trực tiếp đến cách căn chỉnh nhãn.

## Các bước thực hiện

### 1. Normalization

Chuẩn hóa text đầu vào để giảm nhiễu bề mặt trước khi tokenize.

Ví dụ các thao tác có thể có:

- Chuẩn hóa Unicode.
- Chuyển lowercase nếu tokenizer/model yêu cầu.
- Loại hoặc chuẩn hóa dấu, ký tự đặc biệt, khoảng trắng.
- Biến các dạng text tương đương về cùng một biểu diễn.

Điểm cần nhớ: normalization có thể làm mất thông tin bề mặt. Với NER, chữ hoa trong tên riêng đôi khi là tín hiệu hữu ích, nên không phải model nào cũng lowercase.

### 2. Pretokenization

Chia text thành các đơn vị sơ bộ trước khi tokenizer model tách subword.

Ví dụ:

- Tách theo khoảng trắng.
- Tách dấu câu.
- Giữ lại offset để biết mỗi mảnh nằm ở vị trí nào trong chuỗi gốc.

Điểm cần nhớ: pretokenization quyết định ranh giới ban đầu. Với multilingual NLP, phụ thuộc quá mạnh vào khoảng trắng có thể bất lợi vì không phải ngôn ngữ nào cũng tách từ giống tiếng Anh.

### 3. Tokenizer Model

Áp dụng thuật toán tokenization để biến đơn vị sơ bộ thành token/subword trong vocabulary.

Ví dụ thuật toán:

- BPE.
- WordPiece.
- Unigram, thường gặp trong [[SentencePiece]].

Điểm cần nhớ: đây là bước khiến một từ có thể bị tách thành nhiều subword. Trong NER, nhãn word-level cần được map sang subword-level.

### 4. Postprocessing

Tạo input cuối cùng cho model bằng cách thêm special tokens và metadata.

Ví dụ:

- Thêm `[CLS]`, `[SEP]`, `<s>`, `</s>` tùy model.
- Tạo `input_ids`.
- Tạo `attention_mask`.
- Tạo `token_type_ids` nếu model cần.
- Giữ offset mapping để nối token với span gốc.

Điểm cần nhớ: postprocessing giúp input khớp đúng format mà model đã được pretrain. Sai special tokens hoặc mask có thể làm model hoạt động lệch.

## Mental model

```text
raw text
-> normalization
-> pretokenization
-> tokenizer model
-> postprocessing
-> input_ids + attention_mask + offsets
```

## Liên hệ với NER

Với NER, dữ liệu thường có nhãn theo word hoặc span, còn model nhận token/subword. Vì vậy cần:

- Tokenize text nhưng giữ offset hoặc word IDs.
- Xác định subword nào thuộc word/entity nào.
- Gán nhãn cho subword đầu tiên hoặc propagate nhãn sang các subword phụ.
- Ignore special tokens và các subword không muốn tính loss bằng giá trị như `-100`.

Nếu bước align sai, model có thể học sai ranh giới entity dù kiến trúc Transformer vẫn đúng.

Xem chi tiết hơn ở [[Tokenizing Texts for NER]].

## Cần biết

- Tokenizer phải khớp với pretrained model; không nên tùy tiện đổi tokenizer khi dùng lại model.
- Tokenizer ảnh hưởng đến độ dài sequence, tốc độ, chi phí và chất lượng downstream task.
- Với [[Multilingual Transformer]], tokenizer cần xử lý nhiều ngôn ngữ, hệ chữ và tên riêng hiếm.
- Với [[SentencePiece]], text thường được xử lý gần hơn với raw text và ít phụ thuộc vào khoảng trắng.

## Liên kết

- [[Tokenization]]
- [[SentencePiece]]
- [[Tokenizing Texts for NER]]
- [[Multilingual Transformer]]
- [[Named Entity Recognition]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
