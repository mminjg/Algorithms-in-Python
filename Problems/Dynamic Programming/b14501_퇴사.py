import sys
input = sys.stdin.readline

n = int(input())

T = [0] * n
P = [0] * n
dp = [0] * (n + 1)

for i in range(n):
    T[i], P[i] = map(int, input().split())

for i in range(n):
    t, p = T[i], P[i]
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)
    dp[i + 1] = max(dp[i + 1], dp[i])

print(max(dp))
