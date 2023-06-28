import time
import string
number_2=0
number,number_2 = input().split()
number_sum = 0
tmp = string.digits+string.ascii_uppercase
#print(len(tmp))

number_list = [i for i in range(len(number))]

number_list.reverse()

sum_number = 0
count_number = 1

for i in number_list:
    for j in range(len(tmp)):
        if(number[count_number-1] == tmp[j]):
            #print("{}=={}".format(number[count_number-1],tmp[j]))
            #print("{}*(int({})**({}-{}))".format(number[count_number-1],number_2,len(number),count_number-1))
            #print(int(j*(int(number_2)**(len(number)-(count_number-1)))))
            sum_number += int(j*(int(number_2)**(len(number)-(count_number))))
    count_number += 1

print(sum_number)