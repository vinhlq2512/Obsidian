---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 2
start_page: 39
end_page: 77
reading_date: 2026-07-24
planned_sessions:
  - "2026-07-24 | 39-57 | Dataset, nhãn, độ dài văn bản và tokenization | 50 phút"
  - "2026-07-25 | 58-77 | Feature extraction, fine-tuning và viết lại workflow | 55 phút"
estimated_minutes: 75
actual_minutes:
need_review: true
tags:
  - nlp
  - text-classification
  - hugging-face
---

# NLP Transformers - Chapter 02 - Text Classification

## Mục tiêu đọc

- Hiểu pipeline phân loại văn bản từ dataset đến model.
- Nắm tokenization ở mức character, word, subword.
- Phân biệt dùng Transformer như feature extractor và fine-tuning toàn bộ model.
- Biết cách đánh giá model bằng baseline, confusion matrix, F1/accuracy và error analysis.
- Hiểu cách lưu, chia sẻ và dùng lại model đã fine-tune qua Hugging Face Hub hoặc `pipeline`.

## Ý chính

- Text classification không chỉ là gọi model. Workflow đúng bắt đầu từ hiểu dataset, nhãn, độ dài văn bản, imbalance, tokenization, rồi mới tới training.
- Hugging Face `datasets`, `tokenizers`, và `transformers` tạo thành một pipeline thống nhất: raw text -> token IDs/attention mask -> hidden states hoặc classification logits -> metrics/predictions.
- Dữ liệu cần được kiểm tra phân phối nhãn và độ dài văn bản trước khi train. Nếu nhãn lệch, accuracy dễ gây ảo giác; nếu văn bản dài hơn context size, truncation có thể làm mất thông tin quan trọng.
- Subword tokenization cân bằng tốt giữa vocabulary size và khả năng xử lý từ hiếm: từ phổ biến giữ nguyên, từ hiếm bị tách thành mảnh nhỏ.
- Feature extraction dùng Transformer như bộ tạo đặc trưng cố định. Cách này nhanh hơn, ít tốn tài nguyên hơn, phù hợp khi không có GPU hoặc muốn baseline tốt.
- Fine-tuning cập nhật toàn bộ model cùng classification head. Cách này thường cho kết quả tốt hơn vì representation được điều chỉnh trực tiếp cho task, nhưng tốn GPU/compute hơn.
- Error analysis là bước quan trọng sau training: xem sample loss cao/thấp để phát hiện nhãn sai, dữ liệu nhiễu, shortcut mà model đang học, hoặc class dễ bị nhầm.
- Sau khi hoàn thành chapter, mental model cần giữ là: dữ liệu tốt + tokenizer đúng + baseline rõ + fine-tuning có kiểm soát + error analysis thường quan trọng hơn việc chỉ đổi sang model lớn hơn.

## Định nghĩa quan trọng

- [[Text Classification]]: bài toán gán một hoặc nhiều nhãn rời rạc cho một đoạn văn bản. Trong chapter này, input là tweet và output là một trong sáu cảm xúc.
- Dataset split: các phần dữ liệu như `train`, `validation`, `test`. `train` dùng để học, `validation` dùng để chọn/tinh chỉnh mô hình, `test` dùng để đánh giá cuối cùng.
- Class distribution: phân phối số lượng example theo từng nhãn. Phân phối lệch khiến model dễ ưu tiên class phổ biến.
- [[Tokenization]]: quá trình chia text thành token và ánh xạ token thành số để model xử lý.
- Character tokenization: chia text thành ký tự. Dễ bao phủ từ hiếm nhưng sequence dài và model phải tự học cấu trúc từ.
- Word tokenization: chia text thành từ. Giữ cấu trúc ngôn ngữ tốt hơn nhưng vocabulary dễ phình lớn và xử lý từ hiếm kém.
- [[Subword Tokenization]]: chia text ở mức mảnh từ. Đây là compromise giữa character và word tokenization.
- `input_ids`: danh sách ID số tương ứng với token.
- `attention_mask`: vector cho model biết vị trí nào là token thật và vị trí nào là padding.
- Hidden state: vector biểu diễn do Transformer tạo ra cho mỗi token sau các encoder layer.
- `[CLS]` representation: vector ở vị trí token đầu sequence, thường được dùng làm đặc trưng đại diện cho toàn câu trong sequence classification.
- Feature extraction: đóng băng pretrained Transformer, trích hidden states làm feature, rồi train classifier riêng.
- Fine-tuning: train end-to-end toàn bộ pretrained Transformer cùng classification head.
- Classification head: layer phía trên encoder, biến representation thành logits cho từng class.
- Confusion matrix: bảng cho biết nhãn thật bị model dự đoán thành nhãn nào, giúp nhìn lỗi theo từng class.

## Mental model

