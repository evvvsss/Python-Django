
class Intern:
	
	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."
	
	def __init__(self, name=None):
		if name == None:
			self.name = "My name? I’m nobody, an intern, I have no name."
		else:
			self.name = name
	
	def __str__(self):
		return self.name
	
	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")
		
	
	def make_coffee(self):
		return Intern.Coffee()


def my_var():
	k = Intern()
	print(k)
	m = Intern("Mark")
	print(m)
	print(m.make_coffee())
	try:
		k.work()
	except Exception as e:
		print(e)




if __name__ == '__main__':
	my_var()