# 자료구조의 변경

# 커피숍
menu = {"커피", "우유", "주스"} # 집합은 중괄호로 감싸서 만든다.
print(menu, type(menu)) # 결과 : {'커피', '주스', '우유'} <class 'set'>

menu = list(menu) # 집합을 리스트로 변환
print(menu, type(menu)) # 결과 : ['커피', '주스', '우유'] <class 'list'>

menu = tuple(menu) # 리스트를 튜플로 변환
print(menu, type(menu)) # 결과 : ('커피', '주스', '우유') <class 'tuple'>

menu = set(menu) # 튜플을 집합으로 변환
print(menu, type(menu)) # 결과 : {'커피', '주스', '우유'} <class 'set'>