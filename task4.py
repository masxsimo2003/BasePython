from functools import reduce

# 2
# s = list(map(int, input().split()))
s = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
t = [s[i + 1] for i in range(len(s) - 1) if s[i] < s[i + 1]]
print(t)

# 3
t = [i + i // 20 * x for i in range(20, 241, 20) for x in [0, 1]]
print(t)

# 4
# s = list(map(int, input().split()))
s = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
t1 = [i for i in s if s.count(i) == 1]

# 5
s = [i for i in range(100, 1001, 2)]
t = reduce(lambda x, y: x * y, s)
print(t)


# 7
def fact(n):
    if n == 0:
        return (1, )
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


# n = int(input())
n = 7
for i in fact(n):
    print(i)
