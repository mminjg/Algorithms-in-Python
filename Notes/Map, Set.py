x = list(int, input().split())

# 있는지
if 2 in x:

dc = dict()
# [] 사용하면, 해시 테이블에 없는 key 를 검색할 경우 오류
dc["AAA"]

# 테이블에 없는 key면 None 반환
dc.get("AAA")

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