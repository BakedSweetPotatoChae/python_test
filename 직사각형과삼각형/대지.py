number_size = int(input())


x = []
y = []

for i in range(number_size):
    x_1,y_1 = map(int, input().split())
    x.append(x_1)
    y.append(y_1)


x_max = x[0]
y_max = y[0]
x_min = x[0]
y_min = y[0]

for i in range(number_size):
    if(x_max < x[i]):
        x_max = x[i]
    elif(x_min > x[i]):
        x_min = x[i]
    if(y_max < y[i]):
        y_max = y[i]
    elif(y_min > y[i]):
        y_min = y[i]

print((x_max - x_min)*(y_max - y_min))