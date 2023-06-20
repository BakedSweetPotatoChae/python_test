text = str(input())

count = 0
true = 0
for i in range(0, int(len(text)/2)):
    if(text[i] == text[(len(text)-i-1)]):
        true += 1

if(int(len(text)/2)==true):
    print(1)
else:
    print(0)