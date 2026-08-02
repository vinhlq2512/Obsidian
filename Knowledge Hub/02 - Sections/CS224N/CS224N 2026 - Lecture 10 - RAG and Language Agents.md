---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: lecture
title: "CS224N 2026 - Lecture 10 - RAG and Language Agents"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 10 - RAG and Language Agents.pdf]]"
pages: 72
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Retrieval-Augmented Generation]]"
  - "[[Retriever]]"
  - "[[LLM Agent]]"
tags:
  - cs224n
  - lecture
---

# CS224N 2026 - Lecture 10 - RAG and Language Agents

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 10 - RAG and Language Agents.pdf]]
- Vai trò trong khoá: nối [[Retrieval-Augmented Generation]] với [[LLM Agent]], reasoning, memory và tool use.
- Paper đọc kèm: [[2020 - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks - arXiv 2005.11401v4]], [[2023 - ReAct - Synergizing Reasoning and Acting in Language Models - arXiv 2210.03629v3]], [[2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1]].

## Mục tiêu cần hiểu

- Vì sao parametric memory của LM không đủ cho QA/knowledge-intensive tasks.
- RAG tách retrieval và generation như thế nào.
- [[LLM Agent|Agent]] khác chatbot thuần ở khả năng lập kế hoạch, ghi nhớ và dùng tool.
- Đánh giá agent khó hơn đánh giá single-turn generation vì có nhiều bước, môi trường và tool side effects.

## Ý chính

- Question answering cần truy cập tri thức cụ thể, mới, hoặc nằm ngoài training data.
- RAG bổ sung non-parametric memory: truy xuất tài liệu liên quan rồi đưa vào context cho generator.
- Retriever quyết định evidence nào được đưa vào; generator quyết định cách dùng evidence để trả lời.
- Agent mở rộng LM bằng loop: observe, reason, act, use tool, update memory, continue.
- Tool use biến LM từ mô hình sinh text thành controller gọi hành động bên ngoài.

## RAG pipeline

```text
user question
-> query encoder / retriever
-> top-k documents/passages
-> prompt/context construction
-> generator sinh answer dựa trên retrieved evidence
-> optional citation / verification
```

Các failure modes quan trọng:

- Retriever không lấy đúng evidence.
- Evidence đúng nhưng prompt nhồi quá nhiều context gây nhiễu.
- Generator bỏ qua evidence hoặc hallucinate.
- Chunking làm mất ngữ cảnh cần thiết.
- Evaluation chỉ chấm answer mà không chấm evidence path.

## Agent loop

```text
goal
-> plan / reason
-> choose action or tool
-> observe result
-> update memory/state
-> repeat until done
```

Reasoning và planning giúp agent chia nhỏ task; memory giúp giữ trạng thái qua nhiều bước; tool use giúp vượt giới hạn của text-only generation.

## Cách hiểu bằng lời của tôi

RAG là cách cho LM “mở sách trước khi trả lời”. Agent là bước xa hơn: không chỉ đọc thêm tài liệu, mà còn biết chọn hành động, dùng công cụ và lặp lại theo phản hồi của môi trường. Điểm nguy hiểm là mỗi thành phần thêm vào lại tạo thêm chỗ sai.

## Câu hỏi review

1. Parametric memory và non-parametric memory khác nhau thế nào?
2. Retriever sai ảnh hưởng tới generator ra sao?
3. RAG khác fine-tuning ở cách đưa tri thức vào model như thế nào?
4. Agent loop gồm các bước gì?
5. Vì sao đánh giá agent khó hơn QA đơn giản?

## Liên kết

- [[Retrieval-Augmented Generation]]
- [[Retriever]]
- [[Sparse Retriever]]
- [[Dense Passage Retrieval]]
- [[LLM Agent]]
- [[BM25]]
- [[CS224N]]
