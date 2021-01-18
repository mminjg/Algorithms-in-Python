import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    arr[i] = int(input())

dp[1] = arr[1]
if n == 1:
    print(dp[1])
    exit(0)

dp[2] = dp[1] + arr[2]
if n == 2:
    print(dp[2])
    exit(0)

# n이 1 or 2일 때, 인덱스 에러
for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + arr[i - 1], dp[i - 2]) + arr[i]

print(dp[n])

# 포도주 시식