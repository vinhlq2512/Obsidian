---
type: paper
status: draft
title: "Re-TACRED: Addressing Shortcomings of the TACRED Dataset"
aliases:
  - Re-TACRED
authors:
  - George Stoica
  - Emmanouil Antonios Platanios
  - Barnabas Poczos
year: 2021
venue: "AAAI 2021"
url: "https://ojs.aaai.org/index.php/AAAI/article/view/17631"
pdf: "[[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf]]"
zotero_key:
citekey: stoica2021retacred
doi: "10.1609/aaai.v35i15.17631"
arxiv: "2104.08398"
code_url: "https://github.com/gstoica27/Re-TACRED"
dataset_url: "https://github.com/gstoica27/Re-TACRED"
source_version: v1
topic:
  - relation extraction
  - dataset quality
  - TACRED
priority: medium
reading_status: not-started
rating:
related_concepts:
  - "[[Relation Extraction]]"
  - "[[Continual Relation Extraction]]"
created_at: 2026-09-05
updated_at: 2026-09-08
tags:
  - paper
  - dataset
  - relation-extraction
---

# Re-TACRED: Addressing Shortcomings of the TACRED Dataset

## Tóm tắt một câu

Re-TACRED là phiên bản tái gắn nhãn toàn diện và chuẩn hóa của benchmark [[Relation Extraction|relation extraction]] TACRED (giảm từ 106.264 xuống 91.467 câu trên 40 quan hệ), khắc phục tỷ lệ nhãn sai 23,9% trong TACRED gốc và nâng micro F1-score trung bình của các mô hình SOTA thêm +14,3%, qua đó khôi phục thứ hạng thực chất của các kiến trúc mô hình vốn bị che mờ bởi dữ liệu nhiễu.

## Nguồn

- Paper AAAI: [Addressing Shortcomings of the TACRED Dataset (AAAI 2021)](https://ojs.aaai.org/index.php/AAAI/article/view/17631)
- arXiv: [2104.08398](https://arxiv.org/abs/2104.08398)
- PDF trong vault: [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf]]
- Code & dataset patch: [gstoica27/Re-TACRED](https://github.com/gstoica27/Re-TACRED)

## Vấn đề paper giải quyết

TACRED (Zhang et al., 2017) là một trong những tập dữ liệu lớn nhất và được sử dụng rộng rãi nhất cho bài toán trích xuất quan hệ ở mức câu (sentence-level [[Relation Extraction|relation extraction]]), bao gồm 106.264 câu thu thập từ các kỳ đánh giá TAC KBP 2009–2014. Dù các mô hình liên tục tích hợp tri thức ngoài (NER, POS, dependency parsing) và các mô hình ngôn ngữ tiền huấn luyện (SpanBERT, RoBERTa), hiệu năng trên tập test TACRED dường như chạm trần ở mức ~71,5% F1. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=1|PDF, tr. 1]]

Nghiên cứu trước đó của Alt et al. (2020) chỉ ra rằng hơn 50% câu khó bị phân loại sai nhiều nhất trong tập dev/test thực chất là do gán nhãn sai, và việc sửa nhãn giúp tăng 8% F1. Tuy nhiên, nghiên cứu của Alt et al. chỉ giới hạn trên mẫu thiên lệch gồm 5.000 câu (chiếm chưa đầy 5% tập dữ liệu), khiến 95% câu còn lại của TACRED vẫn chưa được kiểm chứng, không thể khái quát hóa và không thể biết rõ lỗi dự đoán phát sinh từ giới hạn mô hình hay do nhãn sai. Paper này giải quyết bài toán tái gắn nhãn toàn bộ 106k câu của TACRED thông qua quy trình crowdsourcing tối ưu chi phí và kiểm soát chất lượng nghiêm ngặt. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=1|PDF, tr. 1]] [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=2|PDF, tr. 2]]

## Gap và đóng góp

