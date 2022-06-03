import sys

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
		d = states.get(sys.argv[1])
		g = capital_cities.get(d)
		if g == None:
			print("Unknown state")
		else:
			print(g)


if __name__ == '__main__':
	my_var()