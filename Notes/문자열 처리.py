# 문자열 뒤집기
word = 'abcd'
print(word[::-1])

# 문자 대체하기
print(word.replace('d', 'k'))
word = word.replace('d', 'k') # d를 k로
print(word)

# 인덱스 슬라이싱, 복사
word = list(word[1:-1])     # 첫번째, 마지막 문자 제거

for i in word:
    print(i)

# 문자, 아스키코드
ord('A')    # 65

# 문자열인지 true, false
s.isaplha()
# 슷자인지 true, false
s.isdigit()

# 문자열 수식 계산
exp = "(6+3)*2-(36/6)"
print(eval(exp))