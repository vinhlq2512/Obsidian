---
type: paper
status: draft
title: "Attention Is All You Need"
authors:
  - Ashish Vaswani
  - Noam Shazeer
  - Niki Parmar
  - Jakob Uszkoreit
  - Llion Jones
  - Aidan N. Gomez
  - Łukasz Kaiser
  - Illia Polosukhin
year: 2017
venue: "31st Conference on Neural Information Processing Systems (NIPS 2017)"
url: "https://arxiv.org/abs/1706.03762"
pdf: "[[Attention Is All You Need.pdf]]"
zotero_key:
citekey:
doi:
arxiv: "1706.03762v7"
code_url: "https://github.com/tensorflow/tensor2tensor"
dataset_url:
source_version: "arXiv v7, 2023-08-02"
topic:
  - transformer
  - attention
  - sequence transduction
  - machine translation
priority: high
reading_status: in-progress
rating:
related_concepts:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Positional Embeddings]]"
  - "[[Encoder-Decoder Architecture]]"
  - "[[Attention Mask]]"
  - "[[Feed-Forward Layer]]"
created_at: 2026-08-13
updated_at: 2026-08-16
tags:
  - paper
  - transformer
  - attention
  - nlp
---

# Attention Is All You Need

> [!info] Ranh giới trạng thái
> Note này là bản phân tích học tập được tạo từ PDF 15 trang. Trạng thái đọc cá nhân: `in-progress` (bắt đầu đọc ngày 2026-08-16).

## Tóm tắt một câu

Paper giới thiệu [[Transformer]]: một kiến trúc encoder-decoder cho sequence transduction dùng attention thay cho recurrence và convolution, giúp train song song tốt hơn và đạt kết quả mạnh trên WMT 2014 machine translation.

## Nguồn

