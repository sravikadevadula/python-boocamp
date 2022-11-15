# import turtle
#
# display=turtle.Screen()
# turtle = turtle.Turtle()
# turtle.color("orange")
# turtle.pensize(8)
# turtle.shape("arrow")
#
# def triangle(edge=100):
#     turtle.forward(edge)
#     turtle.right(120)
#     turtle.forward(edge)
#     turtle.right(120)
#     turtle.forward(edge)
#     turtle.right(120)
#     turtle.forward(edge)
#     turtle.right(60)
#
# triangle()
# triangle()
# triangle()
# triangle()
# triangle()
# triangle()
#
# display.mainloop()
# import numpy as np
# lis=[]
# sequence=[1,2,2,3]
# arr = np.array(sequence)
# a=np.sort(arr)
# b=a[::-1]
# #
# # np.array[::-1].sort(sequence)
# lis.append((a == arr).any())
# # lis.append((b==arr).any())
# print(lis)
# # print(b)
import random
word='apple'
# b=random.randrange(0,len(word))
print(word[random.randrange(0,len(word))])