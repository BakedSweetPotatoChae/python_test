number = list(map(str, input().split()))

one = number[0]
two = number[1]

one_number = int(one[2]+one[1]+one[0])
two_number = int(two[2]+two[1]+two[0])

if(one_number >= two_number):
    print(one_number)
else:
    print(two_number)

