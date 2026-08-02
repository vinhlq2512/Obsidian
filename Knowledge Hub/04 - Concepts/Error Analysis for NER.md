---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]"
  - "[[28-07-2026]]"
tags:
  - concept
  - nlp
  - ner
  - evaluation
---

# Error Analysis for NER

## Định nghĩa

Error analysis for NER là quá trình đọc và phân loại các dự đoán sai của model NER để hiểu model đang lỗi ở đâu, vì sao lỗi xảy ra, và nên cải thiện dữ liệu, tokenization, model hay evaluation như thế nào.

## Cách hiểu bằng lời của tôi

Metric như F1 cho biết model tốt hay kém ở mức tổng. Error analysis trả lời câu hỏi tiếp theo: model kém vì bỏ sót entity, nhận nhầm entity, sai ranh giới, sai type, hay vì labels/tokenization bị align sai. Đây là bước biến số điểm thành hành động sửa lỗi.

## Các kiểu lỗi thường gặp

- **Sai ranh giới entity**: model nhận ra đúng type nhưng lấy thiếu hoặc thừa token.
- **Sai entity type**: model thấy đúng span nhưng gán nhầm `PER`, `ORG`, `LOC`.
- **False positive**: model dự đoán entity ở nơi gold label là `O`.
- **False negative**: gold có entity nhưng model bỏ sót.
- **Lỗi BIO/BILOU**: sequence nhãn không hợp lệ hoặc nhiều `B-...` xuất hiện trong cùng một entity do subword handling sai.
- **Lỗi tokenization/alignment**: `word_ids()`, offsets hoặc label `-100` sai làm model học/predict lệch.
- **Lỗi multilingual transfer**: model tốt ở source language nhưng yếu ở target language.

## Cách làm thực tế

### 1. Lấy prediction và gold labels

Sau evaluation, giữ lại:

- tokens hoặc words gốc.
- gold labels.
- predicted labels.
- offsets hoặc `word_ids`.
- language/domain nếu là multilingual dataset.

### 2. Bỏ qua vị trí không tính loss

Các vị trí có label `-100` thường là special tokens hoặc subword phụ. Khi phân tích lỗi, cần bỏ qua hoặc hiển thị riêng để tránh hiểu nhầm.

### 3. In ví dụ dạng bảng

Một bảng dễ đọc:

```text
token      gold     pred     note
Nguyễn     B-PER    B-PER    đúng
Nhật       I-PER    I-PER    đúng
Ánh        I-PER    O        thiếu token cuối
sinh       O        O        đúng
Quảng      B-LOC    B-LOC    đúng
Nam        I-LOC    I-LOC    đúng
```

Bảng này giúp nhìn ranh giới entity rõ hơn chỉ nhìn danh sách logits.

### 4. Gom lỗi theo nhóm

Nên thống kê lỗi theo:

- entity type.
- ngôn ngữ.
- độ dài entity.
- số subword mỗi word/entity.
- domain hoặc nguồn dữ liệu.
- false positive vs false negative.

### 5. Biến lỗi thành hành động

Ví dụ:

- Sai nhiều ranh giới entity -> kiểm tra BIO conversion và label alignment.
- Bỏ sót `ORG` -> thêm dữ liệu hoặc xem label guideline cho tổ chức.
- Sai nhiều ở tiếng Việt -> xem tokenizer, domain, hoặc cần fine-tune thêm target-language data.
- False positive cao -> xem lại postprocessing, threshold hoặc entity definitions.

## Liên hệ với metric

[[Performance Measures for NER]] cho biết precision/recall/F1. Error analysis giải thích vì sao:

- precision thấp thường đi với nhiều false positives.
- recall thấp thường đi với nhiều false negatives.
- F1 thấp ở một entity type có thể do guideline mơ hồ, dữ liệu ít, hoặc tokenization kém.

## Với multilingual NER

Trong multilingual NER, luôn tách lỗi theo ngôn ngữ. Một F1 trung bình có thể che việc:

- source language tốt, target language yếu.
- ngôn ngữ có dấu/script khác bị tokenizer tách nhiều hơn.
- entity type ở một ngôn ngữ có pattern khác.
- domain của target language lệch source language.

## Cần biết

- Không nên đổi model ngay sau khi thấy F1 thấp; trước hết phải đọc lỗi mẫu.
- Error analysis thường phát hiện lỗi dữ liệu và alignment nhanh hơn training log.
- Với [[Fine-Tuning XLM-RoBERTa]], error analysis quyết định nên sửa data pipeline, thêm dữ liệu, đổi hyperparameters hay thử transfer setup khác.
- Với [[Tokenizing Texts for NER]], bug alignment là nguồn lỗi rất nguy hiểm vì model vẫn train bình thường nhưng học sai.

## Liên kết

- [[Named Entity Recognition]]
- [[Performance Measures for NER]]
- [[Tokenizing Texts for NER]]
- [[Fine-Tuning XLM-RoBERTa]]
- [[NLP Transformers - Chapter 04 - Multilingual Named Entity Recognition]]
