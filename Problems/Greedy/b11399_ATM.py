import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

time = 0
for i in range(n):
    for j in range(i+1):
        time += arr[j]

print(time)