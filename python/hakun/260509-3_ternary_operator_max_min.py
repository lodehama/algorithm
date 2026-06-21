print("두 개의 정수를 입력하세요.")

a, b = map(int, input().split())

print("둘 중 큰 수는", a if a > b else b)
print("둘 중 작은 수는", a if a < b else b)