'''Создать матрицу 3*3, заполнить ее рандомными значениями. Заменить все четные числа на нули.
'''

from itertools import count as count_from

count = count_from(2)
matrix = [[next(count) for _ in range(3)] for _ in range(3)]
print(f'Получили матрицу 3*3 {matrix}')

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0:
            matrix[i][j] = 0

print(f'заменили в исходной матрице все четные числа {matrix}')