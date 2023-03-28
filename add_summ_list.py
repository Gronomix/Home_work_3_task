'''Напишите программу, которая на основе списка из натуральных чисел формирует целое число.
Число формируется «объединением» элементов списка: например, если исходный список [12, 3, 456, 78],
то программа должна получить число 12345678.

'''

print(' Первый способ через цикл')

x_lst = [12, 3, 456, 78]
result = 0

for x in x_lst:
    t = 0
    while x:
        t *= 10
        t += x%10
        x //= 10

    while t:
        result *=10
        result += t%10
        t //= 10

    del t

print(result)

''' ВТОРОЙ СПОСОБ'''

print('Второй способ через распоковку и цикл')

string = f''

for elem in x_lst:
    string += str(elem)
print(string)

print(f' 3 способ через метод join  с использованием метода map так как список int')

print(''.join(map(str, x_lst)))