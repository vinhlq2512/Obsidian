---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
source_sections:
  - "[[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - fine-tuning
  - classification
  - nlp
---

# Classifier Fine-Tuning

## Định nghĩa

Classifier fine-tuning là quá trình tiếp tục huấn luyện pretrained model trên dữ liệu có nhãn để học mapping từ input text sang label.

Trong Chapter 09, đây là bước xảy ra sau khi đã có một lượng labeled examples đủ dùng hoặc sau khi đã làm [[Language Model Fine-Tuning]] để thích nghi domain.

## Khác với language model fine-tuning

| Loại fine-tuning | Dữ liệu | Objective | Mục tiêu |
|---|---|---|---|
| [[Language Model Fine-Tuning]] | Unlabeled domain text | Language modeling objective | Học ngôn ngữ/domain |
| Classifier fine-tuning | Text + label | Classification loss | Học decision boundary giữa các label |

Mental model:

```text
Pretrained model
-> Domain-adapted model nếu cần
-> Classification head / classifier objective
-> Predict label cho text mới
```

## Khi áp dụng

Classifier fine-tuning hợp lý khi:

- đã có một tập nhãn đủ sạch để học thật;
- taxonomy label tương đối ổn định;
- baseline zero-shot/embedding lookup cho thấy vẫn cần decision boundary rõ hơn;
- có validation set để theo dõi overfitting.

## Vì sao vẫn cần trong few-shot setting

Few-shot không có nghĩa là bỏ fine-tuning hoàn toàn. Khi có một số ít ví dụ nhưng đủ đại diện, classifier fine-tuning có thể giúp model học ranh giới label cụ thể hơn zero-shot hoặc nearest-neighbor.

Nhưng với rất ít nhãn, rủi ro lớn là:

- overfit vào vài ví dụ;
- học nhầm từ label noise;
- metric dao động mạnh vì validation nhỏ;
- classifier mạnh trên train slice nhưng kém trên câu thật ngoài distribution.

## Pipeline trực giác

```text
Labeled examples
-> Tokenize / encode text
-> Pretrained encoder
-> Classification head
-> Cross-entropy hoặc classification loss
-> Cập nhật trọng số
```

Nếu đã có [[Language Model Fine-Tuning]], encoder bước vào classifier fine-tuning với representation hợp domain hơn.

## Cách hiểu bằng lời của tôi

Classifier fine-tuning là lúc model học trả lời đúng nhãn mình cần, chứ không chỉ quen với cách domain nói chuyện. Nếu language model fine-tuning là "đọc thêm tài liệu nội bộ", thì classifier fine-tuning là "làm bài tập có đáp án".

## Câu hỏi review

1. Classifier fine-tuning khác language model fine-tuning ở đâu?
2. Khi nào nên dùng classifier fine-tuning thay vì dừng ở zero-shot?
3. Vì sao classifier fine-tuning trong few-shot setting dễ overfit?
4. Vai trò của validation set trong classifier fine-tuning là gì?

## Liên kết

- [[Fine-tuning]]
- [[Language Model Fine-Tuning]]
- [[Text Classification]]
- [[Intent Detection]]
- [[Few-shot Learning]]
- [[Domain Adaptation]]
- [[NLP Transformers - Chapter 09 - Dealing with Few to No Labels]]
