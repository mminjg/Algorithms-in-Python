import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def preorder(v):
    print(chr(v+ord('A')), end='')
    if child_l[v] != ord('.')-ord('A'):
        preorder(child_l[v])
    if child_r[v] != ord('.')-ord('A'):
        preorder(child_r[v])

def inorder(v):
    if child_l[v] != ord('.')-ord('A'):
        inorder(child_l[v])
    print(chr(v+ord('A')), end='')
    if child_r[v] != ord('.')-ord('A'):
        inorder(child_r[v])

def postorder(v):
    if child_l[v] != ord('.')-ord('A'):
        postorder(child_l[v])
    if child_r[v] != ord('.')-ord('A'):
        postorder(child_r[v])
    print(chr(v+ord('A')), end='')

n = int(input())

child_l = [0] * 26
child_r = [0] * 26

for _ in range(n):
    v, l, r = input().split()
    child_l[ord(v)-ord('A')] = ord(l)-ord('A')
    child_r[ord(v)-ord('A')] = ord(r)-ord('A')

preorder(0)
print()
inorder(0)
print()
postorder(0)
