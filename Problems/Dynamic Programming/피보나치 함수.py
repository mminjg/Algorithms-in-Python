# 메모이제이션을 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 dp)
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산되지 않은 문제라면 점화식에 따라 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))


d = [0] * 100

# 첫 번째, 두 번째 피보나치 수 초기화
d[1] = 1
d[2] = 1
n = 6

# 피보나치 함수를 반복문으로 구현(보텀업 dp)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])