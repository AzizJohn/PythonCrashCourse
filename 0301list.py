mylist = ["one", "two", "three"]
print(mylist[1]) # 0-based
print(mylist[-1]) # last item
message = f"The number 1 is {mylist[0].title()}"
mylist.append('four')
del mylist[0]
popped_item = mylist.pop()
first_item = mylist.pop(0)
print(first_item)
mylist = ["one", "two", "three","one"]
mylist.remove("one") # delete the first occurrence
mylist.insert(-1,'one')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #The list is sorted alphabetically.
cars.sort(reverse=True)
print(sorted(cars))
#.sort() method change a list, sorted()function doesn't change
# the original list, it only return a sorted list.
print(sorted(cars,reverse=True))
num=[1,3,7,6]
num.reverse()
count=len(num)
