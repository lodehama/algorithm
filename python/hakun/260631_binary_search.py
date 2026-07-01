def binary_search(arr, key):
  low = 0
  high = len(arr) - 1

  while low <= high:
    print(f"[{low} {high}]")

    middle = (low + high) // 2

    if key == arr[middle]:
      return middle
    elif key > arr[middle]:
      low = middle + 1
    else:
      high = middle - 1

  return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80]

key = int(input("찾을 값을 입력하세요: "))

result = binary_search(arr, key)

if result != -1:
  print("탐색 결과 =", result)
else:
  print("값이 없습니다.")
