'''Напишите программу для решения квадратного уравнения. В процессе поиска решения использовать обработку исключитель-
ных ситуаций.
'''
from cmath import sqrt


def otr():
  if d < 0:

        z = sqrt(d)# корень из D
        print ("Т.к. дискриминант меньше нуля то корни будет комплексные")
        x1 = complex((-B+z)/(2*A))
        x2 = complex((-B-z)/(2*A))
        print('X1 = ',x1)
        print('X1 = ',x2)
print('Нахождение корней квадратного уравнения:')
A = eval(input('A = '))
B = eval(input('B = '))
C = eval(input('C = '))
d = B*B-4*A*C#Находим дискриминант
try:
    if A == 0:
        print(f" Ошибка!!!Деление на ноль запрещенно!!!")
except ZeroDivisionError as e:
    print(e)#Вывод сообщения об ошибке
try:
    if d > 0:
       z = sqrt(d)#нахождения корня из D
       input('Для продолжения нажмите <Enter>')
       x1 = (-B+z)/(2*A)
       x2 = (-B-z)/(2*A)
       print('X1 = ',x1)
       print('X2 = ',x2)
except: otr()

else:
    if d == 0:
        x1 =- B / (2*A)
        print('X = ',x1)

otr()