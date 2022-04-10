# 1
li = ['abc', sum(range(10)), [1, 2, 3], 45]
for el in li:
    print(el, type(el))

# 2
li = list(map(int, input('Введите список через пробел: ').split()))
for i in range(0, len(li)-1, 2):
    li[i], li[i + 1] = li[i + 1], li[i]
print(*li)

# 3
mon = int(input('Введите номер месяца(1-12): '))
li = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
for i in range(4):
    if mon in li[i]:
        if i == 0:
            print('Зима')
        elif i == 1:
            print('Весна')
        elif i == 2:
            print('Лето')
        else:
            print('Осень')

di = {12: 'Зима', 1: 'Зима', 2: 'Зима',
      3: 'Весна', 4: 'Весна', 5: 'Весна',
      6: 'Лето', 7: 'Лето', 8: 'Лето',
      9: 'Осень', 10: 'Осень', 11: 'Осень'}
print(di[mon])

# 4
li = list(input('Введите несколько слов через пробел: ').split())
for w in li:
    if len(w) > 10:
        print(w[0:10])
    else:
        print(w)

# 5
li = [6, 3, 2, 1, int(input('Введите натуральное число (0 для завершения): '))]
while li[-1]:
    for i in range(len(li)-2, -1, -1):
        if li[i+1] > li[i]:
            t = li[i+1]
            li[i+1] = li[i]
            li[i] = t
        else:
            break
    print(li)
    li.append(int(input('Введите натуральное число (0 для завершения): ')))
