import math
m = int(input())
count = 0
for j in range(m):
    coin_type = [25,10,5,1]
    coin_save = [0,0,0,0]
    n = int(input())
    for coin in coin_type:
        #print("n:{}".format(n))
        #print("coin : {}".format(coin))
        #print("n/coin : {}".format(n/coin))
        #print(n//coin)
        coin_save[coin_type.index(coin)]+= int(round(n,4) // coin)
        
        n %= coin

    for i in coin_save:
        print(i,end=" ")
    print()
