#
# 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환

def is_number_exist(number, array):
	for element in array:
		if number == element:
			return True
	return False


# 배열을 전부 다 돌면서 배열의 원소가 찾고자 하는 숫자와 같은지 비교

# 빅오 -> 최악의 경우
# 빅오메가 -> 최선의 경우


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3, 5, 6, 1, 2, 4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6, 6, 6]))
print("정답 = True 현재 풀이 값 =", result(2, [6, 9, 2, 7, 1888]))
