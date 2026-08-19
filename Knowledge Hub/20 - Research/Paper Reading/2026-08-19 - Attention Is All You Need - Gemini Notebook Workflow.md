---
type: paper-reading
date: 2026-08-19
status: draft
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[Attention Is All You Need]]"
pdf: "[[Attention Is All You Need.pdf]]"
paper_note: "[[Attention Is All You Need]]"
notebook_url:
target_minutes: 90
actual_minutes:
reading_goal: "Hiểu Attention Is All You Need theo workflow Gemini Notebook: motivation, Transformer architecture, attention equations, WMT protocol, ablations, limitations và reproducibility."
current_phase: scaffolded
completed: false
need_review: true
review_date:
created_at: 2026-08-19
updated_at: 2026-08-19
tags:
  - paper-reading
  - gemini-notebook
  - transformer
  - attention
  - nlp
---

# 2026-08-19 - Attention Is All You Need - Gemini Notebook Workflow

> [!note] Ranh giới
> Đây là working note scaffold từ paper note/PDF. Các phần closed-book recall và oral exam vẫn để trống cho bạn tự trả lời; không coi note này là bằng chứng đã đọc xong paper.

## Setup

- Paper: [[Attention Is All You Need]]
- PDF: [[Attention Is All You Need.pdf]]
- Paper note chính: [[Attention Is All You Need]]
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc: hiểu vì sao Transformer bỏ recurrence/convolution, cách scaled dot-product attention và multi-head attention hoạt động, và Table 2-3 chứng minh gì.
- Phần cần đọc trước: Abstract, Introduction, Figure 1-2, Sections 3.1-3.5, Table 1-3, Conclusion.
- PDF count đã kiểm tra: 15 trang.

## Phase 1 — Paper Map

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet. Create a structural map of this paper and identify problem, motivation, gap, contributions, pipeline, components, equations, datasets, baselines, metrics, experiments, ablations, and limitations. For every item, point to the relevant section, figure, table, or equation. The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map — scaffold từ nguồn

