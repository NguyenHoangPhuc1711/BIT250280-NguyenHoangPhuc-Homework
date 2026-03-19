chuoi_ki_tu = input("Nhập chuỗi kí tự: ")
ky_tu = input("Nhập ký tự cần đếm: ")
dem = 0
for c in chuoi_ki_tu:
    if c == ky_tu:
        dem += 1
print("Số lần xuất hiện của kí tự cần đếm là:", dem)