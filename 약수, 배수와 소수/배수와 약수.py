number_2, number_1 = 0,0


while True:
    number_1, number_2 = map(int, input().split())
    if(number_1 == 0 and number_2 == 0):
        break
    if(number_2 % number_1 == 0):
        print("factor")
    elif(number_1 % number_2 == 0):
        print("mltiple")
    else:
        print("neither")