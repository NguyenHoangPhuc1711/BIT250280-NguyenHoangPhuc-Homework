import math
numbers = [2, 5, 8, 3, 7, 2, 11]
numbers.append(13)
print(f"Danh sách sau khi thêm: {numbers}")
k = int(input("Nhập phần tử giá trị k: "))
count_k = numbers.count(k)
print(f"Số {k} xuất hiện {count_k} lần trong danh sách.")
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
tong_snt = sum(x for x in numbers if la_so_nguyen_to(x))
print(f"Tổng các số nguyên tố là: {tong_snt}")
numbers.sort()
print(f"Danh sách sau khi sắp xếp: {numbers}")
numbers.clear()
print(f"Danh sách sau khi xóa: {numbers}")