- **Khảo sát và sửa toàn bộ dữ liệu**: Thay vì chỉ kiểm tra một mẫu nhỏ thiên lệch, paper kiểm chứng toàn bộ 106.264 câu của TACRED, phát hiện **23,9% nhãn trong TACRED bị gán sai** (trong số nhãn bị sửa, 75,3% là do TACRED gán nhầm `NO_RELATION` cho các câu thực sự mang quan hệ dương tính). [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5|PDF, tr. 5]]
- **Chiến lược crowdsourcing cải tiến**:
  1. *Xử lý lỗi loại thực thể (Wrong Type Handling)*: Khắc phục điểm yếu chí mạng của TACRED gốc (annotator chỉ được chọn quan hệ khớp với NER type có sẵn) bằng cách gom 27 cặp type thành 8 *super-clusters*, cho phép tùy chọn `WRONG_TYPES` và phân tầng đa giai đoạn (multi-stage) giới hạn tối đa 9 nhãn/lần để giảm tải nhận thức, giúp giảm chi phí annotation tồi nhất xuống ~3,4 lần ($27/8$). [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=3|PDF, tr. 3]] [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=4|PDF, tr. 4]]
  2. *Tinh chỉnh định nghĩa quan hệ*: Loại bỏ các phân định quá chi tiết ở mức tài liệu (document-level) không thể suy diễn ở mức câu đơn (như gộp `MEMBER_OF` và `PARENTS`, gộp `MEMBERS` và `SUBSIDIARIES`); bổ sung `PERSON:IDENTITY` để bao quát quy chiếu đại từ (pronominal references); và nới lỏng `HEADQUARTERS` thành `BRANCH`. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=4|PDF, tr. 4]]
  3. *Đảm bảo chất lượng hai lớp (Trial & Control)*: Kiểm tra năng lực đầu vào (Trial test yêu cầu 100%) kết hợp chèn 20% câu kiểm soát ẩn (Control sentences yêu cầu độ chính xác $\ge 80\%$), loại bỏ hiệu quả các annotator gian lận. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5|PDF, tr. 5]]
- **Bộ dữ liệu Re-TACRED sạch**: Đạt độ đồng thuận giữa các annotator là 82,3% và Fleiss' kappa 0,77 (so với 0,54 của TACRED gốc). Sau khi lọc 1.058 câu không phải tiếng Anh và các câu có entity span bị cắt cụt/nhập nhằng, Re-TACRED còn 91.467 câu phân bố trên 40 quan hệ. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5|PDF, tr. 5]]
- **Đánh giá lại các mô hình SOTA**: Kiểm nghiệm trên 3 mô hình đại diện (PA-LSTM, C-GCN, SpanBERT) cho thấy F1 tăng vọt trung bình 14,3%, đồng thời làm lộ ra sự vượt trội thực sự của các kiến trúc tiên tiến (như C-GCN vượt trội rõ rệt PA-LSTM chứ không chỉ ngang ngửa như trên dữ liệu TACRED nhiễu). [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=6|PDF, tr. 6]]

## Bài toán/formalization

Mỗi mẫu trong bài toán trích xuất quan hệ câu được biểu diễn bằng một bộ dữ liệu:

$$
(x, s, T_s, o, T_o, y)
$$

Trong đó:
- $x = (w_1, w_2, \dots, w_n)$ là chuỗi từ của câu context.
- $s$ và $o$ là hai đoạn văn bản không chồng lấn biểu diễn subject span và object span.
- $T_s \in \{\text{PERSON}, \text{ORGANIZATION}\}$ là loại thực thể được gán trước cho subject.
- $T_o$ là loại thực thể được gán trước cho object (thuộc 1 trong 17 types, tạo thành 27 cặp $(T_s, T_o)$ hợp lệ). [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=2|PDF, tr. 2]]
- $y \in \mathcal{Y}$ là nhãn quan hệ cần dự đoán giữa $s$ và $o$.

**Không gian nhãn $\mathcal{Y}$**:
- **TACRED gốc**: gồm 41 quan hệ dương tính + 1 nhãn `NO_RELATION` = 42 nhãn.
- **Re-TACRED**: gồm 39 quan hệ dương tính + 1 nhãn `NO_RELATION` = 40 nhãn (do gộp 4 quan hệ tổ chức thành 2, mở rộng `ALTERNATE_NAMES` thành `IDENTITY`).
- Tỷ lệ nhãn âm (`NO_RELATION`) giảm mạnh từ **79,6%** trong TACRED xuống **63,2%** trong Re-TACRED, giúp giảm áp lực mất cân bằng lớp (negative bias). [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=8|PDF, tr. 8]]

## Phương pháp tái gắn nhãn Re-TACRED

### 1. Cơ chế xử lý gán sai loại thực thể (Wrong Type Handling) & Super-clusters

Khảo sát 1.000 câu ngẫu nhiên trong TACRED cho thấy khoảng 5% câu có nhãn NER type bị sai (ví dụ "Thomas More Law Center" bị gán nhầm là `PERSON` thay vì `ORGANIZATION`). Do thiết kế cũ của Zhang et al. (2017) chỉ đưa ra danh sách quan hệ ứng viên khớp với cặp type $(T_s, T_o)$, nếu type ban đầu sai thì annotator bắt buộc phải chọn `NO_RELATION` hoặc một nhãn sai khác. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=3|PDF, tr. 3]]

Để khắc phục mà không làm bùng nổ chi phí (nếu thử hết 27 cặp type thì chi phí tăng 130%), nhóm tác giả gom các nhóm câu có type hay bị nhầm lẫn thành **8 super-clusters** (Bảng 1):

