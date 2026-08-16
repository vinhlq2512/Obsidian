---
type: concept
status: seed
sources:
  - "[[2026-03-17_how-reddit-migrated-petabyte-scale-kafka-from-ec2-to-kuberne]]"
  - "[[2025-04-02_how-slack-rebuilt-a-critical-system-without-stopping-the-wor]]"
source_sections:
  - "[[2026-03-17_how-reddit-migrated-petabyte-scale-kafka-from-ec2-to-kuberne]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - migration
  - infrastructure
---

# Zero-Downtime Infrastructure Migration

## Định nghĩa

[[Zero-Downtime Infrastructure Migration]] là migration thay đổi hạ tầng bên dưới mà không làm client ngừng hoạt động, không mất dữ liệu và có đường rollback ở từng bước.

## Cách hiểu bằng lời của tôi

Migration lớn không nên là một cú cutover đẹp trên giấy nhưng nguy hiểm ngoài đời. Cách an toàn hơn là thêm abstraction layer, chạy hai thế giới song song, chuyển traffic/state từng phần, đo liên tục, và đảm bảo mỗi bước có thể pause hoặc đảo ngược.

## Pattern từ Reddit Kafka

- Đặt DNS facade giữa client và broker để tách client config khỏi physical broker.
- Bắt buộc broker mới join logical cluster cũ thay vì dựng cluster mới rồi replay.
- Chuyển broker ID/data/leadership từng phần bằng tooling rebalance.
- Tách data plane migration khỏi control plane migration để không cộng rủi ro.
- Chỉ quay về operator chuẩn sau khi migration hoàn tất và override tạm thời được gỡ.

## Nguyên tắc

- Bảo vệ logical metadata/state trước, hạ tầng vật lý chỉ là thứ thay xung quanh nó.
- Mỗi bước phải reversible.
- Tránh yêu cầu mọi client đổi cùng lúc.
- Chấp nhận trạng thái giữa kỳ trông "lộn xộn" nếu nó giữ production an toàn.

## Liên kết

- [[Runtime Platform Migration]]
- [[Kubernetes Operator Pattern]]
- [[Stateful Workloads on Kubernetes]]
- [[Message Broker]]
- [[Data Replication]]
