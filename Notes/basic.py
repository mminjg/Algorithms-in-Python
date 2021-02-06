# sys를 이용한 input
import sys
input = sys.stdin.readline

# 정수 입력
n = int(input())
# 문자열 입력, 마지막 \n 제거 필요
data = input().rstrip()
# 문자열 한 글자씩 분리해 저장
n = int(input())
words = [[list(input().rstrip())] for _ in range(n)]

arr = [[]] * n
for i in range(n):
    arr[i] = list(input().rstrip())

# 정수 리스트
arr = list(map(int, input().split()))   # 이어서
arr = [int(input()) for _ in range(n)]  # 엔터
# 1차원 리스트 0으로 초기화 [0, 0,  ... , 0]
arr = [0] * n
# 1차원 리스트 i값으로 초기화 [0, 1, 2, 3, .. 9]
arr = [ i for i in range(10)]   # == list(range(10), list(range(0, 10)
# 1차원 리스트에 입력값 넣기
for i in range(n):
    arr[i] = int(sys.stdin.readline())  # append로 초기화 하는 것보다 빠르다
# 2차원 리스트 초기화 [[0, 0], [0, 0], [0, 0]]
arr = [[0] * 2 for _ in range(3)]   # == [[0 for j in range(2)] for i in range(3)]
# 2차원 주어진 개수만큼 초기화
for i in range(n):
    arr.append(a[index:index + m])
    index += m

# 리스트 복사
import copy
arr2 = copy.deepcopy(arr)

# 리스트 정렬
a = [1, 10, 4, 7, 3]
a.sort()
a.sort(reverse=True)    # 내림차순
s = ['가', '나다', '라', '마바아자', '차카파']
s.sort(key=len) # len에 따라 정렬
k = [[1,2],[6,1],[4,9],[3,0]]
k.sort(key=lambda x: (x[1], x[0]))    # 1번째 원소, 0번째 원소 기준 정렬

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


# heapq / 파이썬의 기본 힙은 최소힙 - 오름차순
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,9,7,8,4,0])

# 최대 힙 - 내림차순
import heapq
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


# 아스키코드 <-> 문자
ord('a')
arr = [chr(i) for i in range(ord('a'), ord('z')+1)]
# 문자배열을 문자열로
print(''.join(list))