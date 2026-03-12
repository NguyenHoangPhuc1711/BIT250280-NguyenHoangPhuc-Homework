class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return "Ten hoa: " + self.ten + ", Mau: " + self.mau
n = Hoa("Hoa Hong", "Do")
print(n)