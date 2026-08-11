---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: completed
chapter: 4
start_page: 249
end_page: 291
reading_date: 2026-08-04
planned_sessions:
  - "2026-08-04 | 249-263 | Ứng dụng, pipeline, classifier cơ bản | 55 phút"
  - "2026-08-05 | 264-278 | SVM, neural embeddings, deep classification | 55 phút"
  - "2026-08-06 | 279-291 | Interpretability, low-data setting, case study | 55 phút"
tags:
  - nlp
  - practical-nlp
  - text-classification
---

# Practical NLP - Chapter 04 - Text Classification

## Mục tiêu cần hiểu

- Pipeline để xây hệ thống [[Text Classification]].
- Vai trò của classifier cổ điển, neural embeddings và large pretrained language models.
- Cách nghĩ về interpretability, active learning và domain adaptation.

## Định nghĩa quan trọng

- [[Text Classification]]
- [[Bag of Words]]
- [[Naive Bayes Classifier]]
- [[Logistic Regression]]
- [[Support Vector Machine]]
- [[Class Imbalance]]
- [[Confusion Matrix]]
- fastText
- [[Embedding]]
- [[Word2Vec]]
- [[Document Embedding]]
- [[Neural NLP]]
- [[GloVe]]
- [[LSTM]]
- LIME
- Active Learning
- Domain Adaptation
- [[Weak Supervision]]
- [[Ticket Routing]]
- [[Ensemble Learning]]

## Mental model

```text
Text
-> labeled dataset phù hợp task
-> train / validation / test split
-> feature representation
-> classifier
-> evaluation
-> deployment / monitoring
```

## Phần cần biết

- Text classification là task nền cho nhiều sản phẩm: ticket routing, spam detection, sentiment, intent.
- Khi ít dữ liệu, chất lượng label space và evaluation set nhỏ thường quan trọng hơn model lớn.
- Pipeline trong chapter này là supervised ML pipeline: thu thập hoặc tạo dữ liệu có nhãn, chia dữ liệu, chuyển text thành feature vector, train classifier, benchmark bằng metric, rồi deploy và monitor.
- Vòng lặp quan trọng nằm ở feature representation, classification algorithm, parameter/hyperparameter và evaluation. Chưa nên nhảy thẳng tới deploy khi chưa thử đủ biến thể và hiểu lỗi.

## A Pipeline for Building Text Classification Systems

### Các bước chính

```text
Labeled data
-> train / validation / test split + metric
-> raw text thành feature vector
-> train classifier bằng feature + label
-> benchmark trên test set
-> deploy và monitor trong use case thật
```

- Bước 1-2 dựa nhiều vào [[NLP Pipeline]] và chất lượng dữ liệu: dataset phải phù hợp task và nên đại diện cho dữ liệu sẽ gặp trong production.
- Bước 3 nối trực tiếp với [[Text Representation]]: cách biến text thành vector quyết định model nhìn thấy tín hiệu nào.
- Bước 4-5 là trọng tâm của chapter: so sánh classifier bằng metric như accuracy, precision, recall, F1, ROC-AUC và [[Confusion Matrix|confusion matrix]].
- Bước 6 thuộc bài toán sản phẩm: sau khi deploy cần monitor performance, vì metric offline chưa chắc phản ánh đầy đủ tác động business.

### Khi không cần full pipeline

- Nếu cần MVP nhanh hoặc bài toán có tín hiệu lexical rõ, rule hoặc lexicon-based classifier có thể tạo baseline trước khi dùng ML.
- Nếu task rất generic, ví dụ sentiment analysis hoặc content category, API có sẵn có thể đủ tốt về chi phí và thời gian.
- Nếu task phụ thuộc nghiệp vụ riêng của tổ chức, full supervised pipeline vẫn cần thiết vì API chung khó biết label space và dữ liệu nội bộ.

## One Pipeline, Many Classifiers

### Ý chính

- Phần này giữ cùng một supervised pipeline nhưng thay đổi bước 3-5: cách biểu diễn text, classifier, parameter/hyperparameter và cách đọc evaluation.
- Dataset minh họa là binary classification cho economic news: relevant vs non-relevant. Dataset bị [[Class Imbalance]], nên đoán tất cả là non-relevant đã có accuracy cao giả tạo.
- Vì vậy, cần đọc [[Confusion Matrix|confusion matrix]] theo từng class thay vì chỉ nhìn average accuracy.

### Các biến thể được thử

