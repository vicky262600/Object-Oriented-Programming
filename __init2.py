class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name 
        self.price = price
        self.quantity = quantity   
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("phone", 100)
item2 = Item("laptop", 1000, 2)


print(item1.name)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

print("klsjfa", item2.calculate_total_price())