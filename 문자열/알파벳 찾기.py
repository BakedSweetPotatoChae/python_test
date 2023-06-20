str = input()

text_list = [-1 for i in range(26)]
a='abcdefghijklmnopqrstuvwxyz'

for i in range(26):
    if(str.find(a[i]) != -1):
        text_list[i] = str.find(a[i])
        
for i in range(26):
    print(text_list[i], end=" ")
