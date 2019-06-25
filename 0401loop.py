people = ['alice','bob','carolina']
for person in people:
	print(person)
for value in range(1,5):#1,2,3,4
	print(value)
for value in range(5):#0,1,2,3,4
	print(value)
new_list = list(range(1,5)) #[1,2,3,4]
a = min(new_list) # 1
b = max(new_list) # 4
c = sum(new_list) # 10
print(a,b,c)
squares = [value**2 for value in range(1,11)]
numbers = [i for i in range(1,11)]
myslice = numbers[0:3] # a new list containing first three items
last_three = numbers[-3:]
step_two = numbers[::2]
a = numbers # a and numbers are two names of the same list.
a = numbers[:] # a is an separate list, having the same content as numbers.
my_tuple = (200, 50) # A tuple. Tuples cannot be changed.
my_tuple = 200, 50 # Also a tuple. Comma is essential
one_item_tuple = 12, # must use comma

