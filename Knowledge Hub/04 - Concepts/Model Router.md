---
type: concept
status: seed
sources:
  - "[[2026-07-07_chatgpt-vs-gemini-vs-claude-how-they-differ]]"
  - "[[2026-01-26_how-cursor-shipped-its-coding-agent-to-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - production
---

# Model Router

## Định nghĩa

Model router là lớp chọn model hoặc chế độ suy luận phù hợp cho từng request dựa trên độ phức tạp, modality, latency budget, tool needs, cost và policy.

## Cách hiểu bằng lời của tôi

Không phải lượt nào cũng cần model mạnh nhất. Router là người điều phối: task dễ đi đường nhanh/rẻ, task khó đi model reasoning sâu hơn, task coding có thể dùng model chuyên code, task multimodal cần model hiểu ảnh/audio/video.

## Khi hữu ích

- Có nhiều model với cost/latency/capability khác nhau.
- Workload có cả request đơn giản và request cần reasoning/tool use.
- Cần cân bằng cost per successful task thay vì chỉ tối đa quality từng lượt.

## Rủi ro

- User có thể thấy hành vi không nhất quán nếu hai prompt gần giống bị route khác nhau.
- Routing sai làm task khó rơi vào model yếu hoặc task dễ bị tốn chi phí không cần thiết.
- Eval phải đo cả router + model, không chỉ model riêng lẻ.

## Liên kết

- [[AI Model Serving]]
- [[LLM Inference Engineering]]
- [[LLM Evaluation]]
- [[Multimodal LLM]]
- [[Coding Agent]]
