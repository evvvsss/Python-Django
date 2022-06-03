class HotBeverage:

	def __init__(self):
		self.price = 0.30
		self.name = "hot beverage"

	def description(self):
		return "Just some hot water in a cup."
	
	def __str__(self):
		str = f'name : {self.name}\n'
		str += f'price : {self.price}\n'
		str += f'description : {self.description()}'
		return str

class Coffee(HotBeverage):
	def __init__(self):
		self.name = "coffee"
		self.price = 0.40
	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self):
		self.name = "tea"
		self.price = 0.30
	def description(self):
		return "Just some hot water in a cup."

class Chocolate(HotBeverage):
	def __init__(self):
		self.name = "chocolate"
		self.price = 0.50
	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		self.name =  "cappuccino"
		self.price = 0.45
	def description(self):
		return "Un po’ di Italia nella sua tazza!"

def my_var():
	a = HotBeverage()
	print(a)
	b = Coffee()
	print(b)
	c = Tea()
	print(c)
	d = Cappuccino()
	print(d)
	e = Chocolate()
	print(e)


if __name__ == '__main__':
	my_var()