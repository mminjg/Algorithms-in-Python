n = int(input())
money = list(map(int, input().split()))

dp = [0] * (n+1)

if n == 1:
    print(money[0])
    exit()
elif n == 2:
    print(money[0] + money[1])
    exit()

dp[1] = money[0]
dp[2] = dp[1] + money[1]
for i in range(3, n+1):
    dp[i] = max(dp[i - 2] + money[i - 1], dp[i - 3] + money[i - 2] + money[i - 1], dp[i - 1])
print(dp[n])

# 최대 연속된 2개까지 가능, 3개부터 불가능
# i-3  i-2  i-1  i
#  O    X    O   O
#       O    X   O
#            O   X
