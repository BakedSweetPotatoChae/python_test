
while True:
    i = int(input())
    if(i == -1):
        break
    arr = []
    sum = 0
    for j in range(1, i):
        if(i%j == 0):
            sum += j
            arr.append(j)

    if(sum == i):
        print("{} = ".format(i), end="")
        for j in range(len(arr)):
            if(j <= len(arr) - 2):
                print("{} + ".format(arr[j]),end="")
            else:
                print("{}".format(arr[j]))
    else:
        print("{} is NOT perfect.".format(i))