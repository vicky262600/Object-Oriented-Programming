class Item:

    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=1):
        assert float(price) > 0, f"Price {price} is not greater than or equal to 0"


        self.name = name
        self.price = float(price)
        self.quantity = quantity

        # Assign to self object
        Item.all.append(self)

    def pay_price(self):
        self.price = self.pay_rate * self.price

    def __repr__(self):
        # return "Item"
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("phone", "500", 2)
item2 = Item("tablet", "600", 3)
item3 = Item("Ipot", "400", 4)
item4 = Item("laptop", "1200", 2)
item5 = Item("earbud", "300")

for instance in Item.all:
    print(instance.name, instance.price, instance.quantity)
    
# print(Item.all)