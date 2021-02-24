import sys
input = sys.stdin.readline

# 유클리드 호제, 최대 공약수
def gcd(a, b):
    while b:
        c = a % b
        a = b
        b = c
    return a

n, m = map(int, input().split(":"))

if n > m:
    k = gcd(n, m)
else:
    k = gcd(m, n)
print(str(n//k)+":"+str(m//k))