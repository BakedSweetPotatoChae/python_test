import random as r


list_number = [1,2,3,4,5,6,7,8,9,10]

print(list_number)

r.shuffle(list_number)

print(list_number)

for i in range(len(list_number)-1):
    min_index = i
    for j in range(i+1, len(list_number)):
        if(list_number[min_index] >= list_number[j]):
            min_index = j
    list_number[i], list_number[min_index] = list_number[min_index], list_number[i]

print(list_number)