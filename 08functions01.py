def myfun(): # parentheses, colon, indentation
	"""description""" # docstring enclosed by triple quotes
	print("Hello!")	
myfun() # to call a function, specify its name followed by parentheses

#Any parameter with a default value needs to be listed AFTER all the parameters
#that don't have default values.
def user(name, age=18): #no spaces in age=18
	"""description"""
	string = f"Hello, {name.title()} is {age} years old."
	return string
string = user(age=12, name='Tom') # Keyword arguments. Order is arbitrary.
#no spaces in age=12
print(string)

def function_with_many_arguments( #press ENTER after the opening parenthesis
		parameter_0, parameter_1, parameter_2, #two tabs
		parameter_3, parameter_4, parameter_5): #two tabs
	pass #one tab
	
#If we pass a list as an argument to a function, then the function can modify it
list_a = [1, 2, 3]
list_b = []
def exchange_list (from_list, to_list):
	while from_list:
		to_list.append(from_list.pop())
exchange_list(list_a, list_b) # list_a = [], list_b = [3,2,1]
exchange_list(list_a[:], list_b) # This only sends a copy of list_a.

def make_pizza(*toppings):
#*toppings tells Python to make an empty tuple called toppings and pack whatever
#values it receives into this tuple.
	print(toppings)
	for topping in toppings:
		pass # do something
make_pizza('a') # ('a',)
make_pizza('b', 'c', 'd') # ('b', 'c', 'd')

#Python matches positional and keyword arguments first and then collects
#any remaining arguments in the final parameter.
def make_pizza(size, *toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
#**user_info causes Python to create an empty dictionary called user_into
#and pack whatever name-value pairs it receives into this dictionary.
	user_info['first_name'] = first #user_info is a dictionary
	user_info['last_name'] = last
	return user_info
user_profile = build_profile('albert', 'einstein',
							location='princeton', 
							field='physics')
print(user_profile)
#{'location': 'princeton', 'field': 'physics', 'first_name': 'albert',
#'last_name': 'einstein'}

#Modules should have short, all-lowercase names.
import mymodule
mymodule.hello()

#The following lines introduce another method to use a module.
from mymodule import hello as h
h()

#Use an alias to rename a module
import mymodule as mm
mm.hello()

#import every function in a module. This method is discouraged.
from mymodule import *
hello()
