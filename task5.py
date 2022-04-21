import random

# 1
with open("task5_1.txt", 'w', encoding="utf-8") as f:
    s = input()
    while s != '':
        f.write(s)
        s = input()

# 2
with open("task5_2.txt", 'r', encoding="utf-8") as f:
    s = f.readlines()
print("Количество строк: ", len(s))
print("Количество слов: ", end=' ')
for line in s:
    print(line.count(" "), end=' ')
print()

# 3
with open("task5_3.txt", 'r', encoding="utf-8") as f:
    s = list(map(lambda x: x.split(), f.readlines()))
print("Имеют оклад более 20000 рублей: ", end=' ')
summ = 0
for line in s:
    summ += int(line[1])
    if int(line[1]) > 20000:
        print(line[0], end=' ')
print()
print("Средняя зарплата =", summ/len(s))

# 4
di = dict(One="Один", Two="Два", Three="Три", Four="Четыре")
s = []
with open("task5_4.txt", 'r+', encoding="utf-8") as f:
    for i in range(4):
        s.append(list(f.readline().split(" — ")))
        s[-1][0] = di[s[-1][0]]
        s[-1] = s[-1][0]+' - '+s[-1][1]
    f.seek(0)
    f.writelines(s)

# 5
s = ''
for i in range(100):
    s = s+' '+str(random.randint(0, 100))
with open("task5_5.txt", 'w') as f:
    f.write(s)
with open("task5_5.txt", 'r') as f:
    s = list(map(int, f.read().split()))
print(sum(s))