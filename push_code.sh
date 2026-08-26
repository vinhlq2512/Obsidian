#!/bin/bash
set -euo pipefail

echo "🚀 Bắt đầu quá trình tạo nhánh và push code..."

# Always run from the folder that contains this script.
cd "$(dirname "$0")"

# Tạo tên nhánh theo pattern notes-dd-mm-yyyy
CURRENT_DATE=$(date +'%d-%m-%Y')
BRANCH_NAME="notes-$CURRENT_DATE"
REMOTE_URL="https://github.com/vinhlq2512/Obsidian"

# 1. Khởi tạo một git repository mới
git init

# 2. Thêm remote repository
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

# 3. Lấy lịch sử commit từ nhánh main trên remote để có mốc so sánh (giúp tạo PR không bị lỗi)
git fetch origin main

# 4. Đặt HEAD về mốc của origin/main nhưng vẫn giữ nguyên tất cả file hiện tại (working tree)
git reset --mixed origin/main

# 5. Tạo và chuyển sang nhánh mới
git checkout -B "$BRANCH_NAME"

# 6. Thêm tất cả các file có thay đổi hoặc mới tạo vào staging
git add .

if git diff --cached --quiet; then
  echo "ℹ️ Không có thay đổi mới để commit."
  rm -rf .git
  exit 0
fi

# 7. Commit các thay đổi
git commit -m "Update notes $CURRENT_DATE"

# 8. Push nhánh mới lên GitHub
git push -f origin "$BRANCH_NAME"

# 9. Xoá thư mục .git sau khi hoàn tất
rm -rf .git

echo "✅ Hoàn thành! Đã push code lên nhánh '$BRANCH_NAME'."
echo "👉 Hãy click vào link sau để tạo Pull Request:"
echo "https://github.com/vinhlq2512/Obsidian/pull/new/$BRANCH_NAME"
