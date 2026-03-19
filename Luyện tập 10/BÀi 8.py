danh_sach = []
for i in range(5):
    danh_sach.append(input(f"Nhập chuỗi thứ {i+1}: "))
n = len(danh_sach)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(danh_sach[j]) < len(danh_sach[j+1]):
            danh_sach[j], danh_sach[j+1] = danh_sach[j+1], danh_sach[j]
            print(f"Bước đổi: {danh_sach}")
print("--- Kết quả cuối cùng là ---")
print(danh_sach)