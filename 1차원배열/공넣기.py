pocket_number, ball_input_count = map(int, input().split())

pocket = [0 for i in range(pocket_number)]

for c in range(0, ball_input_count):
    i,j,k = map(int, input().split())
    for f in range(i-1, j):
        pocket[f] = k
        
for i in range(0,pocket_number):
    print(pocket[i])