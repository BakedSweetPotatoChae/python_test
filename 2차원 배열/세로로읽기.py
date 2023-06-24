list_number = [[] for j in range(15)]

for i in range(5):
    text = input()
    for j in range(len(text)):
        try:
            list_number[j].append(text[j])[i]
        except:
            pass



for i in range(len(list_number)):
    for j in range(len(list_number[i])):
        print(list_number[i][j],end="")