import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=1):
        assert price > 0, f"Price {price} is not greater than or equal to 0"


        self.name = name
        self.price = price
        self.quantity = quantity

        # Assign to self object
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity if self.quantity > 0 else self.price
    
    def pay_price(self):
        self.price = self.pay_rate * self.price

    @classmethod
    def form_csv(cls):
        with open('demo.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=item.get('quantity')
            )
            
    @staticmethod
    def is_integer(num):
        #we will countout the floats that are point zero
        # for i.e.: 5.0, 10.0
        if isinstance(num, float):
            # count out the float that are zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



    def __repr__(self):
        # return "Item"
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


Item.form_csv()
# for instance in Item.all:
#     print(instance.name, instance.price, instance.quantity)
    
# print(Item.all)
# print(Item.is_integer(10.5));



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