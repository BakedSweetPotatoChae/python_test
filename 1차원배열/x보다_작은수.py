count, comparison = map(int, input().split())

list_number = list(map(int,input().split()))

comparison_save = []

for i in range(0,count):
    if(comparison > list_number[i]):
        comparison_save.append(list_number[i])

for i in range(0,len(comparison_save)):
    print(comparison_save[i], end=" ")