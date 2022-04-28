from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = "red"
        self.order = {"red": [7, "yellow"],
                      "yellow": [3, "green"],
                      "green": [4, "red"]}

    def running(self):
        for i in range(3):
            print(self.__color)
            delay, self.__color = self.order[self.__color]
            sleep(delay)


class Road:
    def __init__(self, length, width, weight_m=25, height=5):
        self.__length = length
        self.__width = width
        self.__weight_m = weight_m
        self.__height = height

    def count_weight(self):
        print(self.__length*self.__width*self.__weight_m*self.__height/1000, 'т')


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]


class Car:
    def __init__(self, name, color="grey"):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        self.speed = 80
        print("Going...")

    def stop(self):
        self.speed = 0
        print("Stopped!")

    def turn(self, dir):
        print(f'Turned {dir}...')

    def show_speed(self):
        print(f'Speed is {self.speed}')


class PoliceCar(Car):
    def __init__(self, name, color):
        self.is_police = True
        self.name = name
        self.color = color
        self.speed = 0


class SportCar(Car):
    def go(self):
        self.speed = 250
        print("Going...")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed is too high ({self.speed})!!!')
        else:
            print(f'Speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed is too high ({self.speed})!!!')
        else:
            print(f'Speed is {self.speed}')


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Using {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Writing with {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Drawing with {self.title}')


class Handle(Stationary):
    def draw(self):
        print(f'Drawing on a whiteboard with {self.title}')
