def solution(arr, start, end):
    answer = 0
    while True:
        # start와 end가 겹치는 경우 종료
        if start + 1 == end:
            break
        # start가 더 작은 경우
        elif arr[start] < arr[end]:
            arr[start + 1] += arr[start]
            start += 1
            answer += 1
        # end가 더 작은 경우
        elif arr[end] < arr[start]:
            arr[end - 1] += arr[end]
            end -= 1
            answer += 1
        # 같은 경우
        else:
            start += 1
            end -= 1
    return answer


n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1

print(solution(arr, start, end))