- **Problem:** sequence transduction models mạnh trước đó dựa vào recurrence/convolution, gây sequential bottleneck và khó song song hóa trong training. [[Attention Is All You Need.pdf#page=2|PDF tr. 2]]
- **Motivation:** attention đã giúp nối dependency xa; paper hỏi liệu attention có thể trở thành cơ chế chính thay RNN/CNN không. [[Attention Is All You Need.pdf#page=1|PDF tr. 1]]
- **Gap:** chưa có architecture transduction mạnh chỉ dựa vào attention, không recurrence/convolution. [[Attention Is All You Need.pdf#page=2|PDF tr. 2]]
- **Main idea:** Transformer encoder-decoder dùng stacked multi-head self-attention, encoder-decoder attention, FFN, residual connections, layer norm và positional encoding.
- **Main contributions:** attention-only architecture, scaled dot-product attention, multi-head attention, positional encoding, WMT results với training cost thấp.
- **Important figure:** Figure 1 architecture; Figure 2 scaled dot-product attention và multi-head attention. [[Attention Is All You Need.pdf#page=3|PDF tr. 3]], [[Attention Is All You Need.pdf#page=4|PDF tr. 4]]
- **Important equations:** Eq. 1 attention; Eq. 2 multi-head attention; Eq. 3 FFN; positional encoding formulas. [[Attention Is All You Need.pdf#page=4|PDF tr. 4]], [[Attention Is All You Need.pdf#page=5|PDF tr. 5]], [[Attention Is All You Need.pdf#page=6|PDF tr. 6]]
- **Main result table:** Table 2 WMT 2014 BLEU/cost. [[Attention Is All You Need.pdf#page=8|PDF tr. 8]]
- **Ablation table:** Table 3 architecture variations. [[Attention Is All You Need.pdf#page=9|PDF tr. 9]]
- **Limitations:** self-attention quadratic in sequence length; autoregressive generation vẫn tuần tự; future work nhắc local/restricted attention cho image/audio/video. [[Attention Is All You Need.pdf#page=6|PDF tr. 6]], [[Attention Is All You Need.pdf#page=10|PDF tr. 10]]

### Chỗ cần đọc trước

- [ ] Abstract + Introduction
- [ ] Figure 1 architecture
- [ ] Eq. 1-3
- [ ] Table 1 complexity/path length
- [ ] Table 2 main results
- [ ] Table 3 ablation
- [ ] Conclusion/future work

## Phase 2 — Pass 1 Recall

### Closed-book recall của tôi

**Problem**

-

**Why does it matter?**

-

**Research gap**

-

**Main idea**

-

**Main contribution**

-

**Main result**

-

### Prompt kiểm tra recall

```text
I have completed the first pass of the paper.

Here is my understanding:

[PASTE MY NOTES]

Compare my understanding against the paper. Return what is correct, inaccurate, missing, confusing, and which sections/citations I should revisit. Do not rewrite the entire paper for me.
```

## Phase 3 — Problem / Motivation / Gap

| Mục | Diễn giải bằng lời của tôi | Evidence / citation |
|---|---|---|
| General problem | Sequence transduction cần map input sequence sang output sequence, ví dụ machine translation. | [[Attention Is All You Need.pdf#page=2\|PDF tr. 2]] |
| Why it matters | RNN phải tính tuần tự theo position, làm train chậm và dependency xa khó học hơn. | [[Attention Is All You Need.pdf#page=2\|PDF tr. 2]] |
| What prior work solves | RNN/CNN encoder-decoder + attention đã đạt kết quả mạnh trong translation. | [[Attention Is All You Need.pdf#page=2\|PDF tr. 2]] |
| What prior work fails to solve | Recurrence/convolution vẫn gây sequential operations hoặc path length lớn hơn self-attention. | [[Attention Is All You Need.pdf#page=6\|PDF tr. 6]] |
| Exact research gap | Thiếu một architecture transduction attention-only mạnh, song song hóa tốt, không recurrence/convolution. | [[Attention Is All You Need.pdf#page=1\|PDF tr. 1]] |
| Hypothesis / intuition | Attention đủ để model hóa quan hệ giữa token; positional encoding bù thông tin thứ tự. | [[Attention Is All You Need.pdf#page=6\|PDF tr. 6]] |
| Contribution addressing the gap | Transformer dùng attention + FFN + positional encoding trong encoder-decoder stack. | [[Attention Is All You Need.pdf#page=3\|PDF tr. 3]] |

### Câu hỏi tự kiểm tra

- [ ] Paper bỏ recurrence/convolution ở đâu, nhưng vẫn giữ autoregressive decoding ở đâu?
- [ ] Vì sao self-attention có path length $O(1)$ nhưng complexity $O(n^2d)$?
- [ ] Vì sao positional encoding là bắt buộc trong attention-only architecture?

## Phase 4 — Method / Architecture

### Tôi tự vẽ trước

```text
Source tokens
-> token embeddings + positional encodings
-> encoder stack N=6
   -> multi-head self-attention
   -> feed-forward network
-> encoder memory
Shifted target tokens
-> token embeddings + positional encodings
-> decoder stack N=6
   -> masked self-attention
   -> encoder-decoder attention
   -> feed-forward network
-> linear + softmax
-> next-token distribution
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
| Embedding + positional encoding | token ids, positions | sum token embedding and position encoding | position-aware token vectors | inject order without recurrence | [[Attention Is All You Need.pdf#page=6\|PDF tr. 6]] |
| Encoder self-attention | encoder states | Q/K/V from same sequence | contextualized source states | each source token attends to all source tokens | [[Attention Is All You Need.pdf#page=5\|PDF tr. 5]] |
| Decoder masked self-attention | shifted target states | causal mask prevents future attention | prefix-aware target states | autoregressive training | [[Attention Is All You Need.pdf#page=5\|PDF tr. 5]] |
| Encoder-decoder attention | decoder queries, encoder keys/values | attention over source memory | source-conditioned target states | align/condition target generation | [[Attention Is All You Need.pdf#page=5\|PDF tr. 5]] |
| Multi-head attention | Q, K, V | project to multiple heads, concat, project | mixed attention representation | multiple relation subspaces | [[Attention Is All You Need.pdf#page=5\|PDF tr. 5]] |
| Position-wise FFN | each position vector | two linear layers + ReLU | transformed vector | per-token nonlinear processing | [[Attention Is All You Need.pdf#page=5\|PDF tr. 5]] |
| Residual + layer norm | sublayer input/output | $LayerNorm(x + Sublayer(x))$ | stabilized hidden state | train deep stack | [[Attention Is All You Need.pdf#page=3\|PDF tr. 3]] |

### Điều tôi vẫn chưa hiểu

- [ ] Table 1 complexity có giả định gì về $n$, $d$, $k$?
- [ ] Vì sao learned positional embeddings gần ngang sinusoidal trong ablation nhưng paper vẫn chọn sinusoidal?

## Phase 5 — Section Recall

### Section 3.1 — Encoder and Decoder Stacks

- **Input:** source/target embeddings cộng positional encodings.
- **Process:** encoder dùng self-attention + FFN; decoder thêm masked self-attention và encoder-decoder attention.
- **Output:** encoder memory và decoder hidden states để dự đoán next token.
- **Purpose:** thay recurrent/convolutional blocks bằng attention-based blocks nhưng vẫn giữ encoder-decoder formulation.

### Section 3.2 — Attention

- **Input:** query, keys, values.
- **Process:** scaled dot-product attention và multi-head projections.
- **Output:** weighted sum of values, concat multi-head output.
- **Purpose:** cho mỗi token truy cập trực tiếp token liên quan ở toàn sequence.
- **Still unclear:** multi-head attention học các quan hệ khác nhau bằng cơ chế nào nếu không có supervision riêng cho từng head?

## Phase 6 — Equations

| Eq. | Dùng để làm gì? | Biến chính | Behavior được khuyến khích | Evidence / ablation | Status |
|---:|---|---|---|---|---|
| 1 | Tính scaled dot-product attention | $Q,K,V,d_k$ | attend theo similarity nhưng scale để softmax ổn định | [[Attention Is All You Need.pdf#page=4\|PDF tr. 4]] | todo |
| 2 | Multi-head attention | $W_i^Q,W_i^K,W_i^V,W^O,h$ | học nhiều attention subspaces song song | Table 3 head ablation | todo |
| 3 | Position-wise FFN | $W_1,b_1,W_2,b_2$ | nonlinear transform độc lập từng position | [[Attention Is All You Need.pdf#page=5\|PDF tr. 5]] | todo |
| PE | Sin/cos positional encoding | $pos,i,d_{model}$ | inject absolute/relative position signal | Table 3 row E | todo |
| LR schedule | warmup + inverse sqrt decay | $step,warmup,d_{model}$ | stable early training, decay later | [[Attention Is All You Need.pdf#page=7\|PDF tr. 7]] | todo |

## Phase 7 — Loss Functions

```text
Training objective
├── token-level cross-entropy / likelihood -> predict next target token
├── label smoothing epsilon_ls=0.1 -> regularize output distribution
└── dropout -> regularize residual/attention/embedding paths
```

| Loss / regularizer | Equation | Inputs | Trains component | Behavior | Weight | Ablation |
|---|---|---|---|---|---|---|
| Cross-entropy / NLL | not expanded as a named equation | predicted next-token distribution + target token | full encoder-decoder | maximize translation likelihood | standard objective | not ablated as core |
| Label smoothing | described in training section | target distribution | output probabilities | reduce overconfidence, improve BLEU/perplexity trade-off | $\epsilon_{ls}=0.1$ | not isolated in Table 3 |
| Dropout | training setup | residual/attention/embedding paths | full model | regularization | $P_{drop}=0.1$ base | Table 3 shows no dropout hurts |

## Phase 8 — Experiments

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
| Main translation | Transformer có đạt SOTA/cost tốt hơn không? | WMT 2014 EN-DE, EN-FR | prior NMT models | BLEU, training cost | Table 2 | Big: 28.4 EN-DE, 41.8 EN-FR | reported, not reproduced |
| Architecture ablation | head count, dimensions, dropout, PE ảnh hưởng thế nào? | EN-DE dev | Transformer variants | BLEU/perplexity | Table 3 | multi-head, dropout, bigger model matter | dev setting only |
| Complexity comparison | self-attention trade-off gì so với recurrent/convolution? | theoretical layer comparison | recurrent/convolution/separable conv | operations, complexity, path length | Table 1 | self-attention path length/sequential ops tốt nhưng $O(n^2d)$ | assumes sequence length regime |
| Parsing generalization | Transformer có generalize ngoài MT không? | WSJ parsing | parsing baselines | F1 | Table 4 | 91.3 WSJ-only, 92.7 semi-supervised | small experiments, not deeply tuned |
| Attention visualization | heads học dependency nào? | example sentences | visualization | qualitative | Appendix figures | some heads track long-distance/syntactic relations | illustrative, not proof |

### Protocol fingerprint

- Dataset and split: WMT 2014 English-German, English-French; parsing on WSJ.
- Tokenization: EN-DE BPE shared vocab about 37K; EN-FR word-piece 32K.
- Scenario / label space: supervised sequence transduction / machine translation.
- Backbone: Transformer base/big, no recurrence/convolution.
- Model base: $N=6$, $d_{model}=512$, $d_{ff}=2048$, $h=8$, $d_k=d_v=64$.
- Model big: $d_{model}=1024$, $d_{ff}=4096$, $h=16$.
- Training: base 100K steps, big 300K steps.
- Hardware: 8 NVIDIA P100 GPUs.
- Optimizer: Adam $\beta_1=0.9,\beta_2=0.98,\epsilon=10^{-9}$.
- Metric: BLEU for translation; F1 for parsing.
- Result type: reported/observed from paper, not reproduced local.

## Phase 9 — Claim → Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
| Attention-only architecture can replace recurrence/convolution for MT. | Abstract/Intro | WMT Table 2 | Transformer big reaches 28.4 BLEU EN-DE and 41.8 EN-FR. [[Attention Is All You Need.pdf#page=8\|PDF tr. 8]] | Strong for WMT protocol | not proof for every sequence task |
| Transformer trains faster / with lower cost than prior models. | Abstract/Results | Table 2 cost comparison | reported lower training cost than listed baselines. [[Attention Is All You Need.pdf#page=8\|PDF tr. 8]] | Strong reported evidence | hardware/framework differences matter |
| Multi-head attention matters. | Ablation | Table 3 | single head underperforms multi-head variants. [[Attention Is All You Need.pdf#page=9\|PDF tr. 9]] | Supported | ablation dev setting |
| Positional encoding is needed, but learned vs sinusoidal similar. | Method/Ablation | Table 3 row E | learned positional embeddings give similar result to sinusoidal. [[Attention Is All You Need.pdf#page=9\|PDF tr. 9]] | Supported | extrapolation claim is hypothesis |
| Self-attention has better path length but quadratic cost. | Table 1/method | theoretical comparison | self-attention sequential ops/path length O(1), complexity $O(n^2d)$. [[Attention Is All You Need.pdf#page=6\|PDF tr. 6]] | Strong theoretical framing | long sequence cost remains limitation |

## Phase 10 — Ablation Study

| Component | Intended purpose | With component | Without / changed component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
| Multi-head attention | multiple relation subspaces | baseline BLEU in Table 3 | single head lower | about -0.9 BLEU in dev setup | multi-head helps | exact optimal head count universal |
| Attention key/value dimension | capacity per head | baseline | smaller $d_k$ variants lower | varies | dimension matters | bigger always better without cost |
| Dropout | regularization | baseline | no dropout worse | clear degradation | dropout important | dropout value universal |
| Model size | capacity | base/big variants | smaller variants lower | bigger generally better | capacity helps | scaling law proven |
| Positional encoding type | order signal | sinusoidal | learned PE similar | small/no major difference | both viable in setup | sinusoidal always superior |

## Phase 11 — Critical Reading

- Strongest contribution: turning attention into the main sequence modeling primitive and showing strong WMT results with practical training speed.
- Weakest part: evidence for interpretability of heads is qualitative; state-of-the-art claim is protocol-bound.
- Main assumption: machine translation setup with moderate sequence lengths where $O(n^2)$ attention is affordable.
- Alternative explanation: gains come from architecture plus engineering/training recipe, not attention formula alone.
- Missing experiment: broader long-sequence tasks, non-autoregressive generation, systematic head interpretability.
- Generalization risk: image/audio/video require restricted/local attention, as authors note.
- Reproducibility risk: modern exact reproduction depends on preprocessing/tokenization, batching, and framework details.

## Phase 12 — Reproduction Check

| Item | Status | Detail | Missing detail / risk |
|---|---|---|---|
| Dataset and split | Clearly specified | WMT 2014 EN-DE/EN-FR, WSJ parsing | exact preprocessing scripts needed |
| Preprocessing | Partially specified | BPE/word-piece vocab sizes | exact vocab/training pipeline |
| Input representation | Clearly specified | embeddings + positional encodings |  |
| Model / backbone | Clearly specified | Transformer base/big |  |
| Architecture | Clearly specified | encoder/decoder stacks, attention, FFN |  |
| Training procedure | Partially specified | steps, optimizer, schedule | batching/token batching details |
| Sampling procedure | Missing/Not applicable | supervised MT | decoding details for BLEU need scripts |
| Memory / replay strategy | Not applicable | no continual memory |  |
| Loss functions | Partially specified | CE with label smoothing | exact implementation details |
| Optimizer | Clearly specified | Adam params |  |
| Learning rate | Clearly specified | warmup + inverse sqrt |  |
| Batch size | Partially specified | approximate tokens/batch in paper | exact batching can vary |
| Epochs | Not specified as epochs | training by steps |  |
| Hyperparameters | Clearly specified | $N,d_{model},d_{ff},h,dropout$ |  |
| Random seeds | Missing | not reported in scaffold | variance risk |
| Evaluation protocol | Partially specified | BLEU newstest2014 | tokenization BLEU script matters |
| Inference procedure | Partially specified | autoregressive decoding | beam/search settings need full paper/code |

## Phase 13 — Completeness / Oral Exam

- [ ] Giải thích bottleneck sequential của RNN.
- [ ] Vẽ encoder layer và decoder layer.
- [ ] Giải thích Eq. 1 scaling $\sqrt{d_k}$.
- [ ] Phân biệt self-attention, masked self-attention, encoder-decoder attention.
- [ ] Giải thích positional encoding.
- [ ] Đọc Table 1 complexity/path length.
- [ ] Đọc Table 2 BLEU/cost và nêu caveat.
- [ ] Đọc Table 3 ablation.
- [ ] Nêu limitation quadratic attention và autoregressive decoding.

### Prompt oral exam

```text
Act as my PhD advisor. Quiz me on Attention Is All You Need one question at a time. Start from problem/gap, then architecture, equations, experiments/ablation, limitations, and finally ask me to transfer the idea to another sequence modeling setting. Do not reveal the ideal answer before I attempt it.
```

## Final Paper Note Handoff

Chỉ chuyển sang paper note chính những ý đã tự kiểm tra lại bằng PDF citation.

### Ý cần chuyển sang paper note

- [ ] Problem: sequential bottleneck của RNN/CNN.
- [ ] Method overview: encoder-decoder attention-only stack.
- [ ] Important equations: attention, multi-head, FFN, positional encoding.
- [ ] Protocol fingerprint: WMT 2014, BPE/word-piece, base/big, Adam schedule.
- [ ] Main results: Table 2 BLEU/cost.
- [ ] Ablation: head count, model size, dropout, positional encoding.
- [ ] Limitations: quadratic attention, autoregressive generation, qualitative head visualization.
- [ ] Concepts: [[Transformer]], [[Self-Attention]], [[Multi-Head Attention]], [[Positional Embeddings]], [[Encoder-Decoder Architecture]].

## Liên kết

- Paper note: [[Attention Is All You Need]]
- PDF: [[Attention Is All You Need.pdf]]
- Related reading log: [[2026-08-16 - Attention Is All You Need]]
- Concepts: [[Transformer]], [[Self-Attention]], [[Multi-Head Attention]], [[Positional Embeddings]], [[Encoder-Decoder Architecture]], [[Attention Mask]], [[Feed-Forward Layer]]
