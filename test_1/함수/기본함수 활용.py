def sum_all(start, end):
    output = 0

    for i in range(start,end+1):
        output+=i
    
    return output

print("0 to 100", sum_all(0,100))
print("0t to 1000", sum_all(0,1000))


def sum_all_2(start=0,end=0, step=0):
    output = 0
    for i in range(start, end+1, step):
        output += i
    
    return output

print("0 to 100 and step 10", sum_all_2(0,100,10))
