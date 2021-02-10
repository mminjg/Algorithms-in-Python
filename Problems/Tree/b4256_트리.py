import sys
input = sys.stdin.readline

def go(pl, pr, il, ir):
    if pl == pr:
        print(preorder[pl], end=' ')
        return
    for i in range(pr-pl+1):
        if preorder[pl] == inorder[il + i]:
            # 왼쪽 부분
            go(pl+1, pl+i, il, il+i-1)
            # 오른쪽 부분
            go(pl+i+1, pr, il+i+1, ir)
            print(preorder[pl], end=' ')
            return

t = int(input())
for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    go(0, n-1, 0, n-1)
    print()