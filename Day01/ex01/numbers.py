def my_var():
	with open('numbers.txt', 'r') as file:
		s = file.read()
	file.close()
	for i in s.split(","):
		print(i)


if __name__ == '__main__':
	my_var()