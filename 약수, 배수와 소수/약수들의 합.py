
while True:
    i = int(input())
    if(i == -1):
        break
    arr = []
    for j in range(1, i):
        if(i%j == 0):
            arr.append(j)

    if(sum(arr) == i):
        print(i," = "," + ".join(str(i) for i in arr),sep="")
    else:
        print("{} is NOT perfect.".format(i))