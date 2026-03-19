list = []
for i in range(5):
    list.append(input(f"Nhập chuỗi thứ {i+1}: "))
n = len(list)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(list[j]) < len(list[j+1]):
            list[j], list[j+1] = list[j+1],list[j]
            print(f"Bước đổi: {list}")
print("--- Kết quả cuối cùng là ---")
print(list)