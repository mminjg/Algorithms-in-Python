import sys
input = sys.stdin.readline

def solution(n, m):
    day = 0
    cnt = 1
    while n > 0:
        if cnt == m:
            cnt = 1
            n += 1
        else:
            cnt += 1
        n -= 1
        day += 1
    return day

n, m = map(int, input().split())
print(solution(n, m))
