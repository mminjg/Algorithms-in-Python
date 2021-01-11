import sys

n, k = map(int, sys.stdin.readline().split())

coin = [0] * n
for i in range(n):
    coin[i] = int(sys.stdin.readline())

# Ai가 Ai-1의 배수 -> 내림차순으로 구하기
count = 0
i = n - 1
while i >= 0 and k > 0:
    count += (k // coin[i])
    k = k % coin[i]
    i -= 1

print(count)