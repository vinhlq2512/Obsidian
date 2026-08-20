---
type: paper
status: draft
title: "FPrompt-PLM: Flexible-Prompt on Pretrained Language Model for Continual Few-Shot Relation Extraction"
authors:
  - Lingling Zhang
  - Yifei Li
  - Qianying Wang
  - Yun Wang
  - Hang Yan
  - Jiaxin Wang
  - Jun Liu
year: 2024
venue: "IEEE Transactions on Knowledge and Data Engineering"
url: "https://ieeexplore.ieee.org/document/10584140/"
pdf:
doi: "10.1109/TKDE.2024.3419117"
arxiv:
topic:
  - continual few-shot relation extraction
  - prompt learning
  - prototype learning
priority: medium
reading_status: not-started
rating:
related_concepts:
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Relation Extraction]]"
  - "[[Prototype Learning]]"
  - "[[Prompt Tuning]]"
created_at: 2026-08-21
updated_at: 2026-08-21
tags:
  - paper
  - relation-extraction
  - continual-learning
---

# FPrompt-PLM: Flexible-Prompt on Pretrained Language Model for Continual Few-Shot Relation Extraction

## Tóm tắt một câu

FPrompt-PLM xử lý [[Continual Few-Shot Relation Extraction]] bằng cách kết hợp flexible prompts, hiểu ngôn ngữ từ PLM, nearest-prototype prediction, prompt pool và prototype pool để giảm quên thảm họa và overfitting trong bối cảnh ít mẫu.

## Nguồn

