import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

count = 0
# 내 풀이
# i = 0
# while i < n:
#     flag = True
#     for j in range(arr[i]):
#         if i+j >= n or arr[i+j] > arr[i]:
#             flag = False
#     if flag:
#         count += 1
#         i += arr[i]
#     else:
#         i += 1

cur = 0     # 현재 그룹 인원
for i in arr:
    cur += 1
    if cur >= i:
        count += 1
        cur = 0

print(count)