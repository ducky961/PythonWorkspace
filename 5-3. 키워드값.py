def profile(name, age, main_lang):
	print(name, age, main_lang)
	
profile(name="유재석", main_lang="파이썬", age=20) # 굳이 순서대로 하지 않음
profile(main_lang="자바", age=25, name="김태호") # 굳이 순서대로 하지 않음

# 함수에서 전달 받는 매개변수의 값을 키워드를 이용해서 함수를 호출하면
# 키워드 = 값을 넣어주면 그 키워드에 해당하는 값이 순서가 섞여도 상관없음