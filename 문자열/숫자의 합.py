count = int(input())
number = input()
number_save = [0 for i in range(count)]
sum = 0
for i in range(1,count+1):
    sum += int(number[i-1:i])

print(sum)