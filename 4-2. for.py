# 반복문

# 대기번호를 부여하는 프로그램을 만든다 가정
from random import randrange


print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")
# 이렇게 해도 되지만 대기번호가 너무 많으면?


# 아래와 같이 for문을 사용해 코드를 줄일 수 있다.
for waiting_no in [0, 1, 2, 3, 4]:
# [0, 1, 2, 3, 4]라는 범위의 리스트를
# 'waiting_no'라는 함수에 순서대로 처리
	print("대기번호 : {0}".format(waiting_no))
# 실행 결과는
# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4 이렇게 나온다.

# randrange()를 응용
for waiting_no in randrange(5): # 0, 1, 2, 3, 4
# 1,2,3,4,5 까지만 출력하고 싶다면?
# for waiting_no in randrange(1,6): <- 이렇게
	print("대기번호 : {0}".format(waiting_no))