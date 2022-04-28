from task6_classes import *


# 1
tl = TrafficLight()
tl.running()

# 2
r = Road(20, 5000)
r.count_weight()

# 3
p = Position("Вася", "Пупкин", "Погромист", 35000, 5000)
print(p.get_full_name())
print(p.get_total_income())

# 4
for car in [Car("Volga", "black"), PoliceCar("UAZ Patriot", "white"), TownCar("KIA Rio", "blue"), WorkCar("Kamaz", "orange")]:
    print(car.name, car.color)
    car.show_speed()
    car.go()
    car.show_speed()
    car.stop()
    car.show_speed()
    car.speed = 300
    car.show_speed()
    print()

# 5
for stat in [Pen("Pilot"), Pencil("Maped"), Handle("Brauberg")]:
    stat.draw()
