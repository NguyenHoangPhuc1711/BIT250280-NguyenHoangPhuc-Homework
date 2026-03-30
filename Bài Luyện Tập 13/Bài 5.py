class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return f"Hoa {self.name} có màu {self.color}"
rose = Flower("Hồng", "Đỏ")
print(rose)