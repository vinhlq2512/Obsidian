---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 9
start_page: 286
end_page: 325
reading_date: 2026-08-05
planned_sessions:
  - "2026-08-05 | 286-305 | Baseline, ít nhãn và embedding lookup | 55 phút"
  - "2026-08-06 | 306-325 | Prompting, augmentation, unlabeled data và viết lại chiến lược | 55 phút"
estimated_minutes: 90
actual_minutes:
need_review: false
tags:
  - nlp
  - few-shot
  - weak-supervision
---

# NLP Transformers - Chapter 09 - Dealing with Few to No Labels

## Mục tiêu đọc

- Hiểu các chiến lược khi thiếu nhãn dữ liệu.
- Biết dùng baseline đơn giản trước khi fine-tune Transformer.
- Nắm data augmentation, embeddings lookup, prompts và tận dụng unlabeled data.

## Ý chính

- Khi ít nhãn, baseline đơn giản giúp biết Transformer có thật sự cần thiết không.
- Embeddings có thể dùng như lookup table để tìm ví dụ gần nhau.
- Unlabeled data vẫn có giá trị thông qua language model fine-tuning hoặc semi-supervised methods.
- [[Intent Detection]] là case study tự nhiên cho chương này: mỗi intent thường có ít ví dụ, cách diễn đạt của người dùng đa dạng, và cần so sánh baseline trước khi fine-tune.

## Intent Detection as a Case Study

Intent detection biến utterance của người dùng thành nhãn ý định, ví dụ `reset_password`, `track_order`, `cancel_subscription`.

Vì sao phù hợp với bài toán few/no labels:

- Intent taxonomy thường do sản phẩm định nghĩa, nên dữ liệu thật ban đầu ít.
- Một intent có thể được nói bằng nhiều câu khác nhau.
- Một số intent chồng lấn về ngôn ngữ, làm zero-shot hoặc embedding lookup dễ nhầm.
- Cần training slices để biết model yếu ở intent nào, không chỉ nhìn accuracy tổng.

Chiến lược đọc chapter:

```text
Intent labels
-> Baseline đơn giản / zero-shot classification
-> Embedding lookup với vài ví dụ
-> Data augmentation nếu cần thêm biến thể
-> Fine-tune khi có đủ nhãn và có benchmark rõ
```

## Zero-shot or Few-shot Learning

Khi dealing with few to no labels, lựa chọn đầu tiên không nhất thiết là fine-tune Transformer. Chapter này đặt [[Zero-shot Learning|zero-shot]] và [[Few-shot Learning|few-shot]] như hai mức can thiệp trước khi có đủ dữ liệu supervised mạnh.

| Thiết lập | Dữ liệu có sẵn | Cách dùng | Rủi ro chính |
|---|---|---|---|
| Zero-shot | Chưa có ví dụ gán nhãn trực tiếp | Dùng model pretrained/NLI/prompt để chọn label phù hợp | Phụ thuộc tên label, mô tả label và tri thức đã học của model |
| Few-shot | Có vài ví dụ mỗi label | Dùng ví dụ cho embedding lookup, prompt examples hoặc fine-tune nhẹ | Dễ overfit, evaluation nhiễu vì sample quá ít |

### Zero-shot trong text classification

Với [[Zero-shot Classification]], task được viết lại thành bài toán so khớp giữa text và candidate labels. Một cách phổ biến là dùng model NLI: biến `text` thành premise, biến label thành hypothesis, rồi hỏi model hypothesis nào được entail nhiều nhất.

```text
Text: "I cannot log into my account"
Candidate labels: reset_password, billing, bug_report
-> Hypothesis cho từng label
-> Model xếp hạng label theo score
```

Điểm mạnh:

- tạo baseline rất nhanh khi chưa có labeled data;
- giúp kiểm tra taxonomy label có dễ hiểu không;
- hữu ích khi cần prototype hoặc triage ban đầu.

Giới hạn:

- label name mơ hồ làm score sai;
- các intent gần nghĩa nhau dễ bị nhầm;
- model có thể dựa vào prior/pretraining chứ không hiểu domain sản phẩm;
- vẫn cần evaluation bằng dữ liệu thật trước khi deploy.

