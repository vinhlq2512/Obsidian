---
type: concept
status: understood
sources:
  - "[[2026-07-14_how-llms-learn-to-be-helpful-rlhf-vs-dpo]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - alignment
  - preference-learning
---

# Direct Preference Optimization

## Định nghĩa

Direct Preference Optimization (DPO) là phương pháp căn chỉnh (alignment) mô hình ngôn ngữ lớn dựa trên dữ liệu ưu tiên của con người (preference pair: $y_w$ - preferred vs $y_l$ - dispreferred) bằng cách tối ưu hóa trực tiếp policy loss mà không cần huấn luyện một Reward Model riêng biệt hay sử dụng thuật toán Reinforcement Learning (như PPO).

## Cách hiểu bằng lời của tôi

RLHF truyền thống phải huấn luyện 2 bước: học Reward Model từ cặp đáp án $y_w/y_l$, rồi dùng PPO đẩy policy LLM về phía reward cao. DPO toán học hóa để chứng minh rằng ta có thể trích xuất ẩn Reward Model trực tiếp từ chính Policy LLM. Nhờ đó, bài toán RL phức tạp biến thành bài toán Classification Loss đơn giản, ổn định và nhanh hơn rất nhiều.

## Công thức & Cơ chế

DPO tối ưu hóa hàm mất mát (Loss function):

$$\mathcal{L}_{\text{DPO}}(\pi_\theta; \pi_{\text{ref}}) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)} \right) \right]$$

- $\pi_\theta$: Mô hình policy đang huấn luyện.
- $\pi_{\text{ref}}$: Mô hình SFT gốc (reference policy).
- $\beta$: Hệ số điều khiển mức độ lệch khỏi reference model.

## So sánh với RLHF (PPO)

| Tiêu chí | RLHF (PPO) | DPO |
| :--- | :--- | :--- |
| **Thành phần** | Policy, Value Network, Reward Model | Chỉ Policy + Reference Model |
| **Độ ổn định** | Nhạy cảm với hyperparameter, dễ collapse | Rất ổn định (supervised loss) |
| **Chi phí tính toán** | Cao (cần giữ nhiều model trong VRAM) | Thấp (chỉ load Policy + Ref model) |
| **Chất lượng** | Cao trên bài toán open-ended phức tạp | Tương đương hoặc vượt trội trên đa số task |

## Trade-off

- **Phụ thuộc dữ liệu**: DPO nhạy cảm với chất lượng cặp dữ liệu $y_w/y_l$.
- **Overshooting**: Nếu không điều chỉnh $\beta$ phù hợp, DPO có thể phạt quá mức các token phổ biến.

## Liên kết

- [[Preference Learning]]
- [[Model Alignment]]
- [[LLM Agent]]
- [[Production LLM System Design]]
