# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 12, 6, 7, 8, 15]
k = 11

closest_element = min(list_1, key=lambda x: abs(x - k))
print(closest_element)