Một text classifier bằng Transformer có thể được nhìn như một dây chuyền chuyển đổi:

```text
tweet thô
-> dataset có split và label rõ ràng
-> phân tích class distribution và độ dài văn bản
-> tokenizer đúng với pretrained checkpoint
-> input_ids + attention_mask
-> DistilBERT encoder
-> hidden states
-> classifier head
-> logits
-> nhãn cảm xúc
-> metrics + error analysis
```

Điểm cần nhớ: model chỉ là một phần ở giữa pipeline. Chất lượng hệ thống phụ thuộc mạnh vào việc hiểu dữ liệu, dùng tokenizer đúng, chọn metric đúng, và soi lỗi sau khi train.

## Phần cần biết

### 1. Dataset và bước inspect ban đầu

- Chapter dùng emotion dataset với sáu nhãn: sadness, joy, love, anger, fear, surprise.
- Dataset được load bằng `load_dataset("emotion")` và trả về `DatasetDict` gồm `train`, `validation`, `test`.
- Mỗi row là một dictionary với `text` và `label`.
- `ClassLabel` lưu mapping giữa label ID và label name, nên có thể dùng `int2str()` để đọc nhãn dễ hơn.
- Có thể đổi format sang Pandas bằng `set_format(type="pandas")` để dùng API visualize/inspect quen thuộc.

### 2. Class distribution và text length

- Trước khi train cần nhìn phân phối nhãn. Nếu class hiếm quá ít, model có thể học rất kém ở class đó dù accuracy tổng thể không quá xấu.
- Emotion dataset bị imbalance: joy/sadness nhiều hơn, love/surprise ít hơn.
- Cách xử lý imbalance có thể gồm oversampling, undersampling, thu thập thêm dữ liệu, class-weighted loss, hoặc đổi metric sang macro/weighted F1.
- Cần kiểm tra độ dài văn bản vì DistilBERT có maximum context size 512 token.
- Với tweet trong dataset này, đa số text ngắn nên truncation không phải rủi ro lớn.

### 3. Tokenization

- Transformer không nhận raw string. Text phải thành token IDs.
- Character-level tokenizer ít mất thông tin nhưng sequence dài, khó học, tốn tài nguyên.
- Word-level tokenizer dễ hiểu hơn nhưng vocabulary rất lớn và tạo nhiều `[UNK]` cho từ hiếm/typo.
- Subword tokenizer giữ từ phổ biến, tách từ hiếm thành mảnh nhỏ. Đây là lý do pretrained models hiện đại thường dùng subword.
- DistilBERT dùng tokenizer riêng của checkpoint `distilbert-base-uncased`. Khi dùng pretrained model, phải dùng đúng tokenizer đi kèm checkpoint.
- Output tokenizer quan trọng nhất ở phần này là `input_ids` và `attention_mask`.
- Padding làm các sequence trong batch có cùng shape; attention mask giúp model bỏ qua padding.

### 4. Transformer như feature extractor

- Dùng `AutoModel.from_pretrained(model_ckpt)` để load DistilBERT không có classification head.
- Đưa tokenized input vào model để lấy `last_hidden_state`.
- Shape của hidden state là `[batch_size, n_tokens, hidden_dim]`; với DistilBERT, `hidden_dim = 768`.
- Với classification, thường lấy vector ở vị trí `[CLS]`, tức `last_hidden_state[:, 0]`, làm feature cho cả câu.
- Sau đó tạo feature matrix:
  - `X_train`: hidden states.
  - `y_train`: labels.
  - `X_valid`, `y_valid`: dữ liệu validation.
- Có thể train logistic regression trên hidden states. Kết quả trong chapter tốt hơn baseline majority class nhưng vẫn thấp hơn fine-tuning.
- Ưu điểm: nhanh, nhẹ, dùng được khi GPU yếu/không có GPU.
- Nhược điểm: representation bị đóng băng, không được tối ưu riêng cho bài toán emotion classification.

### 5. Visualize representation

- Hidden states có 768 chiều nên khó nhìn trực tiếp.
- Chapter dùng UMAP để giảm xuống 2D và visualize theo label.
- Visualize giúp kiểm tra nhanh xem representation có tách được các class không.
- Joy/love có xu hướng tách khỏi nhóm negative emotion; sadness/anger/fear dễ chồng lấn; surprise bị phân tán.
- Lưu ý: projection 2D chỉ là gợi ý, không chứng minh hoàn toàn class có/không separable trong không gian gốc.

### 6. Fine-tuning