| Super-Cluster | Subject Type | Object Types gộp |
|---|---|---|
| `org2miscmulti` | ORGANIZATION | URL, DATE, NUMBER, RELIGION, IDEOLOGY, MISC |
| `org2locmulti` | ORGANIZATION | CITY, COUNTRY, STATE_OR_PROVINCE, LOCATION |
| `org2org` | ORGANIZATION | ORGANIZATION |
| `org2per` | ORGANIZATION | PERSON |
| `per2miscmulti` | PERSON | TITLE, DATE, CRIMINAL_CHARGE, RELIGION, NUMBER, CAUSE_OF_DEATH, DURATION, MISC |
| `per2locmulti` | PERSON | NATIONALITY, COUNTRY, STATE_OR_PROVINCE, CITY, LOCATION |
| `per2org` | PERSON | ORGANIZATION |
| `per2per` | PERSON | PERSON |

Tập quan hệ ứng viên của mỗi super-cluster là hợp (union) các quan hệ của các nhóm con. Nếu số lượng quan hệ ứng viên $\le 9$, bài toán gắn nhãn thực hiện trong 1 giai đoạn (single-stage). Nếu $> 9$ quan hệ (tối đa lên tới 14), bài toán được chia nhỏ thành nhiều tập con $\le 9$ (multi-stage); câu bị annotator đánh dấu `WRONG_TYPES` sẽ được đẩy sang tập con tiếp theo cho đến khi tìm được nhãn phù hợp. Cách tiếp cận này giảm hệ số chi phí tồi nhất từ 27 xuống 8 ($27/8 \approx 3,4$ lần). [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=3|PDF, tr. 3]] [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=4|PDF, tr. 4]]

### 2. Tinh chỉnh và chuẩn hóa định nghĩa quan hệ

Nhóm tác giả tiến hành 4 điều chỉnh căn bản đối với hướng dẫn gán nhãn TAC KBP: [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=4|PDF, tr. 4]]

1. **`PERSON:IDENTITY`**: Trong TACRED gốc, các câu có đại từ thay thế chỉ cùng một người (pronominal identity, ví dụ: `"[Holly]SUB showed off a few pieces of [her]OBJ jewelry"`) chiếm tới gần 10% dữ liệu nhưng bị gắn lẫn lộn giữa `PERSON:OTHER_FAMILY` và `NO_RELATION`. Nhóm tác giả mở rộng `PERSON:ALTERNATE_NAMES` để bao gồm cả quy chiếu đại từ và đổi tên thành `PERSON:IDENTITY`, đồng thời cấm `PERSON:OTHER_FAMILY` nhận các trường hợp đại từ này.
2. **Gộp quan hệ tổ chức (`ORGANIZATION:MEMBER_OF` và `ORGANIZATION:MEMBERS`)**: TAC KBP phân biệt quan hệ tự nguyện (`MEMBER_OF`) và phụ thuộc công ty mẹ-con (`PARENTS`), cũng như cặp nghịch đảo (`MEMBERS` vs `SUBSIDIARIES`). Việc phân biệt này ở mức câu đơn là bất khả thi nếu không tra cứu thêm thông tin ngoài internet (ví dụ quan hệ giữa LinkedIn và Microsoft). Nhóm tác giả gộp `PARENTS` vào `MEMBER_OF`, và gộp `SUBSIDIARIES` vào `MEMBERS`.
3. **Phân ranh giới đơn nhãn (Single-label disambiguation)**: Thiết lập quy tắc tường minh để tách các quan hệ dễ chồng lấn như `PERSON:CITIES_OF_RESIDENCE` và `PERSON:CITY_OF_BIRTH` (ví dụ: bất kỳ câu nào có từ "native of" hoặc từ đồng nghĩa đều bắt buộc gán quan hệ nơi sinh, không gán nơi cư trú).
4. **`ORGANIZATION:*_OF_BRANCH`**: Cụm từ "ORGANIZATION from CITY" trong thực tế rất mơ hồ, không thể khẳng định là trụ sở chính (`HEADQUARTERS`). Định nghĩa được tổng quát hóa thành văn phòng/chi nhánh đại diện (`BRANCH`).

### 3. Quy trình kiểm soát chất lượng 2 tầng (Quality Assurance)

Áp dụng kỹ thuật gated-instruction để ngăn ngừa dữ liệu rác: [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5|PDF, tr. 5]]

- **Giai đoạn Trial (Đầu vào)**: Crowd-worker phải có ít nhất 500 tasks được chấp thuận trên AMT với tỷ lệ phê duyệt $\ge 95\%$. Sau đó, họ phải vượt qua bài kiểm tra năng lực (qualification test) riêng cho từng super-cluster với số điểm tuyệt đối 100%.
- **Giai đoạn Control (Trong quá trình gán nhãn)**: Để chống lại tình trạng worker làm cẩn thận lúc thi nhưng gắn nhãn ẩu khi làm thật, cứ mỗi 5 câu trong 1 HIT thì có **1 câu gold control** (tổng cộng ~2.000 câu control được gán nhãn chuyên gia). Bất kỳ worker nào có độ chính xác trên tập control rơi xuống dưới $80\%$ đều bị loại bỏ ngay lập tức (loại khoảng 10% worker gian lận). Mỗi HIT gồm 5 câu được trả $0.15.

