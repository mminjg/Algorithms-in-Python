import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 가중치, 현재위치, 전 위치
def solve(w, cur, pre=-1):
    global ans, x
    if ans < w:
        ans = w
        x = cur

    for t in tree[cur]:
        next = t[0]
        d = t[1]
        if next == pre:
            continue
        solve(w + d, next, cur)

n = int(input())
tree = [[] for _ in range(n + 1)]
ans = 0
x = 1

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

solve(0, 1)
solve(0, x)

print(ans)