# Đọc danh sách extension từ tệp
with open('extensions-list.txt', 'r') as file:
    extensions = file.readlines()

# Tạo lệnh cài đặt
with open('install-extensions.sh', 'w') as file:
    for extension in extensions:
        extension = extension.strip()  # Xóa khoảng trắng và ký tự xuống dòng
        file.write(f'code --install-extension {extension}\n')

"""
chmod +x install-extensions.sh
./install-extensions.sh
"""
# Chạy lệnh phía trên trong terminal để cài đặt extension