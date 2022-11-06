# Basic calculator:
from math import *


def calc_math_expression(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == ':':
        if num2 == 0:
            return None
        return num1 / num2
    else:
        return None
#

def calc_math_expression_from_str(str_input):
    numbers = str_input.split(' ')
    num1 = float(numbers[0])
    num2 = float(numbers[2])
    operator = numbers[1]
    return calc_math_expression(num1, num2, operator)

def find_largest_and_smallest_numbers(num1, num2, num3):
    l=[float(num1),float(num2),float(num3)]

    return max(l),min(l)

find_largest_and_smallest_numbers(5, 1, 10)

#
def quadratic_equation_solver(a, b, c):
    if a==0 or ((b**2)<(4*a*c)):
        return None,None
    x1 = (-(b) + sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    x2 = (-(b) - sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    if x1 == x2:
        return x1, None
    else:
        return x1, x2


print(quadratic_equation_solver(1, 1.5, -1))
def quadratic_equation_solver_from_user_input(values):
    values=input('enter 3 numbers:')
    numerics=values.split(' ')
    a = float(numerics[0])
    b = float(numerics[1])
    c = float(numerics[2])
    return quadratic_equation_solver(a,b,c)


def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if temp_1 and temp_2 > min_temp:
        return True
    elif temp_1 and temp_3 > min_temp:
        return True
    elif temp_2 and temp_3 > min_temp:
        return True
    else:
        return False
print(temp_checker(0, 90, 0, 1))




