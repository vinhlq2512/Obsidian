---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: planned
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
- Support Vector Machine
- [[Class Imbalance]]
- [[Confusion Matrix]]
- fastText
- LIME
- Active Learning
- Domain Adaptation

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
-> SVM với class_weight="balanced"
-> so sánh lỗi theo class
```

- **[[Naive Bayes Classifier]]** là baseline xác suất đơn giản. Với feature space quá lớn và sparse, model dễ bị nhiễu; giảm số feature có thể làm average score giảm nhưng cải thiện class quan trọng hơn.
- **[[Logistic Regression]]** học trọng số cho từng feature và có thể dùng `class_weight="balanced"` để tăng trọng số cho class ít mẫu. Đây là cách xử lý imbalance ngay trong classifier.
- **SVM** tìm hyperplane tách lớp với margin lớn. Nó có thể tốt hơn Logistic Regression cho một số class nhưng thường tốn thời gian train hơn, nên số feature cũng cần được kiểm soát.

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
- BoW tạo feature vector dễ dùng cho [[Naive Bayes Classifier]], [[Logistic Regression]] và SVM, nhưng số chiều có thể rất lớn. Ví dụ ban đầu sinh hơn 45,000 feature.
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

## Gợi ý trả lời câu hỏi review

- So sánh baseline cổ điển với pretrained model bằng chi phí dữ liệu, tốc độ, khả năng giải thích và maintenance.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Text Classification]]
- [[Bag of Words]]
- [[Naive Bayes Classifier]]
- [[Confusion Matrix]]
- [[Logistic Regression]]
- [[NLP Pipeline]]
- [[Text Representation]]
- [[Class Imbalance]]