### 4. Loại bỏ câu nhiễu thô (Miscellaneous Revisions)

- Dùng thư viện FastText lọc bỏ 1.058 câu không phải tiếng Anh, đưa số lượng về 105.206 câu. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5|PDF, tr. 5]]
- Phân tích 500 câu có tỷ lệ bất đồng giữa các annotator cao nhất; phát hiện nguyên nhân chủ yếu do entity span bị cắt cụt hoặc đa nghĩa (ví dụ: object span chỉ chứa từ "[Champions]OBJ" trong cụm "Champions League"). Nhóm tác giả quyết định loại bỏ toàn bộ các câu mập mờ này, thu được tập Re-TACRED hoàn chỉnh gồm **91.467 câu**. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5|PDF, tr. 5]]

## Protocol fingerprint

| Trường | Giá trị trong Re-TACRED |
|---|---|
| Nguồn văn bản gốc | Tin tức, bài viết từ các kỳ đánh giá TAC KBP 2009–2014 |
| Quy mô dữ liệu | 91.467 câu (sau khi loại 1.058 câu không phải tiếng Anh và các câu có span nhập nhằng) |
| Không gian nhãn | 40 quan hệ (39 quan hệ dương tính + 1 `NO_RELATION`) |
| Tỷ lệ nhãn âm (`NO_RELATION`) | Giảm từ 79,6% (TACRED) xuống 63,2% (Re-TACRED) |
| Tỷ lệ nhãn TACRED bị sai | 23,9% (75,3% Neg $\to$ Pos; 16,1% Pos $\to$ Neg; 8,6% Pos $\to$ Pos) |
| Chỉ số thỏa thuận | Agreement rate 82,3%; Fleiss' kappa 0,77 (TACRED gốc là 0,54) |
| Chia tập (Splits) | Kế thừa train/dev/test nguyên bản của TACRED (theo năm KBP 2009-2012 / 2013 / 2014) |
| Mô hình thực nghiệm | PA-LSTM (Zhang et al., 2017), C-GCN (Zhang et al., 2018), SpanBERT (Joshi et al., 2020) |
| Hạ tầng phần cứng | 1 GPU Nvidia Titan X cho PA-LSTM và C-GCN; 1 GPU Nvidia Tesla V100 cho SpanBERT |
| Giao thức đo lường | Micro-averaged Precision, Recall, F1 của checkpoint có dev F1 trung vị (median) qua 5 lần chạy độc lập |
| Phương thức phân phối | Script và patch gán nhãn đè (do hạn chế bản quyền LDC của TACRED gốc) |

## Kết quả chính

### 1. Tác động toàn diện lên hiệu năng các mô hình (Bảng 2)

Đánh giá trên tập test cho thấy cả 3 mô hình đều có bước nhảy vọt mạnh mẽ về mọi chỉ số trên Re-TACRED so với TACRED: [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=6|PDF, tr. 6]]

| Dataset | Metric | PA-LSTM | C-GCN | SpanBERT |
|---|---|---:|---:|---:|
| **TACRED** | Precision | 68,1 | 68,5 | 70,1 |
| | Recall | 64,5 | 64,4 | 69,2 |
| | Micro F1 | 66,2 | 66,3 | 69,7 |
| **Re-TACRED** | Precision | 79,2 | 80,9 | 85,2 |
| | Recall | 79,5 | 79,7 | 85,4 |
| | Micro F1 | **79,4** | **80,3** | **85,3** |
| **Độ chênh lệch (Difference)** | Precision | +11,1 | +12,4 | +15,1 |
| | Recall | +15,0 | +15,3 | +16,2 |
| | Micro F1 | **+13,2** | **+14,0** | **+15,6** |

*Nhận xét quan trọng*: Mức tăng F1 trung bình là **+14,3%**. Đáng chú ý, mức tăng này không đối xứng đơn thuần là một hệ số cộng thêm (offset/scaling). Trên TACRED, C-GCN (66,3%) và PA-LSTM (66,2%) dường như tương đương nhau; nhưng trên Re-TACRED, C-GCN (80,3%) bứt phá vượt trội rõ rệt so với PA-LSTM (79,4%), đặc biệt chênh lệch Precision lên tới 1,7%. SpanBERT đạt 85,3% F1, khẳng định ưu thế vượt trội của cơ chế span pretraining khi dữ liệu được đánh giá chính xác. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=6|PDF, tr. 6]]

### 2. Thay đổi hiệu năng theo từng nhóm quan hệ (Bảng 3)

