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
  - zero-shot
  - text-classification
  - nlp
---

# Zero-shot Classification

## Định nghĩa

Zero-shot classification là cách phân loại văn bản vào các nhãn chưa có dữ liệu train trực tiếp cho task đó.

## Cơ chế trực giác

Model nhận text và danh sách candidate labels, rồi ước lượng label nào phù hợp nhất.

```text
Text
Candidate labels
-> Zero-shot classifier
-> Ranking labels theo score
```

Một cách triển khai phổ biến là dùng model NLI:

```text
Premise: text cần phân loại
Hypothesis: "This text is about {label}"
-> Entailment score cho từng label
-> Chọn label có score cao nhất
```

Vì label được đưa vào input, cách đặt tên label ảnh hưởng trực tiếp đến kết quả. Label nên rõ nghĩa và gần với cách người dùng thật diễn đạt intent.

## Khi dùng

- Khi chưa có dữ liệu gán nhãn.
- Khi cần baseline nhanh trước khi xây dataset.
- Khi muốn kiểm tra taxonomy nhãn có hợp lý không.
- Khi muốn biết label nào dễ nhầm trước khi đầu tư fine-tune.

## Working with no labeled data

Khi hoàn toàn chưa có labeled data, zero-shot classification là baseline hợp lý vì nó dùng nghĩa của label thay cho ví dụ train.

```text
Unlabeled text
Candidate labels / label descriptions
-> Zero-shot classifier
-> Ranking label
-> Dùng kết quả để kiểm tra taxonomy và chọn sample cần gán nhãn
```

Điểm cần làm tốt:

- viết label rõ nghĩa, gần với domain;
- thử label description thay vì chỉ label name ngắn;
- xem các case model score cao nhưng có vẻ sai để phát hiện label chồng lấn;
- tạo một tập evaluation nhỏ có nhãn thật trước khi tin baseline.

## Hạn chế

- Phụ thuộc mạnh vào cách đặt tên label.
- Có thể nhầm nếu label mơ hồ hoặc chồng lấn.
- Không thay thế evaluation bằng dữ liệu thật.
- Không chắc hiểu domain nội bộ nếu label hoặc utterance cần kiến thức sản phẩm cụ thể.
- Score cao không đồng nghĩa đúng nếu chưa có ground truth kiểm tra.

## Cách hiểu bằng lời của tôi

Zero-shot classification là cách hỏi model: "câu này giống nhãn nào nhất trong danh sách?" Nó rất hợp để khởi đầu khi chưa có nhãn, nhưng chưa đủ để tin production nếu chưa kiểm tra bằng dữ liệu thật.

## Câu hỏi review

1. Zero-shot classification khác supervised classification ở đâu?
2. Vì sao label wording ảnh hưởng kết quả?
3. Khi nào nên chuyển từ zero-shot sang few-shot?
4. Vì sao no-label baseline vẫn cần một evaluation set nhỏ?

## Liên kết

- [[Few-shot Learning]]
- [[Zero-shot Learning]]
- [[Intent Detection]]
- [[Text Classification]]
