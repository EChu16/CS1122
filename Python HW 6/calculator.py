'''
Erich Chu
CS1122 
HW 6
Calculator in python
'''

while(True):
	equation = raw_input("Enter math: ")
	if equation[1] == "+":
		print int(equation[0] ) + int(equation[2])
	elif equation[1] == "-":
		print int(equation[0] ) - int(equation[2])
	elif equation[1] == "/":
		print int(equation[0] ) / int(equation[2])
	elif equation[1] == "*":
		if equation[2] == "*":
			print int(equation[0] ) ** int(equation[3])
		else: print int(equation[0] ) * int(equation[2])
