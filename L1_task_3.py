# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f',
# то вводятся эти символы. Программа должна вывести на экран любой символ
# алфавита от 'a' до 'f' включительно.

import random

gen_type = (input("Типы генератора:\n"
                 "i - случайное целое число\n"
                 "f - случайное вещественное число\n"
                 "c - случайная буква\n"
                 "Введите нужный код: ")).lower()

if gen_type == "i":
    left_border = int(input("Введите целое число - левую границу диапазона: "))
    right_border = int(input("Введите целое число - правую границу диапазона: "))
    rand_num = random.randint(left_border, right_border)
    print(f"Случайное  число в диапазоне от {left_border} до {right_border} = {rand_num}")

elif gen_type == "f":
    left_border = float(input("Введите число - левую границу диапазона: "))
    right_border = float(input("Введите число - правую границу диапазона: "))
    rand_num = random.uniform(left_border, right_border)
    print(f"Случайное вещественное число в диапазоне от {left_border} до {right_border} = {rand_num}")

elif gen_type == "c":
    left_border = ord(input("Введите символ - левую границу диапазона: "))
    right_border = ord(input("Введите символ - правую границу диапазона: "))
    if left_border < right_border:
        rand_num = random.randint(left_border, right_border)
        rand_char = chr(rand_num)
    else:
        rand_num = random.randint(right_border, left_border)
        rand_char = chr(rand_num)
    print(f"Случайная буква в диапазоне от {chr(left_border)} до {chr(right_border)} - {rand_char}")

else:
    print("Неверно выбран тип генератора. Запустите программу заново")