```text
Economic news text
-> [[Bag of Words]] / CountVectorizer
-> [[Naive Bayes Classifier]]
-> [[Confusion Matrix|confusion matrix]]
-> giảm số feature để bớt sparsity
-> [[Logistic Regression]] với class_weight="balanced"
-> [[Support Vector Machine|SVM]] với class_weight="balanced"
-> so sánh lỗi theo class
```

- **[[Naive Bayes Classifier]]** là baseline xác suất đơn giản. Với feature space quá lớn và sparse, model dễ bị nhiễu; giảm số feature có thể làm average score giảm nhưng cải thiện class quan trọng hơn.
- **[[Logistic Regression]]** học trọng số cho từng feature và có thể dùng `class_weight="balanced"` để tăng trọng số cho class ít mẫu. Đây là cách xử lý imbalance ngay trong classifier.
- **[[Support Vector Machine|SVM]]** tìm hyperplane tách lớp với margin lớn. Nó có thể tốt hơn Logistic Regression cho một số class nhưng thường tốn thời gian train hơn, nên số feature cũng cần được kiểm soát.

### Naive Bayes Classifier

```text
Document-term vector
-> ước lượng xác suất feature theo từng class
-> kết hợp xác suất các feature cho mỗi class
-> chọn class có xác suất lớn nhất
```

- Sách dùng `MultinomialNB` của scikit-learn với feature vector từ `CountVectorizer`.
- Naive Bayes là classifier xác suất và thường được dùng làm baseline trong text classification vì đơn giản, nhanh và dễ so sánh.
- Trong dataset economic news, Naive Bayes nhận diện non-relevant tốt hơn relevant: non-relevant sai ít, nhưng relevant chỉ được bắt đúng khoảng 42%.
- Khi giảm số feature, average score có thể thấp hơn nhưng relevant class được cải thiện mạnh hơn. Vì vậy phải đọc confusion matrix theo mục tiêu use case, không chỉ nhìn accuracy.

### Logistic Regression

```text
Document-term vector
-> học weight cho từng feature
-> học linear separator giữa các class
-> dự đoán xác suất / class
```

- Sách đặt Logistic Regression đối lập với Naive Bayes: Naive Bayes là generative classifier, còn Logistic Regression là discriminative classifier.
- Logistic Regression không chỉ đếm feature theo class; nó học weight cho feature dựa trên mức độ feature đó giúp quyết định class.
- Trong ví dụ, model dùng lại feature vector 5,000 chiều và gọi `LogisticRegression(class_weight="balanced")`.
- `class_weight="balanced"` tăng trọng số cho class ít mẫu theo tỷ lệ ngược với số sample, giúp giảm tác động của [[Class Imbalance]].
- Kết quả trong ví dụ là accuracy khoảng 73.7% và vẫn kém Naive Bayes trên dataset này. Điều này củng cố bài học: không có algorithm nào tốt nhất cho mọi dataset.

### Support Vector Machine

```text
Document-term vector
-> tìm hyperplane tách lớp
-> tối đa hóa margin giữa các class
-> dự đoán class
```

- SVM là discriminative classifier giống Logistic Regression, nhưng mục tiêu của nó là tìm hyperplane tách class với margin lớn nhất có thể.
- Sách nhắc SVM có thể học cả non-linear separation, nhưng đổi lại thường train lâu hơn.
- Trong ví dụ, sách dùng `LinearSVC(class_weight="balanced")` và giảm `max_features` xuống 1,000 để kiểm soát thời gian train.
- SVM cải thiện relevant class so với Logistic Regression trong thử nghiệm này, nhưng Naive Bayes với feature set nhỏ vẫn tốt nhất trong nhóm thử nghiệm nhỏ.
- Bài học: SVM là một classifier đáng thử trong pipeline, nhưng không thay thế việc đọc [[Confusion Matrix]] và kiểm soát feature sparsity.

## Using Neural Embeddings in Text Classification

### Word Embeddings

```text
Text
-> tokenize / preprocess
-> lookup pretrained word vectors
-> average word vectors
-> sentence-level feature vector
-> classifier
```

- Phần này chuyển từ sparse high-dimensional features như [[Bag of Words]] sang dense low-dimensional features từ [[Embedding|word embeddings]].
- Sách dùng pretrained [[Word2Vec]] Google News model qua `gensim`. Model hoạt động như dictionary: word -> learned vector.
- Cách feature engineering đơn giản: lấy embedding của từng token có trong model, cộng lại, rồi chia trung bình để tạo một vector 300 chiều cho toàn bộ text.
- Nếu token không có trong pretrained vocabulary, ví dụ OOV word, đoạn code bỏ qua token đó.
- Khi dùng averaged Word2Vec features với Logistic Regression trên sentiment sentences dataset, sách báo accuracy khoảng 81%. Đây là baseline tốt vì chưa cần train embedding mới.

