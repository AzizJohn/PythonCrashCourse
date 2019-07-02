"""
Class names should be written in CamelCase. To do this, capitalize the first
letter of each word in the name, and don’t use underscores.
Instance and module names should be written in lowercase with underscores
between words
"""
class Dog: #class class_name colon. There is no parenthesis here.
	"""description"""
	
	def __init__(self, name, age): #Python calls __init__ whenever we create
		"""description""" #a new instance of class Dog.
		self.name = name #dot notation
		self.age = age
		#Class attributes DO NOT need to be declared, just initialize them
		#directly.
	
	def sit(self):
		"""description"""
		print(f"{self.name} is now sitting.")
#Every method must have <self> as its first parameter. When an instance calls
#a method, a reference to the instance is automatically passed to the method
#as <self>.

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.\nIt's {my_dog.age} years old.")
my_dog.sit()

class GuideDog(Dog):#class inheritance, put <parent_class_name> in parenthese
	def __init__(self, name, age):#a child class' init method should call its
	#parent's init method.
		super().__init__(name, age)
		# super() is a special function that allows youi to call a method
		# from the parent class. It uses the dot notation.
		self.year_served = 4
	
	def show_experience(self):
		print(f"The guide dog {self.name} has served"
		f" for {self.year_served} years.")
	def sit(self): #this child method has the same name as a parent method,
	#so the child method overrides the parent method.
		print("A guide dog does not sit.")
		
blind_dog = GuideDog('Goody',12)
blind_dog.show_experience()
blind_dog.sit()

class Person:
	def __init__(self, my_name, dog_name, dog_age):
		self.name = my_name
		self.my_dog = GuideDog(dog_name, dog_age)
		#use an instance as an attribute
blind_person = Person("John", "Goody", 5)
blind_person.my_dog.sit()

from class_module import MyClass
# put class definition into a file called class_module.py
test_class = MyClass()
test_class.show()
