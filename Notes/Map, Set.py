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