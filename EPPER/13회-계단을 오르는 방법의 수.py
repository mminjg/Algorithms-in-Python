n = int(input("계단의 수를 입력하시오 : "))
dp = [0] * 100001

dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
	dp[i] = dp[i-1] + dp[i-2]

print("계단 오르는 방법의 수 : "+str(dp[n]))