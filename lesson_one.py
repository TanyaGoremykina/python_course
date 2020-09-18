import datetime
# Практическое задание 1.1.
number = 15
print(number)
word = 'Hello world'
print(word)
name = input('Введите свое имя: ')
print('Привет', name, '!')
number = int(input('Введите число: '))
print(number)

# Практическое задание 1.2.
time = int(input('Введите время в секундах: '))
print(str(datetime.timedelta(seconds=time)))
# вариант 2
seconds = int(input('Введите время в секундах: '))
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print(f'{h:d}:{m:02d}:{s:02d}')

# Практическое задание 1.3.
number = int(input('Введите число: '))
print(number+int(str(number)+str(number))+int(str(number)+str(number)+str(number)))

# Практическое задание 1.4.
a = int(input('Введите число: '))
m = a % 10
a = a//10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a//10
print(m)

# Практическое задание 1.5.
succor = int(input('Введите размер выручки: '))
costs = int(input('Введите размер издержек: '))
if succor > costs:
    print('Поздравляем! Вы работаете с прибылью!!!')
    profitability = succor // (succor - costs)
    print('Рентабельность: ', profitability)
    people = int(input('Введите численность сотрудников: '))
    profit_man = (succor - costs) / people
    print('Прибыль в расчете на одного человека: ', profit_man)
else:
    print('Жаль, но Вы работаете в убыток.')

# Практическое задание 1.6.
first_day = int(input('В первый день спортсмен пробежал, (км): '))
last_day = int(input('Сколько должен пробегать спортсмен, (км): '))
count = 1
while first_day < last_day:
    first_day *= 1.1
    count +=1
print ('На', count, 'день спортсмен достигнет желаемого результата')
