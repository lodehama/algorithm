# 1
# 1. a,b,c 처럼 문자가 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 그 알파벳으로 변환
# a -> hello my name is dingcodingco -> 0 max_occurre = 0 max_alphabet = a
# b -> hello my name is dingcodingco -> 0 max_occurre = 0 max_alphabet = b
# c -> hello my name is dingcodingco -> 0 max_occurre = 2 max_alphabet = c
def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet

print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))


# 2. [0 * 26] 각 알파벳의 빈도수를 저장한 배열을 만든다.
# 그리고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트한다.
# a -> 0번째 인덱스 값을 올리고, z가 나왔다면 25번째 인덱스의 값을 추가
# a
