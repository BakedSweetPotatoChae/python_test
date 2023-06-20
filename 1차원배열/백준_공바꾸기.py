pocket_number, number_input = map(int, input().split())

pocket = [1 for i in range(pocket_number+1)]

for i in range(0,pocket_number):
    pocket[i] = i+1

for i in range(number_input):
    j ,k = map(int, input().split())
    pocket[j-1], pocket[k-1] = pocket[k-1], pocket[j-1]

for i in range(pocket_number):
    print(pocket[i], end=" ")