### Few-shot khi có vài ví dụ

Few-shot learning bắt đầu khi đã có một ít ví dụ gán nhãn. Vài ví dụ này có giá trị lớn vì chúng neo nghĩa của label vào domain thật.

Các cách dùng vài ví dụ:

- làm nearest-neighbor bằng [[Embedding]]: câu mới lấy label của ví dụ gần nhất;
- dùng làm few-shot examples trong prompt;
- tạo training slices để xem intent nào thiếu hoặc dễ nhầm;
- fine-tune model nhỏ nếu dữ liệu đủ sạch và benchmark đủ ổn định.

Điểm cần cẩn thận: vài ví dụ không đại diện có thể làm model học lệch. Vì vậy trong few-shot, chất lượng ví dụ thường quan trọng hơn số lượng tuyệt đối.

Mental model:

```text
No labels -> zero-shot baseline
Vài labels tốt -> few-shot / embedding lookup
Nhiều labels hơn + benchmark ổn -> fine-tuning
```

## Working with No Labeled Data

Khi không có labeled data, vấn đề chính là ta chưa có ground truth để train hoặc evaluate. Vì vậy mục tiêu ban đầu là tạo tín hiệu thay thế đủ rẻ để hiểu bài toán, chứ chưa phải tối ưu model.

Workflow thực tế:

```text
Unlabeled texts + candidate labels
-> Kiểm tra taxonomy label
-> Zero-shot classification baseline
-> Embedding/clustering để xem nhóm tự nhiên
-> Tạo một evaluation set nhỏ bằng nhãn thủ công
-> Quyết định có cần few-shot / augmentation / fine-tuning không
```

### Dùng label semantics

Trong no-label setting, tên nhãn và mô tả nhãn trở thành nguồn tín hiệu chính. Với [[Zero-shot Classification]], model không nhìn thấy ví dụ train, nên nó dựa vào nghĩa của candidate labels.

Ví dụ:

```text
Text: "The checkout button does nothing"
Candidate labels:
- bug
- feature request
- question

Better labels:
- software bug report
- product feature request
- user support question
```

Nhãn rõ hơn giúp model NLI/prompt hiểu đúng hypothesis hơn. Nếu hai nhãn quá gần nghĩa, vấn đề có thể nằm ở taxonomy chứ không chỉ ở model.

### Dùng unlabeled data

Unlabeled data vẫn hữu ích vì nó cho thấy phân phối câu thật:

- đọc sample để phát hiện label còn thiếu;
- dùng [[Embedding]] để clustering các câu gần nhau;
- tìm duplicate hoặc paraphrase tự nhiên;
- chọn representative examples để gán nhãn thủ công trước;
- sau này dùng cho [[Semi-supervised Learning]] hoặc pseudo-labeling.

### Điểm dừng quan trọng

No-label baseline chỉ giúp định hướng. Trước khi deploy hoặc so sánh nghiêm túc, cần tạo một tập evaluation nhỏ có nhãn thật.

```text
Zero-shot / clustering kết quả đẹp
-> Chọn sample đại diện
-> Gán nhãn thủ công
-> Đo error theo từng label
-> Sửa taxonomy hoặc chuyển sang few-shot
```

Nếu bỏ qua bước này, mình có thể nhầm score tự tin của model với độ đúng thật.

## Fine-Tuning a Language Model

Khi không có nhiều labeled data nhưng có unlabeled text cùng domain, một chiến lược mạnh là [[Language Model Fine-Tuning|fine-tune language model]] trước khi fine-tune classifier.

Ý tưởng:

```text
Pretrained language model chung
-> Unlabeled text cùng domain
-> Language model fine-tuning
-> Domain-adapted language model
-> Classifier fine-tuning với ít labeled examples
```

Điểm quan trọng là language model fine-tuning không cần nhãn task thủ công. Nó dùng objective tự giám sát của language model để học phân phối text domain.

Tùy kiến trúc:

- encoder như BERT thường dùng [[Masked Language Modeling]];
- decoder/generative model thường dùng [[Causal Language Model|causal language modeling]] hoặc next-token prediction.

Vì sao giúp trong few/no-label setting:

