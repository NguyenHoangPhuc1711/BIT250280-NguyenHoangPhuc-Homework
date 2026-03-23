chuong_trinh = input("Nhập danh sách số: ")
numbers = [int(x) for x in chuong_trinh.split()]
so_chan = []
tong = 0
for n in numbers:
    if n % 2 == 0:
        so_chan.append(n)
        tong += n
print("Tất cả các số chẵn trong danh sách:", so_chan)
print("Tổng các số chẵn là:", tong)