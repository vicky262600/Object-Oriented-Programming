class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=1):
        # Run validation to the receive argument
        assert price >= 0, f"Price {price} is not greater than or equal to 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity if self.quantity > 0 else self.price
    
    # def pay_price(self):
    #     return self.pay_rate * self.price
    
    def pay_price(self):
        self.price =  self.pay_rate * self.price

item1 = Item("phone", 100)
item2 = Item("laptop", 100, 2)

print(item1.name)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

print("Total Price for item2:", item2.calculate_total_price())
print("Pay Rate:", Item.pay_rate)

print("Item Class Dictionary:", Item.__dict__)
print("Item1 Instance Dictionary:", item1.__dict__)

# print("yo yo", item1.pay_price())
item1.pay_price()
print(item1.price)

# if I want to assign a diffrent pay rate for a isinstance
item2 = Item("laptop", 1000, 2)
item2.pay_rate = 0.7
item2.pay_price()
print(item2.price)