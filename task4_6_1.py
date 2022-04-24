from sys import argv
from itertools import count


def my_count(a):
    for i in count(a):
        if i > 30:
            break
        else:
            print(i)


my_count(int(argv[1]))
