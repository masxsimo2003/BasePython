# 1
def division(a, b):
    if b:
        return a / b
    return "Нельзя делить на ноль!"


# 2 имя, фамилия, год рождения, город проживания, email, телефон
def user(name="", surname="", year="неизвестном", city="Караганде", email="неизвестно", phone="неизвестно"):
    if name == "" and surname == "":
        name = "не представился(-ась)"
    print(
        f'Пользователь {name} {surname}, родился(-ась) в {year} году и проживает в городе {city}. Контактные данные: {email}, {phone}.')


# 3
def my_func(a, b, c):
    return max(a + b, b + c, a + c)


# 4
def my_func1(a, b, easy=True):
    if easy:
        return a ** b
    else:
        ans = 1
        for i in range(b):
            ans *= a
        return ans


# 5
def summer(a):
    global ans, do
    for i in range(len(a)):
        if a[i] != -1:
            ans += a[i]
        else:
            do = False
            break
    print(ans)


# 6
def int_func(s):
    # return s.capitalize()
    return s.title()


# 1
print(division(1, 0))
print(division(4, 2))

# 2
user(name="Вася", year=1925, city="Москва", phone="8(888)888-88-88", email="admin@admin.com", surname="Иванов")

# 3
print(my_func(1, 2, 3))
print(my_func(3, 2, 1))
print(my_func(1, 3, 2))

# 4
print(my_func1(2, 5))
print(my_func1(2, 5, False))

# 5
ans = 0
do = True
while do:
    summer(list(map(int, input("Введите -1 для выхода: ").split())))

# 6
print(int_func("geek brains"))