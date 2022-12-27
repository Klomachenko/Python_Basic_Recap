# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사의의 난수로 정해짐
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 함

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 15분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

# 내 풀이
# from random import *
# customer = range(1, 51) # 50명 승객
# number = 0 # 탑승 승객 수
# for i in customer:
#     time = randint(5, 50) # 무작위 시간 - for 문 안에 넣어줘야 하네...
#     if 5 <= time <= 15:
#         print(f'[O] {i}번째 손님 (소요시간 : {time}분)')
#         number = number +1
#     else:
#         print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')

# print(f'총 탑승 승객 : {number}분')

# 정석 풀이
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1~ 50 이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 매칭 성공 손님
        print(f"[O] {i}번째 손님 (소요시간 : {time}분")
        cnt += 1 # 탑승 승객 수 증가 처리
    else: # 매칭 실패한 경우
        print(f"[ ] {i}번째 손님 (소요시간 : {time}분")

print(f"총 탑승 승객 : {cnt}분")
