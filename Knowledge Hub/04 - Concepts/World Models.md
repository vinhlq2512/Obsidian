---
type: concept
status: understood
sources:
  - "[[2026-07-21_inside-robloxs-bet-on-world-models]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai
  - world-models
  - spatial-computing
  - multimodal
---

# World Models

## Định nghĩa

World Models (Mô hình thế giới) là lớp mô hình AI sinh (Generative AI) được huấn luyện để xây dựng representation nội tại về quy luật vật lý, hình học không gian 3D, sự tương tác vật thể và sự tiến triển theo thời gian của môi trường thực tế hoặc môi trường mô phỏng.

## Cách hiểu bằng lời của tôi

Nếu LLM hiểu thế giới thông qua chuỗi văn bản (1D text sequence), thì World Model hiểu thế giới thông qua vật lý không gian 3D và thời gian (4D spacetime). Nó có thể dự đoán điều gì sẽ xảy ra tiếp theo khi một lực tác động lên vật thể, làm thế nào để sinh ra cả một môi trường 3D tương tác được (như Roblox hay Sora) chỉ từ câu lệnh văn bản.

## Ứng dụng trọng tâm

```text
Prompt / Action
-> Spatial 3D Latent Representation
-> Physics Engine Simulation & Temporal Dynamics
-> Rendered Interactive 3D World / Video
```

- **Spatial Computing & Gaming**: Roblox dùng World Models để giúp creator gõ prompt là sinh ra toàn bộ thế giới 3D với quy luật vật lý (trọng lực, ma sát, ánh sáng) sẵn có.
- **Autonomous Driving & Robotics**: Tesla, Wayve dùng World Models để giả lập hàng triệu kịch bản lái xe nguy hiểm trong không gian ảo trước khi cho xe thật chạy ngoài đời.

## Trade-off

- Vốn đầu tư hạ tầng tính toán (GPU/TPU) khổng lồ để render và train 3D latent spaces.
- Latency sinh môi trường 3D realtime vẫn là rào cản lớn so với game engine truyền thống.

## Liên kết

- [[Multimodal LLM]]
- [[AI Hardware Accelerator]]
- [[Multimodal Search]]
