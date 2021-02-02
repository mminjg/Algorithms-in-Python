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

max_value = 0   # 얼음들의 합(최댓값)
temp = 0    # 얼음들의 합(범위 안 임시값)
# 슬라이딩 윈도우 방법
for x in range(max_x + 1):  # 엘버트의 좌표 이동
    # 엘버트가 닿을 수 있는 거리보다 큐가 작으면 그 좌표의 얼음추가 가능
    if len(queue) < 2 * k + 1:
        queue.append(arr[x])
        temp += arr[x]
        max_value = temp
    else:
        temp -= queue.popleft()
        queue.append(arr[x])
        temp += arr[x]
        if temp > max_value:
            max_value = temp

print(max_value)

# 슬라이딩 윈도우, 투포인터, 큐