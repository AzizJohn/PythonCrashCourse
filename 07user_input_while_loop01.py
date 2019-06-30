#The input() function records every keystroke up to the first ENTER key.
#It returns a string.
age = input("Please enter your age: ") # age is a string
age = int(age) # age is an integer
if age >= 18:
	print("You are an adult")
#To remove from a list every occurrence of a value.
pets = ['cat', 'cat', 'dog', 'cat']
while 'cat' in pets:
	pets.remove('cat')
print(pets)
