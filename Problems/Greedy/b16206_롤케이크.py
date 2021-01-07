import sys

n, m = map(int, sys.stdin.readline().split())
cakes = list(map(int, sys.stdin.readline().split()))
cakes.sort()
num = 0

i = 0
while i < n and m > 0:
    if cakes[i] == 10:
        num += 1
    i += 1

i = 0
while i < n and m > 0:
    if cakes[i] == 20:
        m -= 1
        num += 2
    i += 1

# 20보다 큰 10의 배수인 경우
i = 0
while i < n and m > 0:
    if cakes[i] % 10 == 0 and cakes[i] > 20:
        c = cakes[i] // 10
        while m > 0 and c > 1:
            if c == 2:
                num += 2
            else:
                num += 1
            m -= 1
            c -= 1
    i += 1

# 10의 배수가 아닌 경우
i = 0
while i < n and m > 0:
    if cakes[i] % 10 != 0:
        c = cakes[i] // 10
        while m > 0 and c > 0:
            num += 1
            m -= 1
            c -= 1
    i += 1

print(num)