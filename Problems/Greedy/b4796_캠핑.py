import sys

case = 0
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l == 0:
        break

    case += 1
    days = 0

    days += v // p * l

    if v % p <= l:
        days += v % p
    else:
        days += l
    print("Case "+str(case)+": "+str(days))