import sys
input = sys.stdin.readline

def solution(s):
    result = []
    arr = []
    n = len(s)

    if n == 1:
        return [s]

    start, end = 0, 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            end = i
        else:
            if start < end:
                arr.append((start, end))
            start = i
    if start < end:
        arr.append((start, end))

    # print(arr)

    b = arr[0][0]
    result.append(s[0:b])
    a = arr[0][1]
    for i in range(1, len(arr)):
        b = arr[i][0]
        result.append(s[a+1:b])
        a = arr[i][1]
    result.append(s[a+1:n+1])

    return result

# 대략 이런식으로 풀었던 것 같은데▪▪ 예외처리 어떻게 했는지 기억이 안나요

example = ["pizza", "mississippi", "aabcddddefggg", "abyyy", "kkkkkk"]
for ex in example:
    print(solution(ex))
