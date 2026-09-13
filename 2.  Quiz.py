#quiz 3
#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
#예시 : http://naver.com
#규칙 1 : http:// 부분은 제외 => naver.com
#규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

#예시 : 생성된 비밀번호 : nav51!

# 내가 쓴 풀이
site = "http://naver.com"
print(site[-9:-4]) 
# %%
site = site[-9:-4]
print(site[:3]+str(len(site))+str(site.count("e"))+"!")
# %%
# 강사님 풀이
url = "http://naver.com"
my_str = url.replace("http://","") # 규칙 1 수행
# 이 코드의 의미는 replace가 원하는 구문("http://")을 찾아서
# ("")빈칸으로 바꿈
my_str = my_str[:my_str.index(".")] # 문자열 처음부터 . 위치 직전까지 반환
# my_str[0:5] -> 0~5 직전까지 (0, 1, 2, 3, 4) 와 똑같음
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url,password))

# ai의 풀이
url = "http://naver.com"
url = url.replace("http://", "") # 규칙 1
url = url[:url.index(".")] # 규칙 2
print(url[:3] + str(len(url)) + str(url.count("e")) + "!")