import sys
input = sys.stdin.readline

d = [0] * 251

d[0] = 1
d[1] = 1
d[2] = 3

for i in range(3, 251):
    d[i] = d[i - 1] + d[i - 2] * 2

while True:
    try:
        n = int(input())
    except:
        break
    print(d[n])