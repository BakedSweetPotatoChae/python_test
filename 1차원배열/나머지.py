number = []

for i in range(0, 10):
    j = int(input())
    if(j%42 not in number):
        number.append(j%42)

print(len(number))