- Publisher page: [IEEE Xplore](https://ieeexplore.ieee.org/document/10584140/)
- Metadata/abstract: [Xi'an Jiaotong University publication page](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/)
- Bibliographic check: [DBLP](https://dblp.org/rec/journals/tkde/ZhangLWWYWL24.html)
- Code: [lyfxjtu/FPrompt-PLM](https://github.com/lyfxjtu/FPrompt-PLM)
- PDF local: chưa có. IEEE trả lỗi truy cập khi thử tải tự động ngày 2026-08-21.

## Trạng thái và phạm vi ghi chú

Ghi chú này là bản ingest + scaffold từ metadata chính thức, abstract công khai và README của repository. Chưa có full-text PDF local, nên các phần kết quả định lượng, công thức chính xác, số bảng và số trang cần được kiểm chứng lại khi có PDF.

## Vấn đề paper giải quyết

[[Relation Extraction]] truyền thống thường giả định có tập dữ liệu huấn luyện lớn và cố định. CFS-RE thực tế hơn vì quan hệ mới xuất hiện liên tục, trong khi mỗi quan hệ mới chỉ có rất ít ví dụ gán nhãn.

Hai khó khăn trung tâm:

- `reported`: model phải học quan hệ mới theo thời gian nhưng không quên quan hệ cũ.
- `reported`: few-shot setting dễ khiến mô hình overfit vào vài ví dụ mới.

## Gap và đóng góp

Paper định vị FPrompt-PLM như một framework prompt-learning trên pretrained language model cho CFS-RE.

Các đóng góp được báo cáo:

- Flexible-prompt embedding để biểu diễn thông tin prompt theo từng giai đoạn học.
- Pretrained-language understanding để tận dụng năng lực PLM thay vì huấn luyện encoder từ đầu.
- Nearest-prototype learning để phân loại quan hệ theo khoảng cách tới prototype.
- Hai pool được cập nhật liên tục: prompt pool lưu prompt embedding đặc trưng theo thời kỳ, prototype pool lưu prototype của các relation đã học.
- Loss được mở rộng bằng nhiều distillation loss và prototype-diversity loss.

## Mental model

Có thể đọc FPrompt-PLM như một hệ thống có hai loại bộ nhớ:

1. Prompt pool nhớ cách “đặt câu hỏi” hoặc điều kiện hóa PLM ở các giai đoạn khác nhau.
2. Prototype pool nhớ tâm cụm biểu diễn cho từng relation đã thấy.

Khi task mới đến, mô hình không chỉ fine-tune vào vài mẫu mới. Nó vừa cập nhật prompt/prototype mới, vừa giữ các prompt/prototype cũ đủ phân biệt để tránh trộn relation cũ và mới.

## Phương pháp

### 1. Flexible-prompt embedding

`reported`: framework dùng flexible prompts thay vì chỉ dựa vào hard prompt cố định. Điểm cần kiểm chứng khi có PDF là prompt được parameterize thế nào, có tăng tham số theo số task hay không, và prompt pool được chọn ở inference ra sao.

### 2. Prompt pool và prototype pool

`reported`: prompt pool ghi lại prompt embedding đặc trưng theo từng time period; prototype pool ghi lại prototypes của các relation đã học. Cả hai pool được cập nhật liên tục và được dùng để dự đoán tất cả relation đã thấy tại thời điểm hiện tại.

### 3. Continual meta-finetuning

Paper mô tả ba stage:

- Meta-training.
- Continual meta-finetuning.
- Testing.

Đây là điểm khác với các cách chỉ train tuần tự từng task: FPrompt-PLM muốn dùng meta-learning/fine-tuning để giúp model thích nghi với relation mới trong few-shot regime.

### 4. Nearest-prototype learning

Thay vì dùng classifier head cố định cho toàn bộ nhãn, paper báo cáo dùng nearest-prototype learning. Cần kiểm chứng công thức khoảng cách và cách normalize embedding khi có full-text.

### 5. Distillation và prototype diversity

`reported`: loss gồm nhiều distillation losses và một prototype-diversity loss. Diễn giải học tập: distillation giữ hành vi/tri thức cũ; prototype diversity ép các prototype phân tách hơn để giảm nhầm lẫn khi label space tăng dần.

## Experimental setup

Thông tin đã xác minh từ README/code page:

- Dataset: FewRel và TACRED.
- Sentence encoder trong case study: BERT Base.
- Có case study bằng similarity heatmaps giữa 15 prototypes và 3 prompts trên TACRED.

Thông tin cần đọc lại từ PDF:

- Số task/session, số relation mỗi task, số shot.
- Task order và số random seeds.
- Metric chính và cách average.
- Baselines cụ thể và liệu có retune hyperparameter hay không.
- Memory budget cho prompt/prototype pools.

## Kết quả chính

`reported`: abstract nói thí nghiệm trên hai dataset phổ biến cho thấy FPrompt-PLM cải thiện đáng kể so với SOTA baselines.

Chưa ghi số định lượng vì chưa có bảng kết quả full-text để kiểm chứng. Không nên so sánh trực tiếp với CPL, ConPL, WAVE hoặc WAVE++ cho tới khi protocol fingerprint được đối chiếu.

## Hạn chế và assumptions

- Chưa xác minh được PDF local, nên note này chưa có page-level evidence.
- Prompt pool và prototype pool có thể tăng chi phí lưu trữ hoặc suy luận theo số task/relation; cần đọc chi tiết implementation.
- Nếu prototype diversity chỉ cải thiện phân tách embedding nhưng không xử lý task identity ở inference, model vẫn có thể nhầm giữa relation gần nhau.
- Kết quả “SOTA” cần đọc scope baseline, dataset split và random seed trước khi chấp nhận.

## Diễn giải học tập

FPrompt-PLM nằm giữa hai dòng ý tưởng đang lặp lại trong nhóm paper CRE:

- Giống CPL/ConPL ở chỗ xem prototype là đại diện relation quan trọng.
- Giống WAVE/WAVE++ ở chỗ prompt không còn là một vector duy nhất mà trở thành cấu trúc có bộ nhớ theo thời gian.

Khác biệt cần chú ý là FPrompt đặt cả prompt và prototype vào pool được cập nhật liên tục. Vì vậy câu hỏi nghiên cứu hay là: “Khi nào nên lưu knowledge cũ dưới dạng prototype, khi nào nên lưu dưới dạng prompt?”

## Câu hỏi review

1. CFS-RE trong FPrompt-PLM khác continual relation extraction thông thường ở điểm nào?
2. Prompt pool lưu loại tri thức gì, prototype pool lưu loại tri thức gì?
3. Vì sao nearest-prototype learning hợp với few-shot relation extraction?
4. Distillation loss và prototype-diversity loss nhắm vào hai failure mode nào?
5. Nếu số relation tăng liên tục, prompt/prototype pool có scale tốt không?
6. FPrompt-PLM có dùng exemplar replay không, hay chỉ dùng prompt/prototype memory?
7. Protocol trên FewRel/TACRED có tương thích trực tiếp với CPL/ConPL/WAVE++ không?

## Cần đọc tiếp

- Tải hoặc mở full-text PDF để bổ sung page-level evidence.
- Trích công thức flexible prompt, nearest-prototype, distillation và prototype-diversity loss.
- Điền bảng kết quả và ablation.
- So sánh protocol với [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]], [[Adaptive Prompting for Continual Relation Extraction]], và [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]].

## Evidence map

| Claim | Evidence | Nhãn |
|---|---|---|
| FPrompt-PLM gồm flexible-prompt embedding, pretrained-language understanding và nearest-prototype learning | [Xi'an Jiaotong University metadata/abstract](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) | reported |
| Prompt pool và prototype pool được cập nhật liên tục và dùng để dự đoán các relation đã thấy | [Xi'an Jiaotong University metadata/abstract](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) | reported |
| Paper đăng ở IEEE TKDE 36(12):8267-8282, DOI 10.1109/TKDE.2024.3419117 | [DBLP](https://dblp.org/rec/journals/tkde/ZhangLWWYWL24.html) và [Xi'an Jiaotong University](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) | reported |
| Code repository có split FewRel và TACRED, case study TACRED với BERT Base | [GitHub README](https://github.com/lyfxjtu/FPrompt-PLM) | reported |

## Liên kết

- [[Continual Few-Shot Relation Extraction]]
- [[Relation Extraction]]
- [[Prototype Learning]]
- [[Prompt Tuning]]
- [[Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]
- [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- [[Adaptive Prompting for Continual Relation Extraction]]
- [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]
