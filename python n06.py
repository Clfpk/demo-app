# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:25:59 2023

@author: Prachi
"""
print(5 ** 2)

#===============================================

print(2 ** 7)

#=========================================================

width = 20
height = 5 * 9
x = width * height
print(x)

#========================================================

print(4 * 3.75 - 1)

#==========================================================

tax = 12.5 / 100
price = 100.50
x = price * tax
print(x)

#==========================================================

print('spam eggs')

print("Paris rabbit got your back :! yay!")

print('doesn\'t')

print("doesn\'t")

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('C:\some\name')

print(r'C:\some\name')

print("""\
usage: thingy [OPTION]
     -h
     -H hostname
""")

#==========================================================


s = 'supercalfragilisticeexpiasdsafwewfawerwaWlidocious'
print(len(s))

#====================================================

squares = [0, 4, 9, 16, 25]
print(squares)

squares = [-1]
print(squares)

squares = [0]
print(squares)

#====================================================

squares = [36, 49, 64, 81, 100]
print(squares)

#========================================================

cubs = [1, 8, 27, 65, 125]
print(4 ** 3)

#==========================================================

i = 256*256
print('The valu of i is', i)

#=====================================================

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
    
#fibonacci series==========================================

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
    
a, b = 0, 1
print('The value of i is', i)

#if statement===========================================

x = int(input("Please enter an integer"))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('single')
else:
    print('More')

