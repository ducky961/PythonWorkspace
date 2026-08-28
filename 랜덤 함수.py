from random import * # 라이브러리에서 random 함수에 대한 정보를 참조

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 미만의 임의의 값 생성
# 좀 더 쉽게
print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 값 생성
print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성