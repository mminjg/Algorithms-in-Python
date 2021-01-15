arr = [10, 20, 10, 30, 20, 50]
# answer = [10, 20, 30, 50]

# 1  1  1  1  1  1      초기 상태
# 1  2  1  1  1  1      i = 1
# 1  2  1  1  1  1      i = 2
# 1  2  1  3  1  1      i = 3
# 1  2  1  3  2  1      i = 4
# 1  2  1  3  2  4      i = 5

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)