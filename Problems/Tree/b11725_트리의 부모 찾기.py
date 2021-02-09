import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

child = [[] for _ in range(100001)]
parent = [0] * 100001

def get_parent(idx):
    for i in child[idx]:
        if parent[i] == 0:
            parent[i] = idx
            get_parent(i)

n = int(input())
for _ in range(n-1):
    a, b = map(int, input().split())
    child[a].append(b)
    child[b].append(a)

get_parent(1)

for i in range(2, n+1):
    print(parent[i])