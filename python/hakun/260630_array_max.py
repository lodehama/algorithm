arr = [76, 34, 90, 40, 50, 92, 65, 84, 96, 85]

max_num = arr[0]

for i in range(1, len(arr)):
    if max_num < arr[i]:
        max_num = arr[i]

print(max_num)