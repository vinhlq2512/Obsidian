---
type: concept
status: developing
sources:
  - "[[2026-05-04_connecting-llms-to-the-real-world-tool-use-function-calling]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - tool-use
---

# Function Calling

## Định nghĩa

Function calling là pattern để LLM tạo một yêu cầu có cấu trúc, thường theo JSON/schema, yêu cầu application layer gọi một hàm hoặc API cụ thể rồi đưa kết quả quay lại context.

## Cách hiểu bằng lời của tôi

Model không trực tiếp gọi database hay thanh toán. Nó nói: "tôi muốn gọi hàm này với tham số này". Ứng dụng bên ngoài mới kiểm tra request, gọi hàm thật, xử lý lỗi, rồi đưa observation trở lại cho model.

## Cần biết

- Schema rõ giúp giảm tham số sai nhưng không loại bỏ hoàn toàn lỗi.
- App phải validate tham số, auth, rate limit, retry và side effect.
- Với thao tác nguy hiểm, nên có human approval hoặc policy gate.
- Function result là input mới cho model, không tự động là câu trả lời cuối.

## Khi áp dụng

- Dùng cho workflow có API rõ ràng: tra cứu đơn hàng, tạo ticket, query database, gửi email, chạy code.
- Không nên dùng để thay thế logic nghiệp vụ quan trọng nếu không có guardrail.

## Liên kết

- [[Tool Use]]
- [[Model Context Protocol]]
- [[LLM Agent]]
- [[Agentic Loop]]
