"""A module's name should end in .py.
To use a module, add a line like
	from mymodule import myfunction
in the begining of a program (say my_program.py). Note that the .py part of
the module name is omitted here.
Then use
	python3 my_program.py
to run this python program. Note that the module name is not needed here."""

def hello():
	print("Hello World!")
	
def bye():
	print("Good bye!")

def factorial(x):
	if type(x) != int:
		return None
	result = 1
	for i in range(1,x+1):
		result *= i
	return result
