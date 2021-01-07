# 두 사람은 서로 무게가 다른 볼링볼을 고르려 함
import sys

n, m = map(int, sys.stdin.readline().split())
balls = list(map(int, sys.stdin.readline().split()))

count = 0
# i = 0
# while i < n-1:
#     for j in range(i+1, n):
#         if balls[i] != balls[j]:
#             count += 1
#     i += 1

# 효과적인 방법: 무게마다 볼링볼 개수 계산
arr = [0] * 11
for x in balls:
    arr[x] += 1

for i in range(1, m + 1):
    n -= arr[i] # A 선택 제외
    count += arr[i] * n

print(count)
