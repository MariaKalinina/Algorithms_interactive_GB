# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num_list = input("Для поиска максимального по сумме цифр \nвведите список натуральных чисел через запятую: ")
num_list = num_list.split(",")
max_sum = 0
sum_list = []
for num in num_list:
    sum_i = 0
    for i in num:
        sum_i += int(i)
    sum_list.append(sum_i)
    if sum_i > max_sum:
        max_sum = sum_i
# max_index = sum_list.index(max_sum)
print(f'Наибольшее число по сумме цифр {num_list[sum_list.index(max_sum)]}, сумма = {max_sum}')
