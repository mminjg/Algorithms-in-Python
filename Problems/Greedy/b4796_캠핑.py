import sys

case = 0
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l == 0:  # case가 더이상 없으면 종료한다.
        break

    case += 1
    days = 0

    days += v // p * l  # v일 휴가 // 연속하는 p일 * l일 동안 사용

    if v % p <= l:  # v일 휴가를 p로 나누고 남은 휴가가 l일 보다 작을 때 더해준다
        days += v % p
    else:
        days += l
    print("Case "+str(case)+": "+str(days))