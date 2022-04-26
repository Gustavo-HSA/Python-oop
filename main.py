class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def calculate_total_price(x, y):
        return x * y


item1 = Item("Phone", 100, 5)

item2 = Item("Notebook", 1000, 3)
