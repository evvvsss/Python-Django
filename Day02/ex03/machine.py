import random
from beverages import *

class CoffeeMachine():
	def __init__(self):
		self.serve_count = 10

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.price = 0.90
			self.name = "empty cup"

		def description(self):
			return "An empty cup?! Gimme my money back!"
		
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
	
	def repair(self):
		self.serve_count = 10
		print("Machine is repaired")
	
	def serve(self, drink: HotBeverage):
		if self.serve_count <= 0:
			raise CoffeeMachine.BrokenMachineException
		self.serve_count -= 1
		if random.randint(0, 10) == 0:
			return CoffeeMachine.EmptyCup()
		return drink

def my_var():
	machine = CoffeeMachine()
	for i in range(23):
		try:
			print(machine.serve(random.choice([Coffee, Tea, Cappuccino, Chocolate])))
		except CoffeeMachine.BrokenMachineException as e:
			print(e)
			machine.repair()


if __name__ == '__main__':
	my_var()


	