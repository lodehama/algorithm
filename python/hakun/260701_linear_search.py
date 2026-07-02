arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

key = int(input("탐색할 값을 입력하세요: "))

for i, value in enumerate(arr):
    if value == key:
        print("탐색 성공 인덱스 =", i)
        break
else:
    print("찾는 값이 없습니다.")

print("탐색 종료")