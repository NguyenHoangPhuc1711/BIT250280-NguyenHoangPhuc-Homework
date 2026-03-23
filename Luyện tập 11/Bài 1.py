n = []
for i in range(5):
    s = input(f"Chuỗi thứ {i+1}: ")
    n.append(s)
for i in range(1, len(n)):
    key = n[i]
    j = i - 1
    while j >= 0 and len(key) > len(n[j]):
        n[j + 1] = n[j]
        j -= 1
    n[j + 1] = key
    print(f"Thứ {i}: {n}")
print("Độ dài của chuỗi theo thứ tự giảm dần là:", n)