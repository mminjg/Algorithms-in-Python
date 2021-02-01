import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    order = [i for i in range(n)]
    d1 = deque(arr)
    d2 = deque(order)

    cnt = 0
    flag = False
    while d1:
        if flag:
            break

        cur = d1.popleft()
        idx = d2.popleft()

        if not d1 or cur >= max(d1):
            cnt += 1
            if idx == m:
                flag = True
                print(cnt)
                break
        else:
            d1.append(cur)
            d2.append(idx)