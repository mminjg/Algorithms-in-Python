# greedy, priority queue
import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)

    sum = first + second
    heapq.heappush(heap, sum)
    result += sum

print(result)