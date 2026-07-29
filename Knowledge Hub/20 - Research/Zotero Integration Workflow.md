---
type: technical-note
status: active
created: 2026-07-23
topic: zotero-obsidian
tags:
  - research
  - zotero
  - obsidian
---

# Zotero Integration Workflow

## Mục tiêu

Thiết lập một workflow trong đó Zotero quản lý paper, citation và PDF; còn Obsidian lưu phần hiểu, tổng hợp, concept và tiến trình nghiên cứu.

## Vai trò từng công cụ

- Zotero: lưu metadata, citation key, collection, tag, PDF và annotation gốc.
- Google Drive: sync file PDF nếu muốn dùng linked files trên nhiều máy.
- Obsidian: lưu paper note, paper reading log, literature note, research question và concept.

## Cấu trúc thư mục nên dùng

Trong vault:

```text
00 - Sources/PDFs/Papers
20 - Research/Papers
20 - Research/Paper Reading
20 - Research/Literature Notes
20 - Research/Research Questions
04 - Concepts
```

Nếu dùng Google Drive để sync PDF ngoài vault:

```text
Google Drive/Zotero PDFs/Papers
Google Drive/Zotero PDFs/Books
```

## Cấu hình Zotero

Không đặt toàn bộ Zotero data directory vào Google Drive. Thư mục này chứa `zotero.sqlite`, nếu sync bằng Google Drive/Dropbox/OneDrive có thể gây lỗi database.

Nên dùng một trong hai cách:

- Cách đơn giản: dùng Zotero Sync cho metadata và Zotero Storage hoặc WebDAV cho PDF.
- Cách tiết kiệm dung lượng Zotero: để PDF trong Google Drive và attach vào Zotero bằng linked file.

## Linked files với Google Drive

Khi dùng Google Drive cho PDF:

1. Lưu PDF vào `Google Drive/Zotero PDFs/Papers`.
2. Trong Zotero, chọn item paper.
3. Chọn kẹp giấy hoặc right click item.
4. Chọn `Attach Link to File...`.
5. Trỏ tới PDF trong Google Drive.
6. Vào `Settings -> Advanced -> Files and Folders`.
7. Đặt `Linked Attachment Base Directory` tới thư mục `Google Drive/Zotero PDFs`.

Lưu ý: Zotero không sync linked files. Google Drive chịu trách nhiệm sync PDF, Zotero chỉ sync metadata và đường dẫn tương đối.

## Plugin cần cài

Trong Zotero:

- Better BibTeX.

Trong Obsidian:

- Zotero Integration.

Sau khi cài Better BibTeX, mỗi item nên có citekey ổn định, ví dụ `leAdaptivePromptingContinual2026`.

## Workflow paper mới

1. Thêm paper vào Zotero bằng DOI, arXiv, browser connector hoặc kéo PDF vào Zotero.
2. Kiểm tra metadata: title, authors, year, venue, DOI/arXiv.
3. Gắn PDF theo một trong hai kiểu:
   - Stored file nếu để Zotero quản lý.
   - Linked file nếu PDF nằm trong Google Drive.
4. Lấy citekey từ Zotero.
5. Tạo note trong `20 - Research/Papers` bằng [[Paper Note]].
6. Điền các trường quan trọng: `title`, `authors`, `year`, `venue`, `pdf`, `doi`, `arxiv`, `zotero_key`, `citekey`.
7. Khi đọc mỗi phiên, tạo log trong `20 - Research/Paper Reading` bằng [[Paper Reading]].
8. Nếu một ý tưởng xuất hiện nhiều lần, tách thành concept trong `04 - Concepts`.

## Mẫu liên kết trong paper note

```yaml
pdf: "[[paper-file-name.pdf]]"
zotero_key:
citekey:
related_concepts:
  - "[[Retrieval-Augmented Generation]]"
```

## Quy tắc đặt tên

- Paper note: dùng tên paper ngắn, rõ nghĩa.
- PDF: ưu tiên tên có `author-year-title-short.pdf`.
- Paper reading log: dùng ngày hoặc ngày kèm paper, ví dụ `2026-07-23 - Adaptive Prompting.md`.
- Concept: dùng một note canonical, tránh tạo trùng.

## Checklist khi nhập paper

- [ ] Paper đã có metadata đầy đủ trong Zotero.
- [ ] PDF đã được attach đúng kiểu.
- [ ] Citekey đã ổn định.
- [ ] Paper note đã tạo trong `20 - Research/Papers`.
- [ ] PDF hoặc linked file đã được ghi vào `pdf`.
- [ ] Concept quan trọng đã được link hoặc tạo mới.
- [ ] Reading log đầu tiên đã tạo nếu bắt đầu đọc ngay.

## Liên kết

- [[Research Dashboard]]
- [[Paper Note]]
- [[Paper Reading]]
