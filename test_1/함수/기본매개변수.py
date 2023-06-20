def print_n_times(value, n=2): #뒤에 n은 함수 호출에 따로 값을 선언을 하지 않는 경우에 default값으로 선언할 값을 선택한다.
    for i in range(n):
        print(value)

print_n_times("안녕하세요")

print("----")

print_n_times("안녕하세요",3)