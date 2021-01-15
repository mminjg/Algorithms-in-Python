import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 0으로 초기화
d = [0] * (k + 1)
d[0] = 1

# 화폐별 탐색
for i in range(n):
    # 경우의 수를 구하는 것이므로, 화폐 단위만큼의 이전 값을 현재에 더해 줌
    for j in range(arr[i], k + 1):
        d[j] += d[j - arr[i]]

print(d[k])