# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
num = input("Введите число, в котором нужно посчитать четные и нечетные цифры: ")
odd = 0
even = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Число {num} содержит {even} четных и {odd} нечетных цифр.')