| Model | Dataset | PER:* | ORG:* | PER:ORG | ORG:PER | PER:LOCATION | PER:PER | ORG:ORG |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **PA-LSTM** | TACRED | 66,8 | 65,2 | 65,3 | 72,6 | 51,9 | 59,9 | 59,3 |
| | Re-TACRED | 79,0 | 74,4 | 68,3 | 85,1 | 53,4 | 85,2 | 70,3 |
| | *Chênh lệch* | *+12,2* | *+9,2* | *+3,0* | *+12,5* | *+1,5* | *+15,3* | *+11,0* |
| **C-GCN** | TACRED | 66,5 | 65,9 | 66,4 | 72,2 | 51,5 | 49,9 | 61,6 |
| | Re-TACRED | 81,0 | 78,1 | 69,0 | 86,8 | 55,1 | 86,2 | 73,8 |
| | *Chênh lệch* | *+14,5* | *+12,2* | *+2,6* | *+14,6* | *+3,6* | *+36,3* | *+12,2* |
| **SpanBERT** | TACRED | 69,7 | 69,5 | 68,9 | 74,8 | 55,9 | 61,2 | 68,1 |
| | Re-TACRED | 85,9 | 83,3 | 80,6 | 88,8 | 71,2 | 88,6 | 82,4 |
| | *Chênh lệch* | *+16,2* | *+13,8* | *+11,7* | *+14,0* | *+15,3* | *+17,4* | *+14,3* |

*Hiện tượng thú vị được giải mã*: Trên TACRED, PA-LSTM từng đánh bại C-GCN tới 10% ở nhóm quan hệ `PER:PER` (59,9% vs 49,9%). Tuy nhiên, trên Re-TACRED, C-GCN vươn lên đạt 86,2% (+36,3%), vượt qua PA-LSTM (85,2%). Nhiễu nhãn trong TACRED trước đây đã tạo ra ảo ảnh rằng PA-LSTM học quan hệ người-người tốt hơn đồ thị phụ thuộc (dependency tree) của C-GCN. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=7|PDF, tr. 7]]

### 3. Tác động của việc tinh chỉnh định nghĩa nhãn (Bảng 4)

| Model | Dataset | ORG:MEMBER_OF | ORG:MEMBERS | PER:RESIDENCE | PER:BIRTH | PER:DEATH | ORG:LOCATION | PER:IDENTITY |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **PA-LSTM** | TACRED | 22,6 | 23,5 | 54,1 | 31,0 | 26,7 | 55,9 | 0,0 |
| | Re-TACRED | 42,7 | 48,8 | 55,2 | 57,1 | 40,5 | 68,1 | 87,8 |
| | *Chênh lệch* | *+20,1* | *+25,3* | *+1,1* | *+26,1* | *+13,8* | *+12,2* | *+87,8* |
| **C-GCN** | TACRED | 24,6 | 24,0 | 54,1 | 30,0 | 25,0 | 56,7 | 0,0 |
| | Re-TACRED | 43,1 | 61,8 | 55,8 | 56,4 | 49,4 | 74,1 | 88,0 |
| | *Chênh lệch* | *+18,5* | *+37,8* | *+1,7* | *+26,4* | *+24,4* | *+17,4* | *+88,0* |
| **SpanBERT** | TACRED | 50,3 | 52,2 | 57,6 | 50,0 | 26,7 | 62,7 | 19,1 |
| | Re-TACRED | 73,4 | 70,0 | 70,0 | 81,8 | 74,5 | 78,5 | 90,5 |
| | *Chênh lệch* | *+23,1* | *+17,8* | *+12,4* | *+31,8* | *+47,8* | *+15,8* | *+71,4* |

- `PER:IDENTITY` có mức tăng bùng nổ nhất: từ $0,0\%$ lên $> 87\%$ ở PA-LSTM và C-GCN, và tăng $+71,4\%$ ở SpanBERT (đạt $90,5\%$). Điều này chứng minh các mô hình vốn có khả năng phát hiện quy chiếu đồng nhất cực kỳ tốt, nhưng trước đó bị TACRED chấm 0 điểm do định nghĩa nhãn quá lộn xộn. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=7|PDF, tr. 7]]
- `PER:RESIDENCE` có mức cải thiện thấp nhất ($+1,1\%$ đến $+12,4\%$), phản ánh tính đa dạng từ vựng phức tạp của quan hệ nơi ở ("grew up", "lives", "has home", "from"). [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=7|PDF, tr. 7]]

### 4. Đánh giá chéo giữa các tập train và test (Bảng 6)

Để phân lập hiệu ứng giữa việc đánh giá nhãn sạch và việc huấn luyện trên nhãn sạch (trên tập nhãn không tinh chỉnh - non-refined labels): [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=8|PDF, tr. 8]]

