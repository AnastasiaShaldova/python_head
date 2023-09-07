"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
from random import random, randint


list_generator = list(randint(-10, 10) for i in range(20))
print(list_generator)
_max = 10
_min = 6

for i in range(len(list_generator)):
    if _min <= list_generator[i] <= _max:
        print(i, end=' ')
