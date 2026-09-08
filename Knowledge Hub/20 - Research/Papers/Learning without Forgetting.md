---
type: paper
status: draft
title: "Learning without Forgetting"
aliases:
  - LwF
authors:
  - Zhizhong Li
  - Derek Hoiem
year: 2016
venue: "ECCV 2016 / IEEE TPAMI 2018"
url: "https://arxiv.org/abs/1606.09282"
pdf: "[[Learning without Forgetting.pdf]]"
citekey: li2016learning
doi: "10.1109/TPAMI.2017.2773081"
arxiv: "1606.09282"
code_url: "https://github.com/lizhitwo/LearningWithoutForgetting"
source_version: v3
topic:
  - continual learning
  - knowledge distillation
  - catastrophic forgetting
priority: high
reading_status: not-started
rating:
related_concepts:
  - "[[04 - Concepts/Continual Learning|Continual Learning]]"
  - "[[Knowledge Distillation]]"
  - "[[Catastrophic Forgetting]]"
  - "[[Continual Relation Extraction]]"
created_at: 2026-09-05
updated_at: 2026-09-08
tags:
  - paper
  - continual-learning
  - distillation
---

# Learning without Forgetting

## Tóm tắt một câu

Learning without Forgetting (LwF) là phương pháp học liên tục (continual learning) đột phá sử dụng phân phối dự đoán của mô hình cũ trên dữ liệu tác vụ mới làm mục tiêu chưng cất tri thức (knowledge distillation loss), giúp mạng nơ-ron học thêm các khả năng mới mà không bị quên các tác vụ cũ (catastrophic forgetting) và hoàn toàn không cần lưu trữ hay truy cập dữ liệu quá khứ. [[Learning without Forgetting.pdf#page=1|PDF, tr. 1]]

## Nguồn

- Paper gốc: ECCV 2016 (pp. 614–629); Bản mở rộng: IEEE TPAMI 2018 (Vol. 40, No. 12, pp. 2255–2268).
- arXiv: [1606.09282](https://arxiv.org/abs/1606.09282) (v3)
- PDF trong vault: [[Learning without Forgetting.pdf]]
- Mã nguồn chính thức: [lizhitwo/LearningWithoutForgetting](https://github.com/lizhitwo/LearningWithoutForgetting)

## Vấn đề paper giải quyết

Khi mở rộng hệ thống thị giác máy tính hoặc mô hình học sâu để thực hiện thêm các tác vụ mới theo thời gian, giả định thông thường là dữ liệu huấn luyện của toàn bộ các tác vụ cũ luôn có sẵn để huấn luyện đồng thời (Joint Training). Tuy nhiên, trong thực tế: [[Learning without Forgetting.pdf#page=1|PDF, tr. 1]]
1. Dữ liệu cũ có thể quá đồ sộ, tốn kém chi phí lưu trữ và thời gian huấn luyện lại từ đầu.
2. Dữ liệu cũ có thể bị ràng buộc bởi quyền riêng tư, bí mật thương mại, hoặc không được phép lưu trữ vĩnh viễn (proprietary/unrecorded data).
3. Nếu chỉ đơn thuần tinh chỉnh (Fine-tuning) mạng nơ-ron trên dữ liệu mới, mô hình sẽ gặp hiện tượng **Quên thảm khốc (Catastrophic Forgetting)** — hiệu năng trên các tác vụ ban đầu sụt giảm nghiêm trọng.
4. Nếu cố định đặc trưng (Feature Extraction - chỉ huấn luyện head mới), mô hình bảo toàn được tác vụ cũ nhưng hiệu năng trên tác vụ mới rất hạn chế vì các tầng chia sẻ không được tối ưu hóa cho tác vụ mới.

Paper đặt ra bài toán: **Làm thế nào để học thêm tác vụ mới trên mạng CNN chia sẻ tham số, tối ưu hóa biểu diễn cho tác vụ mới, mà vẫn bảo toàn hiệu năng trên các tác vụ cũ khi KHÔNG CÓ bất kỳ dữ liệu huấn luyện nào của tác vụ cũ?** [[Learning without Forgetting.pdf#page=1|PDF, tr. 1]] [[Learning without Forgetting.pdf#page=2|PDF, tr. 2]]

## Gap và đóng góp

- **Phương pháp LwF (Learning without Forgetting)**: Lần đầu tiên kết hợp ý tưởng Chưng cất tri thức ([[Distilling the Knowledge in a Neural Network|Knowledge Distillation - Hinton et al., 2015]]) vào bài toán Học liên tục mà không cần lưu trữ dữ liệu cũ (rehearsal-free continual learning).
- **Cơ chế ghi nhận phản hồi (Recorded Responses)**: Trước khi cập nhật trọng số, LwF dùng mạng nơ-ron ban đầu chạy feed-forward trên tập dữ liệu của tác vụ mới $X_n$ để thu được phân phối xác suất dự đoán $Y_o$ trên các nhãn cũ. $Y_o$ đóng vai trò là "nhãn mềm thay thế" (surrogate targets) để ràng buộc hành vi của mô hình. [[Learning without Forgetting.pdf#page=4|PDF, tr. 4]] [[Learning without Forgetting.pdf#page=5|PDF, tr. 5]]
- **Quy trình huấn luyện hai giai đoạn (Warm-up & Joint-Optimize)**:
  - *Warm-up*: Đóng băng các tầng chia sẻ $\theta_s$ và tầng cũ $\theta_o$, chỉ huấn luyện tầng tác vụ mới $\theta_n$ đến khi hội tụ để tránh việc khởi tạo ngẫu nhiên của $\theta_n$ tạo gradient lớn làm phá hỏng biểu diễn chia sẻ.
  - *Joint-Optimize*: Huấn luyện đồng thời tất cả các tham số $\{\theta_s, \theta_o, \theta_n\}$ với hàm mất mát kết hợp giữa hard-task loss (cho tác vụ mới) và distillation loss (cho tác vụ cũ). [[Learning without Forgetting.pdf#page=4|PDF, tr. 4]]
- **Hiệu quả thực nghiệm toàn diện**:
  - Trên tác vụ mới, LwF vượt trội hơn Feature Extraction và thậm chí vượt cả Fine-tuning tiêu chuẩn (do hàm distillation loss đóng vai trò như một bộ điều hòa regularizer ngăn overfitting).
  - Trên tác vụ cũ, LwF giữ vững độ chính xác vượt bậc so với Fine-tuning, đạt kết quả tiệm cận với Joint Training (vốn được xem là cận trên lý thuyết sử dụng toàn bộ dữ liệu cũ). [[Learning without Forgetting.pdf#page=6|PDF, tr. 6]] [[Learning without Forgetting.pdf#page=7|PDF, tr. 7]]
- **Phân tích điều kiện suy thoái (Failure Modes)**: Chỉ ra giới hạn bản chất của LwF khi phân phối dữ liệu mới $X_n$ quá khác biệt so với dữ liệu cũ (ví dụ: ImageNet $\to$ MNIST hoặc Places $\to$ CUB), dẫn đến việc dữ liệu mới không kích hoạt được các đặc trưng quan trọng của tác vụ cũ. [[Learning without Forgetting.pdf#page=7|PDF, tr. 7]]

## Bài toán/formalization

Mạng nơ-ron tích chập (CNN) ban đầu bao gồm:
- $\theta_s$: Các tham số chia sẻ (ví dụ: 5 tầng tích chập và 2 tầng fully-connected trong AlexNet).
- $\theta_o$: Các tham số chuyên biệt cho tác vụ cũ (output layer và trọng số kết nối với tầng chia sẻ cuối cùng).
- Mục tiêu: Thêm bộ tham số chuyên biệt $\theta_n$ cho tác vụ mới và học trên tập dữ liệu mới $\mathcal{D}_n = (X_n, Y_n)$ sao cho mô hình hoạt động tốt trên cả tác vụ cũ lẫn tác vụ mới, mà không cần dữ liệu cũ $\mathcal{D}_o$. [[Learning without Forgetting.pdf#page=4|PDF, tr. 4]]

### Quy trình toán học

1. **Khởi tạo và ghi nhận phản hồi cũ**:
   $$Y_o \leftarrow \text{CNN}(X_n; \theta_s, \theta_o)$$
   Khởi tạo ngẫu nhiên $\theta_n \sim \mathcal{N}(0, \sigma^2)$.

2. **Định nghĩa đầu ra dự đoán của mô hình hiện tại**:
   - Dự đoán trên tác vụ cũ: $\hat{Y}_o = \text{CNN}(X_n; \hat{\theta}_s, \hat{\theta}_o)$
   - Dự đoán trên tác vụ mới: $\hat{Y}_n = \text{CNN}(X_n; \hat{\theta}_s, \hat{\theta}_n)$

3. **Hàm mục tiêu tổng quát**:
   $$\theta_s^*, \theta_o^*, \theta_n^* = \arg\min_{\hat{\theta}_s, \hat{\theta}_o, \hat{\theta}_n} \Big( \mathcal{L}_{\text{new}}(Y_n, \hat{Y}_n) + \lambda_o \mathcal{L}_{\text{old}}(Y_o, \hat{Y}_o) + \mathcal{R}(\hat{\theta}_s, \hat{\theta}_o, \hat{\theta}_n) \Big)$$
   Trong đó:
   - $\mathcal{R}$ là hàm điều hòa suy giảm trọng số (weight decay, mặc định 0.0005).
   - $\lambda_o$ là trọng số cân bằng giữa tác vụ cũ và mới (mặc định $\lambda_o = 1$). [[Learning without Forgetting.pdf#page=4|PDF, tr. 4]] [[Learning without Forgetting.pdf#page=5|PDF, tr. 5]]

### Các thành phần hàm mất mát

1. **Mất mát tác vụ mới ($\mathcal{L}_{\text{new}}$)**: Sử dụng cross-entropy đa lớp thông thường:
   $$\mathcal{L}_{\text{new}}(y_n, \hat{y}_n) = - y_n \cdot \log \hat{y}_n = - \sum_{i} y_n^{(i)} \log \hat{y}_n^{(i)}$$
   với $\hat{y}_n = \text{softmax}(z_n)$ và $y_n$ là one-hot ground-truth vector. [[Learning without Forgetting.pdf#page=4|PDF, tr. 4]]

2. **Mất mát chưng cất tác vụ cũ ($\mathcal{L}_{\text{old}}$)**: Sử dụng modified cross-entropy với nhiệt độ làm mềm $T$:
   $$\mathcal{L}_{\text{old}}(y_o, \hat{y}_o) = - \sum_{i=1}^{l} y_o'^{(i)} \log \hat{y}_o'^{(i)}$$
   Trong đó xác suất được làm mềm ở nhiệt độ $T$ (paper chọn $T = 2$ thông qua grid search):
   $$y_o'^{(i)} = \frac{(y_o^{(i)})^{1/T}}{\sum_j (y_o^{(j)})^{1/T}}, \quad \hat{y}_o'^{(i)} = \frac{(\hat{y}_o^{(i)})^{1/T}}{\sum_j (\hat{y}_o^{(j)})^{1/T}}$$
   Việc chọn $T > 1$ giúp khuếch đại các xác suất nhỏ, ép mô hình mới phải ghi nhớ sự tương đồng giữa các lớp cũ thay vì chỉ chú ý vào lớp có xác suất cao nhất. [[Learning without Forgetting.pdf#page=4|PDF, tr. 4]] [[Learning without Forgetting.pdf#page=5|PDF, tr. 5]]

## Phương pháp

```text
[Dữ liệu tác vụ mới X_n]
        │
        ├─────────────────────────────────────────┐
        ▼ (Forward qua mạng cũ θ_s, θ_o)          ▼
[Ghi nhận nhãn mềm cũ Y_o]                 [Nhãn thật tác vụ mới Y_n]
        │                                         │
        ▼                                         ▼
[Forward qua mạng đang học]               [Forward qua mạng đang học]
  sinh ra logits cũ z_o                     sinh ra logits mới z_n
        │                                         │
        ▼ (Softmax tại T=2)                       ▼ (Softmax tại T=1)
  xác suất mềm ŷ'_o                         xác suất dự đoán ŷ_n
        │                                         │
        ▼                                         ▼
[Distillation Loss L_old]                  [Task Loss L_new]
        │                                         │
        └────────────────────┬────────────────────┘
                             ▼
               Loss tổng = L_new + λ_o L_old
                             │
                             ▼
         [Cập nhật đồng thời θ_s, θ_o, θ_n]
```

### So sánh vị thế với các hướng tiếp cận khác (Figure 1, Table 1)

| Phương pháp | Dữ liệu tác vụ cũ | Hiệu năng tác vụ mới | Hiệu năng tác vụ cũ | Bộ nhớ lưu trữ | Thời gian huấn luyện | Thời gian suy luận |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Fine-Tuning** | Không | Tốt | Kém (Quên nặng) | Vừa phải | Nhanh | Nhanh |
| **Duplicating & Fine-Tuning** | Không | Tốt | Hoàn hảo | Lớn ($\times m$ networks) | Nhanh | Chậm ($\times m$ lần) |
| **Feature Extraction** | Không | Trung bình | Hoàn hảo | Vừa phải | Rất nhanh | Nhanh |
| **Joint Training** | **Có (Bắt buộc)** | Tốt nhất | Rất tốt | Rất lớn (Lưu data cũ) | Rất chậm | Nhanh |
| **LwF (Đề xuất)** | **Không** | **Tốt nhất** | **Rất tốt** | **Vừa phải** | **Nhanh** | **Nhanh** |

[[Learning without Forgetting.pdf#page=2|PDF, tr. 2]]

## Protocol fingerprint

| Trường | Giá trị trong LwF |
|---|---|
| Tác vụ thực nghiệm | Phân loại ảnh (Image Classification) & Theo dõi đối tượng video (Tracking) |
| Bộ dữ liệu tác vụ cũ | ImageNet (1.000 lớp, ~1.2M ảnh) hoặc Places365-standard (365 lớp, ~1.8M ảnh) |
| Bộ dữ liệu tác vụ mới | PASCAL VOC 2012 (20 lớp, 5.717 ảnh train), CUB-200-2011 (200 loài chim, 5.994 ảnh train), MIT Indoor Scenes (67 cảnh, 5.360 ảnh train), MNIST (10 số viết tay) |
| Kiến trúc mạng | AlexNet (5 conv + 3 fc) làm mạng chính; mở rộng kiểm chứng trên VGG-16 |
| Tham số chưng cất | Nhiệt độ $T = 2$; trọng số cân bằng $\lambda_o = 1$ |
| Tối ưu hóa | SGD, momentum 0.9, weight decay 0.0005, dropout trên fully-connected layers |
| Giai đoạn huấn luyện | Bước 1: Warm-up chỉ train $\theta_n$ (lr = 0.001); Bước 2: Joint-optimize train $\{\theta_s, \theta_o, \theta_n\}$ (lr = 0.0001, giảm 10 lần sau mỗi số epochs cố định) |
| Độ đo | Mean Average Precision (mAP) cho VOC; Top-1 Accuracy cho tất cả các tập dữ liệu còn lại |
| Phân loại kết quả | Báo cáo từ bài báo gốc (`reported`/`observed`). Không tái lập nội bộ |

## Kết quả chính

### 1. Hiệu năng trong kịch bản thêm một tác vụ đơn lẻ (Bảng 1)

Bảng 1(a) báo cáo độ chênh lệch hiệu năng so với LwF trên kiến trúc AlexNet. Giá trị âm nghĩa là phương pháp so sánh kém hơn LwF: [[Learning without Forgetting.pdf#page=7|PDF, tr. 7]]

| Phương pháp | ImageNet $\to$ VOC | ImageNet $\to$ CUB | ImageNet $\to$ Scenes | Places365 $\to$ VOC | Places365 $\to$ CUB | Places365 $\to$ Scenes | ImageNet $\to$ MNIST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| | **Cũ / Mới** | **Cũ / Mới** | **Cũ / Mới** | **Cũ / Mới** | **Cũ / Mới** | **Cũ / Mới** | **Cũ / Mới** |
| **LwF (Bản thân)** | **56,2 / 76,1** | **54,7 / 57,7** | **55,9 / 64,5** | **50,6 / 70,2** | **47,9 / 34,8** | **50,9 / 75,2** | **49,8 / 99,3** |
| Fine-Tuning | -0,9 / -0,3 | -3,8 / -0,7 | -2,0 / -0,8 | -2,2 / +0,1 | -4,6 / +1,0 | -2,1 / -1,7 | -2,8 / 0,0 |
| LFL (Jung et al.) | 0,0 / -0,4 | -1,9 / -2,6 | -0,3 / -0,9 | +0,2 / -0,7 | +0,7 / -1,7 | -0,2 / -0,5 | -2,9 / -0,6 |
| Fine-tune FC | +0,5 / -0,7 | +0,2 / -3,9 | +0,6 / -2,1 | +0,5 / -1,3 | +1,8 / -4,9 | +0,3 / -1,1 | +7,0 / -0,2 |
| Feature Extraction | +0,8 / -0,5 | +2,3 / -5,2 | +1,2 / -3,3 | +1,1 / -1,4 | +3,8 / -12,3 | +0,8 / -1,7 | +7,3 / -0,8 |
| Joint Training | +0,7 / -0,2 | +0,6 / -1,1 | +0,5 / -0,6 | +0,7 / 0,0 | +2,3 / +1,5 | +0,3 / -0,3 | +7,2 / 0,0 |

*Quan sát mấu chốt*:
1. **LwF vượt Fine-tuning trên tác vụ mới**: Trên hầu hết các cặp tác vụ tương đồng (ImageNet $\to$ VOC, ImageNet $\to$ Scenes, Places $\to$ Scenes), LwF đạt độ chính xác tác vụ mới cao hơn cả Fine-tuning ($+0,3\%$ đến $+1,7\%$). Tín hiệu chưng cất từ tác vụ cũ đóng vai trò như một bộ điều hòa mạnh mẽ chống overfitting.
2. **Khả năng giữ tác vụ cũ**: LwF giảm thiểu tối đa hiện tượng quên so với Fine-tuning (Fine-tuning làm sụt giảm từ 2% đến gần 5% độ chính xác tác vụ cũ).
3. **Tiệm cận Joint Training**: LwF chỉ thua Joint Training khoảng $0,3\% - 0,7\%$ trên tác vụ cũ, dù hoàn toàn không dùng một mẫu dữ liệu cũ nào.

### 2. Kịch bản thêm tuần tự nhiều tác vụ (Figure 4)

Khi tuần tự thêm 3 phần dữ liệu của VOC vào Places365 (Places $\to \text{VOC}_1 \to \text{VOC}_2 \to \text{VOC}_3$) hoặc Scenes vào ImageNet: [[Learning without Forgetting.pdf#page=8|PDF, tr. 8]]
- Độ chính xác của Fine-tuning trên tác vụ gốc suy giảm dốc đứng qua từng tác vụ mới.
- LwF duy trì đường suy thoái rất phẳng, bảo vệ tác vụ gốc tốt hơn hẳn và bám sát đường biểu diễn của Joint Training.

### 3. Tác dụng của bước Warm-up (Bảng 2b)

| Thiết lập | ImageNet $\to$ CUB (Cũ / Mới) | ImageNet $\to$ Scenes (Cũ / Mới) | Places365 $\to$ VOC (Cũ / Mới) |
|---|:---:|:---:|:---:|
| **LwF có Warm-up** | **54,7 / 57,7** | **55,9 / 64,5** | **50,6 / 70,2** |
| LwF không Warm-up | 53,5 / 59,9 | 55,2 / 64,9 | 50,4 / 70,0 |
| **Fine-tuning có Warm-up** | **50,9 / 57,0** | **53,9 / 63,8** | **48,4 / 70,3** |
| Fine-tuning không Warm-up | 42,5 / 59,8 (-8,4% cũ) | 49,8 / 63,9 (-4,1% cũ) | 42,3 / 70,0 (-6,1% cũ) |

*Kết luận*: Nếu Fine-tuning không có bước Warm-up, tác vụ cũ bị xóa sổ nghiêm trọng (sụt giảm $6\% - 8,4\%$). LwF bền vững hơn nhiều: ngay cả khi không có Warm-up, độ sụt giảm của tác vụ cũ chỉ là $0,2\% - 1,2\%$. [[Learning without Forgetting.pdf#page=9|PDF, tr. 9]]

## Hạn chế, giả định, failure modes

- **Sự lệch pha phân phối (Distribution Mismatch / Dissimilar Tasks)**: LwF dựa trên giả định rằng việc ép phản hồi của mạng mới trên $X_n$ giống với mạng cũ sẽ gián tiếp bảo vệ vùng biểu diễn của tác vụ cũ. Nếu dữ liệu tác vụ mới $X_n$ hoàn toàn xa lạ so với $X_o$ (như ImageNet $\to$ MNIST):
  - Ảnh số viết tay đen trắng trên nền đen hoàn toàn không kích hoạt các bộ lọc kết cấu, màu sắc, hình thái tự nhiên của ImageNet.
  - Do đó, distillation loss trên MNIST không cung cấp được bất kỳ ràng buộc có ý nghĩa nào cho các vùng không gian đặc trưng của ImageNet, khiến tác vụ cũ bị tụt 7,2% so với Joint Training. [[Learning without Forgetting.pdf#page=7|PDF, tr. 7]]
- **Tích lũy sai số khi chuỗi tác vụ quá dài (Error Accumulation)**: Vì teacher của task sau chính là student của task trước, các sai lệch nhỏ trong việc xấp xỉ phân phối sẽ bị khuếch đại dần qua nhiều task liên tiếp nếu không có dữ liệu gốc để hiệu chỉnh lại ranh giới quyết định.
- **Phụ thuộc vào kiến trúc chia sẻ toàn phần (Shared Backbone)**: LwF buộc toàn bộ các tác vụ phải chen chúc trong cùng một tập trọng số $\theta_s$, dễ dẫn đến hiện tượng tắc nghẽn dung lượng (capacity bottleneck) khi số lượng tác vụ tăng lên hàng chục hoặc hàng trăm. [[Learning without Forgetting.pdf#page=11|PDF, tr. 11]]

## Đánh giá từ evidence

- **Ý nghĩa lịch sử**: LwF là bài báo kinh điển mở ra phân nhánh **Distillation-based Continual Learning** không cần bộ nhớ đệm (rehearsal-free). Nó chứng minh rằng không nhất thiết phải lưu dữ liệu cũ thì mới chống được quên.
- **Bằng chứng chặt chẽ**: So sánh công bằng trên cả mạng AlexNet và VGG-16, phân tích kỹ lưỡng ảnh hưởng của Warm-up, kích thước tập dữ liệu (3% đến 100%), và trọng số $\lambda_o$.

## Diễn giải học tập

### 1. Cơ chế cốt lõi: Vì sao Teacher chỉ biết nhãn cũ vẫn bảo vệ được mô hình?

Trong LwF, Teacher không cần biết gì về các nhãn mới. Khi một ảnh của task mới $x \in X_n$ đi qua Teacher, Teacher sẽ dự đoán phân phối xác suất trên toàn bộ các nhãn cũ.
- Phân phối này phản ánh vị trí tương đối của $x$ đối với các ranh giới quyết định cũ (decision boundaries).
- Bằng cách ép Student phải tạo ra phân phối y hệt trên các nhãn cũ, Student bị cấm không được làm biến dạng các góc chiếu hoặc dịch chuyển các mặt phẳng phân chia của các lớp cũ trong không gian đặc trưng chung $\theta_s$.

### 2. Mối liên hệ sống còn với Continual Relation Extraction (CRE / TAPTA)

Trong đề tài nghiên cứu **Continual Relation Extraction with Task-Aware Prompt Adaptation (TAPTA)**, LwF là nguồn cảm hứng trực tiếp cho nhánh Teacher-Student Knowledge Distillation.

Trả lời trực tiếp câu hỏi thiết kế trong `Reading Queue và Paper Decisions`:
> **"Hiểu teacher cũ trong continual learning: Teacher dùng để giữ old-label behavior như thế nào? Và áp dụng vào TAPTA ra sao?"**

#### Bài học từ LwF áp dụng vào TAPTA:
1. **Khắc phục điểm yếu Distribution Mismatch của LwF**:
   - Trong CRE, mỗi task mang đến các quan hệ mới trong các câu văn bản khác nhau. Nếu chỉ dùng LwF thuần túy trên Backbone của ngôn ngữ (PLM), câu của task mới có thể không chứa ngữ cảnh kích hoạt các quan hệ cũ.
   - Do đó, trong TAPTA, ta không thể chỉ dựa vào LwF trên toàn bộ câu mới. Cần kết hợp:
     * **Prompt Isolation**: Dùng Router để kích hoạt prompt riêng cho từng task, giảm tải việc chia sẻ toàn bộ trọng số như CNN của LwF.
     * **Similarity Distillation với Prototype cũ**: Thay vì ép khớp logits của một linear head (như LwF), ta ép student giữ nguyên phân phối độ tương đồng giữa đặc trưng câu và các **relation prototypes** cũ.
2. **Kỹ thuật Warm-up**:
   - Bài học từ Bảng 2(b) của LwF cho thấy: khi sang task mới, **bắt buộc phải có giai đoạn Warm-up** (chỉ train module mới / prompt mới của task hiện tại trước, đóng băng router và backbone cũ) trước khi mở khóa joint-optimization. Nếu không có warm-up, gradient khởi tạo ngẫu nhiên từ task mới sẽ phá hủy ngay lập tức các biểu diễn cũ đã ổn định.

## Ghi chú cá nhân

*(Bảo lưu ghi chú định hướng đề tài)*
- Student-Teacher KD trong đề tài là hậu duệ trực tiếp của LwF. Paper này giúp viết phần nền cho:
  - vì sao Teacher chỉ biết old labels vẫn có ích;
  - vì sao KD trên dữ liệu task mới có thể giữ old behavior;
  - giới hạn của KD khi dữ liệu task mới không kích hoạt old decision boundary.

## Câu hỏi review

### Câu 1: Ý tưởng cốt lõi của LwF là gì, và tại sao nó không cần dữ liệu của tác vụ cũ?
*Gợi ý trả lời*: LwF sử dụng chính dữ liệu của tác vụ mới $X_n$, đưa qua mô hình cũ để ghi nhận phân phối dự đoán trên các nhãn cũ $Y_o$. Khi huấn luyện mô hình mới, hàm mất mát chưng cất tri thức (Knowledge Distillation loss tại $T=2$) ép mô hình mới phải tái hiện lại phản hồi $Y_o$ này, qua đó duy trì hành vi trên các nhãn cũ mà không cần lưu trữ bất kỳ mẫu dữ liệu cũ nào.

### Câu 2: Bước Warm-up trong LwF đóng vai trò gì, và điều gì xảy ra nếu bỏ qua bước này?
*Gợi ý trả lời*: Warm-up là bước đóng băng các tầng chia sẻ $\theta_s$ và tầng cũ $\theta_o$, chỉ huấn luyện các tham số mới $\theta_n$ đến khi hội tụ. Nếu bỏ qua bước này, các trọng số ngẫu nhiên ban đầu của $\theta_n$ sẽ sinh ra gradient rất lớn làm xáo trộn các tầng chia sẻ $\theta_s$, khiến tác vụ cũ bị quên nghiêm trọng (trong thực nghiệm Fine-tuning, bỏ warm-up làm sụt giảm $6\% - 8,4\%$ độ chính xác tác vụ cũ).

### Câu 3: Khi nào LwF gặp thất bại nghiêm trọng nhất (Failure Mode)?
*Gợi ý trả lời*: LwF thất bại khi phân phối dữ liệu của tác vụ mới $X_n$ hoàn toàn xa lạ và không có điểm chung với dữ liệu cũ $X_o$ (ví dụ: chuyển từ ImageNet sang ảnh chữ số viết tay MNIST). Khi đó, các mẫu mới không kích hoạt được các đặc trưng ngữ nghĩa của tác vụ cũ, khiến tín hiệu distillation trên $X_n$ không thể bảo vệ được các ranh giới phân loại của tác vụ cũ.

### Câu 4: Tại sao trong nhiều kịch bản, LwF lại đạt kết quả trên tác vụ mới cao hơn cả Fine-tuning thông thường?
*Gợi ý trả lời*: Bởi vì hàm distillation loss trên các nhãn cũ đóng vai trò như một bộ điều hòa (regularizer) mạnh mẽ. Nó ngăn không cho mạng nơ-ron bị overfit vào tập dữ liệu hữu hạn của tác vụ mới, giữ cho không gian đặc trưng tổng quát hơn.

## Evidence map

| Luận điểm / Nội dung | Trang PDF | Bằng chứng cụ thể trong nguồn |
|---|---|---|
| Đặt bài toán & Bảng so sánh 5 phương pháp | [[Learning without Forgetting.pdf#page=2\|PDF, tr. 2]] | Figure 1: So sánh Fine-tuning, Duplicating, Feature Extraction, Joint Training và LwF |
| Kiến trúc mạng chia sẻ & Tách biệt $\theta_s, \theta_o, \theta_n$ | [[Learning without Forgetting.pdf#page=3\|PDF, tr. 3]] | Figure 2: Sơ đồ kiến trúc các tầng chia sẻ và tầng tác vụ |
| Thuật toán LwF & Công thức Distillation Loss ($T=2$) | [[Learning without Forgetting.pdf#page=4\|PDF, tr. 4-5]] | Mục 3, Eq. 1-4 & Figure 3: Khởi tạo, Warm-up và Joint optimization |
| Thiết lập thực nghiệm & Bộ dữ liệu (AlexNet, VGG) | [[Learning without Forgetting.pdf#page=6\|PDF, tr. 6]] | Mục 4: ImageNet, Places365, VOC, CUB, Scenes, MNIST |
| Bảng kết quả chính trên đơn tác vụ (Bảng 1) | [[Learning without Forgetting.pdf#page=7\|PDF, tr. 7]] | Table 1: LwF vượt Fine-tuning trên task mới và giữ vững task cũ |
| Phân tích thất bại trên tác vụ lệch pha (MNIST) | [[Learning without Forgetting.pdf#page=7\|PDF, tr. 7]] | Mục 4.1: ImageNet $\to$ MNIST tụt 7,2% do thiếu kích hoạt đặc trưng cũ |
| Kết quả thêm tuần tự nhiều tác vụ | [[Learning without Forgetting.pdf#page=8\|PDF, tr. 8]] | Figure 4: Đường cong suy thoái hiệu năng qua chuỗi 3 task liên tiếp |
| Ảnh hưởng của bước Warm-up | [[Learning without Forgetting.pdf#page=9\|PDF, tr. 9]] | Table 2(b): Fine-tuning mất $6-8\%$ nếu không warm-up; LwF duy trì ổn định |
| Đánh đổi hiệu năng qua trọng số $\lambda_o$ | [[Learning without Forgetting.pdf#page=10\|PDF, tr. 10]] | Figure 7: Đồ thị Pareto trade-off giữa tác vụ cũ và tác vụ mới |

## Liên kết

- Khái niệm: [[04 - Concepts/Continual Learning|Continual Learning]], [[Knowledge Distillation]], [[Catastrophic Forgetting]], [[Continual Relation Extraction]]
- Papers liên quan trực tiếp:
  - [[Distilling the Knowledge in a Neural Network|Distilling the Knowledge in a Neural Network (Hinton et al., 2015)]]
  - [[Mean Teachers are Better Role Models|Mean Teachers are Better Role Models]]
  - [[Serial Contrastive Knowledge Distillation for Continual Few-shot Relation Extraction|SCKD]]
- Kế hoạch đọc & Quyết định: [[Reading Queue và Paper Decisions]]
