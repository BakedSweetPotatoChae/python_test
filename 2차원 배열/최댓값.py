number = [[0 for j in range(9)] for i in range(9)]

for i in range(9):
    text = input()
    number[i] = (text.split())

max = 0
for i in range(9):
    for j in range(9):
        if(int(number[i][j]) >= int(max)):
            max = number[i][j]
            x = i
            y = j

print(max)
print("{} {}".format(x+1,y+1))