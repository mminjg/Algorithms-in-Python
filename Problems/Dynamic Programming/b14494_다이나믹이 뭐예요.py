import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 맨 위의 행과 왼쪽 열의 경우의 수는 1이다.
for i in range(1, n + 1):
    dp[i][1] = 1

for j in range(1, m + 1):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(2, m + 1):
        # →, ↓, ↘ 에서 오는 경우의 수를 모두 더한다.
        dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]) % 1000000007

print(dp[n][m])