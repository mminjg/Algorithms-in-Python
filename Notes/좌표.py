# 좌상 대각선 \
# i - j 가 일치

# 우상 대각선 /
# i + j 가 일치


# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(4):

    nx = x + dx[i]
    ny = y + dy[i]