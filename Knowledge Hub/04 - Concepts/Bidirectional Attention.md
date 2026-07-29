---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - transformer
  - attention
  - nlp
---

# Bidirectional Attention

## Định nghĩa

Bidirectional attention là dạng self-attention trong đó mỗi token có thể chú ý tới cả token đứng trước và token đứng sau nó trong cùng input sequence.

## Cách hiểu bằng lời của tôi

Bidirectional attention giống như đọc hết cả câu rồi mới giải thích từng từ. Khi model cần hiểu một token, nó được dùng cả ngữ cảnh bên trái lẫn bên phải, nên representation của token giàu thông tin hơn.

Ví dụ, từ `flies` có thể mang nghĩa "bay" hoặc "con ruồi". Nếu model nhìn được toàn câu, các từ như `time`, `arrow`, `fruit`, `banana` sẽ giúp nó chọn nghĩa phù hợp.

## Cần biết

- Bidirectional attention thường gắn với encoder-only models như BERT, RoBERTa và DistilBERT.
- Nó phù hợp với các task cần hiểu toàn bộ input: text classification, named entity recognition, sentence similarity, sentiment analysis.
- Nó khác với causal attention của decoder-only models như GPT, nơi token hiện tại chỉ được nhìn các token trước đó.
- Trong BERT-style classification, token `[CLS]` nhận thông tin từ toàn sequence qua bidirectional attention và thường được đưa vào classification head.
- Bidirectional attention cần toàn bộ input có sẵn, nên không phải cơ chế tự nhiên nhất cho next-token generation từ trái sang phải.

## So sánh với causal attention

| Cơ chế | Được nhìn | Model tiêu biểu | Mục tiêu chính |
| --- | --- | --- | --- |
| Bidirectional attention | Token trước và sau | BERT, DistilBERT | Hiểu văn bản |
| Causal attention | Chỉ token trước đó | GPT | Sinh token tiếp theo |

## Khi áp dụng

- Dùng encoder-only/bidirectional models khi bài toán có toàn bộ input và cần representation giàu ngữ cảnh.
- Dùng decoder-only/causal models khi cần sinh văn bản từng token.
- Với encoder-decoder models, encoder thường dùng bidirectional attention còn decoder dùng causal attention.

## Câu hỏi review

1. Bidirectional attention khác causal attention ở đâu?
2. Vì sao BERT hợp với text classification?
3. Vì sao GPT cần causal attention?
4. `[CLS]` token hưởng lợi gì từ bidirectional attention?

## Gợi ý trả lời câu hỏi review

1. Bidirectional attention nhìn cả trái và phải; causal attention chỉ nhìn các token trước nó.
2. Text classification có toàn bộ input sẵn, nên BERT có thể dùng context hai chiều để tạo representation tốt cho câu.
3. GPT sinh văn bản từ trái sang phải, nên nếu nhìn token tương lai thì sẽ làm sai mục tiêu next-token prediction.
4. `[CLS]` có thể tích lũy thông tin từ toàn sequence qua nhiều layer attention, nên phù hợp làm vector đầu vào cho classification head.

## Liên kết

- [[Self-Attention]]
- [[Transformer]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
