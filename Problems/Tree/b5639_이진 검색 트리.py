import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def postorder(s, e):
    if s > e:
        return
    div = e + 1
    for i in range(s+1, e+1):
        if tree[s] < tree[i]:
            div = i
            break

    postorder(s+1, div-1)
    postorder(div, e)
    print(tree[s])

tree = []
cnt = 0
while True:
    try:
        data = int(input())
    except:
        break
    tree.append(data)

postorder(0, len(tree)-1)