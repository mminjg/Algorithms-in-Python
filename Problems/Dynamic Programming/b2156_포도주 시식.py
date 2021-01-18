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

for i in range(3, n + 1):
    # x o o / x o / x
    dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])

print(dp[n])

# 계단 오르기