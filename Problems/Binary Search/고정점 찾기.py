import sys
input = sys.stdin.readline

def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            return binary_search(arr, mid + 1, end)
        else:
            return binary_search(arr, start, mid - 1)
    return None

n = int(input())
arr = list(map(int, input().split()))

index = binary_search(arr, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)

