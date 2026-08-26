---
type: paper-reading
date: 2026-08-16
status: scaffolded
paper: "[[Attention Is All You Need]]"
pdf: "[[Attention Is All You Need.pdf]]"
created_at: 2026-08-16
updated_at: 2026-08-23
tags:
  - paper-reading
  - transformer
  - attention
---

# 2026-08-16 - Attention Is All You Need

## Tiến độ

- Bắt đầu đọc paper này.
- Working note chi tiết đã được scaffold ở [[2026-08-19 - Attention Is All You Need - Gemini Notebook Workflow]].
- Trạng thái này chỉ ghi nhận phiên đọc đã bắt đầu; không tự coi là đã đọc xong paper.

## Bản đồ đọc nhanh

- **Problem:** RNN/CNN trong sequence transduction bị bottleneck tuần tự hoặc path length dài khi mô hình hóa phụ thuộc xa.
- **Main idea:** dùng encoder-decoder chỉ dựa trên attention, kết hợp scaled dot-product attention, multi-head attention, residual connection, layer normalization, FFN theo từng vị trí và positional encoding.
- **Kết quả chính:** Transformer big đạt 28.4 BLEU trên WMT 2014 English-German và 41.8 BLEU trên English-French theo paper note chính.
- **Cần tự kiểm khi đọc:** Eq. 1 vì sao chia $\sqrt{d_k}$; Table 1 về complexity/path length; Table 2 về BLEU/cost; Table 3 về ablation head count, dropout và positional encoding.

## Việc đọc tiếp

- [ ] Tự recall lại problem/gap mà không nhìn note.
- [ ] Đọc kỹ Figure 1, Eq. 1-3 và Table 1-3 trong PDF.
- [ ] Dùng workflow Gemini để oral exam từng phần.

## Liên kết

- [[Attention Is All You Need]]
- [[Attention Is All You Need.pdf]]
- [[2026-08-19 - Attention Is All You Need - Gemini Notebook Workflow]]
