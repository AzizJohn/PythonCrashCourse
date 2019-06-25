cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw': # condition has no parentheses, use colon, use indentation.
		print(car.upper())
	else: # use colon, use indentation.
		print(car.title())
print('audi' in cars) # True
print('audi' not in cars) # False
# if-elif-else
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
# use a list as a condition
if cars:
	print("cars has at least one item")	
else:
	print("cars is empty")