- Dùng `AutoModelForSequenceClassification.from_pretrained(model_ckpt, num_labels=6)`.
- Classification head mới được thêm vào nên ban đầu có weight random; cảnh báo lúc load model là bình thường.
- Fine-tuning cập nhật cả encoder và classification head, vì vậy hidden states có thể thích nghi với task.
- `Trainer` giúp gom training loop, evaluation, checkpointing, logging, tokenizer, dataset và metrics vào một API.
- `TrainingArguments` kiểm soát output directory, epochs, learning rate, batch size, weight decay, evaluation strategy, logging, push to hub. Các tham số như `learning_rate` và `weight_decay` thường đi cùng optimizer kiểu [[AdamW]] trong pipeline fine-tuning hiện đại.
- Chapter dùng accuracy và weighted F1. Với dataset imbalance, weighted F1 hợp lý hơn accuracy đơn thuần, nhưng vẫn cần xem per-class behavior qua confusion matrix.
- Fine-tuning đạt khoảng 92% F1 trên validation trong ví dụ, tốt hơn rõ rệt so với feature extraction.

### 7. Error analysis

- Sau khi có model tốt, không nên chỉ dừng ở metric tổng.
- Tính loss cho từng validation sample để xem model sai nặng ở đâu.
- Sample loss cao có thể chỉ ra:
  - Nhãn sai hoặc gây tranh cãi.
  - Text mơ hồ, chứa nhiều cảm xúc.
  - Pattern lạ mà training data chưa bao phủ.
  - Class cần tách lại hoặc bổ sung dữ liệu.
- Sample loss thấp cho biết model rất tự tin. Cần kiểm tra để đảm bảo model không dựa vào shortcut hời hợt.
- Trong chapter, joy có vẻ bị mislabeled ở một số sample; sadness là class model rất tự tin.

### 8. Saving và sharing

- Sau fine-tuning, có thể push model lên Hugging Face Hub bằng `trainer.push_to_hub()`.
- Model trên Hub có thể được gọi lại bằng `pipeline("text-classification", model=model_id)`.
- Đây là bước nối từ experimentation sang reuse/deployment.

## Khi áp dụng

- Với bài toán phân loại văn bản mới, bắt đầu bằng dataset inspection chứ không bắt đầu bằng fine-tune ngay.
- Nếu thiếu GPU hoặc cần baseline nhanh, dùng pretrained Transformer làm feature extractor rồi train logistic regression/simple classifier.
- Nếu có GPU và cần hiệu năng tốt, fine-tune end-to-end với `AutoModelForSequenceClassification` và `Trainer`.
- Nếu nhãn lệch, dùng thêm F1, confusion matrix và per-class analysis thay vì chỉ accuracy.
- Nếu text dài, phải quan tâm truncation strategy, max length và thông tin bị mất ở phần bị cắt.
- Nếu model sai nhiều ở vài class, đọc confusion matrix và loss-based examples trước khi đổi sang model lớn hơn.

## Ghi chú sau khi hoàn thành

- Chapter 02 đã hoàn thành qua hai daily:
  - [[24-07-2026]]: dataset, nhãn, class distribution, độ dài văn bản và tokenization.
  - [[25-07-2026]]: feature extraction, fine-tuning, Trainer, metrics, confusion matrix, error analysis và lưu/chia sẻ model.
- Điểm nối quan trọng giữa hai buổi: tokenization tạo input chuẩn cho model, còn training/evaluation quyết định liệu representation đó có giải quyết đúng task classification không.
- Phần nên review lại là metric cho imbalance, vì weighted F1 có thể vẫn che đi lỗi ở class hiếm. Khi áp dụng thật nên xem thêm macro F1, per-class precision/recall và confusion matrix.
- Demo thực hành nên làm ở quy mô nhỏ trước: subset của emotion dataset, `distilbert-base-uncased`, 1-2 epoch, rồi đọc confusion matrix thay vì chỉ nhìn metric tổng.

## Demo thực hành

Fine-tune emotion classifier nhỏ với `Trainer`.

```python
from datasets import load_dataset
from sklearn.metrics import accuracy_score, f1_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

dataset = load_dataset("emotion")
checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding=True)

encoded = dataset.map(tokenize, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=6)

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "f1": f1_score(labels, preds, average="weighted"),
    }

args = TrainingArguments(
    output_dir="demo-emotion-classifier",
    evaluation_strategy="epoch",
    num_train_epochs=2,
    learning_rate=2e-5,
    weight_decay=0.01,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=encoded["train"].shuffle(seed=42).select(range(1000)),
    eval_dataset=encoded["validation"].select(range(300)),
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

trainer.train()
```

## Workflow tự viết lại

