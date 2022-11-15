def input_list():
    numbers = None
    l = []
    while numbers != '':
        numbers = input('enter the number:')
        l.append(numbers)
    return l
def final_list():
    l1 = input_list()
    l1.pop(-1)
    total = 0.0
    for i in l1:
        total = total + float(i)
    l1.append(total)
    print(l1)


final_list()
