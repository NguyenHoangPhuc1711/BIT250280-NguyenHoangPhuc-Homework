class Product:
    def __init__(self, price):
        self.set_price(price)
    def get_price(self):
        return self._price
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Gia phai > 0")
            self._price = 1
    def __str__(self):
        return "Price: " + str(self._price)
p1 = Product(250)
print(p1)