import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(v, i):
    if i == m:
        tmp.append(v)
        return

    if seq[i] == 'L':
        dfs(graph[v][0], i+1)
    if seq[i] == 'R':
        dfs(graph[v][1], i+1)

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    left, right = map(int, input().split())
    graph[i].append(left)
    graph[i].append(right)

seq = list(input().rstrip().split())

tmp = [0]
for i in range(1, n+1):
    dfs(i, 0)

idx = tmp[1]
s = tmp[1]
for _ in range(k-1):
    s = tmp[idx]
    idx = s
print(s)
