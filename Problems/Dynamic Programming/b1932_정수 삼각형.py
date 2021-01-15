import sys
input = sys.stdin.readline

n = int(input())
dp = [] * n
for i in range(n):
    dp.append(list(map(int, input().split())))

# 양쪽 끝 계산
for i in range(1, n):
    dp[i][0] += dp[i - 1][0]
    dp[i][-1] += dp[i - 1][-1]

for i in range(2, n):
    for j in range(1, len(dp[i]) - 1):
        dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n - 1]))