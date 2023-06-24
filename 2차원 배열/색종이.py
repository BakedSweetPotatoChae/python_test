paper = [[0 for i in range(100)] for i in range(100)]

for i in range(100):
    pass
    #print(paper[i])

input_number = int(input())

paperadd = [[] for i in range(input_number)]

for i in range(input_number):
    paperadd[i] = input().split()

for i in range(input_number):
    for j in range(10):
        for k in range(10):
            #print("{}, {}".format(paperadd[i][0], paperadd[i][1]))
            paper[int(paperadd[i][0])+j][int(paperadd[i][1])+k] = 1

count = 0

for i in range(100):
    for j in range(100):
        if(paper[i][j] == 1):
            count += 1

print(count)            