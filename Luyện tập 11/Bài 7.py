import csv
ten = input("Nhập tên của nhân viên: ")
tuoi = input("Nhập tuổi của nhân viên: ")
ma_so_nhan_vien = input("Nhập mã số nhân viên: ")
with open("nhanvien.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(f"Tên: {ten}, Tuổi: {tuoi}, ID: {ma_so_nhan_vien}")
header = ["Tên", "Tuổi", "ID"]
data = [ten, tuoi, ma_so_nhan_vien]
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerow(data)
with open("nhanvien.txt","r",encoding="utf-8") as txt_file:noi_dung = txt_file.read()
print(data)