import sys
input = sys.stdin.readline

def go(cnt, seq):
    if cnt == m:    # 길이가 m이면 종료
        print(seq)
        return

    for i in range(1, n + 1):
        if not visit[i]:
            visit[i] = True
            go(cnt + 1, seq + str(i) + ' ')
            visit[i] = False

n, m = map(int, input().split())
visit = [False] * (n + 1)
go(0, '')
