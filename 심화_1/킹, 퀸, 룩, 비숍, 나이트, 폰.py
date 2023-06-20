list_chess = list(map(int,input().split()))
number_of_chess_without = [1,1,2,2,2,8]
find_the_number_of_msissing_chess_pices = [0,0,0,0,0,0]
for i in range(len(number_of_chess_without)):
    #print("i number : {0}".format(i))
    if(list_chess[i] != number_of_chess_without[i]):
        #print("enter the if gate")
        for j in range(10):
            #print("count the for gate and number is : {0}".format(j))
            if(list_chess[i]+j == number_of_chess_without[i]):
                #print("enter the second if gate, The condition is ==")
                find_the_number_of_msissing_chess_pices[i] = j
            elif(list_chess[i]-j == number_of_chess_without[i]):
                #print("enter the second if gate, The condition is !=")
                find_the_number_of_msissing_chess_pices[i] = -j
for i in range(len(list_chess)):
    print(find_the_number_of_msissing_chess_pices[i],end=" ")