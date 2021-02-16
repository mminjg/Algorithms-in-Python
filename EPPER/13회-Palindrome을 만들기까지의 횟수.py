def solution(arr, start, end):
    answer = 0
    while True:
        if start + 1 == end:
            break
        elif arr[start] < arr[end]:
            arr[start + 1] += arr[start]
            start += 1
            answer += 1
        elif arr[end] < arr[start]:
            arr[end - 1] += arr[end]
            end -= 1
            answer += 1
        else:
            start += 1
            end -= 1
    return answer


n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1

print(solution(arr, start, end))