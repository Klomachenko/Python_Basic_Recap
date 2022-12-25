# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램 작성

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글재 내 'e' 갯수 + "!" 로 구성
# 예) 생성된 비밀번호 : nav51!

# 내 풀이
# psw = "http://naver.com"
# psw = "http://daum.com"

# psw1 = psw[7:] # 규칙1

# psw2 = psw1[:-4] # 규칙2

# psw3 = psw2[0:3] # 처음 세자리

# print(str(psw3) + str(len(psw2)) + str(psw.count("e")) + "!") # 규칙3

# 정석 풀이

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] 
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"{url}의 비밀번호는 {password} 입니다.")