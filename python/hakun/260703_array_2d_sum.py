arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

total = 0

for i in range(3):
  for j in range(3):
    total += arr[i][j]

print("합 =", total)
