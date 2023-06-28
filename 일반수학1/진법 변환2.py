import string

number,number_2 = map(int, input().split())
tmp = string.digits + string.ascii_uppercase
#print(tmp)
number_list = []

def arithmetic(a,b):
    #print("{},{} 들어옴".format(a,b))
    Division,rest=divmod(a,b)
    #print("{},{} 계산됨".format(Division,rest))
    number_list.append(rest)
    if(Division < number_2):
        if(Division > 0):
            number_list.append(Division)
        #print("b")
        pass
    else:
        #print("a")
        return arithmetic(Division, number_2)


        

arithmetic(number, number_2)
#print(number_list)

number_list.reverse()

number_change = []

for i in number_list:
    for j in range(len(tmp)):
        #print("{} = {}".format(i,j))
        if(i == j):
            #print("check")
            number_change.append(tmp[i])

for i in number_change:
    print(i,end="")