- domain text chứa thuật ngữ và cách diễn đạt mà pretrained model chung chưa quen;
- user utterances thật có lỗi gõ, abbreviation, template hoặc style riêng;
- model sau adaptation có representation hợp domain hơn trước khi học classifier;
- tận dụng được unlabeled data rẻ hơn labeled data.

Khác với classifier fine-tuning:

| Bước | Dữ liệu | Mục tiêu |
|---|---|---|
| Language model fine-tuning | Unlabeled domain text | Thích nghi với ngôn ngữ/domain |
| Classifier fine-tuning | Labeled examples | Học decision boundary giữa các label |

Trade-off:

- Có thể cải thiện downstream khi domain khác dữ liệu pretraining chung.
- Cần corpus domain đủ đại diện và sạch.
- Nếu fine-tune quá lâu hoặc corpus quá hẹp, model có thể overfit domain hoặc quên năng lực tổng quát.
- Vẫn phải đánh giá bằng labeled validation set vì LM loss thấp hơn không đảm bảo classifier tốt hơn.

## Fine-Tuning a Classifier

Sau khi đã có labeled examples, bước tiếp theo là [[Classifier Fine-Tuning|fine-tune classifier]]. Đây là lúc model học decision boundary giữa các label của task cụ thể.

Luồng trực giác:

```text
Text có nhãn
-> Tokenizer
-> Pretrained encoder
-> Classification head
-> Classification loss
-> Update trọng số để dự đoán label đúng hơn
```

Nếu đã có [[Language Model Fine-Tuning]], classifier fine-tuning bắt đầu từ một encoder hợp domain hơn. Nếu chưa có bước đó, classifier vẫn có thể fine-tune trực tiếp từ pretrained model chung.

Vì sao bước này quan trọng:

- zero-shot chỉ dùng nghĩa của label, chưa học decision boundary theo dữ liệu thật;
- embedding lookup dựa vào similarity, chưa tối ưu trực tiếp cho label accuracy;
- classifier fine-tuning dùng nhãn thật để học ranh giới phân biệt giữa các intent gần nhau.

Trade-off trong few-shot setting:

- giúp model bám đúng taxonomy hơn zero-shot;
- nhưng rất dễ overfit nếu số nhãn ít hoặc label noise cao;
- validation set nhỏ có thể làm metric dao động mạnh;
- cần training slices để xem label nào thật sự được cải thiện.

Khác với language model fine-tuning:

| Bước | Dữ liệu | Học cái gì |
|---|---|---|
| [[Language Model Fine-Tuning]] | Unlabeled domain text | Ngôn ngữ và style của domain |
| [[Classifier Fine-Tuning]] | Labeled examples | Decision boundary giữa các label |

Practical rule:

```text
No labels -> zero-shot / embedding / clustering
Ít labels + domain text -> LM fine-tuning rồi classifier fine-tuning
Ít labels nhưng domain đã quen -> thử classifier fine-tuning trực tiếp
```

## Playbook ngắn cho ít hoặc không có nhãn

```text
Không có nhãn
-> kiểm tra taxonomy
-> zero-shot / embedding / clustering
-> tạo evaluation set nhỏ

Có rất ít nhãn
-> baseline đơn giản
-> few-shot / augmentation nếu hợp lý
-> cân nhắc LM fine-tuning nếu có nhiều unlabeled text
-> classifier fine-tuning khi đã có tín hiệu đủ rõ
```

Điểm quan trọng của chapter này là: dữ liệu nhãn ít không có nghĩa phải fine-tune ngay. Thứ cần tối ưu trước thường là chiến lược dùng tín hiệu rẻ hơn nhãn.

## Working with Large Datasets

Khi chapter nói về few hoặc no labels, một điểm dễ bỏ sót là ta vẫn có thể có **rất nhiều unlabeled text**. Lúc này khó khăn không còn chỉ là “thiếu nhãn”, mà còn là “xử lý khối lượng dữ liệu lớn sao cho đáng công”.

Large datasets hữu ích vì:

- cho phép [[Language Model Fine-Tuning]] trên đúng domain;
- giúp học representation tốt hơn trước khi làm downstream classification;
- hỗ trợ [[Semi-supervised Learning]] hoặc pseudo-labeling;
- cho thấy phân phối câu thật, lỗi gõ thật, thuật ngữ thật của sản phẩm.

