'''Напишите программу, в которой пользователь вводит целое число
от 1 до 7 включительно, а программа выводит название дня недели,
соответствующее этому числу ("Понедельник" для 1,"Вторник" для 2,
и так далее).

'''

q = int(input('Введите число дня недели от 1 до 7: '))
if q == 1:
    print('Понедельник')
elif q == 2:
    print('Вторник')
elif q == 3:
    print('Среда')
elif q == 4:
    print('Четверг')
elif q == 5:
    print('Пятница')
elif q == 6:
    print('Суббота')
else:
    print('Воскресенье')