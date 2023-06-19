# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
from random import randint


def weather(n):
    max_count = 0
    if n < 1 or n > 100:
        print("вы ввели неверное число. Должно быть натуральное от 1 до 100!")
    else:
        count = 0
        for i in range(1, n + 1):
            next = randint(-50, 50)
            print(next)
            if next > 0:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
    return max_count

num = int(input("Введите натуральное число от 1 до 100: "))
print(f"Самая длинная оттепель: {weather(num)} дней")