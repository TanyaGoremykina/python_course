from functools import reduce
from itertools import cycle, count
# from sys import argv
"""
Что бы запустить скрипт с параметрами снимите # со стр.3, 8-18 в Практическом задании 4.1. и import argv 
"""
# Практическое задание 4.1.

# script_name, work_hour, cost_hour, bonus = argv
#
#
# def payroll_calculation():
#     return int(work_hour) * int(cost_hour) + int(bonus)
#
#
# payment = payroll_calculation()
# print(f"Заработная плата: {payment}")

# Практическое задание 4.2.
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [number for i, number in enumerate(my_list) if i > 0 and my_list[i] > my_list[i - 1]]
print(f'Исходный список {my_list}')
print(f'Новый список {new_list}')

# Практическое задание 4.3.
print(f'Числа от 20 до 240 кратные 20 или 21: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

# Практическое задание 4.4.
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)

# Практическое задание 4.5.
my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Список четных чисел от 100 до 1000: {my_list}')


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, my_list))

# Практическое задание 4.6.
for el in count(3):
    if el > 10:
        break
    else:
        print(el)
c = 0
for el in cycle("Hello"):
    c += 1
    if c > 10:
        break
    print(el)

# Практическое задание 4.7.


def fact(_):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input("Укажите факториал какого числа Вы хотели бы узнать: "))
for el in fact(n):
    print(el)
