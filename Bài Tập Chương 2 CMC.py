
n = int(input("Nhập một số từ 1 đến 9:"))
print("Bảng cửu chương")
for i in range(1, 10):
    print(i)



n = int(input("Nhập một số dương: "))
if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem = dem + 1
    if dem == 2:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")





n = int(input("Nhập n: "))
a = 0
b = 1
if n >= 1:
    print(a, end=" ")
if n >= 2:
    print(b, end=" ")
for i in range(3, n + 1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c



n = int(input("Nhập số: "))
tong = 0
while n > 0:
    tong = tong + n % 10
    n = n // 10
print("Tổng các chữ số là:", tong)



chuoi = input("Nhập vào một chuỗi: ")
ky_tu = input("Nhập vào một ký tự: ")
dem = 0
for i in chuoi:
    if i == ky_tu:
        dem += 1
print("Ký tự", ky_tu, "xuất hiện", dem, "lần trong chuỗi")




def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n - 1)
n = int(input("Nhập vào một số: "))
print("Giai thừa của", n, "là:", giaithua(n))




a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
ucln = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        ucln = i
print("Ước số chung lớn nhất của", a, "và", b, "là:", ucln)






n = int(input("Nhập vào một số dương: "))
dao_nguoc = 0
while n > 0:
    chu_so = n % 10
    dao_nguoc = dao_nguoc * 10 + chu_so
    n = n // 10
print("Số sau khi đảo ngược là:", dao_nguoc)




n = int(input("Nhập vào một số nguyên dương 5 chữ số: "))
max_chu_so = 0
while n > 0:
    chu_so = n % 10
    if chu_so > max_chu_so:
        max_chu_so = chu_so
    n = n // 10
print("Chữ số lớn nhất trong số vừa nhập là:", max_chu_so)




def tinh_tong(n):
    if n == 1:
        return 1
    else:
        return n + tinh_tong(n - 1)
so_n = int(input("Nhập số nguyên dương n: "))

if so_n > 0:
    ket_qua = tinh_tong(so_n)
    print(f"Tổng các số từ 1 đến {so_n} là: {ket_qua}")
else:
    print("Nhập số lớn hơn 0!")




dtb = float(input("Nhập điểm trung bình: "))
if dtb >= 8:
    print("Giỏi")
elif dtb >= 6.5:
    print("Khá")
elif dtb >= 5:
    print("Trung bình")
else:
    print("Dốt")



n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        tong = tong + i
print("Tổng các số lẻ từ 1 đến", n, "là:", tong)





mat_khau = ""
while mat_khau != "Phúc đẹp trai":
    mat_khau = input("Nhập mật khẩu: ")
print("Đăng nhập thành công!")








n = int(input("Nhập số n: "))
if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem = dem + 1
    if dem == 2:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")






n = int(input("Nhập số nguyên dương: "))
tong = 0
while n > 0:
    chu_so = n % 10
    tong = tong + chu_so
    n = n // 10
print("Tổng các chữ số là:", tong)