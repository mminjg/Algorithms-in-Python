import sys
import math
input = sys.stdin.readline

k = int(input())

cnt = 0
while True:
    flag = False
    for i in range(2, k+1):
        if k % i == 0:
            flag = True
            cnt += 1
            k //= i
            break
    if not flag:
        break

if cnt == 0:
    print(0)
    exit()

print(math.ceil(math.log(cnt, 2)))