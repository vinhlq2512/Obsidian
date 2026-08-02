---
type: synthesis
status: developing
sources:
  - "[[CS224N]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - synthesis
  - cs224n
  - nlp
---

# CS224N Learning Path

## Mục tiêu

Note này là bản đồ học sâu cho các source CS224N. Dùng nó để biết nên đọc tài liệu nào trước, tài liệu nào là paper nền, và concept nào cần cập nhật sau mỗi cụm.

## Trục 1: Biểu diễn từ và neural foundation

Đọc theo thứ tự:

1. [[CS224N 2026 - Lecture 02 - Word Vectors]]
2. [[CS224N 2026 - Lecture 03 - Neural Network Foundations]]
3. [[CS224N 2019 - Notes 02 - Word Vectors II - GloVe Evaluation and Training]]
4. [[CS224N 2019 - Notes 03 - Neural Networks and Backpropagation]]

Paper nền:

- [[2013 - Efficient Estimation of Word Representations in Vector Space - arXiv 1301.3781v3]]
- [[2013 - Distributed Representations of Words and Phrases and their Compositionality - NeurIPS]]
- [[2014 - GloVe - Global Vectors for Word Representation]]

Concept cần nắm:

- [[Embedding]]
- [[Word2Vec]]
- [[Loss Function]]

## Trục 2: Sequence modeling đến Transformer

Đọc theo thứ tự:

1. [[CS224N 2026 - Lecture 04 - Language Models and Recurrent Neural Networks]]
2. [[CS224N 2026 - Lecture 05 - Attention and Transformers]]
3. [[CS224N 2026 - Lecture 06 - Final Projects and Practical Tips]]
4. [[CS224N 2023 - Notes 10 - Self-Attention and Transformers - Draft]]

Paper nền:

- [[2013 - On the Difficulty of Training Recurrent Neural Networks - arXiv 1211.5063v2]]
- [[2017 - Attention Is All You Need - arXiv 1706.03762v7]]
- [[2016 - Layer Normalization - arXiv 1607.06450v1]]

Concept cần nắm:

- [[Autoregressive Language Model]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Cross-Attention]]
- [[Transformer]]
- [[Layer Normalization]]

## Trục 3: Pretraining, tokenization và multilinguality

Đọc theo thứ tự:

1. [[CS224N 2026 - Lecture 07 - Pretraining]]
2. [[CS224N 2026 - Lecture 14 - Tokenization and Multilinguality]]
3. [[SLP 2026 - Chapter 02 - Words and Tokens]]
4. [[SLP 2026 - Chapter 10 - Masked Language Models]]

Paper nền:

- [[2016 - Neural Machine Translation of Rare Words with Subword Units - arXiv 1508.07909v5]]
- [[2018 - BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding - arXiv 1810.04805v2]]
- [[2020 - Language Models are Few-Shot Learners - arXiv 2005.14165v4]]
- [[2023 - Do All Languages Cost the Same - Tokenization in the Era of Commercial Language Models - EMNLP Main 614]]

Concept cần nắm:

- [[Tokenization]]
- [[BPE]]
- [[SentencePiece]]
- [[Bidirectional Attention]]
- [[Transfer Learning]]
- [[Multilingual Transformer]]

## Trục 4: Post-training và efficient adaptation

Đọc theo thứ tự:

1. [[CS224N 2026 - Lecture 08 - Post-training]]
2. [[CS224N 2026 - Lecture 09 - Efficient Adaptation]]
3. [[SLP 2026 - Chapter 09 - Post-training - Instruction Tuning Alignment and Test-Time]]

Paper nền:

- [[2022 - Scaling Instruction-Finetuned Language Models - arXiv 2210.11416v5]]
- [[2023 - Direct Preference Optimization - Your Language Model is Secretly a Reward Model - arXiv 2305.18290v3]]
- [[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2]]
- [[2019 - Parameter-Efficient Transfer Learning for NLP - arXiv 1902.00751v2]]

Concept cần nắm:

- [[Instruction Fine-Tuning]]
- [[RLHF]]
- [[DPO]]
- [[Parameter-Efficient Fine-Tuning]]
- [[Adapter]]

## Trục 5: RAG, agents, reasoning và inference

Đọc theo thứ tự:

1. [[CS224N 2026 - Lecture 10 - RAG and Language Agents]]
2. [[CS224N 2026 - Lecture 12 - Reasoning Part 1]]
3. [[CS224N 2026 - Lecture 13 - Reasoning Part 2]]
4. [[CS224N 2026 - Lecture 19 - The Art of Artificial Reasoning for Small Language Models]]

Paper nền:

- [[2020 - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks - arXiv 2005.11401v4]]
- [[2023 - ReAct - Synergizing Reasoning and Acting in Language Models - arXiv 2210.03629v3]]
- [[2023 - Toolformer - Language Models Can Teach Themselves to Use Tools - arXiv 2302.04761v1]]
- [[2022 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - arXiv 2201.11903v6]]
- [[2022 - Fast Inference from Transformers via Speculative Decoding - arXiv 2211.17192v2]]
- [[2025 - DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning - arXiv 2501.12948v2]]

Concept cần nắm:

- [[Retrieval-Augmented Generation]]
- [[Retriever]]
- [[LLM Agent]]
- [[Prompt Engineering]]
- [[Speculative Decoding]]
- [[Text Generation]]

## Trục 6: Evaluation, multimodal và impact

Đọc theo thứ tự:

1. [[CS224N 2026 - Lecture 11 - Evaluation]]
2. [[CS224N 2026 - Lecture 16 - AIs Impact on Humanity]]
3. Các paper multimodal trong [[CS224N]]

Paper nền:

- [[2023 - Holistic Evaluation of Language Models - TMLR 2023]]
- [[2021 - Measuring Massive Multitask Language Understanding - arXiv 2009.03300v3]]
- [[2024 - Chameleon - Mixed-Modal Early-Fusion Foundation Models - arXiv 2405.09818v2]]
- [[2024 - The Llama 3 Herd of Models - arXiv 2407.21783v3]]
- [[2025 - Multimodal RewardBench - Holistic Evaluation of Reward Models for Vision Language Models - arXiv 2502.14191v1]]

Concept cần nắm:

- [[Measuring the Quality of Generated Text]]
- [[Multimodal LLM]]
- [[AI Hallucination]]

## Quy trình đọc mỗi source

```text
đọc lecture note
-> mở paper đọc kèm quan trọng nhất
-> thêm ý mới vào source note
-> nếu ý tái sử dụng, cập nhật concept note
-> nếu nhiều source cùng nói một vấn đề, cập nhật synthesis
```
