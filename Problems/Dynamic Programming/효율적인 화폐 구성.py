import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 화폐구성이 가능하지 않음으로 초기화
d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(arr[i], m + 1):
        # (현재값 - 화폐단위)원을 만드는 방법이 존재하는 경우
        if d[j - arr[i]] != 10001:
            # 최소한의 화폐 개수를 찾아야 함으로 min을 통해 비교한다
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])