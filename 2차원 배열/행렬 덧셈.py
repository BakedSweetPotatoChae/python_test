number, number_2 = map(int, input().split())
#print(number, number_2, sep="\t")

list_number = []
list_number_2 = []
list_number_sum = [[0 for i in range(number)] for i in range(number_2)]

for i in range(number):
    input_number = input()
    list_number.append(input_number.split())

for i in range(number):
    input_number = input()
    list_number_2.append(input_number.split())
        
for i in range(number):
    for j in range(number_2):
        #print("{}+{}".format(int(list_number[i][j]),int(list_number[i][j])))
        list_number_sum[i][j] = int(list_number[i][j]) + int(list_number_2[i][j])

'''
print(list_number)

print(list_number_2)

print(list_number_sum)
'''

for i in range(number):
    for j in range(number_2):
        print(list_number_sum[i][j], end=" ")
    print()