### Khi dùng pretrained word embeddings

- Nếu vocabulary của domain mới overlap tốt với pretrained embedding vocabulary, pretrained embeddings thường hữu ích.
- Rule of thumb trong sách: nếu vocabulary overlap lớn hơn 80%, pretrained word embeddings thường cho kết quả tốt trong text classification.
- Nếu domain vocabulary khác mạnh, nên cân nhắc train embedding riêng.
- Trade-off deployment: pretrained model có thể rất lớn; ví dụ model trong sách khoảng 3.6GB, nên memory/load time là ràng buộc thật.

### Document Embeddings

```text
Document / sentence / paragraph
-> tokenize + tag document
-> train Doc2Vec
-> infer document vector
-> classifier
```

- [[Document Embedding]] học representation trực tiếp cho toàn bộ document, thay vì học word/character vectors rồi gom lại thành text representation.
- Sách dùng Doc2Vec cho tweet emotion classification với ba label phổ biến: neutral, worry, happiness.
- Tweets cần preprocessing riêng vì ngắn, nhiều spelling/syntax biến dạng, emoticon, hashtag và handle. Ví dụ dùng `TweetTokenizer(strip_handles=True, preserve_case=False)`.
- Dữ liệu được đưa vào `TaggedDocument`, rồi train `Doc2Vec(vector_size=50, alpha=0.025, min_count=10, dm=1, epochs=100)`.
- `dm` là distributed memory; sách cũng nhắc biến thể còn lại là `dbow`, tức distributed bag of words.
- Khi dùng model đã train, `infer_vector(..., steps=50)` tạo vector cho text mới; chạy nhiều steps giúp representation ổn định hơn.
- Kết quả trong ví dụ khá kém: F1 khoảng 0.51 trên 3 class. Nguyên nhân có thể đến từ tweet quá ngắn/nhiễu, tokenizer/feature chưa hợp, hoặc hyperparameter chưa tốt.
- Trade-off deployment: phải lưu model representation đã học. Doc2Vec thường không cồng kềnh như fastText nhưng cũng không nhanh bằng fastText.

## Deep Learning for Text Classification

### Input pipeline cho neural classifier

```text
Raw text
-> tokenize thành word index
-> pad sequence về cùng độ dài
-> map index sang embedding vector
-> CNN / RNN-LSTM / pretrained language model
-> softmax / classification output
```

- Deep learning ở đây là nhóm model học qua multilayered neural network architectures, thay vì chỉ train classifier cổ điển trên feature vector dựng sẵn.
- Hai architecture phổ biến sách nêu cho text classification là CNN và RNN; [[LSTM]] là dạng RNN phổ biến. Sách cũng nhắc hướng fine-tune large pretrained language model như BERT cho dataset cụ thể.
- Trước khi train neural network, text phải được đưa về dạng input layer xử lý được: token index vectors, padded sequences và embedding vectors.
- Với Keras, sách dùng `Tokenizer(num_words=MAX_NUM_WORDS)`, fit tokenizer trên train texts, rồi dùng tokenizer đó để convert cả train/test texts thành sequences.
- `pad_sequences(maxlen=MAX_SEQUENCE_LENGTH)` làm mọi input có cùng độ dài; label được chuyển thành categorical vectors bằng `to_categorical`.
- Nếu dùng pretrained [[GloVe]] embeddings, cần đọc file như `glove.6B.100d.txt`, tạo `embeddings_index`, rồi dựng `embedding_matrix` khớp với `word_index` của tokenizer.
- Dimensionality của embedding là hyperparameter. Ví dụ trong sách chọn GloVe 100 chiều, nhưng có thể thử kích thước khác.

### Embedding layer và output layer

```text
word index
-> embedding matrix / Embedding layer
-> hidden layers
-> Dense / softmax
-> class probabilities
```

- Input layer cho textual input thường là embedding layer.
- Nếu muốn train embedding trên chính corpus, có thể dùng Keras `Embedding` layer.
- Nếu muốn dùng pretrained embeddings, sách tạo custom embedding layer từ `embedding_matrix` và đặt `trainable=False`.
- Output layer trong multiclass text classification thường là softmax với categorical output.

