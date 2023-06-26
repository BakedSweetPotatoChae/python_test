import string
number_2=0
number,number_2 = input().split()
number_sum = 0
tmp = string.digits+string.ascii_uppercase

for i in range(len(number)):
    for j in range(len(tmp)):
        if(number[i] == tmp[j]):
            number_sum += j*(int(number_2)**i)


print(number_sum)