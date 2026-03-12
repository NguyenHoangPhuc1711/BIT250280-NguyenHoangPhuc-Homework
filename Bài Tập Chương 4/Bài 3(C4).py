
động_vật = {"con chó": 5, "con mèo": 1, "con cẩu": 8}
ten_can_tim = input("Nhập tên động vật cần kiểm tra trong ba con(con chó , con mèo , con cẩu): ")
if ten_can_tim in động_vật:
    print(f"Có'{ten_can_tim}' trong danh sách!")
else:
    print(f"Không tìm thấy'{ten_can_tim}'.")