n = int(input("Nhập n: "))
print("\nHình 1:")
for i in range(n):
    print("* " * n)
print("\nHình 2:")
for i in range(1, n + 1):
    print("* " * i)
print("\nHình 3:")
for i in range(n, 0, -1):
    print("* " * i)
print("\nHình 4:")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)
print("\n Hình 5:")
for i in range(1, n + 1):
    if i == 1:
        print("*")
    elif i == n:
        print("* " * n)
    else:
        print("* " + "  " * (i - 2) + "*")
print("\nHình 6:")
for i in range(n, 0, -1):
    if i == n:
        print("* " * n)
    elif i == 1:
        print("*")
    else:
        print("* " + "  " * (i - 2) + "*")
print("\nHình 7:")
for i in range(1, n + 1):
    if i == 1:
        print("  " * (n - 1) + "*")
    elif i == n:
        print("* " * n)
    else:
        print("  " * (n - i) + "*" + "  " * (i - 2) + " *")
print("\nHình 8:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
print("\nHình 9:")
for i in range(1, n + 1):
    space_outside = " " * (n - i)
    if i == 1:
        print(space_outside + "*")
    elif i == n:
        print("* " * n)
    else:
        space_inside = " " * (2 * i - 3)
        print(space_outside + "*" + space_inside + "*")
print("\nHình 10:")
for i in range(n, 0, -1):
    space_outside = " " * (n - i)
    if i == n:
        print("* " * n)
    elif i == 1:
        print(space_outside + "*")
    else:
        space_inside = " " * (2 * i - 3)
        print(space_outside + "*" + space_inside + "*")
