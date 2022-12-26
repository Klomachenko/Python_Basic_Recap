# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행합니다.
# 댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받습니다.
# 추첨 프로그램을 작성하시오

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

from random import *

# 내 풀이
# people = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # 조건1

# 조건2 중복 불가 - 차집합 이용 - 리스트에선 리스트 값을 제거할 때 차집합 형식으로 변수-변수 가 불가능하다!
# 조건3 shuffle, sample 이용완료
# shuffle(people)
# chicken = sample(people, 1)
# print(chicken)
# chicken = set(chicken)

# people = set(people)

# people2 = people - chicken
# people2 = list(people2)
# shuffle(people2)

# coffee = sample(people2, 3)
# print(coffee)
# chicken = list(chicken)


# print(f'-- 당첨자 발표 -- \n 치킨 당첨자 : {chicken} \n 커피 당첨자 : {coffee} \n -- 축하합니다 --')

# 정석 풀이
users = range(1, 21) # 1부터 21미만까지 숫자 생성
print(type(users)) # range 라는 타입이 나오므로 -> list로 변환해준다
users = list(users)

print(users)
shuffle(users) # 무작위를 위해 shuffle
print(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0])) # 이런식으로 나눠도 중복이 안되긴 하네... 생각도 못했던 쉬운 방법!
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")