### CNN, LSTM và pretrained language model

- CNN cho text dùng convolution/pooling layers. Sách diễn giải CNN như cách học những feature hữu ích kiểu bag-of-words/n-grams, thay vì đưa toàn bộ collection words/n-grams vào classifier.
- Ví dụ CNN trong sách dùng nhiều `Conv1D`, `MaxPooling1D`, `GlobalMaxPooling1D`, `Dense`, loss `categorical_crossentropy`, optimizer `rmsprop` và metric accuracy.
- Khi train embedding layer trực tiếp trên dataset thay vì dùng pretrained embedding, ví dụ CNN trong notebook có thể cho test classification tốt hơn; nhưng nếu training data ít, pretrained embeddings hoặc domain adaptation có thể hợp lý hơn.
- Với pretrained language model như BERT, workflow là preprocess theo yêu cầu của model rồi fine-tune model cho classification task.

### LSTMs for Text Classification

```text
Padded token sequence
-> Embedding(MAX_NUM_WORDS, 128)
-> LSTM(128, dropout=0.2, recurrent_dropout=0.2)
-> Dense(2, activation="sigmoid")
-> binary_crossentropy + adam
-> accuracy / test evaluation
```

- Sách đặt [[LSTM]] trong nhóm RNN vì ngôn ngữ có tính tuần tự: word hiện tại phụ thuộc vào context trước/sau, còn CNN cơ bản không trực tiếp tận dụng quan hệ tuần tự này.
- Khi đã có input pipeline và embedding layer, chuyển từ CNN sang LSTM trong ví dụ khá cơ học: thay convolution/pooling layers bằng một LSTM layer.
- Ví dụ dùng `Embedding(MAX_NUM_WORDS, 128)` và train embedding layer ngay trên dataset, thay vì dùng pretrained embedding matrix.
- Output dùng `Dense(2, activation="sigmoid")` với `binary_crossentropy` vì ví dụ IMDB là binary sentiment classification.
- Notebook cho thấy LSTM chạy lâu hơn CNN. Sách cảnh báo không nên đọc performance thấp hơn như bằng chứng LSTM kém; có thể dữ liệu chưa đủ lớn để khai thác capacity của LSTM.
- Kết luận thực dụng: LSTM đáng thử khi thứ tự token/context là tín hiệu quan trọng, nhưng cần cân bằng với training time, lượng data và hyperparameter tuning.

### Trade-off thực dụng

- Deep model thêm nhiều lựa chọn cần tuning: activation, hidden layers, layer size, loss, optimizer, metric, epoch và batch size.
- Không có cấu hình neural architecture tốt nhất cho mọi dataset; cần thử nghiệm và so sánh như các classifier trước đó.
- Sách nhấn mạnh deep text classifier phụ thuộc mạnh vào training dataset. Nếu data task-specific ít hoặc compute/deployment cost cao, non-DL baselines vẫn rất đáng dùng trong industry.

### Confusion matrix trong ví dụ

```text
Actual class
-> Predicted class
-> số mẫu đúng/sai cho từng cặp class
-> đọc lỗi theo class
```

- Confusion matrix cho thấy classifier đúng/sai ở từng class, thay vì gộp mọi thứ thành một điểm accuracy.
- Với dataset imbalanced, matrix làm lộ việc model có thể tốt ở non-relevant nhưng yếu ở relevant.
- Trong ví dụ Naive Bayes, non-relevant được nhận diện khá tốt, nhưng relevant chỉ đúng khoảng 42%; sau khi giảm số feature, relevant class tăng hơn 20% dù average score thấp hơn.
- Vì vậy, câu hỏi không chỉ là “model có accuracy bao nhiêu?”, mà là “model đang sai ở class nào, và class đó có quan trọng với use case không?”.

### BoW representation trong ví dụ

```text
Raw news text
-> clean text
-> CountVectorizer
-> document-term matrix
-> classifier
```

- Sách dùng `CountVectorizer` như implementation của [[Bag of Words]]: mỗi document được biến thành vector theo vocabulary, thường là số lần từ xuất hiện.
- Preprocessing trong ví dụ gồm lowercasing, bỏ punctuation, digit, custom strings và stop words trước khi vectorize.
- BoW tạo feature vector dễ dùng cho [[Naive Bayes Classifier]], [[Logistic Regression]] và [[Support Vector Machine|SVM]], nhưng số chiều có thể rất lớn. Ví dụ ban đầu sinh hơn 45,000 feature.
- Khi vocabulary quá rộng, vector trở nên sparse: hầu hết vị trí bằng 0, nhiều feature hiếm thành noise và classifier khó học. Giảm `max_features` xuống 5,000 là một cách kiểm soát sparsity.
- Việc giảm feature không tự động tốt hơn theo mọi metric; nó chỉ tốt nếu cải thiện đúng class hoặc lỗi mà use case quan tâm.

