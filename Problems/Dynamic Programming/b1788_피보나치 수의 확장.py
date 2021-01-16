import sys
input = sys.stdin.readline

n = int(input())
m = abs(n)
dp = [0] * 1000001

dp[0] = 0
dp[1] = 1

for i in range(2, m + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000

if n == 0:
    print(0)
elif n > 0:
    print(1)
else:
    if m % 2 == 0:
        print(-1)
    else:
        print(1)
print(dp[m])