'''Создать матрицу 3*3, заполнить ее рандомными значениями. Заменить все четные числа на нули.
'''

from itertools import count as count_from

count = count_from(1)
matrix = [[next(count) for _ in range(3)] for _ in range(3)]
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0:
            matrix[i][j] = 0

print(matrix)