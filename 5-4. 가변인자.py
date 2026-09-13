# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#	print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
	# end=" " 를 적으면 해당 print문이 끝날 때, 줄바꿈을 하지 않고 끝냄
#	print(lang1, lang2, lang3, lang4, lang5)
	
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#") 
# profile("김태호", 25, "Kotlin", "Swift", "", "", "") 
# 문제점
# 매번 빈 값을 넣어줘야하나?
# 추가되는 것은 어떻게 대응?

def profile(name, age, *language): # *을 넣으면 넣고 싶은 만큼 넣을 수 있음
	print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
	for lang in language:
		print(lang, end=" ")
	print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")