### Mental model quyết định

```text
Classifier performance kém
-> feature quá sparse?
-> class bị lệch?
-> algorithm chưa hợp?
-> preprocessing / feature extraction chưa tốt?
-> hyperparameter chưa ổn?
```

- Không có thuật toán nào tốt nhất cho mọi dataset. Cách làm thực tế là thử nhiều hướng, bắt đầu từ baseline đơn giản, rồi tăng độ phức tạp khi có bằng chứng.
- Mục tiêu không phải tối đa hóa một con số duy nhất, mà chọn trade-off lỗi phù hợp với use case.

## Learning with No or Less Data and Adapting to New Domains

### No Training Data

```text
Raw customer complaints
-> xác định label cần route
-> tạo annotated dataset ban đầu
-> train classifier đầu tiên
-> dùng classifier / human loop để mở rộng dữ liệu
```

- Sách chuyển từ giả định có dataset lớn sang tình huống thực tế hơn: không có training data, có quá ít training data, hoặc cần adapt classifier từ domain cũ sang domain mới.
- Ví dụ no-training-data là phân loại customer complaint emails của e-commerce vào `billing`, `delivery`, `others`.
- Nếu có historical database chứa request và category thì đó là nguồn training data tự nhiên. Nếu không có, bước đầu tiên là tạo annotated dataset.
- Cách trực tiếp: nhờ customer service agents gán nhãn thủ công một phần complaints.
- Cách rẻ hơn để khởi động: [[Weak Supervision|bootstrapping / weak supervision]]. Ta viết pattern/rule dựa trên tín hiệu dễ nhận ra, ví dụ billing có từ liên quan tới bill hoặc currency amount; delivery có từ liên quan tới shipping hoặc delay.
- Các rule này tạo ra một tập annotated nhỏ, có thể nhiễu, rồi dùng nó để train classifier đầu tiên hoặc annotate tập dữ liệu lớn hơn.
- Sách nhắc Snorkel như một công cụ triển khai weak supervision cho classification. Điểm đáng nhớ không phải tên tool, mà là tư duy: dùng nhiều labeling functions/rules để tạo nhãn khởi động khi chưa có hand-labeled dataset lớn.
- Khi cần label quy mô lớn và có thể vận hành được, crowdsourcing như Amazon Mechanical Turk hoặc Figure Eight là một lựa chọn để tạo training data.
- Cẩn thận: weak supervision và crowdsourcing không xóa nhu cầu evaluation set đáng tin. Nhãn tự động hoặc đám đông vẫn cần kiểm tra chất lượng trước khi tin model.

### Less Training Data: Active Learning and Domain Adaptation

```text
Ít labeled data
-> train classifier ban đầu
-> predict trên data mới
-> chọn điểm model không chắc chắn
-> human annotate
-> thêm vào training set
-> retrain
```

- Khi đã có một ít nhãn từ manual annotation hoặc weak supervision, dữ liệu vẫn có thể quá ít hoặc quá lệch class để train classifier tốt.
- [[Active Learning]] giúp chọn data points đáng gán nhãn nhất. Câu hỏi trung tâm là: nếu có 1,000 điểm dữ liệu nhưng chỉ đủ nguồn lực gán nhãn 100 điểm, nên chọn 100 điểm nào?
- Sách mô tả vòng lặp active learning: train với dữ liệu hiện có, dùng classifier dự đoán data mới, gửi các điểm mà model không chắc cho human annotators, thêm nhãn mới vào training set, rồi retrain.
- Trực giác: các điểm model ít tự tin thường chứa nhiều thông tin hơn cho việc cải thiện decision boundary so với các điểm quá dễ.
- Prodigy được sách nhắc như ví dụ tool hỗ trợ active learning cho text classification và tạo annotated data nhanh hơn.

```text
Source domain nhiều data
-> pretrained / source language model
-> unlabeled target-domain text
-> fine-tune LM cho target domain
-> labeled target-domain data ít
-> train classifier từ representation đã adapt
```

