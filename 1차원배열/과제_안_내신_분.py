class_number = [0 for i in range(32)]
check_student = 0
for i in range(0, 28):
    check_student = int(input())
    class_number[check_student] = check_student
for i in range(1, 31):
    if(class_number[i] == 0):
        print(i)