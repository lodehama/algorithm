val1 = 5
val2 = 10

print(f"함수 호출 전의 변수 val 값: {val1}, {val2}")

val1, val2 = val2, val1

print(f"함수 호출 후의 변수 val 값: {val1}, {val2}")