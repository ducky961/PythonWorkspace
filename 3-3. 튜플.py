# 리스트와 다르게 내용을 변경하거나 추가 할 수 없지만, 리스트보다 속도가 빠르다.

menu = ("돈까스", "치즈까스") # 튜플은 소괄호로 감싸서 만든다.
print(menu[0]) # 결과 : 돈까스
print(menu[1]) # 결과 : 치즈까스

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) # 결과 : 김종국 20 코딩

name, age, hobby = ("김종국", 20, "코딩") # 튜플을 이용한 변수 선언
print(name, age, hobby) # 결과 : 김종국 20 코딩