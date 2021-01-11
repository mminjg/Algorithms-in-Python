import sys

n = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

count = 0

while True:
    zero = True # 모든 원소가 0인지
    even = True # 0이 아닌 모든 수가 짝수인지

    for i in range(n):
        if B[i] != 0:
            zero = False
        if B[i] % 2 != 0:
            B[i] -= 1
            count += 1
            even = False

    if zero:
        break

    if even:
        for i in range(n):
            B[i] //= 2
        count += 1

print(count)