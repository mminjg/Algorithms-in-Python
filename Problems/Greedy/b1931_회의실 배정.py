import sys

n = int(sys.stdin.readline())

meeting = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0]))    # 끝나는 시간 -> 시작하는 시간 기준 정렬

cur_s, cur_e = meeting[0][0], meeting[0][1]

count = 1
for i in range(1, n):
    next_s, next_e = meeting[i][0], meeting[i][1]
    if next_s >= cur_e:
        cur_s, cur_e = next_s, next_e
        count += 1

print(count)