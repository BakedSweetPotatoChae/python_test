input_number = int(input())

line = 0
max_num = 0

while max_num<input_number:
    line += 1
    max_num += line

gap = max_num - input_number
print("gap = {} - {}".format(max_num,input_number))
print("gap : {}".format(gap))

if line%2 == 0:
    top = line - gap
    under = gap + 1
    #print("top : {}".format(top))
    #print("nuber : {}".format(under))
    #print("짝수")   
else:
    top = gap + 1
    under = line - gap
    #print("홀수")

#print(line)
#print(max_num)

print("{}/{}".format(top,under))