Nhưng dữ liệu lớn không tự động tốt hơn. Nếu corpus quá nhiễu, nhiều duplicate hoặc lệch domain, model có thể học sai thói quen thay vì học tín hiệu hữu ích.

Mental model:

```text
Nhiều unlabeled text
-> lọc / deduplicate / chọn domain-relevant samples
-> tokenize theo batch
-> LM fine-tuning hoặc representation learning
-> dùng ít labeled data cho classifier
```

### Bài toán thật sự là pipeline

Khi corpus đủ lớn, bottleneck thường nằm ở:

- đọc dữ liệu từ disk/network;
- tokenize quá chậm nếu làm từng mẫu;
- RAM không đủ nếu load mọi thứ cùng lúc;
- preprocessing lặp lại nhiều lần vì không cache.

Trong hệ sinh thái [[Hugging Face]], `Datasets` hữu ích vì cho phép transform theo batch, cache preprocessing và làm việc memory-efficient hơn việc tự nhét toàn bộ data vào Python list/DataFrame rồi tokenize tuần tự.

Ví dụ trực giác:

```text
1 triệu support tickets
-> không cần gán nhãn hết
-> có thể dùng để LM fine-tune encoder
-> sau đó chỉ cần vài trăm / vài nghìn label để fine-tune classifier
```

### Ý nghĩa trong few-shot learning

Điểm hay của large datasets trong chapter này không phải “thay few-shot thành fully supervised”, mà là:

- giảm khoảng cách domain giữa pretrained model và dữ liệu thật;
- tận dụng dữ liệu rẻ hơn dữ liệu gán nhãn;
- cải thiện representation để mỗi nhãn hiếm trở nên có giá trị hơn.

Nói ngắn gọn: **ít nhãn không có nghĩa là ít dữ liệu**. Nhiều khi thứ mình thiếu là nhãn, còn thứ mình có rất nhiều là raw text.

## Demo thực hành

Zero-shot classification khi chưa có dữ liệu gán nhãn.

```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

texts = [
    "The app crashes whenever I try to upload a file.",
    "Please add dark mode to the dashboard.",
]

labels = ["bug", "feature request", "question", "documentation"]

for text in texts:
    result = classifier(text, candidate_labels=labels)
    print(text)
    print(list(zip(result["labels"], result["scores"])))
```

## Khái niệm quan trọng

- [[Few-shot Learning]]
- [[Zero-shot Classification]]
- [[Intent Detection]]
- [[Data Augmentation]]
- [[Embedding]]
- [[Semi-supervised Learning]]
- [[Language Model Fine-Tuning]]
- [[Domain Adaptation]]
- [[Masked Language Modeling]]
- [[Classifier Fine-Tuning]]
- [[Working with Large Datasets]]

## Active Recall

1. Khi ít nhãn, vì sao nên làm baseline trước?
2. Zero-shot classification dựa trên giả định gì?
3. Data augmentation có thể làm hỏng dữ liệu ra sao?
4. Unlabeled data giúp được gì cho classifier?
5. Vì sao intent detection là case study tốt cho few/no-label learning?
6. Zero-shot và few-shot khác nhau ở nguồn tín hiệu nào?
7. Vì sao tên label ảnh hưởng mạnh đến zero-shot classification?
8. Khi nào nên chuyển từ zero-shot sang few-shot?
9. Khi không có labeled data, vì sao chưa nên fine-tune ngay?
10. Unlabeled data giúp gì nếu không có nhãn?
11. Vì sao cần tạo một evaluation set nhỏ có nhãn thật?
12. Fine-tuning a language model khác classifier fine-tuning ở đâu?
13. Vì sao language model fine-tuning dùng được unlabeled domain text?
14. Vì sao LM loss thấp hơn chưa chắc làm classifier tốt hơn?
15. Classifier fine-tuning giúp gì mà zero-shot classification không làm được?
16. Vì sao classifier fine-tuning trong few-shot setting dễ overfit?
17. Khi nào nên fine-tune classifier sau language model fine-tuning?
18. Vì sao large unlabeled datasets vẫn rất giá trị trong few-shot learning?
19. Bottleneck chính khi làm việc với large datasets thường nằm ở đâu?
20. Vì sao “nhiều dữ liệu” không đồng nghĩa “nhiều tín hiệu tốt”?