- [[Domain Adaptation]] xử lý tình huống có nhiều dữ liệu ở domain cũ nhưng phải chuyển classifier sang domain mới chỉ có ít labeled data.
- Text classifier thường bị bias theo vocabulary và language pattern của training data. Nếu source và target domain khác mạnh, classifier train ở source domain khó hoạt động tốt trên target domain.
- Sách gọi domain adaptation là một dạng transfer learning: chuyển thứ học được từ source domain nhiều data sang target domain ít nhãn nhưng có nhiều unlabeled data.
- Workflow trong sách: bắt đầu với pretrained language model từ source/general domain, fine-tune bằng unlabeled text của target domain, rồi train classifier trên labeled target-domain data bằng representation từ model đã fine-tune.
- ULMFit là ví dụ domain adaptation cho text classification. Sách nêu kết quả nghiên cứu: với 100 labeled examples, ULMFit có thể match train-from-scratch cần nhiều ví dụ hơn; khi dùng thêm unlabeled data để fine-tune LM, mức tiết kiệm labeled examples còn lớn hơn.
- Cẩn thận thực dụng: sách cũng nói transfer/domain adaptation chưa phải default cho mọi classification setup trong industry; vẫn cần benchmark với baseline và chi phí triển khai.

## Case Study: Corporate Ticketing

### Bài toán

```text
Corporate tickets
-> phát hiện medical-related issue
-> route tới medical counsel / hospital / team liên quan
```

- Case study dùng [[Ticket Routing|corporate ticketing]] để gom lại các lựa chọn trong chương.
- Công ty có ticket history, nhưng chưa có label `health related`. Vì vậy bài toán không bắt đầu từ train supervised classifier đầy đủ, mà bắt đầu từ cách tạo baseline khi thiếu nhãn.
- Mục tiêu không chỉ là phân loại text, mà là route ticket tới đúng người/team. Sai nhãn có tác động vận hành: ticket y tế bị bỏ sót hoặc ticket không liên quan bị gửi sai chỗ.

### Các hướng baseline

```text
No health labels
-> existing API/library
-> public dataset
-> weak supervision
-> active learning
-> feedback loop sau deploy
```

- **Use existing APIs or libraries**: dùng API/library public rồi map category của nó về taxonomy nội bộ. Ví dụ các category liên quan health/medical có thể hữu ích, nhưng không phải category nào cũng phù hợp với tổ chức.
- Mapping taxonomy là quyết định nghiệp vụ: substance abuse hoặc obesity có thể bị bỏ qua nếu không thuộc phạm vi medical counsel; insurance có thể cần route sang HR hoặc team khác.
- **Use public datasets**: dùng dataset public như 20 Newsgroups, lấy `sci.med` làm medical class và các topic còn lại làm non-medical để train baseline.
- **Utilize weak supervision**: dùng ticket history chưa có nhãn và viết rule khởi động, ví dụ ticket chứa `fever`, `diarrhea`, `headache`, `nausea` thì gán vào medical counsel category.
- **Active learning**: dùng tool như Prodigy để nhờ người ở customer service desk gán nhãn ticket descriptions theo preset categories, ưu tiên những mẫu đáng hỏi.

### Feedback sau deploy

```text
Baseline model vào production
-> explicit feedback
-> implicit feedback
-> refine model
-> active learning chọn mẫu cần label
-> thêm dữ liệu
-> model phức tạp hơn khi đủ data
```

- Explicit feedback: medical counsel hoặc hospital nói rõ ticket không relevant.
- Implicit feedback: response time, response rate hoặc biến vận hành khác có thể gợi ý route đúng/sai.
- Figure 4-11 trong sách tóm tắt pipeline: bắt đầu từ không có labeled data, dùng API/public dataset/weak supervision làm baseline, lấy feedback từ production, rồi dùng active learning để chọn instance cần gán nhãn.
- Bài học thực dụng: với custom classification problem, baseline và feedback loop quan trọng hơn việc chọn model hiện đại ngay từ đầu. Khi dữ liệu tích lũy đủ, mới đáng thử classifier sâu/phức tạp hơn.

## Practical Advice

### Establish strong baselines

- Sách cảnh báo một lỗi phổ biến là bắt đầu ngay bằng state-of-the-art algorithm, nhất là trong thời deep learning.
- Strong baseline giúp hiểu problem statement và key challenges trước khi tăng độ phức tạp.
- Baseline/MVP nhanh giúp lấy feedback sớm từ end users và stakeholders.
- Một research model hiện đại có thể chỉ cải thiện rất ít so với baseline nhưng kéo theo technical debt lớn.

