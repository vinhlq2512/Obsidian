---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 14 - Tokenization and Multilinguality"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 14 - Tokenization and Multilinguality.pdf]]"
pages: 76
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Tokenization]]"
  - "[[Multilingual Transformer]]"
tags:
  - cs224n
  - lecture
---
# CS224N 2026 - Lecture 14 - Tokenization and Multilinguality

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 14 - Tokenization and Multilinguality.pdf]]
- Vai trò trong khoá: tokenization, BPE, multilinguality, fairness và chi phí token giữa ngôn ngữ.
- Paper đọc kèm: [[2023 - Do All Languages Cost the Same - Tokenization in the Era of Commercial Language Models - EMNLP Main 614]], [[2020 - Unsupervised Cross-lingual Representation Learning at Scale - ACL Main 747]].

## Mục tiêu cần hiểu

- Token không giống word; tokenization là quyết định mô hình hoá có hệ quả lớn.
- BPE học vocabulary từ thống kê corpus, không nhất thiết khớp morpheme/ngữ nghĩa.
- Multilingual tokenization ảnh hưởng tới fairness, chi phí inference và chất lượng model.
- Cross-lingual transfer phụ thuộc vào representation, data balance và segmentation.

## Ý chính

- Một “word” có thể tách theo whitespace, morpheme, character, byte hoặc subword; mỗi cách có trade-off.
- LM thật sự thấy token IDs, không thấy text trực tiếp.
- BPE merge cặp token phổ biến, nên ngôn ngữ xuất hiện nhiều trong training thường có tokenization hiệu quả hơn.
- Tokenization có thể vỡ ở spelling variation, glitch tokens, script ít tài nguyên, hoặc ngôn ngữ có morphology khác tiếng Anh.
- Nếu cùng một ý cần nhiều token hơn ở ngôn ngữ A so với B, người dùng ngôn ngữ A có thể trả chi phí cao hơn và bị giới hạn context nặng hơn.

## BPE walkthrough

```text
text corpus
-> tách thành ký tự/byte ban đầu
-> đếm cặp liền nhau phổ biến
-> merge cặp phổ biến nhất
-> lặp đến vocab size
-> encode text mới bằng các token đã học
```

Ưu điểm:

- Giảm OOV.
- Giữ vocab hữu hạn.
- Dễ scale cho LM lớn.

Nhược điểm:

- Segment không luôn có nghĩa ngôn ngữ học.
- Có thể thiên lệch theo phân phối corpus.
- Có thể làm ngôn ngữ ít tài nguyên bị chia nhỏ quá mức.

## Multilinguality

Multilingual model cần chia capacity giữa nhiều ngôn ngữ. Nếu tokenization hoặc dữ liệu mất cân bằng, model có thể tốt ở ngôn ngữ high-resource nhưng yếu ở low-resource. Cross-lingual transfer hữu ích khi representation học được pattern chung, nhưng không đảm bảo công bằng tự động.

## Cách hiểu bằng lời của tôi

Tokenizer là “cửa vào” của LM. Nếu cửa vào chia một ngôn ngữ thành quá nhiều mảnh vụn, model phải dùng nhiều bước hơn để đọc cùng một nội dung. Vì vậy tokenization không chỉ là preprocessing kỹ thuật; nó ảnh hưởng tới chất lượng, chi phí và công bằng.

## Câu hỏi review

1. Vì sao token không đồng nhất với word?
2. BPE học vocabulary bằng quy tắc gì?
3. Vì sao tokenization có thể làm chi phí giữa ngôn ngữ khác nhau?
4. Multilingual tokenization ảnh hưởng tới low-resource languages ra sao?
5. Cross-lingual transfer có giới hạn gì?

## Liên kết

- [[Tokenization]]
- [[SentencePiece]]
- [[Multilingual Transformer]]
- [[Cross-Lingual Transfer]]
- [[Zero-shot Learning]]
- [[CS224N]]
