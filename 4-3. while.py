# 반복문 2
# while (조건):
# 어떤 조건이 만족할 때 까지 반복
customer = "토르"
index = 5 # 5번 확인
while index >= 1: # 'index'가 1보다 크거나 같을 때 까지 진행
	print("{0},커피가 준비 되었습니다.{1}번 남았어요.".format(customer, index))
	index -= 1 # 1개씩 줄이기
	if index == 0: # 0이 되면
		print("커피는 폐기처분 되었습니다")