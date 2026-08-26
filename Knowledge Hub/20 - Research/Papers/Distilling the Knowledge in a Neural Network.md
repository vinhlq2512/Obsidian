---
type: paper
status: draft
title: Distilling the Knowledge in a Neural Network
authors:
  - Geoffrey Hinton
  - Oriol Vinyals
  - Jeff Dean
year: 2015
venue: NIPS 2014 Deep Learning Workshop
url: https://arxiv.org/abs/1503.02531
pdf: "[[Distilling the Knowledge in a Neural Network.pdf]]"
doi:
arxiv: "1503.02531"
source_version: v1
topic:
  - model-compression
  - knowledge-distillation
  - ensemble-learning
priority: medium
reading_status: not-started
rating:
related_concepts:
  - "[[Knowledge Distillation]]"
  - "[[KL Divergence]]"
created_at: 2026-08-26
updated_at: 2026-08-26
tags:
  - paper
  - model-compression
  - distillation
---

# Distilling the Knowledge in a Neural Network

## Tóm tắt một câu

Paper đề xuất huấn luyện một model nhỏ bằng soft targets từ một model/ensemble lớn ở temperature cao, nhờ đó chuyển phần "cách generalize" của model lớn sang student dễ deploy hơn. [[Distilling the Knowledge in a Neural Network.pdf#page=2|PDF tr. 2]]

## Nguồn

- arXiv: [1503.02531](https://arxiv.org/abs/1503.02531), version v1, published 2015-03-09.
- PDF local: [[Distilling the Knowledge in a Neural Network.pdf]]
- Venue/comment trên arXiv: NIPS 2014 Deep Learning Workshop.

## Vấn đề paper giải quyết

Ensemble hoặc model rất lớn thường generalize tốt hơn model đơn, nhưng inference bằng cả ensemble quá đắt để deploy rộng rãi. Paper đặt bài toán: có thể train model "cumbersome" thật mạnh ở giai đoạn training, rồi chuyển knowledge sang model nhỏ hơn cho deployment không? [[Distilling the Knowledge in a Neural Network.pdf#page=1|PDF tr. 1]]

Điểm quan trọng là paper không đồng nhất knowledge với trọng số của model. Knowledge được nhìn như mapping đã học từ input vectors sang output vectors, tức hành vi dự đoán và cách model phân bổ xác suất giữa các class. [[Distilling the Knowledge in a Neural Network.pdf#page=1|PDF tr. 1]]

## Gap và đóng góp

- Paper phát triển hướng model compression của Bucilua, Caruana, và Niculescu-Mizil bằng kỹ thuật softmax temperature thay vì chỉ match logits trực tiếp. [[Distilling the Knowledge in a Neural Network.pdf#page=2|PDF tr. 2]]
- Paper formalize vì sao matching logits là trường hợp đặc biệt của distillation khi temperature cao và logits được zero-mean theo từng case. [[Distilling the Knowledge in a Neural Network.pdf#page=3|PDF tr. 3]]
- Paper báo cáo kết quả trên MNIST và speech recognition: single distilled model có thể giữ phần lớn lợi ích của ensemble trong khi dễ deploy hơn. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]], [[Distilling the Knowledge in a Neural Network.pdf#page=5|PDF tr. 5]]
- Paper giới thiệu ensemble gồm generalist và nhiều specialist models cho bài toán rất nhiều class, nơi specialist tập trung vào các nhóm class dễ nhầm. [[Distilling the Knowledge in a Neural Network.pdf#page=6|PDF tr. 6]]

## Bài toán/formalization

Model tạo xác suất class bằng softmax trên logit `z_i`:

$$
q_i = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}
$$

Trong đó `T` là temperature. Khi `T = 1`, đây là softmax thông thường; khi `T` lớn hơn, phân phối xác suất mềm hơn và để lộ quan hệ giữa các class phụ. [[Distilling the Knowledge in a Neural Network.pdf#page=2|PDF tr. 2]]

Trong distillation, teacher/cumbersome model sinh soft target distribution ở temperature cao. Student được train để khớp phân phối đó, cũng ở temperature cao; sau khi train xong, student dùng temperature 1 khi inference. [[Distilling the Knowledge in a Neural Network.pdf#page=3|PDF tr. 3]]

Nếu có nhãn thật, objective của student kết hợp:

- cross entropy với soft targets ở temperature cao;
- cross entropy với hard labels ở temperature 1;
- soft-target gradient cần nhân với `T^2` khi phối hợp hard và soft targets để giữ tương quan đóng góp khi đổi temperature. [[Distilling the Knowledge in a Neural Network.pdf#page=3|PDF tr. 3]]

## Phương pháp

Quy trình cốt lõi:

```text
Train cumbersome model hoặc ensemble
-> Sinh soft targets trên transfer set bằng temperature cao
-> Train distilled/student model để khớp soft targets
-> Nếu có nhãn thật, thêm hard-label objective với weight thấp hơn
-> Deploy student ở temperature 1
```

Soft targets chứa nhiều thông tin hơn hard labels vì teacher không chỉ nói class đúng, mà còn nói các class sai nào gần đúng hơn các class sai khác. Ví dụ paper dùng trực giác digit `2` có thể giống `3` hơn `7` trong một case, nhưng ngược lại ở case khác. [[Distilling the Knowledge in a Neural Network.pdf#page=2|PDF tr. 2]]

## Mental model

Một cách diễn giải có thể là: hard label chỉ là "đáp án cuối", còn soft target là "bản đồ nhầm lẫn có cấu trúc" của teacher. Student học bản đồ này nên không chỉ học decision boundary từ nhãn thật, mà học cách teacher generalize quanh các vùng nhập liệu mơ hồ. [[Distilling the Knowledge in a Neural Network.pdf#page=2|PDF tr. 2]]

## Công thức quan trọng

Với teacher logits `v_i`, student logits `z_i`, soft target probability `p_i`, student probability `q_i`, gradient cross entropy theo student logit là:

$$
\frac{\partial C}{\partial z_i} = \frac{1}{T}(q_i - p_i)
$$

Khi temperature cao so với độ lớn logits và logits được zero-mean theo từng transfer case:

$$
\frac{\partial C}{\partial z_i} \approx \frac{1}{NT^2}(z_i - v_i)
$$

Vì vậy, trong giới hạn temperature cao, distillation tương đương tối thiểu hóa sai khác bình phương giữa student logits và teacher logits. Ở temperature thấp hơn, objective ít ép student khớp các logit âm rất lớn, có thể hữu ích nếu các logit đó nhiễu. [[Distilling the Knowledge in a Neural Network.pdf#page=3|PDF tr. 3]]

## Experimental setup

### MNIST

- Teacher/cumbersome model: một neural net lớn, 2 hidden layers, mỗi layer 1200 ReLU units, regularized bằng dropout và weight constraints; input images được jitter tối đa 2 pixels. [[Distilling the Knowledge in a Neural Network.pdf#page=3|PDF tr. 3]]
- Student: network nhỏ hơn, 2 hidden layers, 800 ReLU units, không regularization trong baseline thường. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]
- Distillation: student match soft targets của large net ở temperature 20. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]

### Speech recognition

- Task: acoustic model trong ASR, dự đoán HMM state từ acoustic observations. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]
- Architecture: DNN 8 hidden layers, mỗi layer 2560 ReLU units, softmax 14,000 labels, khoảng 85M parameters. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]
- Data: khoảng 2000 giờ spoken English, khoảng 700M training examples. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]
- Distillation: ensemble 10 model cùng architecture; thử temperature `[1, 2, 5, 10]`, hard-target cross entropy có relative weight 0.5. [[Distilling the Knowledge in a Neural Network.pdf#page=5|PDF tr. 5]]

### JFT specialists

- Dataset: JFT nội bộ của Google, 100M labeled images, 15,000 labels. [[Distilling the Knowledge in a Neural Network.pdf#page=5|PDF tr. 5]]
- Specialist models: mỗi specialist tập trung vào subset class dễ nhầm, các class còn lại gộp thành dustbin class; specialist được khởi tạo từ generalist. [[Distilling the Knowledge in a Neural Network.pdf#page=6|PDF tr. 6]]
- Clustering: paper dùng covariance matrix của predictions từ generalist để tìm nhóm class hay được dự đoán cùng nhau. [[Distilling the Knowledge in a Neural Network.pdf#page=6|PDF tr. 6]]

## Protocol fingerprint

| Thành phần | Giá trị |
|---|---|
| Nhiệm vụ chính | Classification / acoustic modeling / large-class image classification |
| Teacher | Large regularized model hoặc ensemble 10 DNNs; với JFT có generalist + specialists |
| Student | Single distilled model, thường dễ deploy hơn ensemble |
| Tín hiệu học | Soft targets từ teacher ở temperature cao, đôi khi kết hợp hard labels |
| Metrics | MNIST test errors; speech frame accuracy và WER; JFT top-1 accuracy |
| Reproduced local | Không. Các số dưới đây là `reported/observed` từ paper |

## Kết quả chính

### MNIST

Paper báo cáo large regularized net đạt 67 test errors; small net baseline đạt 146 errors; small net distilled ở temperature 20 đạt 74 errors. Đây là evidence rằng soft targets chuyển được nhiều knowledge từ model lớn sang model nhỏ. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]

Một thí nghiệm thú vị là bỏ toàn bộ digit `3` khỏi transfer set. Distilled model vẫn có thể nhận ra phần lớn các số 3 sau khi chỉnh bias class 3, cho thấy soft targets từ các ví dụ khác vẫn mang thông tin về quan hệ class. Đây là kết quả `reported`, không phải tái lập local. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]

### Speech recognition

| System | Test frame accuracy | WER |
|---|---:|---:|
| Baseline | 58.9% | 10.9% |
| 10x Ensemble | 61.1% | 10.7% |
| Distilled single model | 60.8% | 10.7% |

Table 1 cho thấy distilled single model gần bằng ensemble trên WER và chuyển hơn 80% improvement frame accuracy của ensemble sang model đơn. [[Distilling the Knowledge in a Neural Network.pdf#page=5|PDF tr. 5]]

### JFT specialists

Với 61 specialist models, paper báo cáo top-1 test accuracy tăng từ 25.0% lên 26.1%, tức 4.4% relative improvement. Đây là ensemble specialist result, và paper nói chưa chứng minh được việc distill specialist knowledge trở lại single large net. [[Distilling the Knowledge in a Neural Network.pdf#page=7|PDF tr. 7]], [[Distilling the Knowledge in a Neural Network.pdf#page=8|PDF tr. 8]]

## Ablation và phân tích

- MNIST: khi student có từ 300 units/layer trở lên, temperature trên 8 cho kết quả khá giống nhau; khi student rất nhỏ, 30 units/layer, temperature khoảng 2.5-4 tốt hơn temperature quá cao hoặc quá thấp. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]
- Speech low-data: với chỉ 3% training set, hard targets dẫn tới overfitting nặng; soft targets đạt test frame accuracy 57.0%, gần với baseline train trên 100% data là 58.9%. Paper dùng kết quả này để lập luận soft targets hoạt động như regularizer mạnh. [[Distilling the Knowledge in a Neural Network.pdf#page=7|PDF tr. 7]], [[Distilling the Knowledge in a Neural Network.pdf#page=8|PDF tr. 8]]
- Specialist models: Table 4 cho thấy relative accuracy change thường tăng khi class đúng được nhiều specialists cover hơn, nhưng đây là phân tích trên JFT nội bộ và không dễ kiểm chứng lại từ nguồn public. [[Distilling the Knowledge in a Neural Network.pdf#page=7|PDF tr. 7]]

## Hạn chế, giả định, failure modes

- Nhiều kết quả mạnh dùng dữ liệu hoặc hệ thống nội bộ của Google như Android voice search acoustic model và JFT, nên khả năng tái lập độc lập bị giới hạn. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]], [[Distilling the Knowledge in a Neural Network.pdf#page=5|PDF tr. 5]]
- Student cần đủ capacity. Paper quan sát temperature tối ưu thay đổi khi student quá nhỏ, gợi ý rằng không phải cứ làm mềm hơn là tốt hơn. [[Distilling the Knowledge in a Neural Network.pdf#page=4|PDF tr. 4]]
- Distillation có thể truyền cách generalize của teacher, nhưng nếu teacher sai hoặc dữ liệu transfer không đại diện, student cũng có thể học sai theo.
- Với specialists, paper báo cáo improvement khi dùng ensemble specialists nhưng chưa chứng minh distill được toàn bộ knowledge của specialists trở lại một single large net. [[Distilling the Knowledge in a Neural Network.pdf#page=8|PDF tr. 8]]

## Đánh giá từ evidence

Evidence mạnh nhất của paper là cơ chế đơn giản, formalization rõ, và kết quả nhất quán ở nhiều setting: MNIST, speech recognition, low-data regularization, và JFT specialists. Tuy nhiên, phần speech/JFT phụ thuộc dataset nội bộ và thiếu chi tiết hiện đại về seed/variance, nên nên đọc các con số là `reported` thay vì benchmark tái lập được ngay.

Một điểm đáng giữ khi học là: giá trị của distillation không chỉ nằm ở nén model, mà nằm ở việc soft targets truyền cấu trúc tương tự và regularities mà hard labels không biểu diễn được. [[Distilling the Knowledge in a Neural Network.pdf#page=2|PDF tr. 2]], [[Distilling the Knowledge in a Neural Network.pdf#page=8|PDF tr. 8]]

## Diễn giải học tập

Paper này là nền tảng của [[Knowledge Distillation]] hiện đại. Nếu nhìn bằng lens production, nó tách training-time computation khỏi serving-time computation: ta có thể cho phép teacher/ensemble đắt đỏ học thật kỹ, rồi chuyển hành vi cần thiết sang student rẻ hơn.

Nếu nhìn bằng lens representation, soft targets là một dạng label giàu thông tin. Với một ảnh digit, hard label chỉ nói "đây là 2"; soft target còn nói "nó giống 3 hơn 7 bao nhiêu". Đó là "dark knowledge" mà student nhận được từ teacher.

## Ghi chú cá nhân


## Câu hỏi review

1. Vì sao soft targets chứa nhiều thông tin hơn hard labels?
2. Temperature cao làm thay đổi phân phối softmax như thế nào?
3. Vì sao matching logits có thể xem là trường hợp đặc biệt của distillation?
4. Trong objective có cả hard và soft targets, vì sao cần nhân soft-target gradients với `T^2`?
5. Kết quả MNIST bỏ digit `3` khỏi transfer set cho thấy điều gì về tri thức trong soft targets?
6. Vì sao distilled single speech model dễ deploy hơn ensemble 10 models?
7. Specialist models khác mixture of experts ở đâu về training parallelism?
8. Những phần nào của paper khó tái lập vì dùng dữ liệu/hệ thống nội bộ?

## Gợi ý trả lời câu hỏi review

1. Soft targets giữ phân phối xác suất trên mọi class, nên biểu diễn quan hệ nhầm lẫn và similarity mà hard label không có.
2. Temperature cao làm phân phối phẳng hơn, giúp các xác suất nhỏ bớt bị triệt tiêu.
3. Ở giới hạn temperature cao, gradient cross entropy theo soft targets xấp xỉ tỉ lệ với sai khác giữa student logits và teacher logits.
4. Gradient từ soft targets scale theo `1/T^2`, nên nhân `T^2` giúp giữ tương quan đóng góp khi thay đổi temperature.
5. Teacher có thể truyền cấu trúc class gián tiếp qua soft targets, ngay cả khi transfer set thiếu trực tiếp một class.
6. Student là một model đơn, tránh chi phí chạy và averaging cả ensemble ở inference.
7. Specialists được train độc lập sau khi generalist xác định nhóm class dễ nhầm, còn mixture of experts cần gating network và assignment thay đổi đồng thời trong training.
8. Speech system và JFT là nội bộ; paper thiếu artifact public đủ để tái lập đầy đủ các kết quả đó.

## Cần đọc tiếp

- Bucilua, Caruana, Niculescu-Mizil 2006: `Model compression`.
- Các biến thể distillation hiện đại cho LLM: logit distillation, sequence-level distillation, on-policy/self-distillation.
- Các paper về teacher-student capacity gap và teacher assistant distillation.

## Evidence map

| Claim / phần note | Link | Evidence |
|---|---|---|
| Distillation chuyển knowledge từ cumbersome model sang deployable small model | [[Distilling the Knowledge in a Neural Network.pdf#page=1]] | Introduction định nghĩa motivation và deployment constraint |
| Soft targets chứa similarity structure giữa class | [[Distilling the Knowledge in a Neural Network.pdf#page=2]] | Ví dụ BMW/garbage truck/carrot và digit `2` giống `3`/`7` |
| Softmax temperature và objective distillation | [[Distilling the Knowledge in a Neural Network.pdf#page=2]] | Equation 1 và mô tả temperature |
| Matching logits là special case | [[Distilling the Knowledge in a Neural Network.pdf#page=3]] | Equations 2-4 |
| MNIST distilled student gần large net hơn small baseline | [[Distilling the Knowledge in a Neural Network.pdf#page=4]] | 67/146/74 test errors |
| Speech recognition distilled model gần ensemble | [[Distilling the Knowledge in a Neural Network.pdf#page=5]] | Table 1 |
| Specialist model setup trên JFT | [[Distilling the Knowledge in a Neural Network.pdf#page=6]] | Specialist/dustbin/clustering setup |
| JFT specialist improvement | [[Distilling the Knowledge in a Neural Network.pdf#page=7]] | Tables 3-4 |
| Soft targets như regularizer low-data | [[Distilling the Knowledge in a Neural Network.pdf#page=8]] | Table 5 |
| Paper chưa distill specialist knowledge về single large net | [[Distilling the Knowledge in a Neural Network.pdf#page=8]] | Discussion caveat |

## Liên kết

- [[Knowledge Distillation]]
- [[KL Divergence]]
- [[Model Distillation]]
- [[Transformer Inference Optimization]]
- [[Model Benchmarking]]
