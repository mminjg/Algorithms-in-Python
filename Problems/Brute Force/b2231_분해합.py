import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    k = i
    sum = k
    while k > 0:
        sum += k % 10
        k //= 10

    if sum == n:
        print(i)
        exit(0)

print(0)
