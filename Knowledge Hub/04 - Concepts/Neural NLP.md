---
type: concept
status: developing
sources:
  - "[[2011 - Natural Language Processing Almost from Scratch - JMLR]]"
  - "[[CS224N 2026 - Lecture 03 - Neural Network Foundations]]"
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[2011 - Natural Language Processing Almost from Scratch - JMLR]]"
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
first_seen: 2026-08-03
last_updated: 2026-08-10
tags:
  - concept
  - nlp
  - cs224n
---

# Neural NLP

## Định nghĩa

Neural NLP là hướng xây hệ thống NLP bằng neural networks học representation từ dữ liệu, thay vì dựa chủ yếu vào feature engineering thủ công cho từng task.

## Cách hiểu bằng lời của tôi

Thay vì con người phải viết feature như "token này viết hoa", "từ này có suffix X", "dependency path là Y", neural NLP để model học các biểu diễn trung gian hữu ích qua training objective.

## Cần biết

- Bước đầu của neural NLP dùng embeddings và task-specific architectures.
- Pretrained [[Transformer]] sau này mở rộng cùng ý tưởng: học representation chung ở scale lớn.
- Neural NLP không xoá nhu cầu thiết kế hệ thống; nó chuyển phần lớn thiết kế sang architecture, objective, data và evaluation.

## Trong text classification

```text
Raw text
-> tokenizer
-> padded word-index sequence
-> embedding layer
-> CNN / RNN-LSTM / pretrained language model
-> classification output
```

- Practical NLP dùng text classification để cho thấy neural model vẫn cần input pipeline rõ ràng: tokenization, padding, embedding matrix/layer và label encoding.
- CNN cho text có thể học các feature hữu ích kiểu n-gram qua convolution/pooling, thay vì dùng toàn bộ sparse feature set như [[Bag of Words]].
- [[LSTM]] tận dụng tính tuần tự của language, nhưng thường train lâu hơn và cần nhiều dữ liệu hơn CNN.
- Fine-tuning pretrained language model như BERT là một hướng neural khác: bắt đầu từ representation đã pretrained rồi điều chỉnh cho dataset classification cụ thể.
- Trade-off quan trọng: deep text classifiers có thể mạnh hơn, nhưng phụ thuộc mạnh vào dataset, hyperparameter tuning, compute và deployment cost. Vì vậy baseline như [[Naive Bayes Classifier]], [[Logistic Regression]] hoặc [[Support Vector Machine]] vẫn có giá trị thực tế.

## Liên kết

- [[Embedding]]
- [[Transformer]]
- [[Representation Model]]
- [[Text Classification]]
- [[GloVe]]
- [[LSTM]]
- [[CS224N]]
