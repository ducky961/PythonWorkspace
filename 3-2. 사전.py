cabinet = {3: "유재석"} # 딕셔너리 자료형, key = 3, value = "유재석"
print(cabinet[3]) # 결과 : 유재석

cabinet = {3: "유재석", 100: "김태호"} # 딕셔너리 자료형, key = 3, value = "유재석", key = 100, value = "김태호"
print(cabinet.get(3)) # 결과 : 유재석
print(cabinet[5]) # 결과 : KeyError, 5라는 key가 없기 때문에 오류 발생
print(cabinet.get(5)) # 결과 : None, 5라는 key가 없기 때문에 None 반환

# None이라는 값으로 출력되는 걸 원치 않는 경우 아래와 같이 가능함
print(cabinet.get(5, "사용 가능")) # 결과 : 사용 가능
# 5라는 key가 없기 때문에 "사용 가능"이라는 값을 반환하도록 설정함

print(3 in cabinet) # 결과 : True, 3이라는 key가 cabinet에 있는지 확인
print(5 in cabinet) # 결과 : False, 5라는 key가 cabinet에 있는지 확인

cabinet = {"A-3": "유재석", "B-100": "김태호"} # 딕셔너리 자료형, key = "A-3", value = "유재석", key = "B-100", value = "김태호"
print(cabinet["A-3"]) # 결과 : 유재석
print(cabinet["B-100"]) # 결과 : 김태호

# 새 손님
print(cabinet) # 결과 : {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국" # 딕셔너리 자료형에 key = "A-3", value = "김종국" 추가
cabinet["C-20"] = "조세호" # 딕셔너리 자료형에 key = "C-20", value = "조세호" 추가
print(cabinet) # 결과 : {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"] # 딕셔너리 자료형에서 key = "A-3" 삭제
print(cabinet) # 결과 : {'B-100': '김태호', 'C-20': '조세호'}

# key들만 출력
print(cabinet.keys())
# 결과 : dict_keys(['B-100', 'C-20']), 딕셔너리 자료형의 key들만 출력

# value들만 출력
print(cabinet.values())
# 결과 : dict_values(['김태호', '조세호']), 딕셔너리 자료형의 value들만 출력

# key, value 쌍으로 출력
print(cabinet.items())
# 결과 : dict_items([('B-100', '김태호'), ('C-20', '조세호')]),
# 딕셔너리 자료형의 key, value 쌍만 출력

# 목욕탕 폐점
cabinet.clear() # clear() : 딕셔너리 자료형의 모든 데이터를 삭제
print(cabinet) # 결과 : {}, 딕셔너리 자료형의 모든 데이터