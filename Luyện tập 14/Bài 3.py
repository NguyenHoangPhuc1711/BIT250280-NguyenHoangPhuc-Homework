n = int(input("Nhập số vào đây để vẽ hình"))
print("Hình 1:")
for i in range(n):
    print("1  1  1  1")
print("\nHình 2:")
for i in range(n):
    print("1  2  3  4")
print("\n Hình 3:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="  ")
    print()
print("\nHình 4:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="  ")
    print()
print("\n Hình 5:")
for i in range(1, n + 1):
    if i == 1:
        print(1)
    elif i == 2:
        print("1  2")
    elif i == 3:
        print("1     3")
    else:
        print("1  2  3  4")
print("\n Hình 6")
for i in range(n, 0, -1):
    if i == 4:
        print("1  2  3  4")
    elif i == 3:
        print("1     3")
    elif i == 2:
        print("1  2")
    else:
        print("1")
print("\n Hình 7")
for i in range(1, n + 1):
    print("   " * (n - i), end="")
    for j in range(i):
        print(i, end="     ")
    print()
print("\nHình 8:")
for i in range(1, n + 1):
    print("   " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="  ")
    for j in range(i - 1, 0, -1):
        print(j, end="  ")
    print()
print("\nHình 9:")
for i in range(1, n + 1):
    print("   " * (n - i), end="")
    if i == 1:
        print(1)
    elif i < n:
        print(1, "   " * (2*i - 3), 1)
    else:
        for j in range(1, n + 1): print(j, end="  ")
        for j in range(n - 1, 0, -1): print(j, end="  ")
        print()
