---
type: paper
status: draft
title: "Prefix-Tuning: Optimizing Continuous Prompts for Generation"
aliases:
  - Prefix-Tuning
authors:
  - Xiang Lisa Li
  - Percy Liang
year: 2021
venue: "ACL 2021"
url: "https://aclanthology.org/2021.acl-long.353/"
pdf:
doi: "10.18653/v1/2021.acl-long.353"
arxiv: "2101.00190"
code: "https://github.com/XiangLi1999/PrefixTuning"
topic:
  - prefix tuning
  - prompt tuning
  - parameter-efficient tuning
priority: high
reading_status: not-started
related_concepts:
  - "[[Prefix Tuning]]"
  - "[[Prompt Tuning]]"
  - "[[Parameter-Efficient Fine-Tuning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - prompting
  - peft
---

# Prefix-Tuning: Optimizing Continuous Prompts for Generation

## Tóm tắt một câu

Prefix-Tuning giữ backbone language model đóng băng và chỉ học một chuỗi vector prefix liên tục để điều kiện hóa mô hình cho task mới.

## Vì sao cần cho đề tài

Đây là nền trực tiếp cho các prompt vector trong Prompt Tree. Trước khi thiết kế root/internal/leaf prompts, cần hiểu prefix được chèn vào attention như “virtual tokens” và vì sao nó tiết kiệm tham số hơn full fine-tuning.

## Nguồn đã kiểm

- ACL Anthology: [2021.acl-long.353](https://aclanthology.org/2021.acl-long.353/)
- arXiv: [2101.00190](https://arxiv.org/abs/2101.00190)

## Cần đọc tiếp

- Prefix được chèn vào layer nào.
- Prefix key/value khác soft prompt input-level ở đâu.
- Khi nào prefix tuning yếu hơn full fine-tuning.
