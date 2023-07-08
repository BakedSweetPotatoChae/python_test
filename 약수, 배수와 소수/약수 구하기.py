i, k = map(int, input().split())

arr = []

count = 0

for j in range(1, i+1):
    if(i%j == 0):
        #print("in")
        arr.append(j)

if(k <= len(arr)):
    print(arr[k-1])
else:
    print(0)