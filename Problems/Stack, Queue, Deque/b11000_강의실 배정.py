import sys
import heapq
input = sys.stdin.readline

room = []
q = []

n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    room.append((s, t))

room.sort(key=lambda x: x[0])

for i in range(n):
    # pq의 가장 빨리 끝나는 시간 <= 새로운 수업 시작하는 시간
    if q and q[0] <= room[i][0]:
        heapq.heappop(q)
    heapq.heappush(q, room[i][1])

print(len(q))