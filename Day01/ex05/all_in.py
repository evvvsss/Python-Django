import sys

def get_key(d, value):
	for k, v in d.items():
		if v.lower() == value.lower():
			return k

def get_value(d, key):
	for k, v in d.items():
		if k.lower() == key.lower():
			return v

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
	i = 0
	if len (sys.argv) == 2:
		t = tuple(str(item) for item in sys.argv[1].split(', '))
		while i < len(t):
			if t[i] != "" and t[i] != " " and t[i] != " ,":
				d = get_key(capital_cities, t[i])
				if d == None:
					d = get_value(states, t[i])
					if d == None:
						print(t[i], "is neither a capital city nor a state")
					else:
						g = get_value(capital_cities, d)
						print(g, "is the capital of", get_key(states, d))
				else:
					g = get_key(states, d)
					if g == None:
						print(t[i], "is neither a capital city nor a state")
					else:
						print(get_value(capital_cities, d), "is the capital of", g)
			i += 1

if __name__ == '__main__':
	my_var()