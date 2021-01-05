# 문제 : 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙을 큰 수의 법칙이라 한다.
# 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

# 단순 풀이 1
import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
first = arr[n - 1]
second = arr[n - 2]

sum = 0
# while True:
#     for _ in range(k):
#         if m == 0:
#             break
#         sum += first
#         m -= 1
#
#     if m == 0:
#         break
#     sum += second
#     m -= 1
#
# print(sum)

# 반복되는 수열 이용
count = int(m / (k + 1)) * k  # 가장 큰 수 횟수
count += m % (k + 1)

sum += count * first
sum += (m - count) * second

print(sum)