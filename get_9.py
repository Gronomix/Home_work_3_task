'''Напишите программу, в которой пользователь вводит целое число
а программа каждую цифру в этом числе меняет на «дополнение до 9,
цифра 0 меняется на 9, цифра 1 меняется на 8, цифра 2 меняется на 7
и так далее - цифра 8 меняется на 1, а цифра 9 меняется на 0.
'''

x = input(' Введите целое число: ')

result = 10 ** len(x) - 1 - int(x)
print(result)

#Проверим числа
print(f' {10 ** len(x)}, {10** len(x) - 1} - {int(x)}')



