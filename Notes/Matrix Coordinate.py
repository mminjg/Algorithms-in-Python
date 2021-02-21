# 좌상 대각선 \
# i - j 가 일치

# 우상 대각선 /
# i + j 가 일치

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0]*n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# [1] x, y 따로
# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y = 0, 0

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

# [2] x, y 같이
# 이동할 방향 담은 리스트
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0
for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if next_x < 1 or next_x > 8 or next_y < 1 or next_y > 8:
        continue
    cnt += 1