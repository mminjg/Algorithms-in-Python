x = list(int, input().split())

dc = dict()
# [] 사용하면, 해시 테이블에 없는 key 를 검색할 경우 오류
dc["AAA"]

# 테이블에 없는 key면 None 반환
dc.get("AAA")

# 키 있는지
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
if 'health' in lux:

# 딕셔너리 수정
# 키가 문자열일 경우
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)
# x = {'a': 90, 'b': 20, 'c': 30, 'd': 40}

# 키가 숫자일 경우
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
# y = {1: 'ONE', 2: 'two', 3: 'THREE'}

# 그냥 for문 돌리면 key값 할당
for key in dc:
    print(key)
# value : values 사용
for val in dc.values():
    print(val)
# items : key와 value 둘다
for item in dc.items():
    print(item[0]) # key
    print(item[1]) # value


# List to Dict

# Dictionary Comprehension
string_list = ['A', 'B', 'C']
dictionary = {string: 0 for string in string_list}
print(dictionary)
# {'A': 0, 'B': 0, 'C': 0}
string_list = ['A', 'B', 'C']
dictionary = {i: string_list[i] for i in range(len(string_list))}
print(dictionary)
# {0: 'A', 1: 'B', 2: 'C'}

# dict.fromkeys(key, value)
string_list = ['A', 'B', 'C']
dictionary = dict.fromkeys(string_list, 0)
print(dictionary)
# {'A': 0, 'B': 0, 'C': 0}
string_list = ['A', 'B', 'C']
dictionary = dict.fromkeys(string_list)
print(dictionary)
# {'A': None, 'B': None, 'C': None}

# Two list to Dict
string_list = ['A','B','C']
int_list = [1, 2, 3]

# zip
string_list = ['A', 'B', 'C']
int_list = [1, 2, 3]
dictionary = dict(zip(string_list, int_list))
print(dictionary)
# {'A': 1, 'B': 2, 'C': 3}

# Tuple to Dict
tuple_list = [('A', 1), ('B', 2), ('C', 3)]
dictionary = dict(tuple_list)
print(dictionary)
# {'A': 1, 'B': 2, 'C': 3}

# set
s1 = set([1,2,3])
l1 = list(s1)
t1 = tuple(s1)

# 교집합
s1 & s2

# 합집합
s1 | s2

# 차집합
s1 - s2

# 추가
s1 = set([1, 2, 3])
s1.add(4)
# s1 = {1, 2, 3, 4}

# 값 여러개 추가
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
# s1 = {1, 2, 3, 4, 5, 6}

# 특정 값 제거
s1 = set([1, 2, 3])
s1.remove(2)