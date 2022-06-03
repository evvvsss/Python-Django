import sys

def get_key(d, value):
	for k, v in d.items():
		if v == value:
			return k

def my_var():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if len (sys.argv) == 2:
		d = get_key(capital_cities, sys.argv[1])
		if d == None:
			print("Unknown capital city")
		else:
			g = get_key(states, d)
			if g == None:
				print("Unknown capital city")
			else:
				print(g)


if __name__ == '__main__':
	my_var()