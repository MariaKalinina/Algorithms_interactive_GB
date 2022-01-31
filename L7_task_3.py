# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random
import statistics

m = 5
two_m = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив {two_m}')


def find_median(array):
    array.sort()
    middle = len(array) // 2
    if len(array) // 2 != 0:
        median_ = array[middle]
    else:
        median_ = (array[middle] + array[middle - 1]) / 2
    return median_


print(f'Медиана, найденнвя с помощью функции = {find_median(two_m)}')
print(f'Медиана, найденнвя с помощью модуля statistics = {statistics.median(two_m)}')
