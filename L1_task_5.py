# 5. Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

n = int(input('Введите порядковый номер буквы: '))
n_ascii = n + 96
print(f'Под номером {n} находится буква "{chr(n_ascii)}"')
