def tinh_diem_trung_binh(danh_sach_lop):
    diem_so = danh_sach_lop.values()
    trung_binh = sum(diem_so) / len(danh_sach_lop)
    return trung_binh
sinh_vien = {
    "Phúc": 8,
    "Hoangf": 10,
    "Nguyễn": 9,
}
dtb = tinh_diem_trung_binh(sinh_vien)
print(f"Điểm trung bình của lớp là: {dtb}")