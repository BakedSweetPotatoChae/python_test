import time as t
import random as r

item = [1,1,3,3,3,3,4,4,4,10]
r.shuffle(item)
print(item)

for j in range(10):
    for i in reversed(range(1, 10)):
        if(item[i] <= item[i-1]):
            print(item)
            #t.sleep(2)
            item[i], item[i-1] = item[i-1], item[i]

print(item)