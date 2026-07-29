#!/bin/bash

echo "🚀 Bắt đầu quá trình push code..."

# 1. Khởi tạo một git repository mới
git init

# 2. Chuyển sang nhánh main (hoặc đổi tên nhánh mặc định thành main)
git checkout -B main

# 3. Thêm tất cả các file vào staging area
git add .

# 4. Commit các thay đổi
git commit -m "Auto backup/push code"

# 5. Thêm remote repository
git remote add origin https://github.com/vinhlq2512/Obsidian

# 6. Push code lên GitHub 
# Lưu ý: Vì chúng ta luôn tạo mới .git và xoá nó đi nên lịch sử commit sẽ bị mất mỗi lần chạy.
# Do đó cần sử dụng --force (-f) để ghi đè lên repository trên GitHub.
git push -f origin main

# 7. Xoá thư mục .git sau khi hoàn tất
rm -rf .git

echo "✅ Hoàn thành! Đã push code lên https://github.com/vinhlq2512/Obsidian và xoá thư mục .git."
