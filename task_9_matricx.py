'''Создать матрицу, найти максимальное значение матрицы.
'''

import random

n = int(input("Введите размер матрицы:"))
arr = [[random.randint(1, 9) for i in range(n)] for j in range(n)]
min_arr = arr[0][0]
max_arr = 0

for i in range(n):
    for j in range(n):
        if(arr[i][j] < min_arr):
            min_arr = arr[i][j]
        elif(arr[i][j] > max_arr):
            max_arr = arr[i][j]
for i in range(n):
    print(arr[i])
    print(max_arr, min_arr)