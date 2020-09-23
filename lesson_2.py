# Практическое задание 2.1.
my_list = [5, 'привет', True, None, 36.6]
for element in my_list:
    print(type(element))

# Практическое задание 2.2.
el_count = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите значение списка: "))
    i += 1
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)

# Практическое задание 2.3.
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
month = int(input('Введите порядковый номер месяца: '))
if month > 12:
    print("Такого месяца не существует")
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input("Введите порядковый номер месяца: "))
if month == 1 or month == 12 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
else:
    print("Такого месяца не существует")

# Практическое задание 2.4.
text_list = input('Введите несколько слов через пробел: ').split()
for index, word in enumerate(text_list, 1):
    print(index, word[0:10])

# Практическое задание 2.5.
my_list = [7, 5, 3, 3, 2]
print("Рейтинг -", my_list)
number = int(input("Введите новый элемент рейтинга: "))
amount = my_list.count(number)
for el in my_list:
    if amount > 0:
        i = my_list.index(number)
        my_list.insert(i + amount, number)
        break
    elif number > el:
        my_list.insert(0, number)
        break
    elif number < my_list[len(my_list) - 1]:
        my_list.append(number)
print("Новый рейтинг - ", my_list)

# Практическое задание 2.6.
goods = []
features = {'наименование': '', 'цена': '', 'количество': '', 'ед.изм.': ''}
analytics = {'наименование': [], 'цена': [], 'количество': [], 'ед.изм.': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмиту 'N', для продолжения нажмите 'Enter'").upper()
    if control == 'N':
        break
    num += 1
    for f in features.keys():
        feature_ = input(f'Введите "{f}": ')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
print('Структура данных "Товары":')
print(goods)
print('"Аналитика о товарах":')
for key, value in analytics.items():
    print(f'{key}: {value}')
