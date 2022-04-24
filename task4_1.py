from sys import argv
# 1
work_hours, salary, prize = map(int, argv[1:])
print(work_hours*salary+prize)
