total = 0

while True:
    number = int(input("숫자 입력(0 종료): "))

    if number == 0:
        break

    total += number

print(total)