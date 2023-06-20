tell_abc = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]


in_text = str(input())

time = int(0)
for j in range(len(in_text)):
    for i in range(8):
        if  in_text[j] in tell_abc[i]:
            time += i+3

print(time)