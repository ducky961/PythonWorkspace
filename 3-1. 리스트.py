# 리스트 []

# 지하철 칸 별로 10, 20, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30
# 이렇게 해도 되지만,

subway = [10, 20, 30] # 리스트 구조 사용
# 리스트를 이용하면 더 짧고, 편리하게 관리할 수 있다.
print(subway) # 결과 : [10, 20, 30]

subway = ["유재석", "조세호", "박명수"] # 문자열도 가능
print(subway) # 결과 : ['유재석', '조세호', '박명수']

# 예시 1
# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호")) # 결과 : 1 (0부터 시작)

# 예시 2
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # append() : 리스트에 새로운 데이터를 추가
print(subway) # 결과 : ['유재석', '조세호', '박명수', '하하']

# 예시 3
# 정형돈씨가 유재석씨와 조세호씨 사이에 탐
subway.insert(1, "정형돈") # insert(위치, 데이터) : 특정 위치에 데이터를 추가
print(subway) # 결과 : ['유재석', '정형돈', '조세호', '박명수', '하하']

# 예시 4
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # pop() : 리스트에서 마지막 데이터를 꺼냄
print(subway) # 결과 : ['유재석', '정형돈', '조세호', '박명수']

# 예시 5
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway.count("유재석")) # 결과 : 2

# 예시 6
# 정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort() # sort() : 리스트를 오름차순으로 정렬
print(num_list) # 결과 : [1, 2, 3, 4, 5]

# 예시 7
# 순서 뒤집기 가능
num_list.reverse() # reverse() : 리스트의 순서를 뒤집음
print(num_list) # 결과 : [5, 4, 3, 2, 1]

# 예시 8
# 리스트를 모두 지우는 것도 가능
num_list.clear() # clear() : 리스트의 모든 데이터를 삭제
print(num_list) # 결과 : []

# 예시 9
# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True] # 문자열, 정수, 불리언
print(mix_list) # 결과 : ['조세호', 20, True]

# 예시 10
# 리스트 확장
num_list = [1, 2, 3, 4, 5]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list) # extend() : 리스트를 확장
print(num_list) # 결과 : [1, 2, 3, 4, 5, '조세호', 20, True]