### Balance training data

- Với classification, dataset cân bằng giữa các categories rất quan trọng vì [[Class Imbalance]] có thể làm classifier bias về majority class.
- Không phải lúc nào cũng kiểm soát được phân phối training data, nhưng sách nêu các hướng xử lý: thu thập thêm data, resampling và weight balancing.
- Resampling gồm undersample majority classes hoặc oversample minority classes.

### Combine models and humans in the loop

```text
Multiple model outputs
+ handcrafted domain rules
+ human fallback khi model không chắc
-> business decision đáng tin hơn
```

- Trong production, có thể kết hợp nhiều classification models với handcrafted rules từ domain experts để đạt hiệu quả business tốt hơn.
- Khi machine không chắc về classification decision, chuyển quyết định cho human evaluator là lựa chọn thực dụng.
- Sách cũng nhắc learned model có thể phải thay đổi theo thời gian và dữ liệu mới, nên cần nghĩ tới end-to-end system ở các chương sau.

### Make it work, make it better

- Xây text classification system không chỉ là xây model. Trong industrial setting, model thường chỉ là khoảng 5-10% project.
- Phần còn lại nằm ở data gathering, data pipelines, deployment, testing, monitoring và iteration.
- Cách làm được khuyên: build model nhanh, dùng nó để dựng system, rồi cải thiện dần dựa trên roadblocks thật. Nhiều khi phần cần làm nhất không phải modeling.

### Use the wisdom of many

- Không có text classification algorithm nào luôn tốt nhất; mỗi thuật toán có strengths và weaknesses riêng.
- [[Ensemble Learning|Ensembling]] là một cách giảm phụ thuộc vào một classifier: train nhiều classifiers, cho data đi qua từng model, rồi combine predictions, ví dụ majority voting.

## Câu hỏi review

1. Khi nào [[Naive Bayes Classifier]] hoặc [[Logistic Regression]] vẫn là baseline tốt?
2. Interpretability giúp phát hiện lỗi dữ liệu hay lỗi model như thế nào?
3. Active learning phù hợp khi nào?
4. Vì sao phải quyết định metric trước khi train classifier?
5. Khi nào nên dùng rule/API thay vì tự xây supervised classifier?
6. Vì sao accuracy có thể đánh lừa khi dataset bị class imbalance?
7. Khi đổi classifier mà performance vẫn kém, nên kiểm tra những phần nào của pipeline?
8. BoW representation giữ lại thông tin gì và làm mất thông tin gì?
9. Confusion matrix cho thấy điều gì mà accuracy trung bình che mất?
10. SVM khác Logistic Regression ở mục tiêu học ranh giới như thế nào?
11. Word embeddings khác BoW ở kiểu thông tin giữ lại và chi phí deployment như thế nào?
12. Document embeddings khác average word embeddings ở đơn vị representation nào?
13. Trước khi CNN/LSTM nhận text, input phải đi qua những bước nào?
14. Vì sao deep model không tự động là lựa chọn tốt nhất cho text classification trong industry?
15. Vì sao LSTM có thể hợp với text hơn CNN cơ bản, và đổi lại phải trả chi phí gì?
16. Khi chưa có training data cho text classification, có những cách nào để tạo annotated dataset ban đầu?
17. Weak supervision khác gán nhãn thủ công ở điểm nào, và rủi ro chính là gì?
18. Active learning chọn dữ liệu để gán nhãn theo tiêu chí nào?
19. Domain adaptation khác train classifier từ đầu ở target domain như thế nào?
20. Case study corporate ticketing cho thấy nên bắt đầu từ baseline và feedback loop ra sao khi chưa có label cho class mới?
21. Vì sao practical advice của chương khuyên bắt đầu bằng strong baseline thay vì state-of-the-art model?
22. Human-in-the-loop và ensemble giúp giảm rủi ro của classifier production như thế nào?

## Gợi ý trả lời câu hỏi review

