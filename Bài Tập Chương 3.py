
mon_hoc = ["Đại số tuyến tình","Cơ Sở Lập Trình"]
print(f"Số lượng môn học là: {len(mon_hoc)}")
print("Danh sách các môn học:")
for mon in mon_hoc:
    print(mon)





ban_be = ["Phúc","Hoàng Phúc","Nguyễn Hoàng Phúc"]
print(f"Danh sách bạn bè: {ban_be}")
ban_be.append("Phúc Hoàng Nguyễn")
print(f"Đã thêm bạn")
ban_be.pop(1)
print(f"Đã xóa bạn: {ban_be}")






mau_sac = ["Xanh", "Đỏ", "Green", "Tím","Vàng"]
print(f"Danh sách màu có: {mau_sac}")
try:
    mau_sac.remove("Green")
    print("Đã xóa'Green'.")
except ValueError:
    print("Lỗi: Màu 'Green' không tồn tại trong danh sách.")
print(f"Danh sách màu hiện tại: {mau_sac}")






numbers = [23, 5, 12, 5, 8, 42]
print(f"Danh sách ban đầu: {numbers}")
numbers.sort()
print(f"Sau khi sắp xếp: {numbers}")
numbers.reverse()
print(f"Sau khi đảo ngược: {numbers}")
count_five = numbers.count(5)
print(f"Số lần số 5 xuất hiện: {count_five}")




def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
input_str = input("Nhập các số thực, cách nhau bởi khoảng trắng: ")
numbers = [float(x) for x in input_str.split()]
insertion_sort_descending(numbers)
print(f"Danh sách sau khi sắp xếp giảm dần: {numbers}")





def bubble_sort_with_count(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True
        if not swapped:
            break
    return swap_count
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Danh sách ban đầu: {numbers}")
total_swaps = bubble_sort_with_count(numbers)
print(f"Danh sách sau khi sắp xếp tăng dần: {numbers}")
print(f"Tổng số lần hoán đổi thực hiện: {total_swaps}")






def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
try:
    input_list = input("Nhập danh sách số (cách nhau bởi khoảng trắng): ")
    numbers = [float(x) for x in input_list.split()]
    target_num = float(input("Nhập số cụ thể cần tìm chỉ số: "))
    result = linear_search(numbers, taret_num)
    if result != -1:
        print(f"Số {target_num} được tìm thấy tại chỉ số: {result}")
    else:
        print(f"Không tìm thấy số {target_num} trong danh sách.")
except ValueError:
    print("Vui lòng chỉ nhập số thực hoặc số nguyên.")







def find_first_greater_than_10(arr):
    for num in arr:
        if num > 10:
            return num
    return None
input_list = input("Nhập danh sách số (cách nhau bởi khoảng trắng): ")
numbers = [float(x) for x in input_list.split()]
found_number = find_first_greater_than_10(numbers)
if found_number is not None:
    print(f"Số đầu tiên lớn hơn 10 là: {found_number}")
else:
    print("Không có số nào lớn hơn 10 trong danh sách.")






numbers = list(map(int, input("Nhập dãy số (cách nhau bởi khoảng trắng): ").split()))
odd_numbers = [num for num in numbers if num % 2 != 0]
print(f"Các số lẻ trong danh sách: {odd_numbers}")






even_numbers = [num for num in numbers if num % 2 == 0]
total_even = sum(even_numbers)
print(f"Các số chẵn trong danh sách: {even_numbers}")
print(f"Tổng các số chẵn là: {total_even}")






arr = [15, 2, 34, 8, 19, 1]
max_val = max(arr)
min_val = min(arr)
print(f"Mảng: {arr}")
print(f"Giá trị lớn nhất: {max_val}")
print(f"Giá trị nhỏ nhất: {min_val}")






A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
print("Ma trận kết quả sau khi cộng:")
for row in result:
    print(row)






def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
test_string = input("Nhập chuỗi cần kiểm tra: ")
if is_palindrome(test_string):
    print(f"'{test_string}' là chuỗi đối xứng.")
else:
    print(f"'{test_string}' không phải là chuỗi đối xứng.")






def count_vowels(s):
    vowels = "aeiou"
    count = 0
    s = s.lower()
    for char in s:
        if char in vowels:
            count += 1
    return count
text = input("Nhập một chuỗi: ")
print(f"Số lượng nguyên âm xuất hiện là: {count_vowels(text)}")





s = input("Nhập chuỗi: ")
reversed_s = s[::-1]
print(f"Đảo ngược : {reversed_s}")