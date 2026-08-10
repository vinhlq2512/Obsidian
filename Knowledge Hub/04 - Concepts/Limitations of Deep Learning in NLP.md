---
type: concept
status: seed
sources:
  - "[[Practical NLP - Chapter 01 - NLP A Primer]]"
source_sections:
  - "[[Practical NLP - Chapter 01 - NLP A Primer]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - deep-learning
  - nlp
---

# Limitations of Deep Learning in NLP

## Định nghĩa

Dù Deep Learning (như Transformer, BERT, LSTM) đã mang lại sự đột phá lớn trong xử lý ngôn ngữ tự nhiên (NLP) trên các bộ benchmark, nhưng trong môi trường công nghiệp thực tế, nó chưa phải là "silver bullet" (giải pháp vạn năng) vì những giới hạn sau:

1. **Overfitting trên dữ liệu nhỏ**: Các mô hình DL có hàng triệu/tỷ tham số, nên chúng rất dễ bị overfit nếu tập dữ liệu huấn luyện (training data) quá nhỏ, dẫn đến khả năng tổng quát hóa kém trong production.
2. **Thiếu khả năng Few-shot learning**: Dù Computer Vision đã làm khá tốt việc học với ít dữ liệu hoặc dùng dữ liệu tổng hợp (synthetic data), NLP vẫn gặp khó khăn trong việc tạo ra dữ liệu tổng hợp chất lượng cao, khiến chi phí gán nhãn rất đắt đỏ.
3. **Domain Adaptation kém**: Mô hình huấn luyện trên bài báo, wikipedia sẽ giảm sút hiệu năng trầm trọng khi áp dụng vào các domain đặc thù như Y tế, Pháp lý hoặc mạng xã hội.
4. **Tính giải thích (Interpretability) thấp**: Mô hình DL hoạt động như "black-box". Khác với Heuristics hay Naive Bayes (dễ dàng biết từ nào ảnh hưởng đến quyết định), DL khó giải thích nguyên nhân dự đoán cho end-user.
5. **Thiếu Common sense và World knowledge**: Ngôn ngữ đòi hỏi khả năng suy luận logic và kiến thức thế giới (VD: "John đi ra vườn" -> "John không còn ở trong phòng"). Các mô hình DL hiện tại phần lớn mới học được các biểu diễn thống kê (statistical representations) chứ chưa có khả năng suy luận (reasoning) thực sự vững chắc.
6. **Chi phí đắt đỏ**: Cần lượng data khổng lồ, chi phí GPU huấn luyện lớn, latency khi inference cao, và đòi hỏi nhiều công sức maintain (Technical debt).
7. **Khó đưa lên On-device**: Khó triển khai trực tiếp lên các thiết bị hạn chế về phần cứng, pin, và bộ nhớ (như thiết bị di động không có internet).

## Cách hiểu bằng lời của tôi

Trong nghiên cứu, Deep Learning luôn là "ngôi sao", nhưng khi đem vào làm sản phẩm thực tế, kỹ sư phải đối mặt với các bài toán về kinh tế (tiền GPU, thời gian, công sức gán nhãn) và tính an toàn (có giải thích được lỗi sai hay không). Đó là lúc mà Heuristics/Rules hoặc các mô hình Machine Learning truyền thống vẫn giữ vị thế quan trọng, ít nhất là dùng để che lấp lỗ hổng cho Deep Learning.

## Cần biết

- Khi bắt đầu một dự án NLP thực tế, thay vì nhảy vào dùng Deep Learning ngay, hãy bắt đầu bằng Heuristics hoặc các mô hình ML đơn giản (như Naive Bayes, SVM) để làm baseline, hiểu rõ data và giải quyết nhanh các "low-hanging fruit".

## Liên kết

- [[Language AI]]
- [[Neural NLP]]
