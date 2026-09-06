absent = [2, 5] # 결석
# 위 조건에 해당하는 값을 제외하고 넘어가는 것이
# continue
for student in range(1, 11): # 1 ~ 10
	if student in absent:
		continue
	print("{0}, 책을 읽어봐",format(student))
	# 결과
	# 1,3,4,6,7,8,9,10 책을 읽어봐