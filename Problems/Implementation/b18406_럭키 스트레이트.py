import sys
input = sys.stdin.readline

num = input().rstrip()
l = len(num)

s1 = 0
for i in range(l // 2):
    s1 += int(num[i])

s2 = 0
for i in range(l // 2, l):
    s2 += int(num[i])

if s1 == s2:
    print("LUCKY")
else:
    print("READY")