# *
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

target = 1
for i in arr:
    if i > target:  # 다음 화폐가 target 보다 크다면 target을 만들 수 없다
        break
    target += i

print(target)