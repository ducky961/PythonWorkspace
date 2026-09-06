# if 조건:
#	 실행 명령문

weather = "비"
if weather == "비": # 날씨가 비가 오면
	print("우산을 챙기세요") # "우산을 챙기세요"를 출력
# 만약 날씨가 다르다면?
# 아무것도 실행되지 않음
elif weather =="미세먼지": # 날씨가 미세먼지면
	print("마스크를 챙기세요")
else: # 날씨가 "비"도 아니고 "미세먼지"도 아니면
	print("준비물 필요 없어요.") # "준비물 필요 없어요." 출력

weather = input("오늘 날씨는 어때요?") # 날씨 입력
if weather == "비": # 날씨가 "비"가 오면
	print("우산을 챙기세요") # "우산을 챙기세요"를 출력
elif weather =="미세먼지": # 날씨가 "미세먼지"면
	print("마스크를 챙기세요")
else: # 날씨가 "비"도 아니고 "미세먼지"도 아니면
	print("준비물 필요 없어요.") # "준비물 필요 없어요." 출력

weather = input("오늘 날씨는 어때요?") 
if weather == "비" or weather == "눈": 
# "비" 또는 "눈"이라고 입력되면
	print("우산을 챙기세요") # "우산을 챙기세요" 출력
elif weather =="미세먼지":
	print("마스크를 챙기세요")
else:
	print("준비물 필요 없어요.")

temp = int(input("기온은 어때요?")) # 기온은 숫자이기 때문에 int로 지정
if 30 <= temp:
	print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
	print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
	print("외투를 챙기세요")
else:
	print("너무 추워요. 나가지 마세요")