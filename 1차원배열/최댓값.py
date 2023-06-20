number = []
max = 0
count = 0
for i in range(0, 9):
    number.append(int(input()))
    if(max < number[i]):
        max = number[i]
        count = i
    
print(max)
print(count+1)