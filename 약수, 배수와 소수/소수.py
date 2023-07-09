number = int(input())


while(True):
    if(number == 1):
        break
    count = 1
    while(True):
        count += 1
        if(number%count == 0):
            print(count)
            number = number/count
            break