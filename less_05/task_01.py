"""
Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
Функция не должна ничего выводить, только возвращать значение.

Пример:

a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8

"""


def f(a: int, b: int):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / f(a, -b)
    elif b % 2 == 0:
        return f(a, b // 2) ** 2
    else:
        return a * f(a, b - 1)


print(whole_degree(2, 3))