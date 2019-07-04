import unittest#The module <unittest> provides tools for testing your code.
from mymodule import factorial#The function factorial is to be tested.

class FactorialTestCase(unittest.TestCase):
#We create a class that inherits from <unittest.TestCase>
#This test case has three unit cases, each of which implemented by a method.

	def setUp(self):
		print("A new unit test begins.")
#Python runs the setUp() method before running each method starting with test_

#When we run this file, any method that starts with <test_> will be run
#automatically.
	def test_five(self):
		result = factorial(5)#We manually call the function to be tested.
		self.assertEqual(result, 120)
#We compare the obtained result with the expected result. The assertEqual
#method will notify us if they are not equal.
#assertEqual(a, b) assertNotEqual(a,b) assertTrue(x) assertFalse(x)
#assertIn(item, list) assertNotIn(item, list)
	def test_one(self):
		result = factorial(1)
		self.assertEqual(result, 1)
	def test_float(self):
		result = factorial(1.1)
		self.assertEqual(result, None)

if __name__ == '__main__':#This if condition is true when we run this file, 
#but is false when we import this file in another file.
	unittest.main()#This method runs the test case.
