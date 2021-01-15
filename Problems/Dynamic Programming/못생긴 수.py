import sys
input = sys.stdin.readline

dp = [0] * 1001
dp[0] = 1

n = int(input())

i2 = i3 = i5 = 0
nxt2, nxt3, nxt5 = 2, 3, 5

# 각 숫자별 인덱스 설정
for i in range(1, n):
    dp[i] = min(nxt2, nxt3, nxt5)
    if dp[i] == nxt2:
        i2 += 1
        nxt2 = dp[i2] * 2
    if dp[i] == nxt3:
        i3 += 1
        nxt3 = dp[i3] * 3
    if dp[i] == nxt5:
        i5 += 1
        nxt5 = dp[i5] * 5

print(dp[n - 1])