## Gợi ý trả lời Active Recall

1. Vì khi ít nhãn, fine-tune model lớn rất dễ overfit và khó biết lỗi đến từ model hay dữ liệu; baseline giúp có mốc so sánh rẻ và rõ.
2. Zero-shot classification giả định model pretrained/NLI đã học đủ quan hệ ngữ nghĩa để so khớp text với candidate labels dù chưa train trực tiếp trên task đó.
3. Data augmentation có thể tạo câu không tự nhiên, đổi nghĩa label, làm nhiễu distribution hoặc nhân rộng lỗi sẵn có trong dữ liệu ít nhãn.
4. Unlabeled data có thể giúp qua language model fine-tuning, semi-supervised learning, pseudo-labeling hoặc học representation/domain tốt hơn.
5. Intent detection phù hợp vì intent taxonomy thường mới, ít ví dụ, câu người dùng đa dạng và nhiều intent gần nghĩa nhau.
6. Zero-shot dựa chủ yếu vào năng lực pretrained/prompt/label description; few-shot dùng thêm một vài ví dụ gán nhãn để neo nghĩa từng label.
7. Vì label name là một phần input mô tả task; nếu tên label mơ hồ hoặc không giống cách model hiểu, score zero-shot có thể lệch.
8. Nên chuyển sang few-shot khi đã thu được vài ví dụ chất lượng cho mỗi label hoặc khi zero-shot baseline cho thấy các label gần nghĩa nhau cần ví dụ domain-specific để phân biệt.
9. Vì không có nhãn thì không có tín hiệu supervised đáng tin để train/evaluate; fine-tune ngay dễ học lệch hoặc chỉ tối ưu nhiễu.
10. Unlabeled data giúp hiểu phân phối câu thật, phát hiện nhóm intent tự nhiên, kiểm tra taxonomy, chọn sample để gán nhãn và tạo nền cho semi-supervised/pseudo-labeling.
11. Vì zero-shot score hoặc clustering không cho biết đúng sai thật; một evaluation set nhỏ là mốc ground truth để đo lỗi và quyết định bước tiếp theo.
12. Language model fine-tuning dùng text thô để thích nghi ngôn ngữ/domain; classifier fine-tuning dùng text có nhãn để học mapping input sang label.
13. Vì objective của language model tự tạo tín hiệu học từ text, ví dụ mask token rồi dự đoán token bị che hoặc dự đoán token tiếp theo.
14. Vì LM loss chỉ đo khả năng mô hình hóa text domain, còn classifier cần decision boundary đúng giữa label; phải kiểm tra bằng validation set có nhãn.
15. Vì classifier fine-tuning dùng nhãn thật để học ranh giới giữa các label cụ thể, còn zero-shot chủ yếu dựa vào nghĩa của label và tri thức pretrained.
16. Vì số ví dụ ít làm model dễ ghi nhớ pattern hẹp, học nhầm từ label noise và cho metric validation dao động mạnh.
17. Nên làm vậy khi có nhiều unlabeled domain text để thích nghi encoder trước, rồi có ít labeled examples để học decision boundary của task.
18. Vì chúng cho model thấy ngôn ngữ, thuật ngữ và phân phối câu thật của domain, nên có thể dùng cho language model fine-tuning hoặc semi-supervised learning dù chưa có nhãn.
19. Thường nằm ở I/O, tokenization, batching, RAM và preprocessing pipeline, không nhất thiết ở bản thân kiến trúc Transformer.
20. Vì dữ liệu có thể nhiễu, duplicate, lệch domain hoặc quá đắt để xử lý; nếu pipeline và filtering kém thì thêm dữ liệu chỉ thêm rác.

## Checklist

- [x] Đọc xong chapter
- [ ] Chạy demo zero-shot classification
- [ ] Nghĩ một use case cá nhân có ít nhãn
- [x] Tách concept cần dùng lại
- [x] Cập nhật tiến độ sách