| Model | Thiết lập (Train, Test) | F1 | Precision | Recall |
|---|---|---:|---:|---:|
| **PA-LSTM** | ($\text{TACRED}_{\text{train}}$, $\text{TACRED}_{\text{test}}$) | 72,3 | 71,3 | 73,3 |
| | ($\text{TACRED}_{\text{train}}$, $\text{Re-TACRED}_{\text{test}}$) | 74,8 | 80,1 | 70,2 |
| | ($\text{Re-TACRED}_{\text{train}}$, $\text{TACRED}_{\text{test}}$) | 65,9 | 59,4 | 74,2 |
| | ($\text{Re-TACRED}_{\text{train}}$, $\text{Re-TACRED}_{\text{test}}$) | **77,6** | 77,1 | 78,1 |
| **C-GCN** | ($\text{TACRED}_{\text{train}}$, $\text{TACRED}_{\text{test}}$) | 72,6 | 71,1 | 74,3 |
| | ($\text{TACRED}_{\text{train}}$, $\text{Re-TACRED}_{\text{test}}$) | 74,8 | 79,6 | 70,6 |
| | ($\text{Re-TACRED}_{\text{train}}$, $\text{TACRED}_{\text{test}}$) | 69,5 | 64,1 | 75,8 |
| | ($\text{Re-TACRED}_{\text{train}}$, $\text{Re-TACRED}_{\text{test}}$) | **79,6** | 81,2 | 78,2 |
| **SpanBERT** | ($\text{TACRED}_{\text{train}}$, $\text{TACRED}_{\text{test}}$) | 75,0 | 74,7 | 75,3 |
| | ($\text{TACRED}_{\text{train}}$, $\text{Re-TACRED}_{\text{test}}$) | 78,9 | 84,9 | 73,7 |
| | ($\text{Re-TACRED}_{\text{train}}$, $\text{TACRED}_{\text{test}}$) | 72,2 | 66,3 | 79,3 |
| | ($\text{Re-TACRED}_{\text{train}}$, $\text{Re-TACRED}_{\text{test}}$) | **84,9** | 85,1 | 84,7 |

*Quan sát cốt lõi*:
1. Mô hình chỉ cần được test trên $\text{Re-TACRED}_{\text{test}}$ (dù chỉ train trên $\text{TACRED}_{\text{train}}$) đã tăng ngay 2,5% - 3,9% F1, chứng minh tập test cũ đánh giá dưới thực lực của mô hình.
2. Mô hình train trên $\text{Re-TACRED}_{\text{train}}$ nhưng test trên $\text{TACRED}_{\text{test}}$ bị tụt điểm thảm hại (SpanBERT giảm từ 75,0% xuống 72,2%, số dự đoán dương tính đúng giảm 49,4%) vì tập test cũ phạt mô hình khi mô hình phát hiện đúng quan hệ thực chất mà TACRED gán nhầm là `NO_RELATION`.
3. Huấn luyện và kiểm tra đồng bộ trên Re-TACRED đem lại hiệu năng cao nhất (SpanBERT đạt 84,9%).

### 5. Bản chất các lỗi được sửa chữa (SpanBERT Error Analysis)

Phân tích 2.788 câu mà SpanBERT huấn luyện trên TACRED dự đoán sai nhưng SpanBERT huấn luyện trên Re-TACRED dự đoán đúng: [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=8|PDF, tr. 8]]
- **84,6% là lỗi Neg $\to$ Pos**: Mô hình cũ đoán `NO_RELATION` trong khi nhãn đúng là quan hệ dương tính. Điều này bắt nguồn trực tiếp từ độ lệch lớp cực đoan của TACRED (79,6% câu là nhãn âm), ép mô hình học bias thiên về phủ định.
- **10,0% là lỗi Pos $\to$ Neg**: Mô hình cũ đoán một quan hệ dương tính trong khi nhãn đúng là âm.
- **5,4% là lỗi Pos $\to$ Pos**: Đoán sai kiểu quan hệ dương tính (ví dụ nhầm giữa `SIBLINGS` và `CHILDREN`).

## Hạn chế, giả định, failure modes

- **Ràng buộc bản quyền LDC**: TACRED gốc thuộc quyền sở hữu của Linguistic Data Consortium (LDC). Do đó, tác giả không thể phân phối trực tiếp file text đầy đủ của Re-TACRED mà phải cung cấp mã nguồn tạo patch gán nhãn, đòi hỏi người dùng phải có sẵn bản quyền TACRED gốc từ LDC. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=2|PDF, tr. 2]]
- **Khó khăn cố hữu của quan hệ nơi cư trú (`PER:RESIDENCE`)**: Mặc dù độ chính xác tổng thể tăng mạnh, các quan hệ chỉ nơi cư trú vẫn gây nhầm lẫn lớn do sự biến thiên ngữ nghĩa quá rộng trong tiếng Anh tự nhiên. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=7|PDF, tr. 7]]
- **Mới chỉ khảo sát trên mô hình supervised truyền thống**: Nghiên cứu giới hạn ở PA-LSTM, C-GCN và SpanBERT. Chưa kiểm chứng trực tiếp xem các kiến trúc sinh văn bản (LLMs) hay các thiết lập học tăng cường/học liên tục thích ứng như thế nào trên Re-TACRED.
- **Lọc bớt các câu khó**: Việc loại bỏ 13.739 câu có span nhập nhằng hoặc tỷ lệ bất đồng cao có thể vô tình làm giảm độ đa dạng của các cấu trúc ngữ pháp phức tạp trong thế giới thực. [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5|PDF, tr. 5]]

