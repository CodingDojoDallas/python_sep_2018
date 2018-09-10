class Product:
	def __init__(self,price,item_name,weight,brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
		self.display_info()

	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self,x):
		self.price = (self.price * x) + self.price
		self.display_info()

	def return_item(self,reason_for_return):
		if "like new" in reason_for_return:
			self.status = "for sale"

		else:
			if "opened" in reason_for_return:
				self.status = "used"
				self.price = self.price - (self.price * .2)
			else: 
				self.status = reason_for_return
				self.price = 0
		self.display_info()

	def display_info(self):
		print("Price:",self.price)
		print("Name:",self.item_name)
		print("Weight:",self.weight)
		print("Brand",self.brand)
		print("Status:",self.status)
		print('*' * 80)

shoes = Product(45,"shoes","2kg","adidas")

shoes.sell()
shoes.return_item("opened")