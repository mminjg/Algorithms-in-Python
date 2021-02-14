import sys
input = sys.stdin.readline

count = [0] * 26
word = input().rstrip()
word = word.upper()

for x in word:
    count[ord(x)-ord('A')] += 1

max_value = -1
max_index = -1
total = 0

for i in range(26):
    if count[i] > max_value:
        max_value = count[i]
        max_index = i
        total = 1

    if count[i] == max_value and max_index != i:
        total += 1

if total == 1:
    print(chr(max_index+ord('A')))
else:
    print('?')