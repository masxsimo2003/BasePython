# 1
Pi = 3.14159
print(Pi)
s = input('Введите Ваше имя: ').title()
print('Вас зовут ', s)

# 2
sec = int(input('Введите время в секундах: '))
min = sec // 60
sec -= min * 60
h = min // 60
min -= h * 60
print(f'{h:02d}:{min:02d}:{sec:02d}')

# 3
n = input('Введите число: ')
nn = n + n
nnn = nn + n
print(int(n) + int(nn) + int(nnn))

# 4
n = int(input('Введите целое положительное число: '))
m = 0
while n > 0:
    t = n % 10
    if t > m:
        m = t
    n //= 10
print(m)

#5
a, b = map(int, input('Введите выручку и издержки(через пробел): ').split())
if a > b:
    print(f'Ваша прибыль составила {a-b}')
    #6
    print(f'Ваша рентабельность составила {(a-b)*100//a}%')
    n = int(input('Введите число сотрудников: '))
    print(f'Прибыль на сотрудника равна {(a-b)/n}')
else:
    print(f'Ваш убыток составил {b-a}')

#7
a, b = map(int, input('Введите начальную и желаемую дистанцию пробежки(через пробел): ').split())
ans = 1
while a < b:
    a *= 1.1
    ans += 1
print(ans)
