print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14, number라는 변수를 생성 및 값 지정
# 해석
# 'number'라는 변수는 '2 + 3 * 4'라는 연산자를 포함한 값을 가지고 있고,
# 계산하면 '14'가 나오니 'number'는 '14'라는 값을 가진 변수이다 
print(number) # 14, number라는 변수의 값 출력
number = number + 2 # 14 + 2 = 16
# 해석
# '14'라는 값을 가지고 있는 'number'라는 변수에 2를 덧셈하여
# '16'이라는 값으로 덮어쓴다.(값의 초기화라고 함)
print(number) # 여기서 'number = 16'이다.
number += 2 # 18, 'number = number + 2'와 동일함
number *= 2 # 36
number /= 2 # 18
number -= 2 # 16
print(number) # 16

number %= 5 # 1
print(number) # 1