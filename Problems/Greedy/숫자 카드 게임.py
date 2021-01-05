# 문제 : 숫자 카드가 n*m 형태로 놓여있다.
# 행 안에 가장 숫자가 낮은 카드, 최종적으로는 가장 높은 숫자의 카드를 뽑아야 한다.

import sys
n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    mv = min(tmp)
    result = max(result, min(tmp))

print(result)