## Đánh giá từ evidence

- **Bằng chứng có độ tin cậy rất cao**: Dữ liệu được tái gắn nhãn toàn diện với 243 crowd-workers qua 784 giờ làm việc tuần tự, hệ số Fleiss' kappa 0,77 và kiểm tra control sentence nghiêm ngặt (ngưỡng 80%), vượt trội hoàn toàn so với mẫu 5k của Alt et al. (2020) hay kiểm tra 300 câu của Zhang et al. (2017). [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5|PDF, tr. 5]] [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=9|PDF, tr. 9]]
- **Ý nghĩa phương pháp luận**: Paper đã chứng minh rõ ràng rằng *trần hiệu năng* (performance ceiling) trước đây của bài toán RE trên TACRED là một rào cản nhân tạo do nhãn sai và phân bố nhãn âm quá lớn (data bottleneck), chứ không phải do năng lực mô hình bị hạn chế.

## Diễn giải học tập

### Mối liên hệ cốt lõi với nghiên cứu Continual Relation Extraction (CRE / TAPTA)

Trong bài toán Học tăng cường trích xuất quan hệ (Continual Relation Extraction - CRE), hai benchmark chuẩn mực chi phối toàn bộ văn hiến là **FewRel** và **TACRED** (thường dùng trong ConPL, CPL, RP-CRE, ERDA, WAVE, WAVE++).

Việc hiểu rõ Re-TACRED mang lại các góc nhìn chiến lược quan trọng cho đề tài nghiên cứu:

1. **Giải thích khoảng cách hiệu năng giữa FewRel và TACRED**:
   - Trên FewRel, các mô hình CRE thường đạt độ chính xác từ $75\% - 88\%$.
   - Trên TACRED, các mô hình CRE thường chỉ đạt F1 khoảng $45\% - 60\%$, và hiện tượng quên (catastrophic forgetting) diễn ra trầm trọng hơn nhiều.
   - *Nguyên nhân thực sự*: TACRED gốc chứa 23,9% nhãn sai và gần 80% câu là `NO_RELATION`. Khi phân chia TACRED thành các task liên tục (ví dụ 10 tasks, mỗi task 4 quan hệ), nhiễu nhãn âm và nhãn sai làm các vector nguyên mẫu (prototypes) bị lệch lạc nặng nề, khiến bộ phân loại (classifier) bị thiên lệch nghiêm trọng về phía nhãn âm.
2. **Quyết định thực nghiệm (Experimental Decision)**:
   - **Bản chính (Primary Experiments)**: **BẮT BUỘC giữ TACRED gốc** theo đúng task split và task order chuẩn mà các baseline CRE (CPL, ConPL, WAVE++) đã công bố. Nếu tự ý chuyển sang Re-TACRED ở bảng so sánh chính, kết quả sẽ không thể so sánh công bằng (unfair comparison) với các công trình đi trước vì Re-TACRED đã bỏ bớt câu và gộp quan hệ.
   - **Phân tích hạn chế & Biện minh (Paper Motivation / Caveat)**: Dùng số liệu của Re-TACRED (23,9% nhãn sai, 79,6% nhãn âm) trong phần *Experimental Setup* hoặc *Error Analysis* để lập luận vì sao độ biến thiên nội task (within-task variance) trên TACRED lại lớn, và vì sao các cơ chế định tuyến tác vụ (task routing/prompt adaptation) cần phải mạnh mẽ để không bị cuốn theo nhiễu của nhãn âm.
   - **Phần phụ lục (Appendix Robustness Check)**: Nếu còn thời gian trước hạn nộp bài, việc chạy một thực nghiệm nhỏ trên Re-TACRED trong Appendix sẽ là điểm cộng rất lớn (reviewer có chuyên môn cao về IE sẽ đánh giá rất cao việc nhóm tác giả nhận thức được vấn đề nhãn của TACRED).

## Ghi chú cá nhân

- Không nên đưa Re-TACRED vào primary experiments ngay nếu deadline chặt. Nhưng cần đọc để viết caveat về TACRED và dùng làm robustness extension nếu còn thời gian.

## Câu hỏi review

### Câu 1: Tỷ lệ nhãn sai trong TACRED gốc được Re-TACRED xác định là bao nhiêu, và thành phần nào chiếm tỷ trọng lớn nhất trong các nhãn bị sửa?

