---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 04 - Text Classification]]"
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
  - "[[Practical Natural Language Processing]]"
source_sections:
  - "[[Practical NLP - Chapter 04 - Text Classification]]"
last_updated: 2026-08-11
tags:
  - concept
  - classification
  - nlp
---

# Text Classification

## Định nghĩa

Text classification là tác vụ gán một hoặc nhiều nhãn cho văn bản.

## Cách hiểu bằng lời của tôi

Đầu vào là text, đầu ra là label. Có thể làm bằng classic ML, representation model, embedding classifier hoặc generative model.

Trong sản phẩm thật, text classification không phải chỉ là chọn model. Nó là một pipeline: định nghĩa label, lấy dữ liệu đại diện, biến text thành vector, train classifier, đo lỗi, rồi mới deploy và monitor.

## Cần biết

- Nếu có dữ liệu nhãn tốt, supervised model thường ổn định.
- Nếu thiếu nhãn, có thể thử zero-shot hoặc few-shot prompting.
- Cần baseline đơn giản để biết LLM có thật sự cần thiết không.
- [[Intent Detection]] là một case study của text classification trong đó nhãn là ý định của người dùng.
- Khi đã có labeled examples đủ dùng, [[Classifier Fine-Tuning]] giúp model học decision boundary rõ hơn zero-shot hoặc nearest-neighbor.
- Pipeline supervised cơ bản: labeled data -> train/validation/test split + metric -> [[Text Representation|feature vector]] -> classifier -> evaluation -> deployment/monitoring.
- Metric cần khớp với lỗi quan trọng của use case. Accuracy có thể gây ảo giác nếu class imbalance mạnh; nên nhìn thêm precision, recall, F1 và [[Confusion Matrix|confusion matrix]] khi phù hợp.
- Rule/lexicon/API có sẵn có thể là baseline hoặc MVP tốt trước khi tự train, nhất là khi task generic hoặc cần kiểm chứng nhanh giá trị business.
- Không có classifier tốt nhất cho mọi dataset. Với cùng một pipeline, cần thử nhiều tổ hợp representation + classifier + hyperparameter rồi đọc lỗi theo từng class.
- Khi classifier kém, đừng chỉ đổi model. Cần kiểm tra feature quá sparse, [[Class Imbalance]], preprocessing/feature extraction, algorithm choice và hyperparameter.
- [[Naive Bayes Classifier]] là baseline cổ điển tốt cho text classification vì chạy nhanh trên sparse features như [[Bag of Words]] và giúp mình có mốc so sánh trước khi dùng model phức tạp hơn.
- [[Logistic Regression]] là baseline tuyến tính phổ biến: nó học weight cho từng feature và có thể dùng class weighting khi dữ liệu bị lệch class.
- [[Support Vector Machine]] là classifier cổ điển đáng thử khi muốn tìm ranh giới tách lớp có margin lớn, nhưng cần chú ý thời gian train khi feature space lớn.
- Với deep learning, pipeline không biến mất: raw text vẫn cần tokenize thành word index, pad sequence, map sang [[Embedding|embedding vectors]], rồi mới đưa vào CNN, [[LSTM]] hoặc pretrained language model như BERT.
- Deep classifier thường có embedding/input layer, hidden layers và classification output như softmax. Nó có thể học representation tốt hơn, nhưng cần nhiều dữ liệu task-specific hơn và tốn compute/deployment hơn baseline cổ điển.
- Khi chưa có training data, bước đầu tiên là tạo annotated dataset ban đầu: gán nhãn thủ công một phần dữ liệu, dùng [[Weak Supervision|weak supervision]] bằng rule/pattern, hoặc crowdsourcing nếu cần quy mô lớn.
- Nhãn tạo bằng rule hoặc crowd có thể nhiễu, nên cần evaluation set đáng tin trước khi dùng để quyết định classifier có tốt thật không.
- Case study [[Ticket Routing]] trong Practical NLP cho thấy một classifier production thường bắt đầu bằng baseline rẻ như API/library, public dataset hoặc weak supervision, rồi học tiếp từ feedback thật sau deploy.
- Practical NLP khuyên bắt đầu bằng strong baseline/MVP trước khi dùng state-of-the-art model, vì baseline giúp hiểu problem, lấy feedback sớm và tránh technical debt không đáng.
- Trong production, classifier có thể kết hợp model outputs, domain rules, human fallback và [[Ensemble Learning|ensembling]] thay vì đặt toàn bộ quyết định vào một model.

## Liên kết

- [[Intent Detection]]
- [[Few-shot Learning]]
- [[Zero-shot Classification]]
- [[Classifier Fine-Tuning]]
- [[Representation Model]]
- [[Generative Model]]
- [[Embedding]]
- [[Fine-tuning]]
- [[NLP Pipeline]]
- [[Text Representation]]
- [[Class Imbalance]]
- [[Naive Bayes Classifier]]
- [[Confusion Matrix]]
- [[Logistic Regression]]
- [[Support Vector Machine]]
- [[Neural NLP]]
- [[LSTM]]
- [[Weak Supervision]]
- [[Semi-supervised Learning]]
- [[Active Learning]]
- [[Domain Adaptation]]
- [[Ticket Routing]]
- [[Ensemble Learning]]
