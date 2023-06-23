number, number_2 = map(int, input().split())

list_number = []
list_number_2 = []
list_number_sum = [[0 for i in range(number_2)] for i in range(number)]

for i in range(number):
    input_number = input()
    list_number.append(input_number.split())

for i in range(number):
    input_number = input()
    list_number_2.append(input_number.split())
        
for i in range(number):
    for j in range(number_2):
        #print("i:{} j:{}, list_number : {} list_number_2 : {}".format(i,j,list_number[i][j],list_number_2[i][j]))
        list_number_sum[i][j] = int(list_number[i][j]) + int(list_number_2[i][j])


for i in range(number):
    for j in range(number_2-1):
        print(list_number_sum[i][j], end=" ")
    print(list_number_sum[i][number_2-1], end="")
    print()