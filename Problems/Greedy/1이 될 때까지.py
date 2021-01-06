# 문제: 다음 두 과정 중 하나를 반복적으로 선택하여 수행
# 1. n에서 1을 뺀다
# 2. n을 k로 나눈다. 단, n이 k로 나누어 질 때만 선택 할 수 있다.

import sys
n, k = map(int, sys.stdin.readline().split())

count = 0
while n != 1:
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n = n - 1
        count += 1

# while True:
#     target = (n // k) * k
#     count += (n - target)
#     n = target
#
#     if n < k:
#         break
#     count += 1
#     n //= k
#
# count += (n - 1)
#
# print(count)
