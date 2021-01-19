import sys
input = sys.stdin.readline

def go(idx, cnt):
    # 수열의 길이가 m이면 print 하고 종료한다.
    if cnt == m:
        for x in seq:
            print(x, end=" ")
        print()
        return

    # 이전과 같은 숫자인지 확인을 위한 pre_num 초기화
    pre_num = 0
    for i in range(n):
        # i번째 숫자를 방문하지 않았거나 전과 같은 숫자가 아니라면 추가한다.
        if not (visit[i] or pre_num == arr[i]):
            visit[i] = True     # 방문 표시
            seq[cnt] = arr[i]   # 수열에 숫자 추가
            pre_num = arr[i]    # 이전 숫자로 등록
            go(idx + 1, cnt + 1)    # 다음으로
            visit[i] = False    # 방문 표시 제거


n, m = map(int, input().split())
arr = list(map(int, input().split()))
visit = [False] * n
seq = [0] * m
arr.sort()
go(0, 0)