class MathDojo:
	def __init__(self,name):
		self.name = name
		self.total = 0

	def add(self,*x):
		self.total = self.total + sum(x)
		return self

	def subtract(self,*x):
		self.total = self.total - sum(x)
		return self

	def result(self):
		print(self.name)
		print(self.total)
		print('*' * 80)

mj = MathDojo('mj')

mj.add(2).add(2,5,1).subtract(3,2).result()