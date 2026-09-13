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