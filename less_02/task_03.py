# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


def degree_of_number(n: int):
    i = 1
    while i <= n:
        if i * 2 > n:
            break
        i *= 2
        print(i, end=' ')


try:
    n = int(input('Введите целое число: '))
    if n > 0:
        degree_of_number(n)
    else:
        print('Введите число > 0')
except ValueError:
    print('Что-то пошло не так. Повторите попытку.')

