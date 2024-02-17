from GettersAndSettersItem6 import Item

class Phone(Item):
    #  pay_rate = 0.8
     all = []
     def __init__(self, name: str, price: float, quantity=1, brokenPhone=0):
        # assert price >= 0, f"Price {price} is not greater than or equal to 0"
        # assert brokenPhone >= 0, f"brokenPhone {brokenPhone} is not greater than or equal to 0"
        # call to super function to have access to all attribue/ methode
        super().__init__(
            name, price, quantity
        )

        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.brokenPhone = brokenPhone


phone1 = Phone("iphone11", 1000, 2, 1)
# print(phone1.calculate_total_price())
phone2 = Phone("iphone12", 1100, 3)

print(Item.all)
# print(Phone.all)