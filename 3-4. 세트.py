# 집합 (set)
# 집합(set) 자료형은 중복을 허용하지 않고, 순서가 없다는 특징이 있습니다.
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3} 중복 제거

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # set() 함수를 이용

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python) # {'유재석', '김태호', '양세형', '박명수'}

# 차집합 (java는 할 수 있지만 python은 할 수 없는 개발자)
print(java - python) # {'김태호', '양세형'}
print(java.difference(python)) # {'김태호', '양세형'}

# [추가] python을 할 수 있는 사람이 늘어남
python.add("김태호")
print(python) # {'유재석', '박명수', '김태호'}

# [추가] java를 잊어버림
java.remove("김태호")