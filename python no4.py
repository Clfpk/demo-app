# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:20:50 2023

@author: Prachi
"""

import re
import json
import json
import math
import platform


class Myclass:
    x = 5


print(Myclass)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = person("john", 36)
print(p1.name)
print(p1.age)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = person("john", 36)
print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

# object modify properties
p1.age = 40
print(p1.age)

# delete object
del p1

# the pass statement


class person:
    pass


x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
'''
for x in "banana":
    print(x)
'''

a = "hello, world!"
print(len(a))

b = "Hello, world!"
print(b[2:5])


# negative indexing

b = "Hello, world!"
print(b[-5:-2])

a = "HELLO, WORLD!"
print(a.lower())

age = 36
txt = "my name is john,and i am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "i want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# LIST
mylist = ["apple", "banana", "cherry"]
print(mylist)

thislist = list(("apple", "banana", "cherry"))
print(thislist)

# list items - data types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

list1 = ["MJ", 50, False, 40, "Female"]
print(list1)

thislist = list(("apple", "banana", "cherry"))
print(type(thislist))

# access items

thislist = list(("apple", "banana", "cherry"))
print(thislist[0])

# Negative indexing

thislist = list(("apple", "banana", "cherry"))
print(thislist[-1])

# Range of indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# check if item exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("yes, 'apple' is in the fruits list.")

# change the range of item value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["Blackcurrent", "melon"]
print(thislist)

# insert items

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# append items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "kiwi"]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3, 4]
list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
    print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3, 4, 5]
list1.extend(list2)
print(list1)

thistuple = ["apple", "banana", "cherry", "apple", "cherry"]
print(thistuple)
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))
# not a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thistuple[2:5])

thistuple = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thistuple[:4])

thistuple = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thistuple[2:])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

p1.age = 40
print(p1.age)

# polymorphism

x = "Hello world!"
print(len(x))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))

# Class polymorphism


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Turing 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

# Inheritance polymorphism


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Turing 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# Local socpe


def myfunc():
    x = 300
    print(x)


myfunc()


# functiom inside the function

def myfunc():
    x = 500

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunc()

# Globel scope

x = 800


def myfunc():
    print(x)


myfunc()
print(x)

'''
#use module

def greeting(name):
  print("Hello, " + name)

import mymodule
mymodule.greeting("Jonathan")
print(mymodule.greeting)
 '''
#variable in module

person1 = {
    "name": "V",
    "age": 30,
    "country": "South Korea"
}
print(person1)

x = dir(platform)
print(x)


def greeting(name):
    print("Hello, " + name)


person = {
    "name": "JK",
    "age": "27",
    "country": "South Korea"
}
print(person)

x = min(5, 15, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)

x = math.sqrt(64)
print(x)


x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)


x = math.pi
print(x)

print(json)

# some json
x = '{ "name":"Taehyung", "age":27, "city":"New York"}'

# parse x
y = json.loads(x)

# the result is python dictionary:
print(y["age"])


x = {
    "name": "JK",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x = {
    "name": "jk",
    "age": "27",
    "married": "True",
    "divorced": "False",
    "children": ("jimin", "jin"),
    "pets": None,
    "cars": [
        {"model": "Rolls-Royce Boat Tail", "mpg": 28.5},
        {"model": "Buggati", "mpg": 24.5}
    ]
}
print(json.dumps(x))

# use indent parameter to define numbers of indents


x = {
    "name": "jk",
    "age": "27",
    "married": "True",
    "divorced": "False",
    "children": ("jimin", "jin"),
    "pets": None,
    "cars": [
        {"model": "Rolls-Royce Boat Tail", "mpg": 28.5},
        {"model": "Buggati", "mpg": 24.5}
    ]
}
print(json.dumps(x, indent=4))


txt = "The rain in Spain"
x = re.search("^The.*spain$", txt)

if x:
    print("yes! we have match!")
else:
    print("No match")

# the findall function


txt = "The rain in spain"
x = re.findall("ai", txt)
print(x)


txt = "the rain in spain"
x = re.findall("portugal", txt)
print(x)


txt = "The rain in spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in spain"
x = re.split("\s", txt, 1)
print(x)


txt = "The rain in spain"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in spain"
x = re.search("ai", txt)
print(x)

txt = "The rain in spain"
x = re.search(r"\bs\w+", txt)
print(x.span())

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

#file handling

f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(5))

f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline()) 

f = open("demofile.txt", "r")
for x in f:
    print(x)
    
f = open("demofile.txt", "r")
print(f.readline())
f.close()

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open ("demofile.txt", "r")
print(f.read())

# METPLOTLIB

import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 5])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# plotting x and y axis

import  matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt .plot(xpoints, ypoints)
plt.show() 


# HISTOGRAM==========================================

import numpy as np
x = np.random.normal(170, 10, 250)
print(x)

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()

#creating pie chart========================================

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

#labels==================================================

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show

#======================================================

import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels= mylabels, explode = myexplode, shadow = True)
plt.show()

#colors==============================================

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["r", "b", "g", "y"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

#legend

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show

#===================================================

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show


