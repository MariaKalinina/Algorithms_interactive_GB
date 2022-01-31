# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

array_10 = [random.randint(-100, 100) for _ in range(10)]

print(f'Исходный массив: {array_10}')


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        return array


def bubble_reverse(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1 - j):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


print('Классическая пузырьковая:', bubble_sort(array_10))
print('Обратная пузырьковая:', bubble_reverse(array_10[:]))
print(array_10)
