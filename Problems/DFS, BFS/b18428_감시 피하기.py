import sys
from itertools import combinations
input = sys.stdin.readline

def watch(x, y):
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if tmp[nx][ny] == 'O':
                break
            check[nx][ny] = True

n = int(input())
graph = [[''] * n for _ in range(n)]
tmp = [[''] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
teacher = []
blank = []
student = []

# 입력
for i in range(n):
    graph[i] = list(map(str, input().rstrip().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))
        elif graph[i][j] == 'X':
            blank.append((i, j))
        else:
            student.append((i, j))

# 장애물을 설치하는 경우의 수
obstacle = list(combinations(blank, 3))
for ob in obstacle:
    check = [[False] * n for _ in range(n)]
    # tmp로 graph 복사
    for i in range(n):
        for j in range(n):
            tmp[i][j] = graph[i][j]
    # 장애물 3개 설치
    for x, y in ob:
        tmp[x][y] = 'O'
    # 선생님 감시
    for x, y in teacher:
        watch(x, y)
    # 감시 피했는지 확인
    result = True
    for x, y in student:
        if check[x][y]:   # 들켰다면
            result = False
    if result:
        print('YES')
        exit(0)

print('NO')

# 조합 라이브러리로 구현