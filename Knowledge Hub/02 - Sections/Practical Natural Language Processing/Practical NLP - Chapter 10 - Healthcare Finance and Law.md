---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: planned
chapter: 10
start_page: 601
end_page: 652
reading_date: 2026-08-21
planned_sessions:
  - "2026-08-21 | 601-617 | Healthcare NLP, medical records, decision support | 55 phút"
  - "2026-08-22 | 618-637 | Mental health, medical IE, finance/law mở đầu | 55 phút"
  - "2026-08-23 | 638-652 | Finance NLP, legal NLP, risk | 55 phút"
tags:
  - nlp
  - practical-nlp
  - domain-nlp
---

# Practical NLP - Chapter 10 - Healthcare Finance and Law

## Mục tiêu cần hiểu

- Domain NLP trong healthcare, finance và law bị ràng buộc mạnh bởi dữ liệu nhạy cảm, thuật ngữ chuyên ngành và yêu cầu độ tin cậy.
- EHR, clinical decision support, pharmacovigilance, financial/legal NLP có failure cost cao hơn task thông thường.
- Cần tách rõ use case, dữ liệu, rủi ro và yêu cầu kiểm định.

## Định nghĩa quan trọng

- Healthcare NLP
- Electronic Health Records
- Pharmacovigilance
- Clinical decision support
- Medical information extraction
- Financial NLP
- Legal NLP

## Mental model

```text
Domain text nhạy cảm
-> domain schema / terminology
-> extraction / classification / retrieval
-> human review
-> audit / compliance
```

## Phần cần biết

- Chapter này nên đọc với tư duy risk management.
- Không đưa claim ngoài nguồn; nếu có ý áp dụng thực tế, ghi rõ là câu hỏi hoặc giả thuyết.

## Câu hỏi review

1. Vì sao healthcare/legal NLP không thể chỉ tối ưu accuracy trung bình?
2. Domain terminology làm khó tokenizer, representation hoặc label space như thế nào?
3. Khi nào cần human-in-the-loop?

## Gợi ý trả lời câu hỏi review

- Trả lời bằng risk, auditability, domain expert review và hậu quả của false positive/false negative.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Information Extraction]]
