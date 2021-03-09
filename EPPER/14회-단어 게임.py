def solution(arr1, arr2):
    answer = []
    words = [[] for _ in range(26)] # 각 알파벳으로 시작하는 단어를 저장할 배열
    cnt = [0] * 26  # 각 알파벳으로 시작하는 단어가 등장한 횟수를 저장하는 배열

    # 알파벳 순
    arr1.sort()

    # 각 알파벳으로 시작하는 단어를 words에 저장
    for i in range(k):
        word = arr1[i]
        words[ord(word[0]) - ord('a')].append(word)

    # cnt % 각 알파벳 배열의 길이를 이용하여 최소 횟수 선택
    for i in range(n):
        first = ord(arr2[i]) - ord('a')
        c = cnt[first]
        answer.append(words[first][c % len(words[first])])
        cnt[first] += 1

    return answer

k, n = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(k):
    arr1.append(input().rstrip())
for _ in range(n):
    arr2.append(input().rstrip())

answer = solution(arr1, arr2)
for x in answer:
    print(x)