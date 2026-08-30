#quiz 2
#당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 
#오프라인으로 하기로 했습니다.

#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
#조건 1 : 랜덤으로 날짜를 뽑아야 함
#조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

#출력문 예제
#오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import *

date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

#quiz 3
#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
#예시 : http://naver.com
#규칙 1 : http:// 부분은 제외 => naver.com
#규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

#예시 : 생성된 비밀번호 : nav51!

# 내가 쓴 풀이
site = "http://naver.com"
print(site[-9:-4]) 
site = site[-9:-4]
print(site[:3]+str(len(site))+str(site.count("e"))+"!")

# 강사님 풀이
url = "http://naver.com"
my_str = url.replace("http://","") # 규칙 1 수행
# 이 코드의 의미는 replace가 원하는 구문("http://")을 찾아서
# ("")빈칸으로 바꿈
my_str = my_str[:my_str.index(".")] # 문자열 처음부터 . 위치 직전까지 반환
# my_str[0:5] -> 0~5 직전까지 (0, 1, 2, 3, 4) 와 똑같음
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url,password))

# ai의 풀이
url = "http://naver.com"
url = url.replace("http://", "") # 규칙 1
url = url[:url.index(".")] # 규칙 2
print(url[:3] + str(len(url)) + str(url.count("e")) + "!")


# quiz 4
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle과 sample을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# 활용 예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))



# 강사님 풀이
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
# 하지만 range는 list type이 아니기 때문에
users = list(users) #리스트로 변환하면 됨

shuffle(users)

winners = sample(users, 4) # 중복 가능성이 있기 때문에 우선 4명을 먼저 추첨
# 4명 중에서 1명은 치킨, 3명은 커피


print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0])) # 먼저 추첨한 4명 중 첫번째
print("커피 당첨자 : {0}".format(winners[1:])) # 제외한 나머지
print("-- 축하합니다 --")