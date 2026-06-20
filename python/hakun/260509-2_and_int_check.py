print("두 개의 정수를 입력하세요.")

# map(int) = 문자열을 정수(int)로 변환
# input() = 용자 입력 받기
# split() = 입력값을 공백 기준으로 나누기

a, b = map(int, input().split())

if a > 0 and b > 0:
    print("두 수가 양수입니다")

elif a > 0 or b > 0:
    print("한 수는 양수입니다.")

else:
    print("양수가 없습니다.")