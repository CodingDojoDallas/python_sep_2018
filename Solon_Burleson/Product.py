class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.price = self.price + (self.price * tax)
        return self

    def returnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like_new":
            self.status = "like new"
        elif reason_for_return == "opened":
            self.status = "opened"
            self.price = self.price * .8
        return self

    def displayAll(self):
        print(self.price)
        print(self.item_name)
        print(self.weight)
        print(self.brand)
        print(self.status)
        return self
