import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    global ans
    # 최대 칸 업데이트
    ans = max(ans, cnt)
    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 보드 벗어난 경우
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
             continue
        # 아직 사용한 알파벳이 나닌 경우
        if not alpha[ord(graph[nx][ny])-ord('A')]:
            # 알파벳 사용 체크
            alpha[ord(graph[nx][ny]) - ord('A')] = True
            # dfs
            dfs(nx, ny, cnt+1)
            # 알파벳 사용 체크 다시 돌리기
            alpha[ord(graph[nx][ny]) - ord('A')] = False

r, c = map(int, input().split())
graph = [[] for _ in range(r)]  # 그래프 초기화
alpha = [False] * 26    # 사용한 알파벳 사용 표시 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력
for i in range(r):
    graph[i] = list(input().rstrip())

ans = 0
alpha[ord(graph[0][0])-ord('A')] = True
dfs(0, 0, 1)
print(ans)