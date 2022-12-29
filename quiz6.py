# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#   남자 : 키(m) x 키(m) x 22
#   여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175 남자의 표준 체중은 67.38kg 입니다.

# 내 풀이
# def std_weight(gender, height):
#     if gender == 'male':
#         maleweight = height * height * 22
#         print(f'키 {height * 100} 남자의 표준 체중은 {maleweight:.2f}kg 입니다.')
#     else:
#         femaleweight = height * height * 21
#         print(f'키 {height * 100} 여자의 표준 체중은 {femaleweight:.2f}kg 입니다.')

# std_weight('male', 1.75)
# std_weight('female', 1.67)

# 정석 풀이

def std_weight(height, gender): # 키 m 단위(실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # 반올림을 해줬네
print(f'키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.')





