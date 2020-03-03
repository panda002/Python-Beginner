class Checkout(object):
    class Discount:
        def __init__(self, quantity, price):
            self.quantity = quantity
            self.price = price

    def __init__(self):
        self.discount = {}
        self.prices = {}
        self.items = {}

    def add_discount(self, item, quantity, price):
        discount = self.Discount(quantity, price)
        self.discount[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self, a: int):
        """

        :param a:
        :return:
        """

        total = 0
        for item, cnt in self.items.items():
            total += self.calculate_item_total(item, cnt)
        return total

    def calculate_item_total(self, item, cnt):
        total = 0
        if item in self.discount:
            discount = self.discount[item]
            if cnt >= discount.quantity:
                nbrdiscount = cnt / discount.quantity
                total += nbrdiscount * discount.price
                remaining = cnt % discount.quantity
                total += remaining * self.prices[item]
            else:
                total += self.price[item] * cnt
        else:
            total += self.prices[item] * cnt

        return total

