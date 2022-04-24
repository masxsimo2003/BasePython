from itertools import cycle


def my_cycle():
    s = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    x = 0
    for i in cycle(s):
        if x > 30:
            break
        else:
            print(i)
            x += 1


my_cycle()
