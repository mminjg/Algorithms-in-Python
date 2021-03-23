import sys
input = sys.stdin.readline

def eureka(target):
    for i in range(1, 45):
        for j in range(1, 45):
            for k in range(1, 45):
                if T[i] + T[j] + T[k] == target:
                    return 1
    return 0

T = [0] * 45
for i in range(1, 45):
    T[i] = i * (i + 1) // 2

tc = int(input())
for _ in range(tc):
    k = int(input())
    print(eureka(k))
