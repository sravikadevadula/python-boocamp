import numpy as np


def input_list():
    numbers = None
    l1 = []
    while numbers != '':
        numbers = input('enter the number:')
        l1.append(numbers)
    return l1


def final_list():
    l1 = input_list()
    l1.pop(-1)
    total = 0.0
    for i in l1:
        total = total + float(i)
    l1.append(total)
    print(l1)


def check_monotonic_sequence(sequence):
    lis = []
    lis1 = []
    lis2 = []
    lis3 = []
    lis4 = []
    length = len(sequence)
    for i in range(length - 1):
        if sequence[i] <= sequence[i + 1]:
            lis1.append(True)
        else:
            lis1.append(False)
    if lis1.count(False) == 0:
        lis.append(True)
    else:
        lis.append(False)

    for i in range(length - 1):
        if sequence[i] < sequence[i + 1]:
            lis2.append(True)
        else:
            lis2.append(False)
    if lis2.count(False) == 0:
        lis.append(True)
    else:
        lis.append(False)
    for i in range(length - 1):
        if sequence[i] >= sequence[i + 1]:
            lis3.append(True)
        else:
            lis3.append(False)
    if lis3.count(False) == 0:
        lis.append(True)
    else:
        lis.append(False)
    for i in range(length - 1):
        if sequence[i] > sequence[i + 1]:
            lis4.append(True)
        else:
            lis4.append(False)
    if lis4.count(False) == 0:
        lis.append(True)
    else:
        lis.append(False)
    return lis


def check_monotonic_sequence_inverse(def_bool):
    match def_bool:
        case [True, True, False, False]:
            return [1, 2, 3, 4, 5, 6, 7, 8]
        case [True, False, False, False]:
            return [1, 2, 2, 3]
        case [True, False, True, False]:
            return [1, 1, 1, 1]
        case [False, False, True, False]:
            return [3, 2, 1, 1]
        case [False, False, True, True]:
            return [7.5, 4, 3.141, 0.111]
        case [False, False, False, False]:
            return [1, 0, -1, 1]
        case [True,True,True,True]:
            return [10]
        case _:
            return None


def primes_generator(n):
    if n == 0:
        return []
    l2 = []
    i = 2
    num = 2
    is_prime = True
    while True:
        while i <= num - 1:
            if (num % i) == 0:
                is_prime = False
            i += 1
        if is_prime:
            l2.append(num)
        if len(l2) == n:
            break
        num += 1
        i = 2
        is_prime = True
    return l2


def is_empty_vecotr(vec_lst):
    if len(vec_lst) == 0:
        return True
    else:
        return False


def vectors_list_sum(vec_lst):
    l3 = []
    if not is_empty_vecotr(vec_lst):
        sum1 = 0
        for i in range(len(vec_lst[0])):
            for j in range(len(vec_lst)):
                sum1 += vec_lst[j][i]
            l3.append(sum1)
            sum1 = 0
    return l3


def calc_the_inner_product(vec_1, vec_2):
    if len(vec_1) == 0 and len(vec_2) == 0:
        return 0
    if len(vec_1) == 0 or len(vec_2) == 0:
        return None
    a = np.multiply(vec_1, vec_2)
    return sum(a)


def orthogonal_number(vectors):
    count = 0
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            product = calc_the_inner_product(vectors[i], vectors[j])
            if product == 0:
                count += 1
    return count
