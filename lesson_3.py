# Практическое задание 3.1.
def del_two_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Делить на ноль нельзя'
    except ValueError:
        return


result = del_two_numbers(x=int(input("Введите первое число: ")), y=int(input("Введите второе число: ")))
print(f"Результат деления: {result}")


# Практическое задание 3.2.
def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


people = my_func(surname=input('Введите фамилию: '), name=input('Введите имя: '),
                 city=input('Введите город проживания: '), year=input('Введите дату рождения: '),
                 telephone=input('Введите номер телефона: '), email=input('Введите email: '))
print(people)


# Практическое задание 3.3.
def my_func(x, y, z):
    num = [x, y, z]
    num.remove(min(x, y, z))
    return sum(num)


result = my_func(x=int(input("Введите первое число: ")), y=int(input("Введите второе число: ")),
                 z=int(input("Введите третье число: ")))
print(f"Сумма двух наибольших чисел: {result}")


# Практическое задание 3.4.
# Вариант 1
def my_func(x, y):
    return 1 / x ** abs(y)


result = my_func(x=int(input("Введите положительное число: ")), y=int(input("Введите отрицательное число: ")))
print(f"Результат возведения положительного числа в отрицательную степень: {result}")


# Вариант 2
def my_func_1(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


result = my_func_1(x=int(input("Введите положительное число: ")), y=int(input("Введите отрицательное число: ")))
print(f"Результат возведения положительного числа в отрицательную степень: {result}")


# Практическое задание 3.5.
def sum_any_numbers():
    res = 0
    while True:
        numbers = input("Введите несколько чисел через пробел или * для выхода: ").split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма чисел: {res}. Выход')
                    return
                else:
                    res += int(i)
            except ValueError:
                print("Введите несколько чисел через пробел или * для выхода")
        print(f'Сумма чисел: {res}')


sum_any_numbers()


# Практическое задание 3.6.
def capitalize(text):
    return text.title()


my_text = input("Введите слово или текст: ")
print(capitalize(my_text))
print(capitalize("hello world"))
print(capitalize("привет"))
