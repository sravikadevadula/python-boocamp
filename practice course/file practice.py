a = 'apple'
b = 'bat'
###Functions:
##indexing:
# print(a[1])                      o/p:p
# print(a.index('p'))             o/p:1
# print(a.index('le')) #gives the index position of the alphabet in the word          o/p:3
# replace function:
# print(a.replace('a','e'))      o/p:epple
##Arithmatic operations:
# abs:absolute value of a number(without considering negative sign in thge front of a number as follows)
# eg:c=-4.5
# print(abs(c))      o/p:4.5
# pow:to get power of desired number.
# print(pow(5,2))    o/p:25
# max:print(max(12,56,3,99))                o/p:99
# min:print(min(1,2,3,4,5))                 o/p:1
# round:to rounden a number as per standard rules
# print(round(4.6))                        o/p:5
# to import multiple math functions following library is supposed to be imported
from math import *

# floor:is similar to integer function
# ceil:is similar to roundening up but it gives the higher number if there is any decimal
# eg:print(ceil(3.1))               o/p:4
# sqrt:square root
# print(sqrt(25))                  o/p:5
##Input function:
# num1=int(input('enter first number:'))
# num2=int(input('enter second number:'))
# print('your total is:',num1+num2)
# color=input('enter the colour:')
# plural_noun=input('enter the plural noun:')
# celebrity=input('enter the plural noun:')
# print('Roses are {0}\n{1} are blue\nI love {2}'.format(color,plural_noun,celebrity))
##Lists:[x,y,z]
l1 = ['apple', 'bat', 'cat', 'dog', 'fat']
# print(l1[1])         o/p:bat
# negative index:
# print(l1[-1])          o/p:fat
# print(l1[-4:-2])        o/p:['bat','cat']
##List functions:
l2 = [12, 567, 7, 98, 13]
# extend:to add desired list to any required list
# l1.extend(l2)
# print(l1)                 o/p:['apple', 'bat', 'cat', 'dog', 'fat', 12, 567, 7, 98, 13]
# append:to add additional item to a list
# l2.append(23)
# print(l2)                  o/p:[12, 567, 7, 98, 13, 23]
# insert:to add a specific item into a desired index position of a list
# l1.insert(1,'grape')
# print(l1)                   o/p:['apple', 'grape', 'bat', 'cat', 'dog', 'fat']
# remove:
# l1.remove('bat')
# print(l1)                    o/p:['apple', 'cat', 'dog', 'fat']
# clear:to empty an entire list
# l1.clear()
# print(l1)
# pop:remove a particular item by entering the index position
# print(l1.pop(1))
# print(l1)
# .index:to get the index position of an item
# print(l1.index('bat'))             o/p:1
# count:to get how many times an item is repeated in a list
# l2.append(13)
# print(l2.count(13))                 o/p:2
# sort:to get a list in alphabetical or ascending order
# l2.sort()
# print(l2)                             o/p:[7, 12, 13, 98, 567]
# reverse:can reverse a list
# l2.reverse()
# print(l2)                              o/p:[13, 98, 7, 567, 12]
# copy:can copy a list into a new one
# l3=l2.copy()
# print(l3)                               o/p:[12, 567, 7, 98, 13]
##Tuples:() immutable
t1 = (12, 35, 14)

# print(t1[0])                            o/p:12
##Functions:
# def  apple():
#    print('it is a fruit')
# print(apple())
# def  area_circle(r):
#     print('this is r\n', 3.12 * (r ** 2))
# print(area_circle(3))
# def algebra(a,b):
#    print((a ** 2) + (b ** 2) + 2 * (a * b))
# print(algebra(2,3))
# return:to get information back from the function like arithmatic equations
# def algebra(a, b):
#    return (a ** 2) + (b ** 2) + 2 * (a * b)


# print(algebra(2, 3))