1. [[Naive Bayes Classifier]] và [[Logistic Regression]] vẫn là baseline tốt khi cần model nhanh, dễ debug, ít tốn compute và dữ liệu có tín hiệu lexical rõ. Chúng cho điểm neo trước khi tăng complexity.
2. Interpretability giúp nhìn classifier đang dựa vào feature nào, class nào bị nhầm và liệu lỗi đến từ data/label/preprocessing hay model. Nó biến lỗi thành hành động sửa cụ thể.
3. [[Active Learning]] phù hợp khi có nhiều unlabeled data nhưng ngân sách gán nhãn hạn chế. Nên ưu tiên những mẫu model ít tự tin vì chúng thường giúp cải thiện decision boundary nhiều hơn mẫu dễ.
4. Metric phải được quyết định trước vì metric định nghĩa “tốt” theo chi phí lỗi của use case. Nếu chọn metric sau khi train, mình dễ tối ưu nhầm hoặc tự hợp thức hóa model.
5. Rule/API đáng thử khi cần MVP nhanh, task generic, hoặc label có tín hiệu pattern rõ. Nếu label space phụ thuộc nghiệp vụ riêng và API chung không biết domain, cần supervised pipeline riêng.
6. Accuracy đánh lừa khi [[Class Imbalance]] mạnh vì model có thể đoán majority class để đạt điểm cao nhưng bỏ sót minority class quan trọng.
7. Khi đổi classifier mà performance vẫn kém, kiểm tra feature sparsity, imbalance, preprocessing, feature extraction, algorithm choice, hyperparameter và chất lượng label.
8. [[Bag of Words]] giữ lại từ nào xuất hiện và tần suất xuất hiện, nhưng mất thứ tự, cú pháp và phần lớn ngữ cảnh.
9. [[Confusion Matrix]] cho thấy lỗi theo từng actual/predicted class, nên lộ việc model tốt ở majority class nhưng yếu ở class business quan trọng.
10. [[Support Vector Machine|SVM]] học ranh giới có margin lớn, còn Logistic Regression học weights để dự đoán xác suất/class qua linear separator. Cả hai là discriminative, nhưng objective khác nhau.
11. Word embeddings giữ tín hiệu semantic dense hơn BoW và giảm sparsity, nhưng có rủi ro OOV/domain mismatch và chi phí memory/deployment khi dùng pretrained model lớn.
12. [[Document Embedding]] học vector cho cả document/sentence/paragraph, còn average word embeddings gom vector từng word thành một đại diện thô cho text.
13. Trước CNN/LSTM, text cần tokenize thành word indices, pad về cùng độ dài, map indices sang embedding vectors, rồi mới đưa vào neural architecture.
14. Deep model không tự động tốt nhất vì cần nhiều task-specific data, tuning, compute và deployment cost; nhiều industry use case vẫn thắng bằng baseline đơn giản hơn.
15. [[LSTM]] hợp với text vì xử lý sequence và context theo thời gian, nhưng đổi lại train lâu hơn CNN và thường data-hungry hơn.
16. Khi chưa có training data, có thể tạo annotated dataset bằng manual labeling, [[Weak Supervision|weak supervision/bootstrapping]], crowdsourcing, API/library mapping hoặc public dataset phù hợp.
17. Weak supervision dùng rule/pattern/labeling functions để tạo noisy labels rẻ hơn hand-label toàn bộ. Rủi ro chính là rule bias và noisy labels làm classifier học sai.
18. Active learning chọn mẫu theo độ không chắc chắn hoặc mức hữu ích dự kiến cho model, rồi gửi human annotate.
19. [[Domain Adaptation]] tận dụng model/data từ source domain và unlabeled target-domain text để adapt trước khi train classifier bằng ít labeled target data; train từ đầu chỉ dựa vào target labels và thường cần nhiều nhãn hơn.
20. Corporate ticketing cho thấy nên bắt đầu bằng baseline rẻ như API/public dataset/weak supervision, deploy hoặc thử nhỏ, lấy explicit/implicit feedback, rồi dùng active learning để cải thiện.
21. Strong baseline giúp hiểu bài toán, lấy feedback sớm và tránh technical debt từ state-of-the-art model chỉ cải thiện nhỏ.
22. Human-in-the-loop cho phép defer các case model không chắc, còn ensemble giảm phụ thuộc vào một classifier đơn lẻ bằng cách kết hợp nhiều model/rule.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Text Classification]]
- [[Bag of Words]]
- [[Naive Bayes Classifier]]
- [[Confusion Matrix]]
- [[Logistic Regression]]
- [[Support Vector Machine]]
- [[Embedding]]
- [[Word2Vec]]
- [[Document Embedding]]
- [[Neural NLP]]
- [[GloVe]]
- [[LSTM]]
- [[Weak Supervision]]
- [[Semi-supervised Learning]]
- [[Active Learning]]
- [[Domain Adaptation]]
- [[Ticket Routing]]
- [[Ensemble Learning]]
- [[NLP Pipeline]]
- [[Text Representation]]
- [[Class Imbalance]]
