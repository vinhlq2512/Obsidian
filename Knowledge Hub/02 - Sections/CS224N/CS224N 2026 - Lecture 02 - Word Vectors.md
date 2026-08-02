---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: lecture
title: "CS224N 2026 - Lecture 02 - Word Vectors"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 02 - Word Vectors.pdf]]"
pages: 44
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Embedding]]"
  - "[[Tokenization]]"
tags:
  - cs224n
  - lecture
---

# CS224N 2026 - Lecture 02 - Word Vectors

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 02 - Word Vectors.pdf]]
- Vai trò trong khoá: mở nền cho [[Embedding]], [[Word2Vec]] và cách biểu diễn nghĩa bằng vector.
- Paper đọc kèm: [[2013 - Efficient Estimation of Word Representations in Vector Space - arXiv 1301.3781v3]], [[2013 - Distributed Representations of Words and Phrases and their Compositionality - NeurIPS]], [[2014 - GloVe - Global Vectors for Word Representation]].

## Mục tiêu cần hiểu

- Vì sao one-hot/discrete symbol không đủ để biểu diễn nghĩa cho NLP hiện đại.
- Cách [[Embedding|word vector]] biến nghĩa của từ thành điểm trong không gian nhiều chiều.
- Skip-gram/word2vec học vector bằng mục tiêu dự đoán context từ center word.
- Vì sao cosine similarity, analogy và downstream task được dùng để đánh giá embedding.

## Ý chính

- Cách cổ điển như WordNet dựa vào synonym/hypernym hữu ích nhưng thiếu sắc thái, khó cập nhật nghĩa mới, tốn công người tạo và không cho model học trực tiếp từ dữ liệu lớn.
- One-hot vector biểu diễn từ như ID rời rạc. Hai từ gần nghĩa vẫn trực giao, nên máy không tự biết `hotel` gần `motel` hơn `cat`.
- Distributional semantics: nghĩa của một từ được suy ra từ ngữ cảnh mà nó xuất hiện. Nếu hai từ xuất hiện trong context tương tự, vector của chúng nên gần nhau.
- Word2vec học embedding bằng cách biến bài toán nghĩa thành bài toán dự đoán: từ center word dự đoán context words hoặc ngược lại.
- Vector tốt không chỉ gom từ đồng nghĩa; nó có thể mã hoá quan hệ tuyến tính tương đối như analogy, nhưng analogy chỉ là một phép kiểm tra nội tại, không đảm bảo hiệu quả downstream.

## Mental model

```text
corpus lớn
-> tạo cặp center/context
-> model dự đoán context từ center
-> cập nhật vector để từ xuất hiện trong context giống nhau nằm gần nhau
-> embedding trở thành biểu diễn nghĩa có thể dùng cho task khác
```

Cách nhớ: word vector là “tọa độ nghĩa” học từ hành vi xuất hiện của từ trong văn bản, không phải từ định nghĩa trong từ điển.

## Cơ chế Word2Vec

Với skip-gram, input là center word $c$, output là xác suất cho mỗi outside/context word $o$:

$$
P(o|c) = \frac{\exp(u_o^T v_c)}{\sum_{w \in V}\exp(u_w^T v_c)}
$$

Trong đó:

- $v_c$ là vector của center word.
- $u_o$ là vector output của outside word.
- $V$ là vocabulary.
- Dot product lớn nghĩa là center và outside tương thích trong context.
- Softmax biến score thành phân phối xác suất.

Mục tiêu học là tăng xác suất cho các context thật và giảm xác suất cho context sai. Vấn đề thực tế: mẫu số softmax chạy qua toàn bộ vocabulary nên rất đắt; vì vậy các biến thể như negative sampling/hierarchical softmax xuất hiện để huấn luyện nhanh hơn.

## Đánh giá embedding

- **Intrinsic evaluation**: kiểm tra trực tiếp embedding bằng word similarity hoặc analogy. Nhanh và dễ debug nhưng chưa chắc tương quan với task thật.
- **Extrinsic evaluation**: đưa embedding vào task downstream như classification, NER, parsing. Chậm hơn nhưng đo đúng giá trị sử dụng.

Cạm bẫy: analogy tuyến tính đẹp không có nghĩa là embedding hiểu ngôn ngữ như con người; nó chỉ cho thấy một số quan hệ được mã hoá tương đối tuyến tính.

## Cách hiểu bằng lời của tôi

Một từ không có nghĩa tuyệt đối trong vector. Nó có vị trí tương đối so với các từ khác. Nếu training bắt model liên tục dự đoán context, vector buộc phải gom những từ có vai trò/ngữ cảnh giống nhau lại gần nhau. Đây là bước chuyển quan trọng: NLP không còn nhìn từ như nhãn rời rạc, mà như điểm trong không gian có hình học.

## Câu hỏi review

1. Vì sao one-hot vector không biểu diễn được độ gần nghĩa giữa hai từ?
2. Skip-gram học từ center word và context word như thế nào?
3. Dot product trong word2vec có ý nghĩa gì?
4. Intrinsic evaluation khác extrinsic evaluation ở điểm nào?
5. Vì sao word analogy không đủ để kết luận embedding tốt?

## Gợi ý trả lời

1. Vì mọi vector one-hot khác nhau đều trực giao, khoảng cách không phản ánh nghĩa.
2. Tạo cặp từ trung tâm và từ xung quanh; tối ưu xác suất context thật cao hơn context sai.
3. Đo mức tương thích giữa hai vector trong mô hình dự đoán context.
4. Intrinsic đo thuộc tính trung gian; extrinsic đo hiệu quả trong task thật.
5. Analogy chỉ kiểm tra một loại quan hệ tuyến tính, không bao phủ toàn bộ năng lực ngôn ngữ.

## Liên kết

- [[Embedding]]
- [[Tokenization]]
- [[Loss Function]]
- [[NLP]]
- [[CS224N]]
