count = int(input())

number = list(map(int, input().split()))

max=number[0]
min=number[0]


for i in range(0,len(number)):
    if(max<number[i]):
        max = number[i]
    
    if(min>number[i]):
        min = number[i]

print(min, max)