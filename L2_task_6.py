# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

number = random.randint(1, 100)
attempt_left = 10

while attempt_left >= 0:
    user_num = input("Введите число: ")
    try:
        user_num = int(user_num)
    except ValueError as k:
        print(k)
    if user_num == number:
        print("Вы угадали! Поздравляем с победой!")
        break
    elif user_num < number:
        print("Ваше число меньше загаданного. Попробуйте ещё раз")
        print(f"Осталось попыток: {attempt_left}")
    elif user_num > number:
        print("Ваше число больше загаданного. Попробуйте ещё раз")
        print(f"Осталось попыток: {attempt_left}")

    attempt_left -= 1
    if attempt_left < 0:
        print(f"Вы проиграли! Было загадано число {number}")
        break
