# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 2

closest_element = min(list_1, key=lambda x: abs(x - k))
print(closest_element)
