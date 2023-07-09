arr = []

in_number = int(input())

count = 0

arr = list(map(int, input().split()))
#print(arr)

'''
for i in range(in_number):
    arr.append(int(input()))
'''


for i in range(len(arr)):
    err = 0
    if(arr[i] > 1):
        for j in range(2, arr[i]):
            if(arr[i]%j == 0):
                err += 1
        if(err == 0):
            count += 1
print(count)
