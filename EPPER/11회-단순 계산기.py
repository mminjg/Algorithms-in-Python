def solution(num_arr, n):
    # 선택하는 순서 정렬
    num_arr.sort()

    a = num_arr[0]
    for i in range(1, n):
        b = num_arr[i]
        m = float(a + b) / 2	# 덧셈 float
        a = m

    return m


n = int(input())
num_arr = []
for i in range(n):
    num_arr.append(int(input()))

answer = solution(num_arr, n)
print('%.6f' % answer)