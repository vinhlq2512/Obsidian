---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 6
start_page: 236
end_page: 278
estimated_minutes: 100
need_review: true
tags:
  - llm
  - prompt-engineering
---

# Hands-On LLM - Chapter 06 - Prompt Engineering

## Mục tiêu cần hiểu

- Hiểu cách dùng text generation models và kiểm soát output bằng decoding parameters.
- Nắm các thành phần của prompt: instruction, context, examples, format, constraints.
- Biết in-context learning, chain prompting, chain-of-thought, self-consistency và tree-of-thought.
- Hiểu output verification bằng examples, grammar hoặc constrained sampling.

## Định nghĩa quan trọng

- **Prompt engineering**: thiết kế input để điều khiển hành vi model.
- **Temperature**: tham số điều chỉnh độ ngẫu nhiên khi sampling.
- **Top-p**: nucleus sampling, giới hạn lựa chọn vào nhóm token có tổng xác suất cao nhất.
- **In-context learning**: đưa ví dụ vào prompt để model bắt chước pattern.
- **Chain-of-thought**: yêu cầu model tạo chuỗi lý luận trung gian.
- **Self-consistency**: sinh nhiều lời giải rồi chọn kết quả ổn định nhất.
- **Constrained sampling**: giới hạn output theo grammar/schema.

## Mental model

Prompt là giao diện lập trình mềm cho model. Bạn không thay weight của model; bạn thay task specification, context và constraints. Prompt tốt làm rõ mục tiêu, dữ liệu, vai trò, format output và tiêu chí đúng/sai.

## Phần cần biết

- Temperature cao tạo output đa dạng hơn nhưng dễ sai hơn.
- Few-shot examples thường mạnh hơn chỉ mô tả task trừu tượng.
- Chain prompting chia bài toán lớn thành nhiều bước nhỏ để giảm lỗi.
- Verification quan trọng khi output cần đúng format hoặc dùng trong pipeline.

## Khi áp dụng

- Với task đơn giản: dùng instruction rõ và output format cụ thể.
- Với task nhiều bước: chia chain hoặc tạo intermediate outputs.
- Với output cần parse: dùng JSON/schema/grammar constraints.
- Với reasoning không ổn định: thử self-consistency hoặc kiểm chứng bằng tool.

## Câu hỏi review

1. Temperature và top-p ảnh hưởng output thế nào?
2. In-context learning khác fine-tuning thế nào?
3. Khi nào chain-of-thought hữu ích, khi nào không nên lộ reasoning?
4. Vì sao output verification là phần của prompt engineering?

## Gợi ý trả lời câu hỏi review

1. Temperature điều chỉnh độ ngẫu nhiên khi chọn token: thấp thì ổn định/deterministic hơn, cao thì đa dạng hơn. Top-p giới hạn sampling trong nhóm token có tổng xác suất cao nhất, giúp kiểm soát độ rộng lựa chọn.
2. In-context learning đưa ví dụ vào prompt để model bắt chước trong lần gọi hiện tại, không đổi weights. Fine-tuning huấn luyện lại hoặc điều chỉnh weights/adapters để model học hành vi bền hơn.
3. Chain-of-thought hữu ích khi task cần nhiều bước suy luận, lập kế hoạch hoặc tính toán trung gian. Không nên lộ reasoning khi cần câu trả lời ngắn, có rủi ro tiết lộ logic nhạy cảm, hoặc production yêu cầu output sạch; khi đó có thể yêu cầu model tự suy nghĩ nhưng chỉ trả lời kết luận/tóm tắt.
4. Output verification là một phần của prompt engineering vì prompt không chỉ tạo câu trả lời, mà còn cần đảm bảo output đúng format, đủ ràng buộc và có thể dùng trong pipeline. Verification giảm lỗi parse, hallucination và kết quả sai cấu trúc.

## Liên kết

- [[Prompt Engineering]]
- [[Generative Model]]
- [[Large Language Model]]
