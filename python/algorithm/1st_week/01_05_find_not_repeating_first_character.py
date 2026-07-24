#
# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac" 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환

input = "abadabac"

# O(N)
def find_not_repeating_first_character(string):
	# 반복되지 않는 첫번째 알파벳 -> 반복 되는지 안 되는지를 판단
	# alphabet_occurence_array
	# string에서 알파벳의 빈도수를 찾기
	occurrence_array = find_alphabet_occurence_array(string)
	# 빈도수가 1인 알파벳들 중에서 string에서 뭐가 먼저 나왔는지를 찾기
	not_repeating_character_array = []
	for index in range(len(occurrence_array)):
		alphabet_occurrence = occurrence_array[index]
		if alphabet_occurrence == 1:
			not_repeating_character_array.append(chr(index + ord('a')))

	print(not_repeating_character_array)
	for char in string:
		if char in not_repeating_character_array:
			return char
	return "_"


def find_alphabet_occurence_array(string):
	alphabet_occurrence_array = [0] * 26

	for char in string:
		if not char.isalpha():
			continue
		arr_index = ord(char) - ord('a')
		alphabet_occurrence_array[arr_index] += 1

	return alphabet_occurrence_array


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
