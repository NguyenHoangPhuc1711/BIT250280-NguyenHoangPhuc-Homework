def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)
n = int(input("Nhập số để tính giai thừa: "))
print("Giai thừa của số đó là:", giai_thua(n))