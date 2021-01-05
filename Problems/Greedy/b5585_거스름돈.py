import sys

arr = [500, 100, 50, 10, 5, 1]
count = 0

m = int(sys.stdin.readline())
m = 1000 - m

for coin in arr:
    count += m // coin
    m = m % coin

print(count)