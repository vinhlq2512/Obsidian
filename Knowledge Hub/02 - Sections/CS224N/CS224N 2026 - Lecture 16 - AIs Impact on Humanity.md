---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: lecture
title: "CS224N 2026 - Lecture 16 - AIs Impact on Humanity"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 16 - AIs Impact on Humanity.pdf]]"
pages: 49
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - lecture
---

# CS224N 2026 - Lecture 16 - AIs Impact on Humanity

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 16 - AIs Impact on Humanity.pdf]]
- Vai trò trong khoá: [[AI Hallucination|hallucination]], AI-assisted creativity, workforce impact và value alignment.
- Paper đọc kèm: [[2025 - We Cant Understand AI Using Our Existing Vocabulary - arXiv 2502.07586v1]], [[2025 - Agentic Interpretability - Because We Have LLMs We Can and Should Pursue It - arXiv 2506.12152v1]].

## Mục tiêu cần hiểu

- Vì sao LM hallucinate ngay cả khi reasoning mạnh hơn.
- AI-assisted creativity tạo nghịch lý: hỗ trợ sáng tạo nhưng có thể làm đồng nhất hoá output.
- Tác động tới workforce không chỉ là thay thế việc làm mà còn là tái cấu trúc task.
- Value alignment khó vì giá trị con người đa dạng, mâu thuẫn và phụ thuộc ngữ cảnh.

## Ý chính

- [[AI Hallucination|Hallucination]] trong citation là failure mode nghiêm trọng vì output có vẻ học thuật nhưng nguồn không tồn tại.
- Reasoning capability cao hơn không tự động làm [[AI Hallucination|hallucination]] thấp hơn; model vẫn có thể tạo câu trả lời tự tin nhưng sai.
- Khi dùng LLM cho nghiên cứu/viết học thuật, cần kiểm tra nguồn độc lập thay vì tin vào format trông hợp lệ.
- AI creativity có thể tăng tốc ideation nhưng cũng tạo áp lực homogenization nếu mọi người dùng cùng model/style.
- Alignment không chỉ là “lọc output xấu”, mà là câu hỏi xã hội: mô hình nên phục vụ ai, theo giá trị nào, trong bối cảnh nào.

## Failure mode: vibe citing

```text
model tạo citation có format hợp lý
-> người dùng tin vì trông chuyên nghiệp
-> citation không tồn tại hoặc sai metadata
-> lỗi lan vào paper/report/workflow
```

Điểm cần nhớ: hình thức đáng tin không đồng nghĩa với provenance đáng tin.

## Cách hiểu bằng lời của tôi

LM không có cơ chế mặc định để phân biệt “tôi biết vì có nguồn” và “tôi sinh ra chuỗi nghe hợp lý”. Khi đưa AI vào workflow nghiêm túc, bước xác minh không được xem là tuỳ chọn.

## Câu hỏi review

1. Vì sao hallucinated citation đặc biệt nguy hiểm trong học thuật?
2. Vì sao reasoning tốt hơn không đảm bảo ít [[AI Hallucination|hallucination]] hơn?
3. AI-assisted creativity có thể làm output đồng nhất bằng cách nào?
4. Alignment khác content moderation ở điểm nào?
5. Khi dùng LLM cho research workflow, cần kiểm tra gì?

## Liên kết

- [[Large Language Model]]
- [[LLM Agent]]
- [[AI Hallucination]]
- [[Measuring the Quality of Generated Text]]
- [[RLHF]]
- [[CS224N]]
