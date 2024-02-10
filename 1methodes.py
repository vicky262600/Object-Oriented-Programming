class Item:
    def calculate_total_price(self, x, y):
        return x * y

item1 = Item()
item1.name = 'phone'
item1.price = 55
item1.quantity = 4
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = 'laptop'
item2.price = 115
item2.quantity = 4
print(item2.calculate_total_price(item2.price, item2.quantity))
