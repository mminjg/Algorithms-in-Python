import sys

input = sys.stdin.readline

n, m = map(int, input().split())

day = 0
cnt = 1
while n > 0:
    if cnt == m:
        cnt = 1
        n += 1
    else:
        cnt += 1
    n -= 1
    day += 1

print(day)
