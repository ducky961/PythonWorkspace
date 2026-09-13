# 지역변수 : 함수 내에서만 쓸 수 있는 변수
# 전역변수 : 프로그램 내에서 어디서든 부를 수 있는 변수

# gun = 10 

# def checkpoint(soldiers): # 경계근무
#	gun = gun - soldiers
#	print("[함수 내] 남은 총 : {0}".format(gun))
# 사실 상 checkpoint 라는 함수 내에 gun에 대한 유효한 정보가 없음

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))

# 실행 시 오류가 남
# gun이라는 함수는 할당(값이 설정)도 안되었는데 사용이 되었다고 오류남



gun = 10 # gun이라는 변수를 정의

def checkpoint(soldiers):
	global gun # 전역 공간에 있는 gun 사용 하겠다는 의미
	gun = gun - soldiers
	print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
	gun = gun - soldiers # 계산으로 변경된 값을 gun에 넣고
	print("[함수 내] 남은 총 : {0}".format(gun)) # 출력을 하고 나서
	return gun # 변경된 값을 return

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
# checkpoint_ret 함수를 호출(변경된 return 값을 받기에 8이 들어감)
print("남은 총 : {0}".format(gun))