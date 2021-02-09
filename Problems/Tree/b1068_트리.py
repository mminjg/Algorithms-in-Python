import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.parent = None
        self.child = []

def dfs(v):
    global cnt
    if v == remove_node:
        if len(tree[tree[v].parent].child) == 1:
            cnt += 1
        return
    if not tree[v].child:
        cnt += 1
        return
    for c in tree[v].child:
        dfs(c)

n = int(input())
par = list(map(int, input().split()))
remove_node = int(input())

tree = [0] * n
root = 0
cnt = 0

# 트리 초기화
for i in range(n):
    tree[i] = Node()

for i in range(n):
    tree[i].parent = par[i]
    if par[i] == -1:
        root = i
    else:
        tree[par[i]].child.append(i)

dfs(root)
print(cnt)