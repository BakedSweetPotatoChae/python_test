import random as r

list_number = [1,2,3,4,5,6,7,8,9,10]

print(list_number)

r.shuffle(list_number)

print(list_number)

for i in range(len(list_number)):
    for j in range(i):
        if(list_number[j] >= list_number[i]):
            list_number[j], list_number[i] = list_number[i], list_number[j]

print(list_number)