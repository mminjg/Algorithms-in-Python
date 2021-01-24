import bisect

# 값이 [left_val, right_val] 데이터의 개수를 반환하는 함수
def count_by_range(a, left_val, right_val):
    right_index = bisect.bisect_right(a, right_val)
    left_index = bisect.bisect_left(a, left_val)
    return right_index - left_index

arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []

    # 단어의 길이별로 저장, ?가 접미사냐 접두사냐에 따라 저장한다.
    # 접두사인경우 뒤집어서 저장한다.
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    
    # 이진 탐색을 위해 각 길이별 단어 리스트를 정렬한다.
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for x in queries:
        if x[0] != '?':
            # ___a ~ ___z 까지의 단어 갯수를 찾음
            result = count_by_range(arr[len(x)], x.replace('?', 'a'), x.replace('?', 'z'))
        else:
            result = count_by_range(reversed_arr[len(x)], x[::-1].replace('?', 'a'), x[::-1].replace('?', 'z'))

        answer.append(result)

    return answer