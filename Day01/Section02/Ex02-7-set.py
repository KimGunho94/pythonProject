'''
파일명: Ex-02-7-set.py

set
    순서가 없다
    변경할 수 없다
    인덱싱되지 않는 컬렉션
'''

thisset = {"피카츄", "라이츄", "파이리"}
# 실행할 때 마다 순서 변경
print(thisset)


# 항목 가져오기
thisset = {"피카츄", "라이츄", "파이리"}
for x in thisset:
    print(x)

# 값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬부기" in thisset)

# 항목 추가하기 (set 에서는 .add로 추가 하기)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.add("꼬부기")
print(thisset)
print("꼬부기" in thisset)

# 다른 Set의 항목 추가 (.update 로 추가 하며 중복값은 허용하지 않는다.)
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

# 항목 제거 (.remone 로 항목을 지울수 있다.)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
# thisset.remove("피카츄")
# print(thisset)
# (.discard 로 없는 값을 지워도 에러가 나지 않는다.)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)

# 항목 제거 (랜덤으로 항목을 지운다.)
thisset.pop()

# 비우기
thisset.clear()
print(thisset)