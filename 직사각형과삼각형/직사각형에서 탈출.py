arr = list(map(int, input().split()))

arr_2 = []

arr_2.append(arr[0])
arr_2.append(arr[1])
arr_2.append(arr[2] - arr[0])
arr_2.append(arr[3] - arr[1])

print(arr_2)

min = arr_2[0]

for i in arr_2:
    if(i < min):
        min = i

print(min)