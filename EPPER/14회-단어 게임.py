k, n = map(int, input().split())
words = [[] for _ in range(26)]
cnt = [0] * 26

arr = []
for _ in range(k):
    arr.append(input().rstrip())
arr.sort()

for i in range(k):
    word = arr[i]
    words[ord(word[0]) - ord('a')].append(word)

for _ in range(n):
    first = ord(input()) - ord('a')
    c = cnt[first]
    print(words[first][c % len(words[first])])
    cnt[first] += 1
