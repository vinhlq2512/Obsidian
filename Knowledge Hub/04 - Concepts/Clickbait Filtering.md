---
type: concept
status: understood
sources:
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - recommendation
  - machine-learning
---

# Clickbait Filtering

## Định nghĩa

Clickbait Filtering (Bộ lọc tiêu đề câu view) là hệ thống Machine Learning được tích hợp trong quy trình Ranking của các nền tảng mạng xã hội và giải trí (như Meta, LinkedIn, YouTube) nhằm phát hiện, hạ điểm tín hiệu (demotion) và loại bỏ các nội dung dùng tiêu đề giật gân, thiếu thông tin hoặc gây hiểu nhầm.

## Cơ chế hoạt động & Metrics

```text
Content Item (Title, Image, Video Body)
-> NLP / Vision Classifier (Detect Suspicious Patterns: Exaggeration, Withholding Info)
-> Post-Click User Behavior Signals (Watch-Time, Dwell-Time, Immediate Back-Click)
-> Calculate Quality Score: Quality = CTR / Expected_WatchTime
-> Feed Ranking Engine (Apply Demotion Multiplier)
```

- **Early Signals (NLP/Multimodal)**: Phân tích tiêu đề bằng các thuật toán NLP để tìm cấu trúc giật gân ("Bạn sẽ không tin được...", "Bí mật này sẽ...").
- **Behavioral Signals (Post-Click)**:
  - **Dwell Time / Watch Time**: Nếu CTR rất cao nhưng thời gian đọc/xem lại rất thấp (dưới vài giây), đây là tín hiệu clickbait điển hình.
  - **Click-to-Bounce Ratio**: Tỷ lệ người dùng click vào xong lập tức bấm back quay lại feed.

## So sánh cách tiếp cận

- **YouTube**: Sử dụng **Expected Watch Time** thay vì Click-Through Rate (CTR) làm mục tiêu tối ưu hóa của mô hình gợi ý.
- **LinkedIn / Meta**: Áp dụng mô hình hai giai đoạn: Giai đoạn 1 phân loại bài viết có hành vi câu tương tác (engagement bait), Giai đoạn 2 giảm bớt trọng số hiển thị (demote) ở bước Reranking.

## Liên kết

- [[Recommendation Funnel]]
- [[Ranking]]
- [[Reranking]]
- [[Semantic Feed Retrieval Systems]]
