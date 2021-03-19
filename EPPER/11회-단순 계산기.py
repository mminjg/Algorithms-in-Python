def solution(num_arr, n):
    num_arr.sort()

    b = num_arr[0]
    for i in range(1, n):
        m = (num_arr[i] + b) / 2
        b = m

    return m


n = int(input())
num_arr = []
for i in range(n):
    num_arr.append(int(input()))

answer = solution(num_arr, n)
print('%.6f' % answer)