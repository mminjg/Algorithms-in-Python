import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    land_idx = []   # 인구 이동할 땅의 인덱스를 저장하는 리스트
    move = False    # 인구 이동 발생 했는지 체크하는 boolean

    land_idx.append((x, y))
    queue = deque()
    queue.append((x, y))
    union[x][y] = True
    people = A[x][y]    # 연합 인구수
    land = 1            # 연합을 이루고 있는 칸의 개수

    # bfs
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상하좌우 인접 나라 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            dif = abs(A[x][y] - A[nx][ny])  # 인구 차이 계산
            # 인구 차이가 l과 r 사이고 다른 연합이 아니라면
            if l <= dif <= r and not union[nx][ny]:
                # 연합에 추가
                union[nx][ny] = True
                queue.append((nx, ny))
                people += A[nx][ny]
                land += 1
                land_idx.append((nx, ny))
                move = True #인구 이동 체크

    # 인구 이동이 없는 경우 False 리턴
    if not move:
        return move

    # 연합 인구 이동
    change = people // land
    for x, y in land_idx:
        A[x][y] = change
    # 인구 이동이 있는 경우 True 리턴
    return move

n, l, r = map(int, input().split())
A = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    A[i] = list(map(int, input().split()))

cnt = 0     # 인구 이동 횟수
# 더 이상 인구 이동이 없을 때까지 지속한다.
while True:
    flag = True     # 인구 이동이 없는 경우
    union = [[False] * n for _ in range(n)] # 연합, 고려한 나라인지 체크할 리스트

    for i in range(n):
        for j in range(n):
            # 연합이 아닌 경우, 고려하지 않은 나라인 경우 bfs진행
            if not union[i][j]:
                if bfs(i, j):
                    flag = False    # 인구 이동 check

    # 하루 동안 인구 이동이 없는 경우 종료
    if flag:
        break
    # 하루 동안 인구 이동이 있는 경우 증가
    else:
        cnt += 1
print(cnt)

# 날짜가 까다로운 문제.. 하루 동안은 연합<- 이 중요..