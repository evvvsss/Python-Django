import sys
import os
import re
from settings import *

g = globals()

def my_var():
	if len(sys.argv) != 2:
		return print("Wrong number of arguments")
	
	template_file = sys.argv[1]
	if not template_file.endswith(".template"):
		return print("Wrong file extension")
	if not os.path.isfile(template_file):
		return print("Non-existing file")

	with open(template_file, 'r') as file:
		template_data = "".join(file.readlines())
	file.close()

	new_data = template_data.format(**g)
	print(new_data)
	with open("index.html", "w") as f:
		f.write(new_data)

if __name__ == '__main__':
	my_var()