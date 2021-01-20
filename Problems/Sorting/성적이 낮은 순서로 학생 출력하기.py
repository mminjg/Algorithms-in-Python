import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    name, score = map(str, input().split())
    arr.append((name, int(score)))

arr = sorted(arr, key=lambda x: x[1])

for x in arr:
    print(x[0], end=' ')