import sys
import heapq
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0:
        # 파이썬의 기본 힙은 최소힙, 따라서 -로 부호 바꾸어서 힙에 넣어준다.
        heapq.heappush(q, -x)
    else:
        if q:
            # 다시 부호를 바꾸어 출력한다.
            print(-heapq.heappop(q))
        else:
            print(0)
