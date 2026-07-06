str1 = "apple"
str2 = "banana"
str3 = "melon"

if str2 < str3:
    print(f"{str2}는 {str3}보다 사전순으로 앞에 옵니다.")
elif str2 > str3:
    print(f"{str2}는 {str3}보다 사전순으로 뒤에 옵니다.")
else:
    print(f"{str2}와 {str3} 문자열은 동일합니다.")