# 2. [0 * 26] 각 알파벳의 빈도수를 저장한 배열을 만든다.
# 그리고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트한다.
# a -> 0번째 인덱스 값을 올리고, z가 나왔다면 25번째 인덱스의 값을 추가


def find_max_occurred_alphabet(string):
	alphabet_occurrence_array = [0] * 26

	for char in string:
		if not char.isalpha():  # 알파벳인지 검사
			continue
		arr_index = ord(char) - ord('a')  # 해당 문자를 인덱스로 치환. a -> 0, b -> 1
		alphabet_occurrence_array[arr_index] += 1  # 빈도수 배열에 인덱스로 찾아가서 해당 값을 추가

	max_occurrence = 0
	max_alphabet_index = 0

	for index in range(len(alphabet_occurrence_array)):  # 0,1...25
		alphabet_occurrence = alphabet_occurrence_array[index]
		if alphabet_occurrence > max_occurrence:
			max_occurrence = alphabet_occurrence
			max_alphabet_index = index

	print("max_alphabet_index is ", max_alphabet_index)

	return chr(max_alphabet_index + ord('a'))


# 8 -> i 인덱스 -> 아스키코드 형태로 만들고 -> 알파벳
# 0 -> a
# 0 -> 97 -> a
# chr(0 + ord('a')) -> 'a'

# chr(97) == 'a'
# chr(0 + ord('a')) == 'a'
# chr(0 + 97) == 'a'
# chr(1 + 97) == 'b'

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
