import sys
input = sys.stdin.readline

dc = dict()
arr = []
n = int(input())

for i in range(n):
    dc[input().rstrip()] = i

for i in range(n):
    arr.append(dc[input().rstrip()])

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            cnt += 1
            break

print(cnt)