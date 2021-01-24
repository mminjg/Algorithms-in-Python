def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 인덱스 반환
    if arr[mid] == target:
        return mid
    # 중간값보다 target이 작은 경우 왼쪽 부분 확인
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    # 중간값보다 target이 큰 경우 오른쪽 부분 확인
    else:
        return binary_search(arr, target, mid + 1, end)

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 인덱스 반환
        if arr[mid] == target:
            return mid
        # 중간값보다 target이 작은 경우 왼쪽 부분 확인
        elif arr[mid] > target:
            end = mid - 1
        # 중간값보다 target이 큰 경우 오른쪽 부분 확인
        else:
            start = mid + 1
    return None

import bisect
def count_by_range(a, left_value, right_value):
    right_index = bisect.bisect_right(a, right_value)
    left_index = bisect.bisect_left(a, left_value)
    return right_index - left_index