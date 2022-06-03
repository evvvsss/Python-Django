import sys

def my_var():
	with open('periodic_table.txt', 'r') as file:
		s = file.read()
	very_small_list = []
	small_list = []
	big_list = []
	count = 0
	for i in s.split("\n"):
		i = i+'\n'
		small_list.append(i[0:i.find(" ")])
		small_list.append(i[i.find(":")+1:i.find(",")])
		small_list.append(i[i.find("number:")+7:i.find(", small")])
		small_list.append(i[i.find("small:")+7:i.find(", molar:")])
		small_list.append(i[i.find("molar:")+6:i.find(", elect")])
		str = i[i.find("electron:")+9:i.find("\n")]
		for k in str.split(" "):
			if k != '':
				count += int(k)
		small_list.append(count)
		count = 0
		big_list.append(small_list)
		small_list = []
		very_small_list = []
	big_list.remove(['', '', '', '', '', 0])
	print(big_list)
	f = open('periodic_table.html','w')
	head = """<!DOCTYPE html>\n<html lang="en">
	<head>
		<title>Periodic Table</title>
		<meta charset="UTF-8">
	</head>
	<body>
		<table style=" border: 1px solid black">\n"""
	f.write(head)
	colomn = 0
	for i in big_list:
		if colomn == 18 or colomn == 0:
			f.write(f'\t\t\t<tr>\n')
			colomn = 0	
		while colomn != int(i[1]) and colomn != 17:
			f.write(f'\t\t\t\t<td style="border: 0px solid black; padding:10px"></td>\n')
			colomn += 1
		if colomn == int(i[1]):
			f.write(f'\t\t\t\t<td style="background: #E6E6FA;border: 1px solid black; padding:10px">\n')
			f.write(f'\t\t\t\t\t<h4> {i[0]} </h4>\n')
			f.write(f'\t\t\t\t\t<ul>\n')
			f.write(f'\t\t\t\t\t\t<li>№ {i[2]}</li>\n')
			f.write(f'\t\t\t\t\t\t<li> {i[3]}</li>\n')
			f.write(f'\t\t\t\t\t\t<li>m={i[4]}</li>\n')
			f.write(f'\t\t\t\t\t\t<li> {i[5]}e</li>\n')
			f.write(f'\t\t\t\t\t</ul>\n')
			f.write(f'\t\t\t\t</td>\n')
			colomn += 1
		if colomn == 18:
			f.write(f'\t\t\t</tr>\n')


	end = """		</table>
	</body>
</html>
	"""
	f.write(end)





if __name__ == '__main__':
	my_var()