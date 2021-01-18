import sys
input = sys.stdin.readline

def go(cnt, st, seq):
    if cnt == m:
        print(seq)
        return

    for i in range(st, n + 1):
        if not visit[i]:
            visit[i] = True
            go(cnt + 1, i + 1, seq + str(i) + ' ')
            visit[i] = False

n, m = map(int, input().split())
visit = [False] * (n + 1)
go(0, 1, '')
