def lay_name_file(duong_dan):
    parts = duong_dan.split("\\")
    return parts[-1]
def lay_name_bai_hat(duong_dan):
    name_file = lay_name_file(duong_dan)
    name = name_file.split(".")[0]
    return name
path = "d:\\music\\muabui.mp3"
print(lay_name_file(path))
print(lay_name_bai_hat(path))