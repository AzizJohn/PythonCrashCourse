filename = 'pi_digits.txt'
with open(filename) as file_object: #open(file) defaults to open(file, 'r')
	contents = file_object.read()
print(contents.rstrip())
"""
The keyword <with> closes the file when the <with> block is exited.
The read() method returns the entire contents of the file. read() adds
an empty line when it reaches EOF, so we use .rstrip() method to remove
the extra blank line.
"""

with open(filename) as file_object:
	for line in file_object: #iterate through <filename> line by line
		print(line.rstrip())
		
with open(filename) as file_object:
	lines = file_object.readlines()#<lines> is a list of lines from <filename>
for line in lines:
	print(line.rstrip())

pi_string = ''
for line in lines:
	pi_string += line.strip()
#strip() method can remove leading and trailing whitespaces. 
print(pi_string)
print(len(pi_string))

message = 'I like dogs.'
message.replace('dog', 'cat') # message == 'I like whcatsw'

filename = 'programming.txt'
with open(filename, 'w') as file_object: # 'w' is write mode
	file_object.write("I love programming.\n")
	
filename = 'programming.txt'
with open(filename, 'a') as file_object: # 'a' is append mode
	file_object.write("I also love finding meaning in large datasets.\n")
	
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
else:
	print("Python does not raise the exception.")
#If a ZeroDivisionError is raised, then the except block is executed.
#If not, the else block is executed.
#In either situation, the program continues to run.

filename = 'alice.txt'
try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
	
mystring = "Alice in Wonderland"
print(mystring.split())#['Alice', 'in', 'Wonderland']

line = "Row, row, row your boat"
line.count('row') #2
line.lower().count('row') #3

import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)
#The json.dump() function takes two arguments: a piece of data to store
#and a file object it can use to store the data.
	
import json
filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)
print(numbers)
