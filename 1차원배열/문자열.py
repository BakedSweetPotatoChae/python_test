count = int(input())

start = [0 for i in range(count)]
end = [0 for i in range(count)]

for i in range(0,count):
    str = input()
    start[i] = str[0]
    end[i] = str.strip()[-1]

for i in range(count):
    print(start[i],end ="")
    print(end[i])