1. Load dataset từ Hub hoặc file local bằng `load_dataset`.
2. Kiểm tra split, cột dữ liệu, label mapping và một vài sample thật.
3. Chuyển sang Pandas nếu cần visualize phân phối nhãn và độ dài văn bản.
4. Chọn pretrained checkpoint phù hợp, ví dụ `distilbert-base-uncased`.
5. Load tokenizer bằng `AutoTokenizer.from_pretrained(checkpoint)`.
6. Tokenize toàn bộ dataset bằng `map(tokenize, batched=True)` với `padding` và `truncation`.
7. Chọn hướng training:
   - Feature extraction: dùng `AutoModel`, lấy `[CLS]` hidden state, train classifier bên ngoài.
   - Fine-tuning: dùng `AutoModelForSequenceClassification`, train end-to-end bằng `Trainer`.
8. Định nghĩa metric phù hợp, ít nhất gồm accuracy và F1 nếu có imbalance.
9. Train trên `train`, đánh giá trên `validation`.
10. Đọc confusion matrix và phân tích sample loss cao/thấp.
11. Sửa dữ liệu hoặc training setup nếu phát hiện lỗi nhãn, class mơ hồ, hoặc shortcut.
12. Lưu/push model và dùng lại bằng `pipeline` khi cần inference.

## Khái niệm quan trọng

- [[Text Classification]]
- [[Tokenization]]
- [[Subword Tokenization]]
- [[Fine-tuning]]
- [[Hugging Face]]
- [[Transfer Learning]]

## Liên kết

- Book: [[Natural Language Processing with Transformers]]
- Daily liên quan:
  - [[24-07-2026]]
  - [[25-07-2026]]
- Concept nên cập nhật thêm:
  - [[Tokenization]]
  - [[Text Classification]]
  - [[Fine-tuning]]

## Active Recall

1. Vì sao cần xem class distribution trước khi train?
2. Subword tokenization xử lý từ chưa từng thấy như thế nào?
3. Feature extraction khác fine-tuning ở điểm nào?
4. Metric nào phù hợp nếu nhãn bị lệch?
5. Vì sao phải dùng tokenizer đúng với pretrained checkpoint?
6. `attention_mask` giải quyết vấn đề gì khi padding?
7. Vì sao lấy hidden state của `[CLS]` cho sequence classification?
8. Vì sao fine-tuning thường tốt hơn feature extraction?
9. Confusion matrix cho biết điều gì mà accuracy không nói rõ?
10. Error analysis bằng loss cao/thấp giúp phát hiện vấn đề gì?

## Gợi ý trả lời câu hỏi review

1. Cần xem class distribution vì dataset lệch làm model thiên về class phổ biến. Nếu chỉ nhìn accuracy, model có thể đạt điểm khá cao bằng cách đoán class nhiều mẫu nhưng thất bại ở class hiếm.
2. Subword tokenization xử lý từ chưa từng thấy bằng cách chia từ đó thành các mảnh nhỏ hơn đã có trong vocabulary. Nhờ vậy model không phải gom mọi từ lạ vào `[UNK]`.
3. Feature extraction đóng băng Transformer và dùng hidden states làm feature cho classifier ngoài. Fine-tuning train toàn bộ Transformer cùng classification head, nên representation thích nghi với task nhưng tốn tài nguyên hơn.
4. Nếu nhãn bị lệch, nên dùng F1, đặc biệt macro F1 nếu muốn coi trọng class hiếm ngang class lớn, hoặc weighted F1 nếu muốn phản ánh phân phối thật nhưng vẫn xét precision/recall.
5. Phải dùng tokenizer đúng checkpoint vì model đã học embedding/vocabulary theo tokenizer đó. Đổi tokenizer làm ID-token mapping lệch, khiến model hiểu sai input.
6. `attention_mask` cho model biết token nào là nội dung thật và token nào chỉ là padding. Nhờ đó attention không tính nhầm các `[PAD]` token.
7. `[CLS]` được đặt ở đầu sequence và thường được huấn luyện/thiết kế để gom thông tin cấp sequence. Với classification, vector này được đưa vào classification head.
8. Fine-tuning thường tốt hơn vì pretrained representation được cập nhật để giảm loss của task cụ thể, thay vì giữ nguyên như feature extraction.
9. Confusion matrix cho biết class nào hay bị nhầm với class nào. Điều này giúp phát hiện lỗi theo từng nhãn, ví dụ fear/anger bị nhầm với sadness.
10. Loss cao giúp tìm sample model sai nặng hoặc nhãn có vấn đề. Loss thấp giúp kiểm tra các dự đoán model quá tự tin, từ đó phát hiện shortcut hoặc bias dữ liệu.

## Checklist

- [x] Đọc xong chapter
- [x] Viết tóm tắt
- [x] Chạy hoặc hiểu demo fine-tuning ở mức workflow
- [x] Ghi lại lỗi hoặc vấn đề tài nguyên nếu có: chưa chạy demo nên chưa có lỗi runtime; cần lưu ý fine-tuning cần GPU/VRAM nếu chạy full dataset.
- [x] Cập nhật tiến độ sách khi daily 25 hoàn thành
