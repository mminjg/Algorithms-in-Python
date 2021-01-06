import sys

s = sys.stdin.readline().rstrip()

count0 = 0  # 0으로 바꾸는 횟수
count1 = 0  # 1로 바꾸는 횟수

if s[0] == '1':
    count1 += 1
else:
    count0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count1 += 1
        else:
            count0 += 1

print(min(count1, count0))