- PDF gốc: [[Attention Is All You Need.pdf]]
- arXiv: [1706.03762](https://arxiv.org/abs/1706.03762)
- Code được paper công bố: [tensorflow/tensor2tensor](https://github.com/tensorflow/tensor2tensor)
- Bản local trùng checksum với bản CS224N trong vault: [[2017 - Attention Is All You Need - arXiv 1706.03762v7.pdf]]
- Venue trong PDF: NIPS 2017, Long Beach, CA, USA. [[Attention Is All You Need.pdf#page=1|PDF, tr. 1]]

## Vấn đề paper giải quyết

Trước Transformer, các mô hình sequence transduction mạnh thường dựa trên RNN/LSTM/GRU hoặc CNN, rồi thêm attention để nối encoder và decoder. Điểm nghẽn chính của RNN là tính tuần tự: hidden state ở vị trí $t$ phụ thuộc vào $h_{t-1}$, nên khó song song hóa trong một training example và càng đau khi sequence dài. [[Attention Is All You Need.pdf#page=2|PDF, tr. 2]]

Paper đặt câu hỏi rất gọn: nếu attention đã giúp model nối các dependency xa, liệu có thể bỏ recurrence và convolution hoàn toàn, rồi xây encoder-decoder chỉ bằng attention không?

## Gap và đóng góp

- **reported:** Paper đề xuất Transformer, kiến trúc dựa hoàn toàn trên attention mechanisms, không dùng recurrence/convolution. [[Attention Is All You Need.pdf#page=1|PDF, tr. 1]]
- **observed:** Figure 1 cho thấy encoder và decoder đều là stack nhiều layer, mỗi layer kết hợp attention, feed-forward, residual connection và layer normalization. [[Attention Is All You Need.pdf#page=3|PDF, tr. 3]]
- **reported:** Transformer train nhanh hơn nhờ parallelization, đạt BLEU 28.4 trên WMT 2014 English-German và BLEU 41.8 trên English-French với Transformer big. [[Attention Is All You Need.pdf#page=1|PDF, tr. 1]]
- **reported:** Paper cũng thử English constituency parsing để kiểm tra khả năng generalize ngoài translation. [[Attention Is All You Need.pdf#page=9|PDF, tr. 9]]

## Bài toán/formalization

Paper đặt trong framework encoder-decoder:

$$
(x_1,\ldots,x_n) \rightarrow z=(z_1,\ldots,z_n)
$$

Encoder map input sequence thành chuỗi continuous representations $z$. Decoder sinh output sequence:

$$
(y_1,\ldots,y_m)
$$

theo kiểu autoregressive: mỗi bước sinh token tiếp theo dựa trên các token đã sinh trước đó và representation từ encoder. [[Attention Is All You Need.pdf#page=2|PDF, tr. 2]]

## Phương pháp

### Kiến trúc Transformer gốc

Transformer gốc là encoder-decoder architecture:

```text
source tokens
-> token embeddings + positional encodings
-> encoder stack N=6
-> decoder stack N=6, dùng shifted target tokens
-> linear + softmax
-> output probabilities
```

Encoder layer có hai sublayers:

1. multi-head self-attention;
2. position-wise feed-forward network.

Decoder layer có ba sublayers:

1. masked multi-head self-attention trên output prefix;
2. encoder-decoder attention, trong đó decoder attend sang encoder output;
3. position-wise feed-forward network.

Mỗi sublayer đều được bọc bằng residual connection và layer normalization:

$$
\text{LayerNorm}(x + \text{Sublayer}(x)).
$$

Paper dùng $N=6$ layers và $d_{\text{model}}=512$ cho base model. [[Attention Is All You Need.pdf#page=3|PDF, tr. 3]]

### Scaled dot-product attention

Attention nhận query, keys, values và trả ra weighted sum của values. Công thức lõi:

$$
\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.
$$

Chia cho $\sqrt{d_k}$ để tránh dot product có magnitude quá lớn khi $d_k$ lớn, khiến softmax đi vào vùng gradient rất nhỏ. [[Attention Is All You Need.pdf#page=4|PDF, tr. 4]]

### Multi-head attention

Thay vì chạy một attention duy nhất trên toàn bộ $d_{\text{model}}$, paper project $Q,K,V$ thành nhiều subspace rồi chạy attention song song:

$$
\text{MultiHead}(Q,K,V)=\text{Concat}(\text{head}_1,\ldots,\text{head}_h)W^O
$$

$$
\text{head}_i=\text{Attention}(QW_i^Q,KW_i^K,VW_i^V).
$$

Base model dùng $h=8$ heads, $d_k=d_v=d_{\text{model}}/h=64$. [[Attention Is All You Need.pdf#page=5|PDF, tr. 5]]

### Ba nơi dùng attention

Paper dùng multi-head attention theo ba cách:

- encoder self-attention: $Q,K,V$ đều đến từ encoder layer trước;
- decoder masked self-attention: decoder chỉ attend tới các vị trí hiện tại/quá khứ;
- encoder-decoder attention: query từ decoder, key/value từ encoder output. [[Attention Is All You Need.pdf#page=5|PDF, tr. 5]]

### Feed-forward network

Mỗi layer có position-wise FFN:

$$
\text{FFN}(x)=\max(0,xW_1+b_1)W_2+b_2.
$$

Paper dùng $d_{\text{model}}=512$ và $d_{ff}=2048$. Đây là cùng một FFN áp dụng độc lập cho từng position, nhưng parameters khác nhau giữa các layer. [[Attention Is All You Need.pdf#page=5|PDF, tr. 5]]

### Positional encoding

Vì model không có recurrence/convolution, paper cộng positional encodings vào input embeddings ở đáy encoder và decoder. Sinusoidal encoding:

$$
PE_{(pos,2i)}=\sin(pos/10000^{2i/d_{\text{model}}})
$$

$$
PE_{(pos,2i+1)}=\cos(pos/10000^{2i/d_{\text{model}}})
$$

Paper chọn sinusoidal vì hypothesize rằng nó giúp model học relative position dễ hơn và có thể extrapolate sang sequence dài hơn training. Learned positional embeddings cho kết quả gần như tương đương trong Table 3 row E. [[Attention Is All You Need.pdf#page=6|PDF, tr. 6]]

## Mental model

Một Transformer block có thể hiểu như hai bước luân phiên:

```text
attention: token lấy thông tin từ token khác
feed-forward: từng token xử lý representation đã có ngữ cảnh
```

Điểm táo bạo của paper là attention không còn là phụ kiện nối encoder-decoder như trong seq2seq RNN; attention trở thành cơ chế chính để tạo representation.

## Protocol fingerprint

| Trường | Chi tiết |
|---|---|
| Task chính | Machine translation, WMT 2014 English-German và English-French |
| Tokenization | EN-DE dùng BPE shared source-target vocab khoảng 37K tokens; EN-FR dùng word-piece vocab 32K |
| Model base | $N=6$, $d_{\text{model}}=512$, $d_{ff}=2048$, $h=8$, $d_k=d_v=64$ |
| Model big | $d_{\text{model}}=1024$, $d_{ff}=4096$, $h=16$, 300K steps |
| Hardware | Một máy với 8 NVIDIA P100 GPUs |
| Training schedule | Base: 100K steps, khoảng 12 giờ; big: 300K steps, khoảng 3.5 ngày |
| Optimizer | Adam, $\beta_1=0.9$, $\beta_2=0.98$, $\epsilon=10^{-9}$ |
| Learning rate | Warmup 4000 steps rồi inverse square-root decay |
| Regularization | Residual dropout, embedding/positional dropout, label smoothing $\epsilon_{ls}=0.1$ |
| Metric | BLEU trên newstest2014; parsing dùng WSJ Section 23 F1 |
| Result type | Reported/observed từ paper, không phải reproduced local |

## Kết quả chính

### Machine translation

| Model | EN-DE BLEU | EN-FR BLEU | Training cost EN-DE | Training cost EN-FR |
|---|---:|---:|---:|---:|
| Transformer base | 27.3 | 38.1 | $3.3\cdot10^{18}$ FLOPs |  |
| Transformer big | 28.4 | 41.8 | $2.3\cdot10^{19}$ FLOPs |  |

**reported/observed:** Table 2 cho thấy Transformer big đạt 28.4 BLEU trên EN-DE và 41.8 BLEU trên EN-FR, đồng thời paper nhấn mạnh training cost thấp hơn nhiều baseline cạnh tranh. [[Attention Is All You Need.pdf#page=8|PDF, tr. 8]]

### Ablation

Table 3 cho thấy:

- single-head attention kém hơn multi-head khoảng 0.9 BLEU trong setup dev;
- giảm attention key size $d_k$ làm chất lượng giảm;
- model lớn hơn thường tốt hơn;
- dropout quan trọng để tránh overfitting;
- learned positional embeddings gần như ngang sinusoidal positional encoding trong setup này. [[Attention Is All You Need.pdf#page=9|PDF, tr. 9]]

### Parsing

Paper thử English constituency parsing để kiểm tra generalization. Transformer 4-layer đạt 91.3 F1 trong WSJ-only setting và 92.7 F1 trong semi-supervised setting, nhưng paper cũng nói đây chỉ là một số thí nghiệm nhỏ, không phải tuning sâu cho parsing. [[Attention Is All You Need.pdf#page=10|PDF, tr. 10]]

## Hạn chế, giả định, failure modes

- **Quadratic cost:** self-attention có complexity $O(n^2\cdot d)$ theo sequence length, nên sequence rất dài vẫn là vấn đề. [[Attention Is All You Need.pdf#page=6|PDF, tr. 6]]
- **Generation vẫn tuần tự:** paper bỏ recurrence trong architecture, nhưng autoregressive decoding vẫn sinh token từng bước. Conclusion cũng nêu future work về making generation less sequential. [[Attention Is All You Need.pdf#page=10|PDF, tr. 10]]
- **Attention visualization không phải proof hoàn chỉnh:** appendix cho thấy một số heads học pattern cú pháp/ngữ nghĩa, nhưng đây là evidence minh họa, không phải diễn giải đầy đủ mọi head. [[Attention Is All You Need.pdf#page=13|PDF, tr. 13]]
- **State-of-the-art là trong phạm vi protocol:** claim SOTA dựa trên WMT 2014 translation setup và các baseline/chi phí được paper báo cáo, không nên kéo thẳng sang mọi NLP task.

## Đánh giá từ evidence

- **inferred:** Đóng góp lớn nhất không chỉ là công thức attention, mà là việc biến attention thành primitive chính của toàn bộ sequence model.
- **observed:** Figure 1 cho thấy Transformer vẫn giữ tư duy encoder-decoder của seq2seq, nhưng thay RNN/CNN blocks bằng attention + FFN blocks. [[Attention Is All You Need.pdf#page=3|PDF, tr. 3]]
- **reported:** Paper không nói Transformer giải quyết mọi vấn đề sequence; chính authors đã nêu hướng restricted/local attention cho input/output lớn như image, audio, video. [[Attention Is All You Need.pdf#page=10|PDF, tr. 10]]

## Diễn giải học tập

Nếu RNN đọc câu như một người đi qua từng từ, Transformer giống một căn phòng họp nơi mọi token có thể hỏi mọi token khác ngay lập tức. Nhưng để cuộc họp không hỗn loạn, model cần:

- query/key/value để quyết định token nào liên quan;
- scaling để softmax không bị saturate;
- nhiều heads để có nhiều kiểu quan hệ song song;
- positional encodings để biết thứ tự;
- causal mask để decoder không nhìn trước đáp án;
- feed-forward layer để xử lý từng token sau khi đã nhận ngữ cảnh.

## Câu hỏi review

1. Paper muốn loại bỏ bottleneck nào của RNN/CNN trong sequence transduction?
2. Vì sao scaled dot-product attention chia cho $\sqrt{d_k}$?
3. Multi-head attention khác một attention head lớn ở đâu?
4. Encoder self-attention, decoder self-attention và encoder-decoder attention khác nhau thế nào?
5. Vì sao Transformer cần positional encoding?
6. Table 1 nói gì về trade-off giữa self-attention và recurrent/convolutional layers?
7. Claim “state-of-the-art” trong paper nên được hiểu trong phạm vi protocol nào?

## Gợi ý trả lời câu hỏi review

1. Bottleneck là computation tuần tự theo vị trí, làm khó parallelization và học dependency xa.
2. Vì dot product có variance tăng theo $d_k$; không scale thì softmax dễ rơi vào vùng gradient nhỏ.
3. Multi-head dùng nhiều projection/subspace và nhiều attention distributions song song, rồi concat và project lại.
4. Encoder self-attention nhìn toàn input; decoder self-attention bị causal mask; encoder-decoder attention dùng query từ decoder và key/value từ encoder.
5. Vì attention-only model không có recurrence/convolution nên không tự có tín hiệu thứ tự token.
6. Self-attention có sequential operations $O(1)$ và path length $O(1)$, nhưng complexity theo sequence length là $O(n^2d)$.
7. Trong WMT 2014 translation setup và baseline/cost mà paper báo cáo; không phải claim bao trùm mọi task hoặc mọi protocol.

## Evidence map

| Link | Trang | Evidence chính | Dùng để kết luận |
|---|---:|---|---|
| [[Attention Is All You Need.pdf#page=1]] | PDF tr. 1 | Abstract, authors, venue, headline BLEU | Problem, contribution, metadata |
| [[Attention Is All You Need.pdf#page=2]] | PDF tr. 2 | RNN sequential bottleneck, first attention-only transduction claim | Motivation và formulation |
| [[Attention Is All You Need.pdf#page=3]] | PDF tr. 3 | Figure 1, encoder/decoder stacks, residual + layer norm | Architecture |
| [[Attention Is All You Need.pdf#page=4]] | PDF tr. 4 | Figure 2, scaled dot-product attention, Eq. 1 | Attention formula |
| [[Attention Is All You Need.pdf#page=5]] | PDF tr. 5 | Multi-head equations, attention applications, FFN Eq. 2 | MHA/FFN details |
| [[Attention Is All You Need.pdf#page=6]] | PDF tr. 6 | Positional encodings, Table 1, why self-attention | Position và complexity trade-off |
| [[Attention Is All You Need.pdf#page=8]] | PDF tr. 8 | Table 2, training data/schedule, BLEU results | Main translation results |
| [[Attention Is All You Need.pdf#page=9]] | PDF tr. 9 | Table 3 ablations | Head count, dimensions, dropout, positional embedding |
| [[Attention Is All You Need.pdf#page=10]] | PDF tr. 10 | Table 4, conclusion, code URL | Parsing generalization, limitations/future work |
| [[Attention Is All You Need.pdf#page=13]] | PDF tr. 13 | Attention visualization Figure 3 | Long-distance dependency example |

## Liên kết

- [[2017 - Attention Is All You Need - arXiv 1706.03762v7]]
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Embeddings]]
- [[Encoder-Decoder Architecture]]
- [[Attention Mask]]
- [[Feed-Forward Layer]]
