# 출석번호가 1, 2, 3, 4
# 앞에 100을 붙이기로 함 -> 101, 102, 103, 104

students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students]
# students라는 리스트에 있는 i들을 하나씩 불러오면서
# 거기에 100을 더한 값을 리스트로 바꿔서 집어넣어라는 의미
print(students)

# 학생 이름을 길이로 반환
students = ["Iron man", "Thor", "groot"]
students = [len(i) for i in students]
# len를 써서 i의 값을 변경
# students라는 리스트의 값들을 하나씩 조회하면서
# 그 길이를 len(i)에 집어 넣겠다라는 의미
print(students)