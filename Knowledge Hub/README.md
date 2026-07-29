# Knowledge Hub

Đây là Obsidian vault dùng để quản lý kiến thức đọc sách, kiến thức kỹ thuật cho developer, nghiên cứu học thuật, paper, concept và project.

## Mục tiêu của vault

- Lưu tài liệu gốc ở một nơi rõ ràng.
- Biến sách, paper và tài liệu kỹ thuật thành note có cấu trúc.
- Tách khái niệm tái sử dụng thành concept notes.
- Theo dõi tiến độ đọc bằng daily reading.
- Quản lý research questions, experiments và projects liên quan.

## Cấu trúc thư mục

| Folder | Vai trò |
| --- | --- |
| `00 - Inbox` | Nơi ghi nhanh ý tưởng, paper muốn đọc, topic cần học. |
| `00 - Sources` | Kho tài liệu gốc: PDF, ảnh, dataset, web clips. |
| `01 - Books` | Note tổng quan cho từng cuốn sách. |
| `02 - Sections` | Note từng chapter/section của sách, chia folder theo tên sách. |
| `03 - Daily Reading` | Nhật ký đọc theo ngày, chia folder theo tên sách khi có nhiều note. |
| `04 - Concepts` | Khái niệm tái sử dụng nhiều nơi. |
| `05 - Templates` | Template cho sách, section, concept, paper, project, experiment. |
| `06 - Attachments` | File đính kèm do Obsidian hoặc người dùng thêm. |
| `10 - Technical` | Knowledge base kỹ thuật cho developer. |
| `20 - Research` | Quản lý paper, literature notes, research questions và experiments. |
| `30 - Projects` | Coding projects và research projects. |

## Quy tắc phân loại note

### Tài liệu gốc

Đặt file gốc vào `00 - Sources`.

- Ebook: `00 - Sources/PDFs/Books`
- Paper: `00 - Sources/PDFs/Papers`
- Tài liệu kỹ thuật/whitepaper/manual: `00 - Sources/PDFs/Docs`
- Ảnh/screenshot/diagram: `00 - Sources/Images`
- Dataset nhỏ: `00 - Sources/Datasets`
- Bài web đã lưu: `00 - Sources/Web Clips`

Không viết phân tích dài trong `00 - Sources`; đây chỉ là kho nguồn.

### Sách

- Note tổng quan sách nằm trong `01 - Books`.
- Chapter/section nằm trong `02 - Sections/<Tên sách>`.
- Daily reading nằm trong `03 - Daily Reading/<Tên sách>`.
- PDF gốc nằm trong `00 - Sources/PDFs/Books`.

Book note nên có property:

```yaml
type: book
author:
status:
total_pages:
started:
target_date:
priority:
source_file: "[[Tên file PDF.pdf]]"
tags:
  - book
```

### Paper

- Paper note nằm trong `20 - Research/Papers`.
- Nhật ký đọc paper nằm trong `20 - Research/Paper Reading`.
- Literature note nằm trong `20 - Research/Literature Notes`.
- Research question nằm trong `20 - Research/Research Questions`.
- Experiment nằm trong `20 - Research/Experiments`.
- PDF paper nằm trong `00 - Sources/PDFs/Papers`.

Paper note nên có property:

```yaml
type: paper
status: unread
title:
authors:
year:
venue:
url:
pdf: "[[Tên paper.pdf]]"
topic:
priority:
reading_status:
tags:
  - paper
```

### Concepts

Concept note nằm trong `04 - Concepts`.

Tạo concept khi một ý tưởng:

- Xuất hiện ở nhiều sách/paper/project.
- Cần được định nghĩa rõ.
- Có thể tái sử dụng trong graph tri thức.

Ví dụ: [[Large Language Model]], [[Embedding]], [[Tokenization]], [[Retrieval-Augmented Generation]], [[Fine-tuning]].

## Liên kết nguồn rõ ràng

Mỗi note xử lý kiến thức nên link ngược về nguồn:

- Book note dùng `source_file`.
- Paper note dùng `pdf`.
- Section note dùng `book`.
- Concept note dùng `source`.
- Experiment note dùng `research_question`, `project`, `related_papers`.

Ví dụ:

```yaml
source:
  - "[[Hands-On LLM - Chapter 02 - Tokens and Embeddings]]"
```

## Dashboard quan trọng

- [[Reading Dashboard]]
- [[Research Dashboard]]
- [[Technical Dashboard]]

## Graph view

Graph tri thức nên ưu tiên Books, Sections, Concepts, Research và Projects.

Filter gợi ý để ẩn daily logs và tài liệu gốc:

```text
-path:"03 - Daily Reading" -path:"00 - Sources"
```

Filter chỉ xem knowledge graph chính:

```text
path:"01 - Books" OR path:"02 - Sections" OR path:"04 - Concepts" OR path:"20 - Research" OR path:"30 - Projects"
```

## Workflow đề xuất

1. Thả tài liệu gốc vào `00 - Sources`.
2. Tạo book note hoặc paper note bằng template trong `05 - Templates`.
3. Tạo section/chapter notes khi đọc sâu.
4. Tạo daily reading nếu muốn theo dõi tiến độ đọc.
5. Tách khái niệm quan trọng sang `04 - Concepts`.
6. Link concept với sách, paper, project và experiment.

## Template nên dùng

- `Book Overview`
- `Reading Section`
- `Daily Reading`
- `Concept`
- `Technical Note`
- `Paper Note`
- `Paper Reading`
- `Literature Note`
- `Research Question`
- `Experiment`
- `Project Note`

