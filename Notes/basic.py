# sys를 이용한 input
import sys

# 정수 입력
n = int(sys.stdin.readline())
# 문자열 입력, 마지막 \n 제거 필요
data = sys.stdin.readline().rstrip()
# 정수 리스트
arr = list(map(int, sys.stdin.readline().split()))


# 1차원 리스트 0으로 초기화 [0, 0,  ... , 0]
arr = [0] * n
# 1차원 리스트 i값으로 초기화 [0, 1, 2, 3, .. 9]
arr = [ i for i in range(10)]   # == list(range(10), list(range(0, 10)
# 1차원 리스트에 입력값 넣기
for i in range(n):
    arr[i] = int(sys.stdin.readline())  # append로 초기화 하는 것보다 빠르다

# 2차원 리스트 초기화 [[0, 0], [0, 0], [0, 0]]
arr = [[0] * 2 for _ in range(3)]   # == [[0 for j in range(2)] for i in range(3)]


# 리스트 정렬
a = [1, 10, 4, 7, 3]
a.sort()
a.sort(reverse=True)    # 내림차순
s = ['가', '나다', '라', '마바아자', '차카파']
s.sort(key=len) # len에 따라 정렬


# 반복되는 수열
M= 8; K=3
int(M / (K + 1)) * K + M % (K + 1)

# itertools
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
data = ['a','b','c']

# 모든 순열 구하기
result = list(permutations(data,3))
# 모든 조합 구하기
result = list(combinations(data, 3))
# 중복 순열 구하기
result = list(product(data, repeat=2)) # 2개 뽑는 모든 순열 (중복 허용)
# 중복 조합 구하기
result = list(combinations_with_replacement(data, 2)) # 2개 뽑는 모든 조합 (중복 허용)