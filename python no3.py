# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 10:09:23 2023

@author: Prachi
"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#range of negative indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#check if item exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple" )
    
#change tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "kiwi"
x = tuple(y)
print(x)

#add items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#add tuple to a tuple
thistuple = thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#unpacking a tuple

# 1 packing tuple

fruits =("apple", "banana", "cherry")
print(fruits)

#unpacking tuple

fruits = ("apple", "banana", "cherry")
(green, red, yellow) = fruits
print(green)
print(red)
print(yellow) 

#using astrrisk*

fruits = ("apple", "banana", "cherry", "strawberry", "rasberry")
(green, red, *yellow) = fruits
print(green)
print(red)
print(yellow)

#add a list of values the tropic variable

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#python-loop tuples
#you can loop through the tuple item by using a for loop

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    
#loop through a index no
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
    
#using a while loop
thituple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
    
#join tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2

#multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 3
print(mytuple)

#set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#duplicate not allowed
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#get the length of set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#set items -Data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False,False}
print(set1) 
print(set2) 
print(set3)

#set with string,integer and boolean value:
set = {"abc", 34, True, "male"}
print(set)

#type class
myset = {"apple", "banana", "cherry"}
print(type(myset))

#access set items
#loop through the set,and print the values
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
    
#check if banana is present the set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#add set items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#add set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove set items
#remove banana by using remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#remove random item by using pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#clear method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
'''
#del leyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
'''

#joim two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#update(method inserts the items in set2 into set1:)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#keep omly the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

#keep all,but not the duplicate
#keep the items that are not present in both sets:
    
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

#create a print dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict)

#dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict["model"])

#duplicate not allowed
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964",
    "year": "2020"
}
print(thisdict)

#dictionary length
print(len(thisdict))

#dictionary items-data types
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": "1964",
    "colors": ["red", "white", "blue"]
}
print(thisdict)

#dict constructor
thisdict = dict(name = "john", age = 36, country = "norway")
print(thisdict)

#access dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
x = thisdict["model"]
print(x)

#get key
x = thisdict.keys()
print(x)

car = {
       "brand": "Ford",
       "model": "Mustang",
       "year": "1964"
   }
x = car.keys()
print(x)
car["color"] = "white"
print(x)

x = thisdict.values()
print(x)


car = {
       "brand": "Ford",
       "model": "Mustang",
       "year": "1964"
   }
x = car.values()
print(x)
car["year"] = 2020
print(x)


car = {
           "brand": "Ford",
           "model": "Mustang",
           "year": "1964"
       }
x = car.values()
print(x)
car["color"] = "red"
print(x)

#get item
x = thisdict.items()
print(x)

#check if key exist
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
if "model" in thisdict:
    print("Yes",'model is one of the keys in the thisdict dictionary')
    
#change dictionary items 
#change values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
thisdict["year"] = 2018
print(thisdict)

#update dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
thisdict.update({"year": 2020})
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
thisdict["color"] = "red"
print(thisdict)

#add color item to the dictionary by using the update() method

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
thisdict.update({"color":"red"})
print(thisdict) 

#remove dictionary(removing items)
#pop() method removes the item with the specific key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
thisdict.popitem()
print(thisdict)

#del keyword removes the item with the specific key name
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
del thisdict["model"]
print(thisdict)

# the clear method empties the dictionary:
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
thisdict.clear()
print(thisdict)

# loop dictionary
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
for x in thisdict:
    print(x)
    
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
for x in thisdict:
    print(thisdict[x])
    
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
for x in thisdict.values():
    print(x)
    
thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": "1964"
}
for x in thisdict.keys():
    print(x)
    
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
for x in thisdict.items():
    print(x)
    
#copy dictionary
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
mydict = thisdict.copy()
print(mydict)


#make a copy of a dictionary with the dict() function
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : "2004"

    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "linus",
        "year" : 2011
}
}
print(myfamily)  

#Creat three dictionarues,then creat one dictionary that will contain the other three dictionaries  
child1 = {
    "name" : "V",
    "year" : 1995
}
child2 = {
    "name" : "Jk",
    "year" : 1997
}
child3 = {
    "name" : "Jimin",
    "year" : 1995
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)

print(myfamily["child2"]["name"])

# If-else statement
a = 33
b = 200
if b > a:
    print("b is grater then a")
    
    #Elif (Else-if)
a = 33
b = 33
if b > a:
    print("b is grater than a")
elif a == b:
    print("a and b are equal")
    
# Else keyword

a = 200
b = 33
if b > a:
    print("b is grater than a")
elif a == b:
    print(" a and b are equal")
else:
    print("a is grater than b")
    
#short hand if
if a > b: print("a is grater than b")

#short hand if-else

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# AND Statement

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both condition are True")

# OR 
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the condition is True")
    
# NOT Statement
a = 33
b = 200
if not a > b:
    print("a is not grater than b")
    
# Nested if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
        
# The pass statemnet
a = 33
b = 200
if b > a:
    pass

if 5 > 2:
  print("Five is greater than two!")

#While loop

i =1
while i < 6:
    print(i)
    i += 1
    
# break statement

i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1
    
# continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
#Else statement

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
    
# FOR loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
         print(x)
         
# looping through string

for x in "banana":
  print(x)
  
  #break statement
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    

        
        