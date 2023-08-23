# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:51:16 2023

@author: Prachi
"""

#type conversion

x = 1
y = 2.5
z = 5j

#convert int to float
a = float(x)

#convert float to int
b = int(y)

#convert int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random number

import random
print(random.randrange(1,10))

#srring

print('hello')
print("hello")

#multiline strings

a = '''I need somebody who can love me at my worst
       No,I'm not perfect, 
       but I hope you see my worth,.'''
print(a)

a = "Hello, World!"
print(a[1])

txt = "the best thing in life are free!"
if "free" in txt:
    print("yes, 'free' is present.")
    

    txt = "the best thing in life are free!"
    if "expensive" not in txt:
        print("No, 'expensive' is Not present.")
        
b = "HELLO,WORLD!"
print(b[-5:-2]) 

a = 200
b = 33
if b>a:
    print("b is grater than a")
else:
    print("b is not grater than a")
   
#pytho boolean    
   
print(bool("Hello"))
print(bool(15))

x = "hello"
y = 15
print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool("123"))
print(bool(["apple" , "banana" , "cherry"]))


#function can return a boolean
def myfunction():
    return True
print(myfunction())

def myfunction():
    return True
if myfunction():
    print("Yes!")
else:
    print("No!")
    
    

    