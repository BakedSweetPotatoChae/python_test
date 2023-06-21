text = input()

text += "000"
i = 0
number = 0

while(1):
    if(text[i]+text[i+1] == "c="):
        number +=1
        i += 1
    elif(text[i]+text[i+1] == "c-"):
        number +=1
        i += 1
    elif(text[i]+text[i+1]+text[i+2] == "dz="):
        number +=1
        i += 2
    elif(text[i]+text[i+1] == "d-"):
        number +=1
        i += 1
    elif(text[i]+text[i+1] == "lj"):
        i += 1
        number +=1
    elif(text[i]+text[i+1] == "nj"):
        i += 1
        number +=1
    elif(text[i]+text[i+1] == "s="):
        i += 1
        number +=1
    elif(text[i]+text[i+1] == "z="):
        i += 1
        number +=1
    else:
        number +=1

    
    if(i >= len(text)-4):
        break
    i+=1

print(number)