*Gợi ý trả lời*: Paper phát hiện **23,9%** nhãn trong TACRED gốc bị sai. Trong số các nhãn bị sửa, thành phần lớn nhất chiếm tới **75,3%** là các câu vốn dĩ có quan hệ dương tính nhưng bị TACRED gán nhầm thành `NO_RELATION`. 16,1% là từ quan hệ dương tính chuyển về `NO_RELATION`, và 8,6% là chuyển đổi giữa các quan hệ dương tính khác nhau.

### Câu 2: Tại sao cơ chế 8 super-clusters lại giúp giải quyết triệt để lỗi loại thực thể (wrong types) mà vẫn tiết kiệm chi phí crowdsourcing?

*Gợi ý trả lời*: Khảo sát cho thấy khoảng 5% câu có NER type bị sai, khiến annotator không thể chọn đúng quan hệ trong giao diện TACRED cũ. Nếu kiểm tra toàn bộ 27 cặp type thì chi phí tăng 130%. Nhóm tác giả gộp các cặp type hay nhầm lẫn thành 8 super-clusters. Khi annotator chọn `WRONG_TYPES`, câu chỉ cần duyệt qua các quan hệ trong super-cluster tương ứng thay vì toàn bộ 27 cặp, giúp giảm chi phí tình huống tồi nhất xuống ~3,4 lần ($27/8$).

### Câu 3: Vì sao hiệu năng của mô hình PA-LSTM và C-GCN trên TACRED gốc lại gây hiểu lầm về năng lực thực tế của kiến trúc đồ thị?

*Gợi ý trả lời*: Trên TACRED gốc, điểm F1 tổng thể của PA-LSTM (66,2%) và C-GCN (66,3%) gần như tương đương, thậm chí PA-LSTM còn vượt C-GCN tới 10% trên nhóm quan hệ `PER:PER`. Tuy nhiên, trên Re-TACRED, C-GCN vượt trội PA-LSTM ở mọi nhóm quan hệ (đặc biệt `PER:PER` tăng từ 49,9% lên 86,2%). Điều này chứng minh dữ liệu TACRED nhiễu đã che mờ năng lực thực sự của bộ mã hóa đồ thị phụ thuộc (C-GCN).

## Evidence map

| Mục tiêu / Luận điểm | Trang PDF | Bằng chứng cụ thể trong nguồn |
|---|---|---|
| Lỗ hổng của TACRED & giới hạn nghiên cứu Alt et al. | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=1\|PDF, tr. 1-2]] | Section 1 & 2.1: Mẫu 5k câu của Alt et al. là thiên lệch; 95% TACRED chưa sửa |
| Thiết kế 8 Super-clusters & xử lý sai NER type | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=4\|PDF, tr. 4]] | Table 1: Bảng ánh xạ 8 super-clusters và tiết kiệm chi phí 3,4x |
| Tinh chỉnh định nghĩa nhãn & `PERSON:IDENTITY` | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=4\|PDF, tr. 4]] | Section 3.3: Mở rộng đại từ cho IDENTITY, gộp MEMBER_OF/MEMBERS |
| Quy trình kiểm soát chất lượng Trial & Control | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5\|PDF, tr. 5]] | Section 3.4: 1/5 câu là gold control, yêu cầu độ chính xác $\ge 80\%$ |
| Thống kê Re-TACRED & tỷ lệ nhãn sai 23,9% | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=5\|PDF, tr. 5]] | Section 4.1: 91.467 câu, 40 quan hệ, Fleiss' kappa 0,77, 23,9% nhãn sai |
| Kết quả tổng thể các mô hình (+14,3% F1) | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=6\|PDF, tr. 6]] | Table 2: PA-LSTM (79,4), C-GCN (80,3), SpanBERT (85,3) |
| Đánh giá theo nhóm quan hệ & tinh chỉnh nhãn | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=7\|PDF, tr. 7]] | Table 3 & Table 4: F1 tăng vọt ở PER:IDENTITY (+88,0%), đảo ngược vị thế C-GCN |
| Đánh giá chéo train/test & phân tích lỗi SpanBERT | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=8\|PDF, tr. 8]] | Table 6 & Table 5: 84,6% lỗi của TACRED-trained model là đoán nhầm NO_RELATION |
| Chi tiết AMT và siêu tham số | [[Re-TACRED - Addressing Shortcomings of the TACRED Dataset.pdf#page=9\|PDF, tr. 9]] | Appendix A & B: 243 workers, 784 giờ, 1 GPU Titan X / Tesla V100 |

## Liên kết

- Khái niệm: [[Relation Extraction]], [[Continual Relation Extraction]]
- Benchmark liên quan: [[FewRel - A Large-Scale Supervised Few-Shot Relation Classification Dataset]]
- Nghiên cứu CRE sử dụng TACRED:
  - [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction|Consistent Prototype Learning (ConPL)]]
  - [[Adaptive Prompting for Continual Relation Extraction]]
  - [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]
- Kế hoạch đọc & Quyết định: [[Reading Queue và Paper Decisions]]
