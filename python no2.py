# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 09:58:24 2023

@author: Prachi
"""

thislist = ["apple" , "banana", "cherry"]
thistuple = ["kiwi", "orange"]
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

thislist = ["apple", "cherry", "banana"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
print(thistuple)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) 

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i]) 
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i > len(thislist):
      print(thislist[i])
i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)
        
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

fruits = ["ple", "ban", "cher", "ki", "go"]
newlist = [ x if x !="banana" else "orange" for x in fruits]
print(newlist)

thislist = ["orange", "mango", "cherry", "pineapple", "banana", "apple", "kiwi"]
thislist.sort()
print(thislist)

#sort numerically

thislist = [100 , 50, 65, 85, 30]
thislist.sort()
print(thislist)

#sort the list decending
thislist = ["orange", "mango", "cherry", "pineapple", "banana", "apple", "kiwi"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
    return abs(n - 50)

thislist = [100 , 50, 65, 85, 30]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy method 

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(mylist)
print(mylist)

#join two lists 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#join two list 2
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    print(list1)
    
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#allow duplicate

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#create tuple with one item

thistuple = ("apple",)
print(type(thistuple))

#Not a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple item data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", "34", True, 40, "male")
print(tuple1)

#type

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#tuple constructor

thistuple = tuple(("apple", "banana", "cherry"))#note the double round brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[2])

#negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#range of indexing

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[:4])

thislist = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[2:])

#range of nagative index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[-4:-1])

#cheak if item exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple'is in the fruits tuple")
    
#set

thisset = {"apple", "banana", "cherry"}
print(thisset)

#duplicates not allowed
thisset =  {"apple", "banana", "cherry", "apple"}
print(thisset)
    
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)