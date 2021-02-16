n = int(raw_input())
num_arr = []
for i in range(n):
	num_arr.append(int(raw_input()))

num_arr.sort()

m = 0
a = num_arr[0]
for i in range(1, n):
	b = num_arr[i]
    # 덧셈할 때 float
	m = float(a + b) / 2
	a = m

# 소수점 6째 자리까지
print('%.6f' % m)