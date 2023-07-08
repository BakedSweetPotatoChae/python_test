A,B,V = map(int, input().split())

day = (V-B) / (A-B)
print(day)
if(day-int(day) == 0):
    print(int(day))
else:
    print(int(day+1))

