'''Напишите программу, в которой решается уравнение вида
А(А - 1)* x=sin(A) , причем при значении A = 0 должно вычисляться решение x= -1.
'''

import math

a = float(input('Введите число a = '))
try:
    if a > 0:
        x = (a * (a - 1)) / math.sin(a)
        print(x)
    elif a == 0:
        x = (a - 1) / math.sin(a)
        print(f'{(a - 1) / math.sin(a)}')
except ZeroDivisionError as e:
    x = a - 1
    print(math.sin(a))
    print(x)

