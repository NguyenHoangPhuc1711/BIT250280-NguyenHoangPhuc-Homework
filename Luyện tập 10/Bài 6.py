chuoi = input("Nhập chuỗi cần đảo ngược: ")
chuoi_dao_nguoc = ""
for i in range(len(chuoi) - 1, -1, -1):
    chuoi_dao_nguoc += chuoi[i]
print(f"Chuỗi sau khi đảo: {chuoi_dao_nguoc}")