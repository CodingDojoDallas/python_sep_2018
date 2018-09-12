class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

    def sell(self):
        self.status = 'sold'
        return(self)

    def add_tax(self, num):
        self.price = (int(self.price) * num + int(self.price))
        return (self)
        
    def return_item (self, reason_for_return):
        if reason_for_return == 'defective':
            self.status = 'defective'
            self.price = 0
            return(self)

        elif reason_for_return == 'like_new':
            self.status = 'for sale'
            return(self)

        elif reason_for_return == 'opened':
            self.status = 'used'
            self.price = (int(self.price) - .20 * int(self.price)) 
            return(self)
        
    def display_info(self):
        print('the item price is '+ str(self.price))
        print('the item is a '+str(self.item_name))
        print('the item weight is '+str(self.weight))
        print('the item brand name is '+str(self.brand))
        print('the item status is '+str(self.status))
        return(self)

product1 = Product(140, 'bike', '40lbs', 'harley')
product1.add_tax(.10).return_item('defective').display_info()
product2 = Product(200, 'matress', '140lbs', 'serta')
product2.add_tax(.10).return_item('like_new').display_info()
product3 = Product(300, 'playstation', '50lbs', 'sony')
product3.add_tax(.10).return_item('opened').display_info()









    

        

