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