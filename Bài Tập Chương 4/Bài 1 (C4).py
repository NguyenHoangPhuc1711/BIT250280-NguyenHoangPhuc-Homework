def tinh_toan_tuple(numbers):
    tong = sum(numbers)
    lon_nhat = max(numbers)
    nho_nhat = min(numbers)
    return tong, lon_nhat, nho_nhat
day_so = (10, 5, 8, 20, 3)
kq_tong, kq_max, kq_min = tinh_toan_tuple(day_so)
print(f"Tổng là: {kq_tong}")
print(f"Số lớn nhất: {kq_max}")
print(f"Số nhỏ nhất: {kq_min}")