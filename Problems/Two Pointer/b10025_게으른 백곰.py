import sys
from collections import deque
input = sys.stdin.readline

arr = [0] * 1000001     # arr[i] = 좌표가 i일때의 얼음 g
n, k = map(int, input().split())
queue = deque()

max_x = 0   # 좌표 최대값
for i in range(n):
    g, x = map(int, sys.stdin.readline().split())
    arr[x] = g
    if x > max_x:
        max_x = x

max_value = 0   # 얼음들의 최대합
temp = 0    # 범위 안의 임시 얼음들의 합
# 슬라이딩 윈도우 방법
for x in range(max_x + 1):  # 엘버트의 좌표 이동
    # 엘버트가 닿을 수 있는 거리보다 큐의 크기가 작으면 현재 좌표의 얼음 추가
    if len(queue) < 2 * k + 1:
        queue.append(arr[x])
        temp += arr[x]
        max_value = temp
    # 큐에서 pop한만큼 얼음의 임시 합에서 빼주고, 현재 좌표의 얼음추가
    else:
        temp -= queue.popleft()
        queue.append(arr[x])
        temp += arr[x]
        if temp > max_value:    # 얼음들의 최대합 업데이트
            max_value = temp

print(max_value)

# 슬라이딩 윈도우, 투포인터, 큐