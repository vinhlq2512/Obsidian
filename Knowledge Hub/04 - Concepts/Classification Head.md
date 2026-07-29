---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 02 - Text Classification]]"
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
tags:
  - concept
  - nlp
  - transformer
  - classification
---

# Classification Head

## Định nghĩa

Classification head là layer hoặc cụm layer đặt phía trên pretrained Transformer để biến representation của model thành logits cho các class cần dự đoán.

## Cách hiểu bằng lời của tôi

Pretrained Transformer giống một encoder tạo representation giàu ngữ cảnh. Nhưng representation đó chưa phải nhãn cuối cùng. Classification head là phần "đọc" representation này và đưa ra điểm số cho từng nhãn.

Với BERT-style sequence classification, thường lấy vector của token `[CLS]` làm representation cấp câu, rồi đưa qua classification head.

Mental model:

```text
input text
-> tokenizer
-> Transformer encoder
-> [CLS] hidden state
-> classification head
-> logits
-> softmax
-> predicted label
```

## Công thức trực giác

Nếu $h_{\text{CLS}}$ là hidden state của token `[CLS]`, classification head đơn giản có thể là một linear layer:

$$
z = Wh_{\text{CLS}} + b
$$

Trong đó:

- $h_{\text{CLS}}$ là vector đại diện cho toàn sequence.
- $W$ và $b$ là tham số của classification head.
- $z$ là logits, mỗi chiều tương ứng với một class.

Sau đó softmax biến logits thành phân phối xác suất:

$$
p(y \mid x) = \text{softmax}(z)
$$

## Adding a Classification Head

Khi dùng pretrained checkpoint cho task classification, phần encoder đã học representation tổng quát từ pretraining. Classification head thường được thêm mới cho task cụ thể, ví dụ phân loại cảm xúc, phân loại chủ đề hoặc sentiment analysis.

Điểm quan trọng:

- Classification head mới thêm thường có weights khởi tạo ngẫu nhiên.
- Khi fine-tuning, model học cả head mới và có thể cập nhật cả encoder.
- Cảnh báo kiểu "some weights were not initialized" khi load `AutoModelForSequenceClassification` là bình thường nếu head mới chưa có pretrained weights.
- `num_labels` quyết định số logits đầu ra của head.

## First token, dropout và linear layer

Trong BERT/DistilBERT-style models, input thường có một token đặc biệt ở đầu sequence, ví dụ `[CLS]`. Sau khi đi qua nhiều Transformer layers, hidden state ở vị trí đầu tiên này không chỉ chứa thông tin của riêng token `[CLS]`; nhờ bidirectional self-attention, nó đã nhận thông tin từ toàn bộ sequence.

Vì vậy với sequence classification, ta thường dùng hidden state của first token làm representation cấp câu:

```python
first_token_hidden_state = last_hidden_state[:, 0]
```

Sau đó gắn thêm classification head đơn giản:

```text
first token hidden state
-> dropout
-> linear layer
-> logits
```

Cách hiểu từng bước:

- **First token hidden state**: vector đại diện cho toàn câu/sequence sau khi encoder đã contextualize.
- **Dropout**: tắt ngẫu nhiên một phần chiều của vector trong lúc training để model không phụ thuộc quá mạnh vào vài feature cụ thể.
- **Linear layer**: chiếu vector hidden size, ví dụ 768 chiều, sang số class cần dự đoán.

Ví dụ nếu `hidden_dim = 768` và có 6 emotion labels:

```text
[batch_size, 768]
-> dropout
-> linear layer 768 -> 6
-> logits [batch_size, 6]
```

Điểm dễ nhầm: "first token is used for prediction" không có nghĩa là model chỉ đọc token đầu tiên của câu. Nó dùng **hidden state ở vị trí đầu tiên sau Transformer**, và hidden state này đã trộn thông tin từ toàn bộ input qua attention.

## Feature extraction và fine-tuning

- **Feature extraction**: đóng băng Transformer, lấy hidden state như feature, rồi train classifier riêng. Nhanh và nhẹ, nhưng representation không thích nghi sâu với task.
- **Fine-tuning**: train Transformer cùng classification head end-to-end. Tốn compute hơn, nhưng thường tốt hơn vì representation được điều chỉnh theo loss của task.

## Cần biết

- Classification head không thay thế Transformer; nó là tầng ra quyết định đặt trên representation của Transformer.
- Với sequence classification, `[CLS]` thường được dùng vì nó có thể nhận thông tin từ toàn sequence qua bidirectional attention.
- Dropout trong classification head là regularization: nó giúp giảm overfitting khi fine-tuning.
- Linear layer cuối cùng biến hidden state thành logits có kích thước bằng số class.
- Với token classification như NER, classification head thường áp dụng lên hidden state của từng token, không chỉ `[CLS]`.
- Logits chưa phải xác suất; cần softmax cho single-label classification hoặc sigmoid cho multi-label classification.
- Classification head có thể rất đơn giản, nhưng chất lượng vẫn phụ thuộc mạnh vào representation bên dưới và dữ liệu fine-tuning.

## Khi áp dụng

- Dùng classification head khi task cần chọn nhãn rời rạc từ input text.
- Khi số class thay đổi, cần tạo head mới với `num_labels` tương ứng.
- Khi debug model classification, kiểm tra cả encoder representation, head initialization, label mapping và loss function.

## Câu hỏi review

1. Classification head làm gì trong Transformer classifier?
2. Vì sao BERT-style classifier thường dùng hidden state của `[CLS]`?
3. Logits khác xác suất ở đâu?
4. Vì sao classification head mới thêm thường cần fine-tuning?
5. Classification head trong sequence classification khác token classification thế nào?
6. Vì sao nói dùng first token để prediction không có nghĩa là model chỉ đọc token đầu tiên?
7. Dropout trong classification head có vai trò gì?

## Gợi ý trả lời câu hỏi review

1. Nó biến representation của Transformer thành logits cho từng class.
2. Vì `[CLS]` có thể nhận thông tin từ toàn sequence qua bidirectional attention và được dùng như vector đại diện cấp câu.
3. Logits là điểm số thô chưa chuẩn hóa; xác suất thường được tạo bằng softmax hoặc sigmoid.
4. Vì head mới thường được khởi tạo ngẫu nhiên và chưa biết mapping từ representation sang nhãn của task.
5. Sequence classification thường dùng một vector cấp câu như `[CLS]`; token classification dự đoán nhãn cho từng token hidden state.
6. Vì first token hidden state sau Transformer đã nhận thông tin từ toàn sequence qua self-attention.
7. Dropout tắt ngẫu nhiên một phần feature trong training để giảm overfitting và buộc head không phụ thuộc quá mức vào vài chiều cụ thể.

## Liên kết

- [[Text Classification]]
- [[Fine-tuning]]
- [[Transformer]]
- [[Bidirectional Attention]]
- [[NLP Transformers - Chapter 02 - Text Classification]]
- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
