class product:
    def __init__(self, name, price, brand, weight):
        self.name = name
        self.price = price
        self.brand = brand
        self.weight = weight
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    def salesTax(self):
        tax = .08
        self.price *= (1 + tax)
        return self
    def returns(self,reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like_new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            self.price *= .8
        return self
    def itemInfo(self):
        print(self.name)
        print("price:", self.price)
        print("brand:", self.brand)
        print("weight:", self.weight)
        print("status", self.status)

product1 = product("toy", 20, "hasbro", "2lbs")
product2 = product("tv", 500, "samsung", "20lbs")
product3 = product("chair", 75, "ikea", "10lbs")
product4 = product("food", 10, "kellogs", "1lb")

product1.salesTax().sell().itemInfo()
product1.returns("defective").itemInfo()
product2.salesTax().sell().returns("used").itemInfo()
product3.salesTax().sell().returns("like_new").itemInfo()
product4.sell().itemInfo()
