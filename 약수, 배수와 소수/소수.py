number = int(input())
number_2 = int(input())
#1과 자기 자신만을 가지고 있는 소수
sum_a = 0
arr = []
for i in range(number, number_2+1):
    sum_a = 0
    for j in range(2, i):
        if(i%j==0):
            sum_a += 1
    if(sum_a == 0 and i != 1):
        arr.append(i)
A = sum(arr)
if(A == 0):
    print("-1")
else:
    print(A)
    print(arr[0])
    
