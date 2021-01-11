import sys

n = int(sys.stdin.readline())

count = 0
while n > 2:
    if n % 5 == 0:
        count += n // 5
        n = 0
        break
    n -= 3
    count += 1

if n > 0:
    count = -1

print(count)